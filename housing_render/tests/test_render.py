import base64
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from housing_render import contracts as c, engine
from housing_render.brief import compile_brief

EXAMPLES=engine.ROOT/'examples/site-concept'
SCENE=c.load(EXAMPLES/'scene.json');SCENARIO=c.load(EXAMPLES/'scenario.json')
PNG=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a9eQAAAAASUVORK5CYII=')

def prepare(root,scenario=None,scene=None,photo=None,analysis=None):
    return engine.prepare(copy.deepcopy(scene or SCENE),copy.deepcopy(scenario or SCENARIO),root,analysis,photo)

def invocation(root):
    b=c.load(root/'render-brief.json')
    return {'provider':'test-fixture','prompt_sha256':c.digest(b['prompt'].encode()),'brief_sha256':c.digest((root/'render-brief.json').read_bytes()),'reference_id':b['reference']['id'],'reference_delivery':b['reference']['storage'],'parameters':{'num_last_images_to_include':3},'executed_at':'synthetic fixture, not real generation','execution_note':'Synthetic execution record only'}

def review():
    return {'reviewer_kind':'assistant_visual_inspection','summary':'Synthetic review for validation tests only.','checks':[{'id':k,'status':'not_verified','note':'Synthetic fixture, no professional review.'} for k in ['reference_setting','story_count','caption','invented_site_details','geometry_fidelity']]}

class RenderTests(unittest.TestCase):
    def test_saved_real_generation_is_bound(self):
        result=engine.verify(EXAMPLES/'with-analysis')
        self.assertEqual(result['stage'],'generated_and_reviewed')
        self.assertFalse(result['source_image_byte_bound'])
        b=c.load(EXAMPLES/'with-analysis/render-brief.json')
        self.assertEqual(len(b['analysis']['context_bindings']),5)
        self.assertFalse(b['analysis']['geometry_or_area_budget_reconciled'])
    def test_standalone_brief_needs_no_analysis(self):
        result=engine.verify(EXAMPLES/'standalone')
        self.assertEqual(result['stage'],'brief_prepared')
        self.assertFalse(c.load(EXAMPLES/'standalone/render-brief.json')['analysis']['available'])
    def test_changed_stories_change_prompt_and_binding(self):
        with tempfile.TemporaryDirectory() as d:
            s=copy.deepcopy(SCENARIO);s['parameters']['total_stories']['value']=8
            a=prepare(Path(d)/'six');b=prepare(Path(d)/'eight',s)
            self.assertNotEqual(a['prompt'],b['prompt'])
            self.assertEqual(b['derived_visual_instructions'][0]['value'],7)
            self.assertIn('ASSUMED 8 STORIES',b['required_caption'])
    def test_scene_and_scenario_site_must_match(self):
        with tempfile.TemporaryDirectory() as d:
            s=copy.deepcopy(SCENARIO);s['site_bbl']='2028560051'
            with self.assertRaisesRegex(ValueError,'parcel mismatch'):prepare(Path(d)/'run',s)
    def test_imported_analysis_must_match_site(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'analysis.json';c.save(p,{'resolved_bbl':'2028560051','claims':[]})
            with self.assertRaisesRegex(ValueError,'different parcel'):prepare(Path(d)/'run',analysis=p)
    def test_reference_asset_is_hashed_when_local(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);photo=root/'ref.png';photo.write_bytes(PNG)
            scene=copy.deepcopy(SCENE);scene['reference']['availability']='local_file'
            b=prepare(root/'run',scene=scene,photo=photo)
            self.assertEqual(b['reference']['sha256'],c.digest(PNG))
            self.assertTrue(engine.verify(root/'run')['source_image_byte_bound'])
    def test_missing_local_reference_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            scene=copy.deepcopy(SCENE);scene['reference']['availability']='local_file'
            with self.assertRaisesRegex(ValueError,'--photo'):prepare(Path(d)/'run',scene=scene)
    def test_no_unimplemented_geometry_certification(self):
        with tempfile.TemporaryDirectory() as d:
            s=copy.deepcopy(SCENARIO);s['geometry_status']='verified'
            with self.assertRaisesRegex(ValueError,'cannot certify'):prepare(Path(d)/'run',s)
        r=review();next(x for x in r['checks'] if x['id']=='geometry_fidelity')['status']='consistent_by_inspection'
        with self.assertRaisesRegex(ValueError,'cannot certify'):c.validate_review(r)
    def test_changed_brief_invalidates_invocation(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);prepare(root/'six');v=invocation(root/'six')
            s=copy.deepcopy(SCENARIO);s['parameters']['total_stories']['value']=8
            b=prepare(root/'eight',s)
            with self.assertRaisesRegex(ValueError,'stale'):engine.validate_invocation(v,b,root/'eight')
    def test_image_bytes_and_review_receipt_are_checked(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);run=root/'run';prepare(run);image=root/'out.png';image.write_bytes(PNG)
            engine.attach(run,image,invocation(run),review())
            (run/'render.png').write_bytes(PNG+b'changed')
            with self.assertRaisesRegex(ValueError,'bytes changed'):engine.verify(run)
    def test_incomplete_review_blocks_attach(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);run=root/'run';prepare(run);image=root/'out.png';image.write_bytes(PNG)
            r=review();r['checks'].pop()
            with self.assertRaisesRegex(ValueError,'coverage'):engine.attach(run,image,invocation(run),r)
    def test_existing_generation_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);run=root/'run';prepare(run);image=root/'out.png';image.write_bytes(PNG)
            v=invocation(run);r=review();engine.attach(run,image,v,r)
            with self.assertRaisesRegex(ValueError,'already attached'):engine.attach(run,image,v,r)
    def test_parameter_basis_must_be_explicit(self):
        with tempfile.TemporaryDirectory() as d:
            s=copy.deepcopy(SCENARIO);s['parameters']['total_stories']['kind']='approved'
            with self.assertRaisesRegex(ValueError,'basis'):prepare(Path(d)/'run',s)
    def test_module_runs_without_collection_or_model_package(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            shutil.copytree(engine.ROOT/'housing_render',root/'housing_render',ignore=shutil.ignore_patterns('__pycache__','tests'))
            shutil.copyfile(engine.ROOT/'housing_runtime.py',root/'housing_runtime.py')
            (root/'workflows').mkdir();shutil.copyfile(engine.WORKFLOW,root/'workflows/site-concept.json')
            for name in ['prepare-render-brief','render-site-concept']:
                shutil.copytree(engine.ROOT/'skills'/name,root/'skills'/name)
            c.save(root/'scene.json',SCENE);c.save(root/'scenario.json',SCENARIO)
            r=subprocess.run([sys.executable,'-m','housing_render','prepare','--scene','scene.json','--scenario','scenario.json','--out','run'],cwd=root,capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertFalse((root/'housing_workflow').exists())
    def test_unrelated_skills_do_not_stale_analysis(self):
        from housing_workflow.engine import implementation
        before=implementation()
        with tempfile.TemporaryDirectory(dir=engine.ROOT/'skills') as d:
            (Path(d)/'SKILL.md').write_text('Unrelated skill fixture')
            self.assertEqual(before,implementation())

if __name__=='__main__':unittest.main()
