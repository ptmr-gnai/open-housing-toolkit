import importlib.util
from pathlib import Path
import unittest

S = Path(__file__).resolve().parents[1] / 'validate_retrospective_portable.py'
spec = importlib.util.spec_from_file_location('portable_paths', S)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class PortablePaths(unittest.TestCase):
    def test_original_input_maps(self):
        self.assertEqual(v.recorded_input_name(str(v.OLD_INPUTS / 'task.md')), 'task.md')
    def test_same_name_outside_boundary_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            v.recorded_input_name('/another/inputs/task.md')
    def test_traversal_and_nested_files_rejected(self):
        for suffix in ['../inputs/task.md', 'nested/task.md']:
            with self.assertRaises(ValueError):v.recorded_input_name(str(v.OLD_INPUTS) + '/' + suffix)
    def test_relocated_frozen_case(self):
        self.assertEqual(v.validate()['page_matched_citations'], 82)

if __name__ == '__main__':
    unittest.main()
