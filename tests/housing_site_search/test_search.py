"""Counterexamples for broad discovery, explicit targets and conditional models. MIT."""
import copy
from decimal import Decimal as D
import unittest
from housing_common.local_outputs import ROOT
from housing_underwriting.engine import load
from housing_site_search.model import evaluate,build_trial_request,validate


def template():return load(ROOT/'config/underwriting/rental-60-lower-rent.json')
def request():
    req=load(ROOT/'config/site-search/transit-rental-targets.json');req['program_grid']['homes']=[60];req['land_price_per_lot_sf_values']=['100']
    req['targets'].update(max_unallocated_capital_per_home_usd=None,max_required_zoning_far=None)
    return req


def lot(identity='2020000001'):
    return {'bbl':identity,'address':'SYNTHETIC TEST LOT','in_recorded_nonhousing_set':True,'current_use_category':'recorded_nonhousing',
            'recorded_lot_area_sf':10000,'recorded_residential_far':8,'recorded_affordable_residential_far':9,
            'dwelling_review':{'status':'no_positive_returned_housing_signal'},'zoning_path':{'path':'housing_permitted_by_general_use_rule'},'review_lane':'other_nonhousing_review','flags':[],
            'public_context':{'nearest_station':{'straight_line_m':100},'industrial_zone_point_relation':'outside_returned_polygons'}}


