import copy,json,pathlib,subprocess,sys,unittest
P=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from coverage_engine import load,pinned_audit,packet_check,contract
from fixtures import packet,reviewed,create_files
from scan import fp,discover
from coverage_check import combined
import engine as eligibility
class Coverage(unittest.TestCase):
    def codes(self,a):return {i['code'] for i in a['issues']}
    def req(self,r,rid):return next(x for x in r['requirements'] if x['id']==rid)
    def test_source_enumeration_independent_of_registry(self):
        sources,registry=load();u=next(x for x in registry['units'] if 'west169.form_G' in x['requirements']);registry['units'].remove(u)
        _,audit=pinned_audit(registry);self.assertIn('unaccounted_source_unit',self.codes(audit));self.assertFalse(audit['full_semantic_coverage'])
    def test_required_form_definition_omitted(self):
        _,registry=load();registry['requirements']=[r for r in registry['requirements'] if r['id']!='west169.form_G']
        _,a=pinned_audit(registry);self.assertIn('missing_requirement_definition',self.codes(a));self.assertIn('baseline_requirement_omitted',self.codes(a))
    def test_required_form_reclassified_optional(self):
        _,registry=load();next(r for r in registry['requirements'] if r['id']=='west169.form_G')['mode']='optional'
        _,a=pinned_audit(registry);self.assertIn('unreviewed_requirement_change',self.codes(a))
    def test_unsupported_coverage_acceptance_rejected(self):
        _,registry=load()
        for u in registry['units']:u['review_status']='accepted';u['expansion']='fully_expanded'
        _,a=pinned_audit(registry);self.assertIn('unreviewed_source_disposition_change',self.codes(a));self.assertFalse(a['full_semantic_coverage'])
    def test_missing_required_form_in_complete_packet(self):
        p=packet('west169');p['artifacts'].pop('west169.form_G');r=packet_check('west169',p);self.assertEqual(self.req(r,'west169.form_G')['status'],'missing')
    def test_unsupplied_packet_is_unknown_not_missing(self):
        r=packet_check('west169',{'id':'not-supplied','kind':'actual','inventory_complete':False})
        self.assertEqual(self.req(r,'west169.form_G')['status'],'unknown');self.assertFalse(r['submission_completeness_claim_allowed'])
    def test_conditional_false_requires_scoped_review(self):
        p=packet('west169',facts={'nonprofit_team':False,'nonresidential_space':False});p['artifacts'].pop('west169.form_D2');p['artifacts'].pop('west169.commercial_management')
        self.assertEqual(self.req(packet_check('west169',p),'west169.form_D2')['status'],'not_applicable')
        p['facts_review']={'status':'pending'};self.assertEqual(self.req(packet_check('west169',p),'west169.form_D2')['status'],'unknown')
    def test_nonprofit_form_required_when_applicable(self):
        p=packet('west169',facts={'nonprofit_team':True,'nonresidential_space':False});p['artifacts'].pop('west169.form_D2');self.assertEqual(self.req(packet_check('west169',p),'west169.form_D2')['status'],'missing')
    def test_obsolete_e4_request_detected_without_dropping_evidence(self):
        p=packet('west169');p['required_requests']=['west169.form_E4'];r=packet_check('west169',p);self.assertTrue(r['obsolete_requests'])
        p['artifacts'].pop('west169.commercial_management');r=packet_check('west169',p);self.assertEqual(self.req(r,'west169.commercial_management')['status'],'missing')
    def test_optional_staffing_not_a_required_artifact(self):
        p=packet('west169');p['artifacts'].pop('west169.staffing_plan');r=packet_check('west169',p);self.assertEqual(self.req(r,'west169.staffing_plan')['status'],'not_a_submission_blocker')
    def test_scanner_preserves_optional_scope(self):
        sources,_=load();u=next(u for u in discover(sources) if u['case']=='west169' and u['quote'].startswith('Project Staffing and Governance Plan'));self.assertTrue(u['optional_context'])
    def test_addendum_operation_cannot_disappear(self):
        _,r=load();r['changes']=[c for c in r['changes'] if c['id']!='west169.replace_e4'];_,a=pinned_audit(r);self.assertIn('addendum_operation_omitted_or_changed',self.codes(a))
    def test_deferred_certificate_cannot_be_required_at_submission(self):
        _,r=load();req=next(q for q in r['requirements'] if q['id']=='stanns.green_certificate');req['mode']='required';req['phase']='submission';_,a=pinned_audit(r);self.assertIn('addendum_effect_not_applied',self.codes(a))
    def test_deferred_certificate_preserves_submission_material(self):
        p=packet('stanns');p['artifacts'].pop('stanns.green_certificate');r=packet_check('stanns',p);self.assertEqual(self.req(r,'stanns.green_certificate')['status'],'not_a_submission_blocker')
        p['artifacts'].pop('stanns.sustainability_submission');r=packet_check('stanns',p);self.assertEqual(self.req(r,'stanns.sustainability_submission')['status'],'requested_material_absent')
    def test_gc_omission_and_old_multisite_request_detected(self):
        p=packet('stanns');p['artifacts'].pop('stanns.gc_identified');p['required_requests']=['stanns.multiple_site_submissions'];r=packet_check('stanns',p);self.assertEqual(self.req(r,'stanns.gc_identified')['status'],'missing');self.assertTrue(r['obsolete_requests'])
    def test_none_experience_does_not_drop_required_forms(self):
        p=packet('stanns');p['artifacts'].pop('stanns.form_D1');self.assertEqual(self.req(packet_check('stanns',p),'stanns.form_D1')['status'],'missing')
    def test_file_presence_does_not_mean_content_passed(self):
        p=packet('west169',accepted=False);self.assertEqual(self.req(packet_check('west169',p),'west169.form_G')['status'],'present_unreviewed')
    def test_excel_requirement_rejects_text_only_artifact(self):
        p=packet('west169');_,text=create_files();a=p['artifacts']['west169.form_G'];a['file']=str(text.relative_to(eligibility.ROOT));a['sha256']=eligibility.sha(text.read_bytes());a['review']=reviewed({k:v for k,v in a.items() if k!='review'},contract(*reversed(load())))
        self.assertEqual(self.req(packet_check('west169',p),'west169.form_G')['status'],'wrong_format')
    def test_changed_artifact_review_rejected(self):
        p=packet('west169');p['artifacts']['west169.form_G']['synthetic']=False
        with self.assertRaisesRegex(ValueError,'Stale packet'):packet_check('west169',p)
    def test_changed_applicability_review_rejected(self):
        p=packet('west169');p['facts']['nonprofit_team']=True
        with self.assertRaisesRegex(ValueError,'Stale packet'):packet_check('west169',p)
    def test_all_scoped_artifacts_cannot_certify_full_coverage(self):
        r=packet_check('west169',packet('west169'));self.assertFalse(r['submission_completeness_claim_allowed']);self.assertIn('coverage.semantic_expansion_and_review',r['blockers']);self.assertEqual(len(r['coverage']['review_queue']),79)
    def test_synthetic_packet_cannot_be_relabelled_actual(self):
        p=packet('west169');p['kind']='actual'
        with self.assertRaisesRegex(ValueError,'Synthetic'):packet_check('west169',p)
    def test_combined_boundary_keeps_eligibility_and_coverage(self):
        p=packet('west169');p['artifacts'].pop('west169.form_G');r=combined('west169',p,purpose='submission-readiness-claim');self.assertFalse(r['allowed']);self.assertIn('team.development',r['eligibility']['blocking_gates']);self.assertIn('west169.form_G',r['coverage']['blockers'])
    def test_scoped_review_cannot_be_reused_for_another_form(self):
        p=packet('west169');p['artifacts']['west169.form_G']=copy.deepcopy(p['artifacts']['west169.form_E1'])
        with self.assertRaisesRegex(ValueError,'another requirement'):packet_check('west169',p)
    def test_applicability_review_requires_retained_source(self):
        p=packet('west169');p['facts_evidence']=None;sources,registry=load();p['facts_review']=reviewed({'facts':p['facts'],'evidence':None},contract(registry,sources))
        with self.assertRaisesRegex(ValueError,'no source evidence'):packet_check('west169',p)
    def test_coordinated_requirement_and_anchor_deletion_detected(self):
        _,r=load();anchor=next(u['anchor'] for u in r['units'] if 'west169.form_G' in u['requirements'])
        r['units']=[u for u in r['units'] if u['anchor']!=anchor];r['requirements']=[x for x in r['requirements'] if x['id']!='west169.form_G']
        _,a=pinned_audit(r);self.assertIn('unaccounted_source_unit',self.codes(a));self.assertIn('baseline_requirement_omitted',self.codes(a))
    def test_cli_blocked_readiness_but_evidence_pack_available(self):
        for purpose,expected in [('submission-readiness-claim',2),('evidence-pack',0)]:
            p=subprocess.run([sys.executable,str(P/'coverage_check.py'),'--case','west169','--purpose',purpose],capture_output=True,text=True);self.assertEqual(p.returncode,expected,p.stderr)
if __name__=='__main__':unittest.main()
