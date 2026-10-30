"""Consequential onboarding failures: no overwrites, no downstream after failure."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts/first_run.py'
spec = importlib.util.spec_from_file_location('first_run', SCRIPT)
first_run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(first_run)


class OnboardingSafetyTests(unittest.TestCase):
    def test_existing_output_is_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sentinel = root / 'private-input.txt'
            sentinel.write_text('preserve me')
            with patch.object(first_run.subprocess, 'run') as execute:
                with self.assertRaisesRegex(ValueError, 'already exists'):
                    first_run.run(root)
                execute.assert_not_called()
            self.assertEqual(sentinel.read_text(), 'preserve me')
            self.assertEqual(list(root.iterdir()), [sentinel])

    def test_failed_stage_stops_and_retains_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'attempt'
            failure = subprocess.CompletedProcess(['python'], 2, '', 'upstream verification failed')
            with patch.object(first_run.subprocess, 'run', return_value=failure) as execute:
                with self.assertRaisesRegex(ValueError, 'Stopped at housing_workflow demo'):
                    first_run.run(out)
                self.assertEqual(execute.call_count, 1)
            self.assertFalse((out / 'README.md').exists())
            self.assertIn('upstream verification failed', (out / '01-housing_workflow-demo.log').read_text())
            self.assertTrue((out / 'steps.json').exists())

    def test_cannot_write_into_source_tree(self):
        with self.assertRaisesRegex(ValueError, 'under runs'):
            first_run.run(first_run.ROOT / 'examples' / 'never-create-onboarding-output')


if __name__ == '__main__':
    unittest.main()
