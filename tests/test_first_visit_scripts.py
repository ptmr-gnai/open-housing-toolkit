"""Offline checks for the first-visit install and place helpers. MIT."""
import importlib.util
import json
import math
import pathlib
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


locate = load('locate')
preflight = load('preflight')


class Locate(unittest.TestCase):
    def test_bbox_is_square_in_meters(self):
        west, south, east, north = locate.bbox(40.84, -73.92, 400)
        self.assertAlmostEqual((north - south) * 111320, 800, delta=1)
        self.assertAlmostEqual((east - west) * 111320 * math.cos(math.radians(40.84)), 800, delta=1)

    def test_area_request_matches_discovery_schema(self):
        import jsonschema
        match = {'label': '170 St station (4), Bx', 'borough': 'BX', 'lat': 40.840075, 'lon': -73.917791, 'bbl': None}
        with tempfile.TemporaryDirectory() as d:
            out = pathlib.Path(d) / 'area' / 'request.json'
            with patch.object(locate, 'stations', return_value=[match]), \
                 patch('sys.argv', ['locate.py', 'area', '--station', '170 St', '--out', str(out)]):
                self.assertEqual(locate.main(), 0)
            request = json.loads(out.read_text())
        schema = json.loads((ROOT / 'src/housing_site_discovery/request.schema.json').read_text())
        jsonschema.validate(request, schema)
        self.assertEqual(request['scope']['borough'], 'BX')

    def test_existing_output_is_never_overwritten(self):
        match = {'label': 'x', 'borough': 'BK', 'lat': 40.68, 'lon': -73.95, 'bbl': None}
        with tempfile.TemporaryDirectory() as d:
            out = pathlib.Path(d) / 'request.json'
            out.write_text('keep')
            with patch.object(locate, 'search', return_value=[match]), \
                 patch('sys.argv', ['locate.py', 'area', 'somewhere', '--out', str(out)]):
                with self.assertRaisesRegex(ValueError, 'already exists'):
                    locate.main()
            self.assertEqual(out.read_text(), 'keep')


class Preflight(unittest.TestCase):
    def test_runtime_detection(self):
        with patch.dict('os.environ', {'CLAUDECODE': '1'}, clear=True):
            self.assertEqual(preflight.agent_runtime(), 'claude-code')
        with patch.dict('os.environ', {'CODEX_SANDBOX': 'seatbelt'}, clear=True):
            self.assertEqual(preflight.agent_runtime(), 'codex')
        with patch.dict('os.environ', {}, clear=True):
            self.assertEqual(preflight.agent_runtime(), 'unknown')

    def test_current_interpreter_is_accepted_when_new_enough(self):
        python, how = preflight.find_python()
        self.assertIsNotNone(python)
        self.assertIn('Python 3.', how)


if __name__ == '__main__':
    unittest.main()
