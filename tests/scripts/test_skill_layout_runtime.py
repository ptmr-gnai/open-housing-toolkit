"""Historical verification survives the layout move without trusting edited outputs."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from housing_common import runtime

ROOT = Path(__file__).resolve().parents[2]


class HistoricalSkillLayout(unittest.TestCase):
    def test_original_package_uses_original_verifier(self):
        result = runtime.verify_historical('housing_workflow', ROOT/'examples/parcel-investigation')
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['verification_runtime'], 'archived-skill-layout-v0')

    def test_unknown_implementation_does_not_get_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)/'run'
            shutil.copytree(ROOT/'examples/parcel-investigation',run)
            manifest = json.loads((run/'manifest.json').read_text())
            manifest['implementation']['housing_workflow/engine.py'] = '0'*64
            (run/'manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Historical verification rejected'):
                runtime.verify_historical('housing_workflow',run)

    def test_rehashed_output_tampering_is_recomputed_and_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)/'run'
            shutil.copytree(ROOT/'examples/parcel-investigation',run)
            packet = run/'packet.md'
            packet.write_bytes(packet.read_bytes()+b'\nInvented conclusion.\n')
            manifest = json.loads((run/'manifest.json').read_text())
            manifest['files']['packet.md'] = hashlib.sha256(packet.read_bytes()).hexdigest()
            (run/'manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Packet projection changed'):
                runtime.verify_historical('housing_workflow',run)

    def test_changed_archive_is_rejected_before_execution(self):
        with tempfile.TemporaryDirectory() as d:
            archive = Path(d)/'archive'
            shutil.copytree(runtime.ARCHIVE,archive,ignore=shutil.ignore_patterns('__pycache__'))
            (archive/'housing_workflow/engine.py').write_text('raise RuntimeError("do not run")')
            with patch.object(runtime,'ARCHIVE',archive), patch.object(runtime.subprocess,'run') as execute:
                with self.assertRaisesRegex(ValueError,'Historical runtime source changed'):
                    runtime.verify_historical('housing_workflow',ROOT/'examples/parcel-investigation')
                execute.assert_not_called()

    def test_new_packages_bind_active_reference_files(self):
        from housing_render.engine import implementation
        bound = implementation()
        self.assertIn('skills/prepare-render-brief/references/runbook.md',bound)
        self.assertIn('skills/render-site-concept/references/runbook.md',bound)
        self.assertIn('src/housing_common/runtime.py',bound)
        self.assertFalse(any('skills/current/' in path for path in bound))


if __name__ == '__main__':
    unittest.main()
