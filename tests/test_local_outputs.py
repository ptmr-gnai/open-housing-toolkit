"""Regression: user runs and development checks must not overwrite shipped files. MIT."""
import pathlib,tempfile,unittest
from unittest.mock import patch
from housing_common import local_outputs
import sys
ROOT=local_outputs.ROOT
sys.path.insert(0,str(ROOT/'research/legacy-probe'))
import pipeline
from housing_workflow import engine as evidence
from housing_render import engine as renderer


class LocalOutputSafety(unittest.TestCase):
    def test_shipped_destinations_and_symlink_aliases_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);(root/'outputs').mkdir();(root/'runs').mkdir()
            for target in [root,root/'outputs',root/'examples/new',root/'cache/source.json']:
                with self.assertRaisesRegex(ValueError,'read-only'):local_outputs.destination(target,root)
            self.assertEqual(local_outputs.destination(root/'runs/new',root),root/'runs/new')
            try:(root/'runs/alias').symlink_to(root/'outputs',target_is_directory=True)
            except (OSError,NotImplementedError):return
            with self.assertRaisesRegex(ValueError,'read-only'):local_outputs.destination(root/'runs/alias/new',root)

    def test_export_and_renderer_reject_shipped_target_before_writing(self):
        target=pipeline.ROOT/'outputs'
        with self.assertRaisesRegex(ValueError,'read-only'):pipeline.export({},target,pipeline.ROOT/'probe.json')
        with self.assertRaisesRegex(ValueError,'read-only'):renderer.prepare({}, {},target)

    def test_build_and_collection_reject_shipped_examples_before_io(self):
        with patch.object(evidence.router,'collect',side_effect=AssertionError('Must not contact source')):
            with self.assertRaisesRegex(ValueError,'read-only'):evidence.collect({'version':'0.2.0','bbl':'2028710002','question':'test'},pipeline.ROOT/'cache')
        with self.assertRaisesRegex(ValueError,'read-only'):evidence.build(ROOT/'examples/parcel-investigation')
        with self.assertRaisesRegex(ValueError,'read-only'):evidence.fresh(ROOT/'examples/new-should-never-exist')

    def test_research_validators_leave_shipped_results_untouched(self):
        import subprocess,sys
        before=local_outputs.checkout_snapshot()
        for script in ['research/jerome-brief/validate.py','research/benchmark-case-search/validate_inputs.py','research/retrospective-run/validate.py']:
            result=subprocess.run([sys.executable,script],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
        local_outputs.assert_checkout_unchanged(before)

    def test_browser_writer_rejects_shipped_output_before_launch(self):
        import subprocess,shutil
        if not shutil.which('node'):self.skipTest('Optional browser command needs Node')
        result=subprocess.run(['node','research/legacy-probe/tests/check_explorer.cjs',str(pipeline.ROOT/'outputs')],cwd=ROOT,capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('read-only',result.stderr)

    def test_check_never_reports_success_before_checkout_guard(self):
        import importlib.util,io,subprocess,sys
        spec=importlib.util.spec_from_file_location('local_project_check',ROOT/'scripts/check_project.py')
        check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)
        with tempfile.TemporaryDirectory() as d:
            stdout=io.StringIO()
            with patch.object(sys,'argv',['check_project.py','check']), patch.object(check,'new_run',return_value=pathlib.Path(d)), patch.object(check,'checkout_snapshot',return_value={}), patch.object(check,'assert_checkout_unchanged',side_effect=ValueError('shipped file changed')), patch.object(check.pipeline,'build',return_value={}), patch.object(check.pipeline,'export'), patch.object(check.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), patch.object(sys,'stdout',stdout):
                with self.assertRaisesRegex(ValueError,'shipped file changed'):check.main()
            self.assertNotIn('"status": "passed"',stdout.getvalue())

    def test_same_byte_rewrite_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);file=root/'shipped.txt';file.write_text('preserve')
            before=local_outputs.checkout_snapshot(root)
            import os
            os.utime(file,ns=(file.stat().st_atime_ns,file.stat().st_mtime_ns+1_000_000))
            with self.assertRaisesRegex(ValueError,'modified'):local_outputs.assert_checkout_unchanged(before,root)

    def test_ignored_local_runs_do_not_count_as_shipped_changes(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);(root/'source.txt').write_text('fixed')
            before=local_outputs.checkout_snapshot(root)
            run=local_outputs.new_run('test',root);(run/'report.md').write_text('local')
            local_outputs.assert_checkout_unchanged(before,root)
            self.assertTrue(run.is_relative_to(root/'runs'))


if __name__=='__main__':unittest.main()
