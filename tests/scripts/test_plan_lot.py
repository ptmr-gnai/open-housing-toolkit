"""plan_lot: massing, area request and scenario inputs stay consistent. MIT."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
EVIDENCE = ROOT / 'examples/parcel-investigation'
PARCEL = ROOT / 'examples/geometry-inputs/parcel-source'


def run(*args):
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/plan_lot.py'), *args], capture_output=True, text=True, cwd=ROOT)
    return result.returncode, json.loads(result.stdout)


class PlanLot(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()

    def test_massing_scenarios_and_downstream_builds_agree(self):
        from housing_workflow.engine import replay
        from housing_geometry.engine import build as build_massing
        from housing_underwriting.engine import build as build_uw, load
        from housing_render.contracts import validate_scenario
        code, out = run('massing', '--evidence', str(EVIDENCE), '--parcel-source', str(PARCEL), '--stories', '6',
                        '--ground-nonresidential-sf', '5000', '--upper-coverage', '0.8', '--out', str(self.tmp / 'plan'))
        self.assertEqual(code, 0, out)
        program = json.loads((self.tmp / 'plan/program.json').read_text())
        validate_scenario(json.loads((self.tmp / 'plan/render-scenario.json').read_text()))
        replay(EVIDENCE, self.tmp / 'area', json.loads((self.tmp / 'plan/area-request.json').read_text()))
        result = build_massing(self.tmp / 'area', PARCEL, json.loads((self.tmp / 'plan/geometry-scenario.json').read_text()), self.tmp / 'massing')
        self.assertEqual(result['visual_handoff_status'], 'schematic_reference_only')
        geometry = json.loads((self.tmp / 'massing/geometry.json').read_text())
        self.assertTrue(all(c['status'] == 'consistent_within_tolerance' for c in geometry['comparisons']))
        code, out = run('scenarios', '--program', str(self.tmp / 'plan/program.json'), '--land-usd', '4000000',
                        '--hard-cost-psf', '450,550', '--rent-per-home-month', '2000,2600', '--out', str(self.tmp / 'scen'))
        self.assertEqual(code, 0, out)
        self.assertEqual(out['scenarios'], 4)
        for path in sorted((self.tmp / 'scen').glob('*.json')):
            if path.name == 'scenarios.json':
                continue
            req = load(path)
            self.assertEqual(req['program']['gross_area_sf'], program['gross_sf'])
            build_uw(req, self.tmp / 'uw' / req['id'], {})
        self.assertTrue((self.tmp / 'scen/assumptions.md').exists())
        code, out = run('results', '--underwriting', str(self.tmp / 'uw'))
        self.assertEqual((code, out['packages_verified']), (0, 4))
        code, out = run('ownership', '--run', str(ROOT / 'research/ownership-evidence/derived-20261020T033000Z/run-20261020T020741Z-2028710002'))
        self.assertEqual(code, 0)
        self.assertEqual(out['latest_dof_sale']['sale_price_usd'], '13797661.00')

    def test_refuses_existing_output_and_oversized_retail(self):
        (self.tmp / 'busy').mkdir()
        (self.tmp / 'busy/x').write_text('x')
        code, out = run('massing', '--evidence', str(EVIDENCE), '--parcel-source', str(PARCEL), '--stories', '5', '--out', str(self.tmp / 'busy'))
        self.assertEqual(code, 2)
        code, out = run('massing', '--evidence', str(EVIDENCE), '--parcel-source', str(PARCEL), '--stories', '5',
                        '--ground-nonresidential-sf', '9999999', '--out', str(self.tmp / 'big'))
        self.assertEqual(code, 2)
        self.assertIn('exceeds', out['reason'])


if __name__ == '__main__':
    unittest.main()
