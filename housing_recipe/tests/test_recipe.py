import copy
from pathlib import Path
import tempfile
import unittest
from housing_workflow import engine as evidence
from housing_workflow.contracts import digest, load, save
from housing_workflow.tests.test_workflow import make_run
from housing_recipe import engine
from housing_recipe.recipe import compile_recipe, impact

ROOT=engine.ROOT
SOURCE=ROOT/'examples/parcel-investigation'
IR=load(SOURCE/'ir.json')
BASE=load(ROOT/'recipes/area-budget.json')
RESERVE=load(ROOT/'recipes/area-budget-with-reserve.json')
GROSS=load(ROOT/'recipes/area-budget-gross-method.json')

def claims(ir):return {c['id']:c for c in ir['claims']}

class Recipes(unittest.TestCase):
    def test_base_reproduces_current_area_model_and_preserves_evidence(self):
        ir,trace=compile_recipe(BASE,IR);a=claims(ir);b=claims(IR)
        for cid,c in b.items():
            if not cid.startswith('scenario.'):self.assertEqual(a[cid],c)
        for cid in ['scenario.residential_gross_sf','scenario.residential_net_sf','scenario.home_equivalents','scenario.gross_to_recorded_lot_ratio']:
            self.assertEqual(a[cid]['value'],b[cid]['value'])
        self.assertEqual(len(trace['review_gates']),8)
    def test_inserted_step_changes_result_and_trace(self):
        ir,trace=compile_recipe(RESERVE,IR)
        self.assertEqual(claims(ir)['scenario.home_equivalents']['value'],30)
        order=[s['id'] for s in trace['steps']]
        self.assertLess(order.index('recipe.after_reserve_sf'),order.index('scenario.residential_net_sf'))
    def test_replaced_method_same_answer_still_has_impact(self):
        a,_=compile_recipe(BASE,IR);b,_=compile_recipe(GROSS,IR)
        self.assertEqual(claims(a)['scenario.home_equivalents']['value'],claims(b)['scenario.home_equivalents']['value'])
        report=impact(a,BASE,b,GROSS)
        self.assertIn('scenario.home_equivalents',report['directly_changed_claims_or_steps'])
        self.assertNotIn('scenario.home_equivalents',report['numerically_changed_claims'])
        self.assertIn('image-prompts.json',report['requires_regeneration'])
    def test_parameter_impact_is_transitive_and_does_not_flag_unrelated_ratio(self):
        r=copy.deepcopy(BASE);r['parameters'][3]['value']=680
        a,_=compile_recipe(BASE,IR);b,_=compile_recipe(r,IR);report=impact(a,BASE,b,r)
        self.assertEqual(claims(b)['scenario.home_equivalents']['value'],40)
        self.assertEqual(report['directly_changed_claims_or_steps'],['scenario.average_net_home_sf'])
        self.assertIn('scenario.home_equivalents',report['affected_claims'])
        self.assertNotIn('scenario.gross_to_recorded_lot_ratio',report['affected_claims'])
    def test_step_declaration_order_does_not_control_execution(self):
        r=copy.deepcopy(RESERVE);r['steps'].reverse()
        ir,_=compile_recipe(r,IR)
        self.assertEqual(claims(ir)['scenario.home_equivalents']['value'],30)
    def test_cycles_and_unknown_dependencies_block(self):
        for dep,message in [('scenario.residential_net_sf','cycle'),('recipe.missing','dependency')]:
            r=copy.deepcopy(BASE);r['steps'][1]['inputs'][0]=dep
            # Give the self-reference the expected gross type via another gross step.
            if 'cycle'==message:r['steps'][0]['inputs'][0]='scenario.residential_gross_sf'
            with self.assertRaises(ValueError):compile_recipe(r,IR)
    def test_semantic_gross_and_net_types_cannot_be_substituted(self):
        r=copy.deepcopy(BASE);r['steps'][2]['method']='homes.gross_quotient@1'
        with self.assertRaisesRegex(ValueError,'semantic type'):compile_recipe(r,IR)
    def test_unversioned_or_unknown_methods_block(self):
        for method in ['homes.net_quotient','homes.net_quotient@2','__import__']:
            r=copy.deepcopy(BASE);r['steps'][2]['method']=method
            with self.assertRaisesRegex(ValueError,'versioned method'):compile_recipe(r,IR)
    def test_duplicate_overwritten_or_missing_output_blocks(self):
        for mutate in [lambda r:r['steps'].append(copy.deepcopy(r['steps'][0])),lambda r:r['steps'][0].update(id='pluto.0.lotarea'),lambda r:r['steps'].pop(2)]:
            r=copy.deepcopy(BASE);mutate(r)
            with self.assertRaises(ValueError):compile_recipe(r,IR)
    def test_professional_gates_cannot_be_removed_or_cleared(self):
        r=copy.deepcopy(BASE);r['review_gates'].pop()
        with self.assertRaisesRegex(ValueError,'cannot be removed'):compile_recipe(r,IR)
        ir=copy.deepcopy(IR);claims(ir)['unknown.physical_fit']['kind']='judgment'
        with self.assertRaisesRegex(ValueError,'retained unknown'):compile_recipe(BASE,ir)
    def test_missing_optional_import_is_visible_and_required_input_blocks(self):
        ir=copy.deepcopy(IR);ir['claims']=[c for c in ir['claims'] if c['id']!='pluto.0.lotarea']
        out,trace=compile_recipe(BASE,ir)
        self.assertNotIn('scenario.gross_to_recorded_lot_ratio',claims(out))
        self.assertEqual(trace['steps'][-1]['status'],'skipped_missing_input')
        r=copy.deepcopy(BASE);r['steps'][-1]['on_missing']='block'
        with self.assertRaisesRegex(ValueError,'unavailable'):compile_recipe(r,ir)
    def test_arbitrary_fact_type_relabeling_blocks(self):
        r=copy.deepcopy(BASE);r['imports'][0]['claim_id']='pluto.0.unitsres'
        with self.assertRaisesRegex(ValueError,'reviewed source'):compile_recipe(r,IR)
    def test_negative_nonfinite_boolean_or_unexplained_inputs_block(self):
        for val in [-1,float('inf'),float('nan'),True]:
            r=copy.deepcopy(BASE);r['parameters'][0]['value']=val
            with self.assertRaises(ValueError):compile_recipe(r,IR)
        r=copy.deepcopy(BASE);r['parameters'][0]['rationale']=''
        with self.assertRaises(ValueError):compile_recipe(r,IR)
        r=copy.deepcopy(BASE);r['parameters'][1]['value']=50000
        with self.assertRaises(ValueError):compile_recipe(r,IR)
    def test_source_judgment_with_scenario_dependency_requires_reconciliation(self):
        ir=copy.deepcopy(IR);claims(ir)['review.next_diligence']['inputs'].append('scenario.home_equivalents')
        with self.assertRaisesRegex(ValueError,'professional reconciliation'):compile_recipe(BASE,ir)
    def test_real_run_replay_exports_and_source_links(self):
        with tempfile.TemporaryDirectory() as d:
            a=Path(d)/'a';b=Path(d)/'b'
            engine.build(SOURCE,BASE,a);engine.build(a,BASE,b)
            self.assertEqual((a/'evidence-run/manifest.json').read_bytes(),(SOURCE/'manifest.json').read_bytes())
            for name in ['recipe.json','ir.json','trace.json','packet.md','packet.html','calculation-steps.csv','image-prompts.json']:
                self.assertEqual((a/name).read_bytes(),(b/name).read_bytes())
            ir=load(a/'ir.json');prompt=load(a/'image-prompts.json')
            self.assertEqual(prompt['model_sha256'],digest((a/'ir.json').read_bytes()))
            for c in ir['claims']:
                for ref in c['references']:
                    self.assertTrue((a/'sources'/f"{ref['source_id']}.json").exists())
            engine.verify(b)
    def test_stale_recipe_even_with_rehashed_inventory_fails_recompute(self):
        with tempfile.TemporaryDirectory() as d:
            run=Path(d)/'run';engine.build(SOURCE,BASE,run)
            r=load(run/'recipe.json');r['parameters'][3]['value']=680;save(run/'recipe.json',r)
            with self.assertRaisesRegex(ValueError,'hash changed'):engine.verify(run)
            m=load(run/'manifest.json');m['files']=engine.inventory(run);save(run/'manifest.json',m)
            with self.assertRaisesRegex(ValueError,'projection differs'):engine.verify(run)
    def test_corrupt_source_blocks_and_outputs_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);source=root/'source';make_run(source)
            run=root/'run';engine.build(source,BASE,run)
            with self.assertRaisesRegex(ValueError,'new empty'):engine.build(source,BASE,run)
            (source/'sources/pluto.json').write_text('[]')
            with self.assertRaisesRegex(ValueError,'hash mismatch'):engine.build(source,BASE,root/'bad')
    def test_json_schemas_validate_examples_and_reject_unknown_fields(self):
        import jsonschema
        schema=load(ROOT/'housing_recipe/recipe.schema.json')
        for recipe in [BASE,RESERVE,GROSS]:jsonschema.validate(recipe,schema)
        r=copy.deepcopy(BASE);r['hidden_override']=True
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(r,schema)
        with self.assertRaises(ValueError):compile_recipe(r,IR)
    def test_current_saved_example_if_present(self):
        for name in ['base','with-reserve','gross-method']:
            p=ROOT/'examples/analysis-recipe'/name
            if p.exists():engine.verify(p)

if __name__=='__main__':unittest.main()
