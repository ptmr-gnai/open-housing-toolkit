import copy
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from housing_workflow.contracts import load,save
from housing_benefit import engine as comparisons
from housing_rer import engine,model
from housing_rer.contracts import REQUIRED_IDS

ROOT=engine.ROOT
PARENT=ROOT/'examples/affordability-comparison'
REQ=load(ROOT/'examples/rer-inputs/request.json')
CAT=load(ROOT/'src/housing_rer/requirements.json');GUIDE=load(ROOT/'src/housing_rer/guidance.json')


def compiled(req=None,catalog=None,guidance=None):
    from housing_workflow.contracts import digest
    return model.compile_drafts(copy.deepcopy(req or REQ),load(PARENT/'ir.json'),digest((PARENT/'ir.json').read_bytes()),load(PARENT/'analysis-run/ir.json'),digest((PARENT/'analysis-run/ir.json').read_bytes()),copy.deepcopy(catalog or CAT),copy.deepcopy(guidance or GUIDE))


def slots(report):return {s['requirement_id']:s for s in report['slots']}

class RER(unittest.TestCase):
    def test_exact_instruction_inventory_and_no_readiness_claim(self):
        ir=compiled();self.assertEqual(len(ir['reports']),2);self.assertEqual(len(REQUIRED_IDS),50)
        for report in ir['reports']:
            self.assertEqual(set(slots(report)),REQUIRED_IDS)
            self.assertFalse(report['official_submission_ready']);self.assertEqual(report['applicability'],'not_determined')
            self.assertEqual(report['professional_review'],'pending');self.assertEqual(sum(report['status_counts'].values()),50)
    def test_five_ordered_sections_and_diagnostic_outside_them(self):
        from housing_rer.packet import projections
        out=projections(compiled());md=out['report-program_a.md']
        headings=re.findall(r'^## Section ([1-5]):',md,re.M)
        self.assertEqual(headings,['1','2','3','4','5'])
        self.assertGreater(md.index('## Supplemental appendix A'),md.index('## Section 5:'))
        self.assertIn('not a completed RER affordability table',md)
    def test_illustrative_counts_are_not_approved_counts(self):
        ir=compiled();a,b=ir['reports']
        self.assertEqual(slots(a)['res.total']['value'],24);self.assertEqual(slots(b)['res.total']['value'],36)
        self.assertEqual(slots(a)['res.total']['status'],'illustrative')
        self.assertEqual(slots(a)['res.total']['bindings'][0]['kind'],'assumption')
    def test_non_demo_program_sizes_are_used_in_area_explanations(self):
        request=load(ROOT/'examples/affordability-inputs/request.json')
        for program,counts in zip(request['programs'],[(8,4),(4,14)]):
            program['total_homes']={'value':sum(counts),'rationale':'Explicit non-demo test total.'}
            for offer,count in zip(program['bins'],counts):
                offer['homes']={'value':count,'rationale':'Explicit non-demo test program.'}
        with tempfile.TemporaryDirectory() as d:
            parent=Path(d)/'comparison';out=Path(d)/'rer'
            comparisons.replay(PARENT,parent,request)
            engine.build(parent,copy.deepcopy(REQ),out)
            for report,total in zip(load(out/'rer.json')['reports'],[12,18]):
                reasons=[slot['reason'] for slot in report['slots']]
                self.assertTrue(any('this '+str(total)+'-home program' in reason for reason in reasons))
                self.assertFalse(any('24/36-home' in reason for reason in reasons))
                self.assertFalse(report['official_submission_ready'])

    def test_hypothetical_income_is_not_eligibility_and_cost_bins_not_ami(self):
        s=slots(compiled()['reports'][0])
        for rid in ['res.incomes','res.classification','res.ami','res.band_counts','res.band_shares','res.programs']:
            self.assertIsNone(s[rid]['value']);self.assertEqual(s[rid]['status'],'needs_interpretation')
        self.assertEqual(s['res.incomes']['bindings'][0]['use'],'candidate_only_not_populated')
        self.assertIn('not program eligibility',s['res.incomes']['reason'])
    def test_contract_rents_do_not_populate_guide_rent_ranges(self):
        s=slots(compiled()['reports'][0])['res.rents']
        self.assertIsNone(s['value']);self.assertEqual(s['status'],'needs_interpretation')
        self.assertEqual(s['bindings'][0]['value'],'1000.00')
    def test_gross_area_is_not_zoning_area_or_construction_job_input(self):
        s=slots(compiled()['reports'][0])
        for rid in ['res.zsf','nonres.zsf','construction.gsf']:
            self.assertIsNone(s[rid]['value']);self.assertEqual(s[rid]['status'],'needs_interpretation')
            self.assertEqual(s[rid]['bindings'][0]['use'],'candidate_only_not_populated')
        for rid in ['construction.person_years','construction.workers','construction.duration']:
            self.assertIsNone(s[rid]['value']);self.assertEqual(s[rid]['status'],'missing')
    def test_guide_form_divergence_retains_both_sources(self):
        r=slots(compiled()['reports'][0])['nonres.area_conflict']
        self.assertEqual({s['document'] for s in r['sources']},{'form','guide'})
        self.assertEqual(r['status'],'needs_interpretation')
        cat=copy.deepcopy(CAT);row=next(x for x in cat['requirements'] if x['id']==r['requirement_id']);row['citations']=row['citations'][:1]
        with self.assertRaisesRegex(ValueError,'lost a source'):model.validate_catalog(cat,GUIDE)
    def test_unknown_tenants_do_not_generate_jobs_or_sector_data(self):
        s=slots(compiled()['reports'][0])
        for rid in ['nonres.jobs','nonres.workforce']:
            self.assertEqual(s[rid]['status'],'needs_interpretation');self.assertIsNone(s[rid]['value'])
    def test_no_known_tenant_assumption_only_conditionally_suppresses_jobs(self):
        req=copy.deepcopy(REQ);req['nonresidential_tenants'].update(status='none_identified',rationale='Illustrative assumption; no specific future tenant.',attribution='Demo author')
        s=slots(compiled(req)['reports'][0])
        for rid in ['nonres.jobs','nonres.workforce']:
            self.assertEqual(s[rid]['status'],'not_applicable');self.assertIsNone(s[rid]['value']);self.assertIn('Demo author',s[rid]['reason'])
        self.assertEqual(s['nonres.area_conflict']['status'],'needs_interpretation')
        self.assertNotEqual(s['nonres.zsf']['status'],'not_applicable')
    def test_missing_community_materials_stay_missing(self):
        s=slots(compiled()['reports'][0])
        for rid in ['community.geography','community.summary','community.displacement','appendix.local','appendix.borough','appendix.city','appendix.all_indicators']:
            self.assertEqual(s[rid]['status'],'missing');self.assertIsNone(s[rid]['value'])
    def test_narrative_goal_prompts_not_legal_pass_fail_tests(self):
        s=slots(compiled()['reports'][0])
        for i in range(1,7):self.assertEqual(s['narrative.goal'+str(i)]['status'],'needs_interpretation')
        cat=copy.deepcopy(CAT);next(r for r in cat['requirements'] if r['id']=='narrative.goal1')['category']='instruction_slot'
        with self.assertRaisesRegex(ValueError,'independent legal'):model.validate_catalog(cat,GUIDE)
    def test_reference_year_not_silently_updated(self):
        s=slots(compiled()['reports'][0])['res.years']
        self.assertEqual(s['status'],'needs_interpretation');self.assertIn('2025',s['reason']);self.assertIn('2026',s['reason'])
        r=copy.deepcopy(REQ);r['prepared_on']='2025-10-29';s=slots(compiled(r)['reports'][0])['res.years']
        self.assertEqual(s['status'],'illustrative');self.assertEqual(s['value'],'2025')
    def test_missing_or_duplicate_instruction_is_rejected(self):
        for mutate in [lambda c:c['requirements'].remove(next(r for r in c['requirements'] if r['id']=='res.zsf')),lambda c:c['requirements'].append(copy.deepcopy(c['requirements'][0]))]:
            cat=copy.deepcopy(CAT);mutate(cat)
            with self.assertRaisesRegex(ValueError,'inventory'):model.validate_catalog(cat,GUIDE)
    def test_changed_guidance_hash_or_page_binding_requires_remap(self):
        g=copy.deepcopy(GUIDE);g['sources'][0]['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'binding changed'):model.validate_catalog(CAT,g)
        g=copy.deepcopy(GUIDE);g['sources'][0]['pages'][0]['normalized_text_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'binding changed'):model.validate_catalog(CAT,g)
    def test_duplicate_authoritative_source_rejected(self):
        g=copy.deepcopy(GUIDE);g['sources'].append(copy.deepcopy(g['sources'][0]))
        with self.assertRaisesRegex(ValueError,'reference document'):model.validate_catalog(CAT,g)
    def test_unsupported_applicability_or_known_tenant_adapter_blocks(self):
        for key in ['application','contact']:
            r=copy.deepcopy(REQ);r[key]['status']='known'
            with self.assertRaisesRegex(ValueError,'adapter'):compiled(r)
        r=copy.deepcopy(REQ);r['nonresidential_tenants']['status']='known'
        with self.assertRaisesRegex(ValueError,'adapter'):compiled(r)
    def test_no_request_switch_for_submission_readiness(self):
        r=copy.deepcopy(REQ);r['official_submission_ready']=True
        with self.assertRaises(ValueError):compiled(r)
    def test_schema_coverage_and_readiness_false(self):
        import jsonschema
        jsonschema.validate(REQ,load(ROOT/'src/housing_rer/request.schema.json'))
        ir=compiled();schema=load(ROOT/'src/housing_rer/ir.schema.json');jsonschema.validate(ir,schema)
        ir['reports'][0]['official_submission_ready']=True
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(ir,schema)
    def test_exact_replay_preserves_parent_and_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a',Path(d)/'b';engine.build(PARENT,REQ,a);engine.replay(a,b)
            self.assertEqual(engine.inventory(a),engine.inventory(b))
            self.assertEqual((a/'comparison-run/manifest.json').read_bytes(),(PARENT/'manifest.json').read_bytes())
            engine.verify(b)
    def test_removed_obligation_and_fake_readiness_fail_even_after_rehash(self):
        for change in ['remove','readiness']:
            with self.subTest(change=change),tempfile.TemporaryDirectory() as d:
                root=Path(d)/'run';engine.build(PARENT,REQ,root);ir=load(root/'rer.json')
                if change=='remove':ir['reports'][0]['slots']=[s for s in ir['reports'][0]['slots'] if s['requirement_id']!='res.zsf']
                else:ir['reports'][0]['official_submission_ready']=True
                save(root/'rer.json',ir);m=load(root/'manifest.json');m['files']=engine.inventory(root);save(root/'manifest.json',m)
                with self.assertRaisesRegex(ValueError,'differs from retained'):engine.verify(root)
    def test_changed_program_updates_diagnostic_but_not_eligibility(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);changed=root/'comparison'
            comparisons.replay(PARENT,changed,load(ROOT/'examples/affordability-inputs/higher-utilities.json'))
            a,b=root/'base',root/'changed';engine.build(PARENT,REQ,a);engine.build(changed,REQ,b)
            ia,ib=load(a/'rer.json'),load(b/'rer.json')
            self.assertEqual(slots(ia['reports'][0])['res.incomes']['value'],None)
            self.assertEqual(slots(ib['reports'][0])['res.incomes']['value'],None)
            self.assertNotEqual((a/'report-program_a.md').read_bytes(),(b/'report-program_a.md').read_bytes())
            self.assertFalse(ib['reports'][0]['official_submission_ready'])
    def test_html_has_safe_working_local_links_and_escaped_metadata(self):
        r=copy.deepcopy(REQ);r['prepared_by']='<script>alert(1)</script>'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(PARENT,r,root);page=(root/'report-program_a.html').read_text()
            self.assertNotIn('<script>',page);self.assertIn('&lt;script&gt;',page)
            self.assertIn('href="coverage.html"',page)
            self.assertIn('href="report-program_a.html"',(root/'packet.html').read_text())
    def test_existing_run_and_corrupt_output_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(PARENT,REQ,root)
            with self.assertRaisesRegex(ValueError,'new empty'):engine.build(PARENT,REQ,root)
            (root/'coverage.md').write_text('Everything compliant')
            with self.assertRaisesRegex(ValueError,'artifact hash'):engine.verify(root)
    def test_cli_blocked_input_has_no_released_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);r=copy.deepcopy(REQ);r['prepared_on']='not-a-date';save(root/'req.json',r)
            p=subprocess.run([sys.executable,'-m','housing_rer','build','--comparison',str(PARENT),'--input',str(root/'req.json'),'--out',str(root/'out')],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(p.returncode,2);self.assertFalse((root/'out/manifest.json').exists())
    def test_saved_example_when_present(self):
        p=ROOT/'examples/rer-preparation'
        if p.exists():engine.verify(p)

if __name__=='__main__':unittest.main()
