"""Financial counterexamples: timing, scope, leverage, source status and replay. MIT."""
import copy
from decimal import Decimal as D
from pathlib import Path
import tempfile
import unittest
from housing_underwriting import model,engine
from housing_common.local_outputs import ROOT


def request():return engine.load(ROOT/'config/underwriting/rental-60-base.json')


class Underwriting(unittest.TestCase):
    def test_zero_interest_amortization_and_balloon(self):
        self.assertEqual(model.constant(D(0),30),D(1)/30)
        self.assertEqual(model.balance(D(300),D(0),30,10),D(200))
        self.assertEqual(model.balance(D(300),D(0),30,30),D(0))
        # Standard independently calculable loan: 100,000 at 6%, 30 years.
        payment=D(100000)*model.constant(D('.06'),30)/12
        self.assertEqual(model.money(payment),D('599.55'))
        self.assertEqual(model.money(model.balance(D(100000),D('.06'),30,30)),D('0.00'))

    def test_full_capital_scope_includes_land_and_every_category(self):
        result=model.evaluate(request())
        self.assertEqual(result['total_development_cost_usd'],'53262500.00')
        req=request();req['capital']['lines']=[x for x in req['capital']['lines'] if x['category']!='remediation']
        with self.assertRaisesRegex(ValueError,'every capital'):model.evaluate(req)

    def test_annual_support_expiry_is_not_permanent_income(self):
        req=request();op=req['operations'];op['income'][0].update(annual_growth='0',end_year=10)
        result=model.evaluate(req)
        self.assertEqual(result['annual'][10]['effective_gross_income_usd'],'0.00')
        self.assertEqual(result['modeled_primary_loan_usd'],'0.00')
        self.assertIn(11,result['cashflow_shortfall_years'])
        self.assertIsNone(result['annual'][10]['dscr'])
        self.assertIsNone(result['annual'][10]['meets_declared_dscr'])
        self.assertIsNone(result['annual'][10]['additional_effective_income_for_coverage_usd'])
        self.assertLess(D(result['annual'][10]['cash_after_reserves_debt_and_below_line_usd']),0)

    def test_later_cost_pressure_changes_debt_and_exposes_year_one_shortcut(self):
        req=request();req['operations']['income'][0]['annual_growth']='0'
        long=model.evaluate(req);req['debt']['sizing_years']=1;short=model.evaluate(req)
        self.assertGreater(D(short['modeled_primary_loan_usd']),D(long['modeled_primary_loan_usd']))
        self.assertTrue(short['coverage_breach_years']);self.assertFalse(long['coverage_breach_years'])

    def test_fully_amortized_debt_can_end_before_projection_without_phantom_service(self):
        req=request();req['debt'].update(amortization_years=15,term_years=15)
        result=model.evaluate(req)
        self.assertGreater(D(result['annual'][14]['primary_debt_service_usd']),0)
        self.assertEqual(D(result['annual'][15]['primary_debt_service_usd']),0)
        self.assertEqual(D(result['annual'][15]['primary_loan_balance_year_end_usd']),0)
        self.assertIsNone(result['annual'][15]['dscr'])
        self.assertEqual(result['primary_debt_sizing_years'],15)

    def test_post_debt_operating_deficit_is_not_a_dscr_covenant_breach(self):
        req=request();req['debt'].update(amortization_years=10,term_years=10)
        req['operations']['income'][0].update(annual_usd='1000000',annual_growth='0')
        result=model.evaluate(req);last=result['annual'][-1]
        self.assertGreater(D(result['modeled_primary_loan_usd']),0)
        self.assertIsNone(last['dscr']);self.assertIsNone(last['required_dscr'])
        self.assertIsNone(last['meets_declared_dscr'])
        self.assertNotIn(20,result['coverage_breach_years'])
        self.assertIn(20,result['cashflow_shortfall_years'])

    def test_balloon_is_a_cash_obligation_at_maturity_not_silently_refinanced(self):
        req=request();req['debt'].update(term_years=20,absolute_cap_usd='5000000')
        result=model.evaluate(req)
        self.assertGreater(D(result['balloon_at_term_usd']),0)
        self.assertEqual(result['annual'][-1]['maturity_principal_due_usd'],result['balloon_at_term_usd'])
        self.assertEqual(result['annual'][-1]['primary_loan_balance_before_maturity_payment_usd'],result['balloon_at_term_usd'])
        self.assertEqual(result['annual'][-1]['primary_loan_balance_year_end_usd'],'0.00')
        self.assertLess(D(result['annual'][-1]['cash_after_reserves_debt_and_below_line_usd']),0)
        req['debt']['term_years']=15
        with self.assertRaisesRegex(ValueError,'refinancing'):model.evaluate(req)

    def test_staged_coverage_schedule_is_applied_year_by_year(self):
        req=request();req['operations']['income'][0]['annual_growth']='0'
        strict=model.evaluate(req)
        req['debt']['minimum_dscr_by_year']=['1.15']+['1.00']*19
        staged=model.evaluate(req)
        self.assertGreater(D(staged['modeled_primary_loan_usd']),D(strict['modeled_primary_loan_usd']))
        self.assertEqual(staged['annual'][0]['required_dscr'],'1.15')
        self.assertEqual(staged['annual'][-1]['required_dscr'],'1.00')
        self.assertFalse(staged['coverage_breach_years'])
        req['debt']['minimum_dscr_by_year']=['1.15']
        with self.assertRaisesRegex(ValueError,'every projection year'):model.evaluate(req)

    def test_reserve_counted_once_in_cash_and_coverage_choice_is_explicit(self):
        req=request();req['debt']['absolute_cap_usd']='1000000'
        a=model.evaluate(req);req['operations']['reserve_deducted_for_coverage']=False;b=model.evaluate(req)
        self.assertEqual(a['annual'][0]['cash_after_reserves_debt_and_below_line_usd'],b['annual'][0]['cash_after_reserves_debt_and_below_line_usd'])
        self.assertEqual(D(b['annual'][0]['coverage_noi_usd'])-D(a['annual'][0]['coverage_noi_usd']),D(24000))

    def test_debt_capacity_is_distinct_from_the_scenario_amount_actually_needed(self):
        req=request();req['sources'][0]['amount_usd']='53262500'
        result=model.evaluate(req)
        self.assertGreater(D(result['maximum_primary_loan_capacity_usd']),0)
        self.assertEqual(result['modeled_primary_loan_usd'],'0.00')
        self.assertIn('funding_need',result['binding_debt_caps'])
        self.assertEqual(result['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd'],'0.00')
        self.assertFalse(result['modeled_primary_loan_is_committed'])
        self.assertIsNone(result['annual'][0]['dscr'])

    def test_ltc_counts_subordinate_debt_and_proposed_sources_are_not_commitments(self):
        req=request();req['debt']['maximum_total_ltc']='0.1'
        req['sources'].append({'id':'subordinate','kind':'soft_loan','amount_usd':'5000000','status':'proposed','basis':req['basis']})
        result=model.evaluate(req)
        self.assertEqual(result['modeled_primary_loan_usd'],'326250.00')
        self.assertEqual(result['binding_debt_caps'],['loan_to_cost'])
        self.assertEqual(result['committed_other_sources_usd'],'0.00')
        self.assertEqual(result['capital_not_covered_by_committed_sources_usd'],result['total_development_cost_usd'])

    def test_subordinate_debt_alone_can_breach_combined_leverage(self):
        req=request();req['debt']['maximum_total_ltc']='0.01'
        req['sources'].append({'id':'subordinate','kind':'soft_loan','amount_usd':'1000000','status':'proposed','basis':req['basis']})
        result=model.evaluate(req)
        self.assertEqual(result['modeled_primary_loan_usd'],'0.00')
        self.assertIn('declared_subordinate_principal_exceeds_combined_ltc_limit',result['financing_limit_breaches'])

    def test_missing_appraisal_cannot_silently_remove_selected_ltv_constraint(self):
        req=request();req['debt']['maximum_ltv']='0.8'
        with self.assertRaisesRegex(ValueError,'property value'):model.evaluate(req)
        req['debt']['appraised_value_usd']='10000000'
        self.assertEqual(model.evaluate(req)['modeled_primary_loan_usd'],'8000000.00')

    def test_bad_units_nonfinite_booleans_unknowns_and_duplicate_ids_block(self):
        mutations=[lambda r:r['capital']['lines'][0].update(usd=True),lambda r:r['capital']['lines'][0].update(usd='NaN'),lambda r:r['debt'].update(annual_interest_rate='-0.01'),lambda r:r['program'].update(homes=True),lambda r:r.update(unexpected=1),lambda r:r['operations']['income'].append(copy.deepcopy(r['operations']['income'][0])),lambda r:r['basis'].update(kind='agency_approved')]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                req=request();mutate(req)
                with self.assertRaises(ValueError):model.evaluate(req)

    def test_rounding_never_creates_unexplained_coverage_failure(self):
        result=model.evaluate(request())
        self.assertFalse(result['coverage_breach_years'])
        self.assertEqual(result['annual'][0]['dscr'],'1.150000')
        self.assertIsNone(model.evaluate(self.no_debt_request())['annual'][0]['dscr'])

    @staticmethod
    def no_debt_request():
        req=request();req['debt']['absolute_cap_usd']='0';return req

    def test_selected_stanyan_budget_arithmetic_and_known_one_dollar_difference(self):
        result=model.evaluate(engine.load(ROOT/'config/underwriting/stanyan-separate-budget-control.json'))
        year=result['annual'][0]
        self.assertEqual(result['total_development_cost_usd'],'169152004.00')
        self.assertEqual(year['effective_gross_income_usd'],'3946019.00')
        self.assertEqual(D(year['effective_gross_income_usd'])-D(3946018),D(1))
        self.assertEqual(year['coverage_noi_usd'],'1272978.00')
        self.assertEqual(year['cash_after_reserves_debt_and_below_line_usd'],'207183.00')
        self.assertEqual(year['dscr'],'1.215942')
        self.assertEqual(result['modeled_primary_loan_usd'],'0.00')

    def test_stanyan_supportable_loan_uses_printed_terms_without_erasing_residual(self):
        req=engine.load(ROOT/'config/underwriting/stanyan-supportable-loan-control.json')
        result=model.evaluate(req)
        self.assertEqual(result['modeled_primary_loan_usd'],'12793048.57')
        self.assertEqual(D(result['modeled_primary_loan_usd'])-D(12793046),D('2.57'))
        self.assertEqual(result['annual'][0]['primary_debt_service_usd'],'1106937.39')

    def test_schema_accepts_all_reference_requests_and_rejects_unknown_fields(self):
        import jsonschema
        schema=engine.load(ROOT/'src/housing_underwriting/request.schema.json')
        for path in (ROOT/'config/underwriting').glob('*.json'):
            req=engine.load(path);jsonschema.validate(req,schema);model.validate(req)
        req=request();req['program']['net_new_homes']=60
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(req,schema)

    def test_verify_recomputes_outputs_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'run';engine.build(request(),out)
            self.assertEqual(engine.verify(out)['status'],'passed')
            with self.assertRaises(FileExistsError):engine.build(request(),out)
            result=engine.load(out/'results.json');result['modeled_primary_loan_usd']='999999999.00';engine.save(out/'results.json',result);engine.seal(out,'underwriting')
            with self.assertRaisesRegex(ValueError,'recomputation'):engine.verify(out)

    def test_reported_inputs_need_declared_reference_and_retained_bytes_verify(self):
        req=request();req['program']['basis']={**req['basis'],'kind':'reported_input'}
        with self.assertRaisesRegex(ValueError,'source reference'):model.evaluate(req)
        req=request()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'source.txt';source.write_text('Independent source bytes, synthetic fixture')
            out=root/'run';engine.build(req,out,{'hpd-ncf-2025':source})
            self.assertEqual(engine.verify(out)['status'],'passed')
            ref=next(x for x in engine.load(out/'references.json') if x['retention']=='retained_bytes')
            (out/ref['body_path']).write_text('Changed')
            with self.assertRaisesRegex(ValueError,'Changed'):engine.verify(out)


if __name__=='__main__':unittest.main()