class Search(unittest.TestCase):
    def test_no_additional_far_or_auto_use_admission_requirement(self):
        row=lot();result=evaluate({'lots':[row]},template(),request())
        self.assertEqual(result['counts']['recorded_nonhousing_lots'],1)
        self.assertEqual(result['trials'][0]['status'],'matches_declared_targets')
        self.assertLess(D(result['trials'][0]['required_zoning_far']),D(row['recorded_residential_far']))
        self.assertIsNone(result['trials'][0]['professional_feasibility'])

    def test_all_lots_retained_and_missing_station_is_unknown_not_zero(self):
        missing=lot();missing['public_context']['nearest_station']=None
        housing=lot('2020000002');housing.update(in_recorded_nonhousing_set=False,current_use_category='housing_recorded')
        result=evaluate({'lots':[missing,housing]},template(),request())
        self.assertEqual(len(result['lots']),2)
        self.assertEqual(result['trials'][0]['status'],'needs_review')
        self.assertIn('station_proximity_unknown',result['trials'][0]['unknown_targets'])
        self.assertEqual(result['lots'][1]['trial_count'],0)

    def test_industrial_policy_filter_is_explicit_and_does_not_erase_lot(self):
        row=lot();row['public_context']['industrial_zone_point_relation']='inside'
        req=request();a=evaluate({'lots':[row]},template(),req)
        self.assertIn('industrial_policy_area_point_review',a['trials'][0]['failed_targets'])
        req['targets']['require_lot_point_outside_ibz']=False;b=evaluate({'lots':[row]},template(),req)
        self.assertEqual(b['trials'][0]['status'],'matches_declared_targets')
        self.assertEqual(len(a['lots']),len(b['lots']))

    def test_unknown_ibz_and_pipeline_context_cannot_match_required_known_targets(self):
        row=lot();row['public_context']['industrial_zone_point_relation']='unknown';row['flags']=['zap_projects_context_incomplete']
        result=evaluate({'lots':[row]},template(),request())
        self.assertEqual(result['trials'][0]['status'],'needs_review')
        self.assertEqual(len(result['trials'][0]['unknown_targets']),2)

    def test_historical_housing_signals_and_missing_review_never_become_clean_matches(self):
        for status,expected in [('positive_returned_housing_signal','does_not_match_declared_targets'),('housing_signal_coverage_unknown','needs_review'),(None,'needs_review')]:
            row=lot();row['dwelling_review']={'status':status}
            result=evaluate({'lots':[row]},template(),request())
            self.assertEqual(result['trials'][0]['status'],expected)
            self.assertEqual(len(result['lots']),1)
        req=request();req['targets']['require_no_positive_returned_housing_signal']=False
        row=lot();row['dwelling_review']={'status':'positive_returned_housing_signal'}
        self.assertEqual(evaluate({'lots':[row]},template(),req)['trials'][0]['status'],'matches_declared_targets')

    def test_fixed_template_commitment_does_not_become_commitment_to_another_site(self):
        base=template();base['sources'][0]['status']='committed'
        req=request();trial=build_trial_request(base,req,lot(),60,D(100),'synthetic-trial')
        self.assertEqual(trial['sources'][0]['status'],'proposed')
        self.assertEqual(trial['sources'][0]['basis']['kind'],'analyst_assumption')
        self.assertEqual(base['sources'][0]['status'],'committed')

    def test_required_area_obeys_distinct_net_gross_and_zoning_units(self):
        req=request();req['program_grid'].update(net_sf_per_home='700',net_efficiency='0.8',residential_share_of_gross='0.875',gross_per_zoning_sf='1.2')
        result=evaluate({'lots':[lot()]},template(),req)['trials'][0]
        self.assertEqual(result['required_gross_area_sf'],'60000.00')
        self.assertEqual(result['required_zoning_area_proxy_sf'],'50000.00')
        self.assertEqual(result['required_zoning_far'],'5.000000')

    def test_land_price_is_explicit_scenario_and_increases_gap(self):
        req=request();req['land_price_per_lot_sf_values']=['100','200']
        result=evaluate({'lots':[lot()]},template(),req)
        a,b=result['trials'];self.assertEqual(D(b['total_development_cost_usd'])-D(a['total_development_cost_usd']),D(1000000))
        self.assertGreater(D(b['unallocated_capital_per_home_usd']),D(a['unallocated_capital_per_home_usd']))
        self.assertTrue(a['pareto_under_declared_metrics']);self.assertFalse(b['pareto_under_declared_metrics'])

    def test_maturity_cash_shortfall_cannot_match_cashflow_target(self):
        base=template();base['debt'].update(term_years=20,absolute_cap_usd='5000000')
        result=evaluate({'lots':[lot()]},base,request())
        self.assertIn('cashflow_below_declared_target',result['trials'][0]['failed_targets'])

    def test_target_failure_and_active_pipeline_are_retained_with_reasons(self):
        row=lot();row['flags']=['active_or_on_hold_zap_project_review']
        req=request();req['targets']['max_required_zoning_far']='1'
        result=evaluate({'lots':[row]},template(),req)
        self.assertIn('required_far_exceeds_declared_scenario_cap',result['trials'][0]['failed_targets'])
        self.assertIn('active_linked_zap_project',result['trials'][0]['failed_targets'])
        self.assertEqual(result['detailed_trial_ids'],[])

    def test_tenant_rent_time_scope_is_explicit_and_later_growth_is_visible(self):
        req=request();base=template()
        first=evaluate({'lots':[lot()]},base,req)['trials'][0]
        self.assertEqual(first['status'],'matches_declared_targets')
        self.assertGreater(D(first['peak_monthly_scheduled_tenant_rent_per_home_usd']),D(2000))
        req['targets']['tenant_rent_cap_scope']='all_projection_years'
        all_years=evaluate({'lots':[lot()]},base,req)['trials'][0]
        self.assertIn('scheduled_tenant_rent_exceeds_target',all_years['failed_targets'])

    def test_unknown_area_keeps_unmodeled_lot_visible(self):
        row=lot();row['recorded_lot_area_sf']=None;result=evaluate({'lots':[row]},template(),request())
        self.assertEqual(result['trials'],[]);self.assertEqual(result['lots'][0]['status'],'needs_review')
        self.assertIn('lot_area_missing_or_invalid',result['lots'][0]['reasons'])

    def test_low_capital_gap_cannot_hide_leverage_breach(self):
        base=template();base['debt']['maximum_total_ltc']='0.01'
        base['sources'].append({'id':'subordinate','kind':'soft_loan','amount_usd':'1000000','status':'proposed','basis':base['basis']})
        req=request();req['scaling']['sources']['subordinate']='fixed'
        result=evaluate({'lots':[lot()]},base,req)
        self.assertEqual(result['trials'][0]['status'],'does_not_match_declared_targets')
        self.assertIn('declared_subordinate_principal_exceeds_combined_ltc_limit',result['trials'][0]['failed_targets'])

    def test_missing_scaling_unknown_keys_and_invalid_targets_block(self):
        for mutate in [lambda r:r['scaling']['expenses'].pop('taxes'),lambda r:r.update(extra=1),lambda r:r['targets'].update(require_lot_point_outside_ibz='yes'),lambda r:r['program_grid'].update(homes=[True]),lambda r:r['targets'].update(tenant_rent_stream_ids=['imaginary']),lambda r:r.update(land_price_per_lot_sf_values=['100','100.0']),lambda r:r['basis'].update(reference_ids=['unrecognized'])]:
            req=request();mutate(req)
            with self.assertRaises(ValueError):validate(req,template())

    def test_comparison_includes_cost_and_loan_changes_even_when_goal_metrics_stay_equal(self):
        import tempfile
        from pathlib import Path
        from housing_common.packages import save
        from housing_site_search.comparison import differences
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,cost,loan in [('left','1000000','100000'),('right','1100000','200000')]:
                p=root/name;(p/'discovery').mkdir(parents=True);(p/'underwriting-template').mkdir()
                save(p/'discovery/manifest.json',{'same_source':True})
                save(p/'request.json',{});save(p/'underwriting-template/request.json',{})
                save(p/'results.json',{'counts':{'lots_by_status':{'matches_declared_targets':1}},'trials':[{'id':'same-trial','bbl':'2020000001','status':'matches_declared_targets','required_zoning_far':'4','unallocated_capital_per_home_usd':'300000','total_development_cost_usd':cost,'modeled_primary_loan_usd':loan}]})
            result=differences(root/'left',root/'right')
            delta=result['changed_trials'][0]['changes']
            self.assertIn('total_development_cost_usd',delta)
            self.assertIn('modeled_primary_loan_usd',delta)
            self.assertEqual(result['entered_matching_lots'],[])

    def test_trial_budget_is_bounded_before_expensive_modeling(self):
        req=request();req['program_grid']['homes']=[40,60,100];req['land_price_per_lot_sf_values']=['100','200']
        with self.assertRaisesRegex(ValueError,'25,000'):evaluate({'lots':[lot()]*5000},template(),req)


if __name__=='__main__':unittest.main()
