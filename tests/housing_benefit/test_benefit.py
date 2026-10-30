import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from housing_workflow.contracts import digest,dumps,load,save
from housing_benefit import contracts as c,engine,model,methods,sources

ROOT=engine.ROOT
ANALYSIS=ROOT/'examples/analysis-recipe/base'
REF=ROOT/'examples/affordability-inputs/reference-source'
REQ=load(ROOT/'examples/affordability-inputs/request.json')
SENSITIVITY=load(ROOT/'examples/affordability-inputs/higher-utilities.json')


def compiled(req=None,ref=None):
    ir=model.compile_model(copy.deepcopy(req or REQ),ref or sources.validate_source(REF),load(ANALYSIS/'ir.json'),digest((ANALYSIS/'ir.json').read_bytes()),digest(dumps(req or REQ).encode()),digest((REF/'receipt.json').read_bytes()))
    model.validate_claims(ir);return ir


def claim_map(ir):return {x['id']:x for x in ir['claims']}

class Benefit(unittest.TestCase):
    def test_constructed_tradeoff_no_winner_and_unknowns(self):
        ir=compiled();claims=claim_map(ir)
        self.assertEqual([claims[x['claim']]['value'] for x in ir['comparisons']],[12,-8,12])
        self.assertEqual(claims['program.program_a.for_lower_income.cost_test_homes']['value'],16)
        self.assertEqual(claims['program.program_b.for_lower_income.cost_test_homes']['value'],8)
        self.assertIsNone(ir['overall_ranking']);self.assertEqual(ir['eligibility'],'not_determined')
        self.assertEqual(ir['project_attributable_benefit'],'not_estimated')
        for k in ['review.no_action','review.occupancy','review.access','program.program_a.delivery','program.program_b.delivery']:
            self.assertEqual(claims[k]['kind'],'unknown');self.assertIsNone(claims[k]['value'])
    def test_reference_fact_separate_from_hypothetical_household(self):
        ir=compiled();claims=claim_map(ir)
        fact=claims['reference.ami30_income_four'];assumption=claims['profile.lower_income.annual_income_usd']
        self.assertEqual(fact['value'],'48600.00');self.assertEqual(fact['kind'],'fact')
        self.assertEqual(assumption['kind'],'assumption');self.assertEqual(assumption['inputs'],[fact['id']])
        self.assertEqual(fact['references'][0]['page'],6);self.assertIn('$48,600',fact['references'][0]['quote'])
    def test_utility_change_recomputes_correct_profile_only(self):
        ir=compiled(SENSITIVITY);claims=claim_map(ir)
        self.assertEqual(claims['program.program_a.lower_rent.gross_monthly_cost']['value'],'1250.00')
        self.assertEqual(claims['program.program_a.for_lower_income.cost_test_homes']['value'],0)
        self.assertEqual(claims['program.program_a.for_higher_income.cost_test_homes']['value'],24)
        self.assertEqual(claims['program.program_b.for_lower_income.cost_test_homes']['value'],8)
        self.assertEqual(claims['program.program_a.declared_homes']['value'],24)
    def test_exact_threshold_equality_passes_one_cent_over_fails_before_rounding(self):
        for rent,expected in [('1115.00',True),('1115.01',False)]:
            r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['monthly_rent_usd']['value']=rent
            ir=compiled(r);c=claim_map(ir)
            self.assertEqual(c['program.program_a.lower_rent.for_lower_income.cost_test']['value'],expected)
    def test_decimal_cost_addition_is_exact(self):
        r=copy.deepcopy(REQ);b=r['programs'][0]['bins'][0]
        b['monthly_rent_usd']['value']='0.10';b['tenant_utilities_usd']['value']='0.20'
        c=claim_map(compiled(r));self.assertEqual(c['program.program_a.lower_rent.gross_monthly_cost']['value'],'0.30')
        self.assertEqual(c['program.program_a.lower_rent.annual_cost']['value'],'3.60')
    def test_wrong_bedroom_is_not_counted_as_suitable_or_eligible(self):
        r=copy.deepcopy(REQ);r['profiles'][0]['bedrooms']=1;c=claim_map(compiled(r))
        self.assertEqual(c['program.program_a.for_lower_income.cost_test_homes']['value'],0)
        self.assertTrue(c['program.program_a.lower_rent.for_lower_income.cost_test']['value'])
        self.assertFalse(c['program.program_a.lower_rent.for_lower_income.bedroom_test']['value'])
    def test_household_size_reference_mismatch_blocks(self):
        r=copy.deepcopy(REQ);r['profiles'][0]['household_size']=1
        with self.assertRaisesRegex(ValueError,'household size'):compiled(r)
    def test_rent_reference_cannot_be_used_as_annual_income(self):
        r=copy.deepcopy(REQ);r['profiles'][0]['income_reference_id']='ami30_rent_two'
        with self.assertRaisesRegex(ValueError,'income reference'):compiled(r)
    def test_restriction_duration_changes_row_not_cost_count(self):
        a=claim_map(compiled());r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['restriction_years']['value']=40
        b=claim_map(compiled(r))
        self.assertEqual(b['program.program_a.lower_rent.restriction_years']['value'],40)
        self.assertEqual(a['program.program_a.for_lower_income.cost_test_homes']['value'],b['program.program_a.for_lower_income.cost_test_homes']['value'])
    def test_fractional_boolean_negative_unit_counts_block(self):
        for v in [1.2,True,-1,'16']:
            r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['homes']['value']=v
            with self.subTest(v=v),self.assertRaises(ValueError):compiled(r)
    def test_invalid_money_inputs_block(self):
        for v in [1000,True,'NaN','Infinity','-1.00','1e3','0010','1.001']:
            r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['monthly_rent_usd']['value']=v
            with self.subTest(v=v),self.assertRaises(ValueError):compiled(r)
    def test_unit_bin_totals_must_reconcile(self):
        r=copy.deepcopy(REQ);r['programs'][0]['total_homes']['value']=25
        with self.assertRaisesRegex(ValueError,'reconcile'):compiled(r)
    def test_duplicate_ids_missing_rationales_and_unknown_fields_block(self):
        mutations=[lambda r:r['profiles'][1].update(id=r['profiles'][0]['id']),lambda r:r['programs'][1].update(id=r['programs'][0]['id']),lambda r:r['programs'][0]['bins'][1].update(id='lower_rent'),lambda r:r['programs'][0]['bins'][0]['homes'].update(rationale=''),lambda r:r.update(unit_count_from_area=34)]
        for mutate in mutations:
            r=copy.deepcopy(REQ);mutate(r)
            with self.subTest(mutate=mutate),self.assertRaises(ValueError):compiled(r)
    def test_impossible_threshold_blocks(self):
        for v in ['0.00','100.01']:
            r=copy.deepcopy(REQ);r['cost_threshold_percent']['value']=v
            with self.assertRaisesRegex(ValueError,'Threshold'):compiled(r)
    def test_cannot_clear_occupancy_delivery_or_no_action_without_adapter(self):
        for path in ['occupancy','no_action','delivery']:
            r=copy.deepcopy(REQ);target=r['programs'][0]['delivery'] if path=='delivery' else r[path];target['status']='known'
            with self.assertRaisesRegex(ValueError,'cannot clear'):compiled(r)
        r=copy.deepcopy(REQ);r['programs'][0]['commitment_status']='secured'
        with self.assertRaisesRegex(ValueError,'evidence adapter'):compiled(r)
    def test_wrong_parcel_and_mismatched_price_year_block(self):
        r=copy.deepcopy(REQ);r['site_bbl']='2028560051'
        with self.assertRaisesRegex(ValueError,'parcel mismatch'):compiled(r)
        r=copy.deepcopy(REQ);r['price_year']=2026
        with self.assertRaisesRegex(ValueError,'vintages differ'):compiled(r)
    def test_changed_source_bytes_fail_without_rehash(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'refs';shutil.copytree(REF,root)
            (root/'passages.txt').write_text((root/'passages.txt').read_text().replace('$48,600','$48,700'))
            with self.assertRaisesRegex(ValueError,'passage hash'):sources.validate_source(root)
    def test_mixed_reference_table_vintages_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'refs';shutil.copytree(REF,root);r=load(root/'receipt.json');r['income_year']=2026;save(root/'receipt.json',r)
            with self.assertRaisesRegex(ValueError,'Mixed-vintage'):sources.validate_source(root)
    def test_source_columns_and_duplicate_ami_rows_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'refs';shutil.copytree(REF,root);r=load(root/'receipt.json');r['column_order'].reverse();save(root/'receipt.json',r)
            with self.assertRaisesRegex(ValueError,'column mapping'):sources.validate_source(root)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'refs';shutil.copytree(REF,root);lines=(root/'passages.txt').read_text().splitlines();lines[2]=lines[1]
            (root/'passages.txt').write_text('\n'.join(lines)+'\n');r=load(root/'receipt.json');r['passages_sha256']=digest((root/'passages.txt').read_bytes());save(root/'receipt.json',r)
            with self.assertRaisesRegex(ValueError,'duplicate'):sources.validate_source(root)
    def test_missing_graph_dependency_cycle_and_unknown_promotion_block(self):
        ir=compiled();c=claim_map(ir);c['review.occupancy']['value']='no displacement'
        with self.assertRaisesRegex(ValueError,'Unknown promoted'):model.validate_claims(ir)
        ir=compiled();c=claim_map(ir);c['program.program_a.lower_rent.gross_monthly_cost']['inputs'][0]='nonexistent'
        with self.assertRaisesRegex(ValueError,'Missing claim'):model.validate_claims(ir)
        ir=compiled();c=claim_map(ir);cid='program.program_a.lower_rent.gross_monthly_cost';c[cid]['inputs'][0]=cid
        with self.assertRaisesRegex(ValueError,'cycle'):model.validate_claims(ir)
    def test_method_type_signature_and_version_block(self):
        ir=compiled();c=claim_map(ir);cid='program.program_a.lower_rent.gross_monthly_cost'
        c[cid]['inputs'][0]='profile.lower_income.annual_income_usd'
        with self.assertRaisesRegex(ValueError,'semantic input'):model.validate_claims(ir)
        ir=compiled();claim_map(ir)[cid]['method']='housing.gross_monthly_cost@2'
        with self.assertRaisesRegex(ValueError,'Unsupported versioned'):model.validate_claims(ir)
    def test_quantity_scalar_types_block_even_if_python_bool_equals_one(self):
        ir=compiled();claim_map(ir)['program.program_a.lower_rent.homes']['value']=True
        with self.assertRaisesRegex(ValueError,'integer quantity'):model.validate_claims(ir)
    def test_schemas_validate_actual_semantic_ir_and_requests(self):
        import jsonschema
        for req in [REQ,SENSITIVITY]:jsonschema.validate(req,load(ROOT/'src/housing_benefit/request.schema.json'))
        ir=compiled();schema=load(ROOT/'src/housing_benefit/ir.schema.json');jsonschema.validate(ir,schema)
        ir['overall_ranking']='program_b'
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(ir,schema)
    def test_duplicate_json_keys_and_nonfinite_constants_block(self):
        for text in ['{"value":1,"value":2}','{"x":NaN}','{"x":Infinity}']:
            with tempfile.TemporaryDirectory() as d:
                p=Path(d)/'bad.json';p.write_text(text)
                with self.assertRaises(ValueError):c.read_json(p)
    def test_build_and_replay_are_byte_identical_and_preserve_upstream(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a',Path(d)/'b';engine.build(ANALYSIS,REF,REQ,a);engine.replay(a,b)
            self.assertEqual(engine.inventory(a),engine.inventory(b))
            self.assertEqual((a/'analysis-run/manifest.json').read_bytes(),(ANALYSIS/'manifest.json').read_bytes())
            engine.verify(b)
    def test_impact_tracks_utility_dependency_and_does_not_flag_other_program(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,REQ,root);report=engine.impact(root,SENSITIVITY)
            self.assertEqual(report['directly_changed_claims'],['program.program_a.lower_rent.tenant_utilities_usd'])
            self.assertIn('program.program_a.for_lower_income.cost_test_homes',report['affected_claims'])
            self.assertFalse(any(cid.startswith('program.program_b.') for cid in report['affected_claims']))
            self.assertIn('packet.html',report['requires_regeneration'])
    def test_duration_impact_regenerates_packet_but_not_cost_counts(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,REQ,root);r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['restriction_years']['value']=40
            report=engine.impact(root,r)
            self.assertEqual(report['affected_claims'],['program.program_a.lower_rent.restriction_years'])
            target=Path(d)/'changed';engine.replay(root,target,r)
            self.assertNotEqual((root/'packet.html').read_bytes(),(target/'packet.html').read_bytes())
    def test_rehashed_tampered_request_stales_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,REQ,root);save(root/'request.json',SENSITIVITY)
            with self.assertRaisesRegex(ValueError,'artifact hash'):engine.verify(root)
            m=load(root/'manifest.json');m['files']=engine.inventory(root);save(root/'manifest.json',m)
            with self.assertRaisesRegex(ValueError,'differs from retained'):engine.verify(root)
    def test_known_corrupt_output_and_reusing_directory_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,REQ,root)
            with self.assertRaisesRegex(ValueError,'new empty'):engine.build(ANALYSIS,REF,REQ,root)
            (root/'packet.html').write_text('best project; no displacement')
            with self.assertRaisesRegex(ValueError,'artifact hash'):engine.verify(root)
    def test_unknown_gate_removal_stales_projection_even_after_rehash(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,REQ,root);ir=load(root/'ir.json')
            ir['claims']=[x for x in ir['claims'] if x['id']!='review.occupancy'];save(root/'ir.json',ir)
            m=load(root/'manifest.json');m['files']=engine.inventory(root);save(root/'manifest.json',m)
            with self.assertRaisesRegex(ValueError,'differs from retained'):engine.verify(root)
    def test_program_text_cannot_execute_html(self):
        r=copy.deepcopy(REQ);r['question']='<script>alert(1)</script>'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,REF,r,root);page=(root/'packet.html').read_text()
            self.assertNotIn('<script>',page);self.assertIn('&lt;script&gt;',page)
    def test_source_package_extra_file_and_traversal_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'refs';shutil.copytree(REF,root);(root/'extra.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'inventory'):sources.validate_source(root)
    def test_cli_invalid_input_returns_blocked_and_no_released_run(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);r=copy.deepcopy(REQ);r['price_year']=2026;save(root/'input.json',r)
            result=subprocess.run([sys.executable,'-m','housing_benefit','build','--analysis',str(ANALYSIS),'--references',str(REF),'--input',str(root/'input.json'),'--out',str(root/'out')],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2);self.assertIn('blocked',result.stderr);self.assertFalse((root/'out/manifest.json').exists())
    def test_csv_includes_provenance_and_neutralizes_formula_text(self):
        import csv,io
        r=copy.deepcopy(REQ);r['programs'][0]['bins'][0]['homes']['rationale']='=HYPERLINK("https://example.com")'
        from housing_benefit.packet import project
        out=project(compiled(r),sources.validate_source(REF))
        rows={row['claim_id']:row for row in csv.DictReader(io.StringIO(out['claim-register.csv']))}
        self.assertTrue(rows['program.program_a.lower_rent.homes']['rationale'].startswith("'="))
        self.assertIn('source_pdf_sha256',rows['reference.ami30_income_four']['references'])
    def test_supplied_home_equivalents_cannot_replace_integer_offer_bins(self):
        r=copy.deepcopy(REQ);r['programs'][0].pop('bins');r['programs'][0]['home_equivalents']=34.0
        with self.assertRaises(ValueError):compiled(r)
    def test_method_metadata_matches_implementation(self):engine.validate_method_registry()
    def test_saved_examples_when_present(self):
        for name in ['affordability-comparison','affordability-utilities']:
            p=ROOT/'examples'/name
            if p.exists():engine.verify(p)

if __name__=='__main__':unittest.main()
