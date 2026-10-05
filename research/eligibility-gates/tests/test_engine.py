import copy,json,pathlib,subprocess,sys,unittest
P=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from engine import compile_case,evaluate,combine,fingerprint,sha,BASE,ROOT
from build import profile_for,DATA
from check import release
class Gates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources=json.loads((P/'sources.json').read_text());cls.cases={p.stem:json.loads(p.read_text()) for p in (P/'cases').glob('*.json')};cls.compiled={k:compile_case(c,cls.sources) for k,c in cls.cases.items()};cls.scenarios={s['id']:s for s in DATA['scenarios']}
    def profile(self,case,scenario):return profile_for(self.compiled[case],self.scenarios[scenario])
    def result(self,case,scenario):return evaluate(self.compiled[case],self.profile(case,scenario))
    def gate(self,result,key):return next(g for g in result['gates'] if g['id']==key)
    def test_unknown_actual_credentials_do_not_pass_or_fail(self):
        for compiled in self.compiled.values():
            r=evaluate(compiled,{'id':'not-supplied','kind':'actual'});self.assertTrue(all(g['status']=='unknown' for g in r['gates']));self.assertFalse(r['submission_readiness_claim_allowed']);self.assertTrue(r['low_cost_exploration_allowed'])
    def test_source_specific_threshold_and_discretion(self):
        west=self.result('west169','sixty_units');east=self.result('stanns','sixty_units')
        self.assertEqual(self.gate(west,'team.development')['status'],'pass');self.assertEqual(self.gate(west,'team.management')['status'],'pass')
        dev=self.gate(east,'team.development');self.assertEqual(dev['base_status'],'fail');self.assertEqual(dev['status'],'unknown');self.assertEqual(self.gate(east,'team.management')['status'],'fail')
    def test_single_development_project_cannot_be_summed(self):
        r=self.result('west169','split_projects');self.assertEqual(self.gate(r,'team.development')['status'],'fail');self.assertEqual(self.gate(r,'team.management')['status'],'pass')
    def test_rehabilitation_qualification_differs(self):
        self.assertEqual(self.gate(self.result('west169','rehabilitation'),'team.development')['status'],'pass')
        r=self.gate(self.result('stanns','rehabilitation'),'team.development');self.assertEqual(r['base_status'],'fail');self.assertEqual(r['status'],'unknown')
    def test_outside_nyc_and_future_experience_not_qualifying(self):
        for case in self.cases:
            for scenario in ['outside_nyc','future_experience','old_experience']:
                self.assertEqual(self.gate(self.result(case,scenario),'team.management')['status'],'fail')
    def test_incomplete_history_cannot_prove_failure(self):
        for case in self.cases:
            for gate in ['team.development','team.management']:self.assertEqual(self.gate(self.result(case,'incomplete_history'),gate)['status'],'unknown')
    def test_unreviewed_and_missing_roles_cannot_promote(self):
        for case in self.cases:
            for scenario in ['missing_role','unreviewed_assertions']:
                for gate in ['team.development','team.management']:self.assertEqual(self.gate(self.result(case,scenario),gate)['status'],'unknown')
    def test_partial_boolean_logic_preserves_known_failure(self):
        self.assertIs(combine('all',[False,None]),False);self.assertIsNone(combine('all',[True,None]));self.assertIs(combine('any',[True,None]),True);self.assertIsNone(combine('any',[False,None]))
    def test_all_synthetic_gates_pass_without_readiness_promotion(self):
        for case in self.cases:
            r=self.result(case,'all_scoped_reviews_match');self.assertTrue(all(g['status']=='pass' for g in r['gates']));self.assertFalse(r['submission_readiness_claim_allowed']);self.assertIn('coverage.full_submission_inventory',r['blocking_gates']);self.assertIn('synthetic_profile_not_actual_evidence',r['blocking_gates'])
    def test_source_numeric_mutation_rejected(self):
        case=copy.deepcopy(self.cases['west169']);g=case['gates'][0];g['bindings'][0]['value']=59;g['where']['args'][0]['value']=59
        with self.assertRaisesRegex(ValueError,'disagrees with source'):compile_case(case,self.sources)
    def test_wrong_page_rejected(self):
        case=copy.deepcopy(self.cases['west169']);case['gates'][0]['citations'][0]['pdf_page']=102
        with self.assertRaisesRegex(ValueError,'Quote not on cited page'):compile_case(case,self.sources)
    def test_cross_case_source_rejected(self):
        case=copy.deepcopy(self.cases['west169']);case['gates'][0]['citations'][0]['source_id']='stanns_rfp'
        with self.assertRaisesRegex(ValueError,'Cross-case'):compile_case(case,self.sources)
    def test_post_cutoff_document_rejected(self):
        sources=copy.deepcopy(self.sources);next(d for d in sources['sources'] if d['id']=='west169_rfp')['pdf_modified']='Fri Apr 05 00:00:00 2019 UTC'
        with self.assertRaisesRegex(ValueError,'Post-cutoff PDF'):compile_case(self.cases['west169'],sources)
    def test_source_byte_mismatch_rejected(self):
        sources=copy.deepcopy(self.sources);next(d for d in sources['sources'] if d['id']=='west169_rfp')['text_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'Changed source bytes'):compile_case(self.cases['west169'],sources)
    def test_unknown_dsl_operator_rejected(self):
        case=copy.deepcopy(self.cases['west169']);case['gates'][0]['where']['op']='eval'
        with self.assertRaisesRegex(ValueError,'DSL schema'):compile_case(case,self.sources)
    def test_stale_fact_review_rejected(self):
        profile=self.profile('west169','seventy_units');profile['collections']['development']['records'][0]['facts']['residential_units']=100
        with self.assertRaisesRegex(ValueError,'facts changed'):evaluate(self.compiled['west169'],profile)
    def test_stale_requirement_review_rejected(self):
        case=copy.deepcopy(self.cases['west169']);case['assumptions'][0]['rationale']+=' changed'
        compiled=compile_case(case,self.sources)
        with self.assertRaisesRegex(ValueError,'rules changed'):evaluate(compiled,self.profile('west169','seventy_units'))
    def test_credential_source_digest_rejected(self):
        profile=self.profile('west169','seventy_units');record=profile['collections']['development']['records'][0];record['evidence']['sha256']='0'*64;record['review']['payload_fingerprint']=fingerprint({k:v for k,v in record.items() if k!='review'})
        with self.assertRaisesRegex(ValueError,'Credential evidence changed'):evaluate(self.compiled['west169'],profile)
    def test_scope_review_binds_negative_history(self):
        profile=self.profile('west169','split_projects');profile['collections']['development']['records'].pop()
        with self.assertRaisesRegex(ValueError,'bind complete history'):evaluate(self.compiled['west169'],profile)
    def test_fixture_cannot_be_relabelled_actual(self):
        profile=self.profile('west169','seventy_units');profile['kind']='actual'
        with self.assertRaisesRegex(ValueError,'Synthetic credential'):evaluate(self.compiled['west169'],profile)
    def test_synthetic_tag_removal_cannot_promote_fixture(self):
        profile=self.profile('west169','seventy_units');profile['kind']='actual';record=profile['collections']['development']['records'][0];record['evidence']['synthetic']=False;record['review']['payload_fingerprint']=fingerprint({k:v for k,v in record.items() if k!='review'})
        with self.assertRaisesRegex(ValueError,'Synthetic credential'):evaluate(self.compiled['west169'],profile)
    def test_unit_type_not_coerced(self):
        profile=self.profile('west169','seventy_units');record=profile['collections']['development']['records'][0];record['facts']['residential_units']='70';record['review']['payload_fingerprint']=fingerprint({k:v for k,v in record.items() if k!='review'})
        with self.assertRaisesRegex(ValueError,'Unit count'):evaluate(self.compiled['west169'],profile)
    def test_window_boundaries_use_declared_cutoff(self):
        case=self.compiled['west169'];profile=self.profile('west169','seventy_units');record=profile['collections']['development']['records'][0]
        for date,expected in [('2012-04-04','pass'),('2012-04-03','fail'),('2019-04-04','pass'),('2019-04-05','fail')]:
            record['facts']['completion_date']=date;record['review']['payload_fingerprint']=fingerprint({k:v for k,v in record.items() if k!='review'});collection=profile['collections']['development'];scope=collection['scope_review'];scope['facts']['record_set_fingerprint']=fingerprint(collection['records']);scope['review']['payload_fingerprint']=fingerprint({k:v for k,v in scope.items() if k!='review'})
            self.assertEqual(self.gate(evaluate(case,profile),'team.development')['status'],expected)
    def test_release_boundary(self):
        compiled=self.compiled['west169'];profile=self.profile('west169','seventy_units');self.assertTrue(release(compiled,profile,'evidence-pack')['allowed']);self.assertFalse(release(compiled,profile,'submission-readiness-claim')['allowed'])
        with self.assertRaisesRegex(ValueError,'Unsupported'):release(compiled,profile,'agency-approval')
    def test_forged_readiness_assertion_does_not_bypass_evaluation(self):
        profile={'id':'not-supplied','kind':'actual','submission_readiness_claim_allowed':True,'blocking_gates':[]}
        r=release(self.compiled['west169'],profile,'submission-readiness-claim');self.assertFalse(r['allowed']);self.assertTrue(r['blocking_gates'])
    def test_cli_blocked_exit_status(self):
        r=subprocess.run([sys.executable,str(P/'check.py'),'--case','west169','--purpose','submission-readiness-claim'],capture_output=True,text=True);self.assertEqual(r.returncode,2);self.assertFalse(json.loads(r.stdout)['allowed'])
if __name__=='__main__':unittest.main()
