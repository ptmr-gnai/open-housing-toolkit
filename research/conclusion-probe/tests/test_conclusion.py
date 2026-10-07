"""Behavioral faults for one decision chain; no professional utility claim. MIT."""
import copy, math, pathlib, sys, tempfile, unittest, subprocess
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from conclusion_engine import BASE, ROOT, build, load, closure, validate_graph, numeric, sha, write, fp
from controls import run_control, expected_response, snapshot, mutate, competing

class ConclusionProbe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline=build();cls.spec=load(BASE/'spec.json')

    def test_each_precommitted_control_response(self):
        for control in self.spec['controls']:
            with self.subTest(control=control['id']):
                observation,_=run_control(control,self.baseline)
                self.assertTrue(expected_response(observation,self.baseline),observation)

    def test_every_material_observed_fact_has_exact_versioned_locator(self):
        for c in self.baseline['claims'].values():
            if c['kind']=='observed':
                e=c['evidence'];s=self.baseline['sources'][e['source_id']]
                self.assertEqual(sha((ROOT/s['cache_path']).read_bytes()),e['sha256'])
                self.assertIn('locator',e);self.assertTrue(e['retrieved_at'])

    def test_claims_are_connected_and_typed(self):
        self.assertEqual(closure(self.baseline['claims'],['conclusion.next_step']),set(self.baseline['claims']))
        self.assertEqual({c['kind'] for c in self.baseline['claims'].values()},{'observed','derived','assumption','judgment','unknown'})

    def test_edited_assumptions_resolve_to_the_embedded_config(self):
        config=load(ROOT/'probe.json');config['assumptions']['hard_cost_per_gsf']['value']=525
        r=build(config=config)
        for c in r['claims'].values():
            if c['kind']=='assumption':
                value=r['config']
                for part in c['config_locator'].strip('/').split('/'):
                    value=value[int(part)] if isinstance(value,list) else value[part]
                self.assertEqual(c['value'],value)
                self.assertEqual(c['config_fingerprint'],fp(r['config']))

    def test_conditional_rent_satisfies_underwriting_identity(self):
        c=self.baseline['claims'];v=lambda k:c[k]['value'];p='scenario.2028710002.A.'
        noi=v(p+'debt_support_rent_month')*v(p+'units')*12*(1-v('assumption.vacancy_share'))*(1-v('assumption.opex_share_egi'))
        self.assertAlmostEqual(noi/v(p+'annual_debt_service'),v('assumption.dscr'))
        self.assertLessEqual(v(p+'units')*v('assumption.avg_net_unit_sf'),v(p+'net_sf'))
        self.assertGreater((v(p+'units')+1)*v('assumption.avg_net_unit_sf'),v(p+'net_sf'))

    def test_finance_changes_do_not_clear_occupancy(self):
        control=next(c for c in self.spec['controls'] if c['id']=='lower_cost');_,r=run_control(control,self.baseline)
        self.assertEqual(r['claims']['finance.model_gap']['value'],False)
        self.assertIsNone(r['claims']['gate.current_occupancy_and_leases']['value'])
        self.assertFalse(r['release']['acquisition_or_design_clearance'])

    def test_conflict_flags_precise_dependents_without_picking_winner(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);r=build(s,competing=competing(s))
        self.assertIn('resident.recorded_units',r['affected_by_conflict'])
        self.assertIn('conclusion.next_step',r['affected_by_conflict'])
        self.assertNotIn('scenario.2028710002.A.gross_sf',r['affected_by_conflict'])
        self.assertEqual(r['claims']['lot.2028710002.unitsres']['value'],0)
        self.assertEqual(r['claims']['competing.unitsres']['value'],48)
        self.assertEqual(r['claims']['conclusion.next_step']['state'],'withheld')

    def test_conflicting_area_blocks_geometry_and_finance(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);r=build(s,competing=competing(s,field='lotarea',value=47240))
        self.assertIn('scenario.2028710002.A.gross_sf',r['affected_by_conflict'])
        self.assertIn('finance.model_gap',r['affected_by_conflict'])
        self.assertFalse(r['release']['investigation_conclusion'])

    def test_equal_assertion_is_not_a_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);r=build(s,competing=competing(s,value=0))
        self.assertFalse(r['conflicts']);self.assertEqual(r['disposition'],self.baseline['disposition'])

    def test_change_invalidates_the_old_judgment_basis(self):
        c=load(ROOT/'probe.json');c['assumptions']['hard_cost_per_gsf']['value']=525
        r=build(config=c,prior_basis=self.baseline['basis_fingerprint'])
        self.assertEqual(r['prior_judgment_basis'],'stale');self.assertEqual(r['disposition'],self.baseline['disposition'])

    def test_decisive_gate_cannot_be_removed_with_its_edge(self):
        r=copy.deepcopy(self.baseline);del r['claims']['gate.current_occupancy_and_leases']
        r['claims']['conclusion.next_step']['inputs'].remove('gate.current_occupancy_and_leases')
        r['claims']['judgment.investigation_priority']['inputs'].remove('gate.current_occupancy_and_leases')
        r['required_gates'].remove('current_occupancy_and_leases')
        with self.assertRaisesRegex(ValueError,'Missing decisive requirement'):validate_graph(r)

    def test_invented_verified_gate_rejected(self):
        r=copy.deepcopy(self.baseline);r['claims']['gate.current_occupancy_and_leases'].update(kind='judgment',value='verified',inputs=['lot.2028710002.unitsres'],actor='caller')
        with self.assertRaisesRegex(ValueError,'Unverified site requirement promoted'):validate_graph(r)

    def test_caller_cannot_force_conflicted_conclusion_release(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);r=build(s,competing=competing(s))
        r['release']['investigation_conclusion']=True
        with self.assertRaisesRegex(ValueError,'release disagrees'):validate_graph(r)

    def test_synthetic_update_cannot_be_relabelled_as_real(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);mutate(s,'pluto_universe',lambda rows:None,'rehash')
            p=s/'cache/pluto_universe.source.json';v=load(p);v['kind']='actual';write(p,v)
            with self.assertRaisesRegex(ValueError,'synthetic lineage'):build(s)

    def test_competing_evidence_cannot_be_relabelled_real(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);rival=competing(s);rival['receipt']['kind']='actual'
            with self.assertRaisesRegex(ValueError,'explicitly synthetic'):build(s,competing=rival)

    def test_failed_status_cannot_bypass_hash_integrity(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);mutate(s,'pluto_universe',lambda rows:None,'failed-status')
            p=s/'cache/pluto_universe.source.json';v=load(p);v['status']='failed';write(p,v)
            with self.assertRaisesRegex(ValueError,'successful-status'):build(s)

    def test_foreign_source_cannot_overwrite_expected_identity(self):
        with tempfile.TemporaryDirectory() as d:
            s=snapshot(d);write(s/'cache/extra.source.json',load(s/'cache/pluto_universe.source.json'))
            with self.assertRaisesRegex(ValueError,'inventory differs'):build(s)

    def test_boolean_and_nonfinite_numeric_assumptions_rejected(self):
        for value in [True,float('nan'),float('inf')]:
            c=load(ROOT/'probe.json');c['assumptions']['hard_cost_per_gsf']['value']=value
            with self.assertRaises(ValueError):build(config=c)

    def test_unchanged_original_snapshot_and_repeatable_baseline(self):
        self.assertEqual(build(),self.baseline)

    def test_external_export_boundary_blocks_design_clearance(self):
        for purpose,expected in [('challenge-pack',0),('acquisition-or-design',2)]:
            p=subprocess.run([sys.executable,str(BASE/'inspect_conclusion.py'),'--purpose',purpose],capture_output=True,text=True)
            self.assertEqual(p.returncode,expected,p.stderr)

if __name__=='__main__':unittest.main()
