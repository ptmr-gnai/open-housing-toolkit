"""Challenge evidence-stage, accounting and population boundaries. MIT."""
import copy
import importlib.util
from pathlib import Path
import unittest

CASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('stanyan_validation', CASE / 'validate.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(v.load('case-data.json'))
        self.sources = v.load('sources.json')

    def reject(self, pattern):
        with self.assertRaisesRegex(ValueError, pattern):
            v.validate_boundaries(self.data, self.sources)

    def test_later_budget_cannot_become_2022_evidence(self):
        self.data['finance'][1]['source_id'] = 'board-packet-2023'
        self.reject('another decision stage')

    def test_losp_cannot_close_a_capital_gap(self):
        self.data['finance'][2]['sources_usd']['losp_contract'] = 11720975
        self.reject('not permanent development capital')

    def test_paid_land_cannot_be_added_twice(self):
        self.data['finance'][2]['excluded_city_land_usd'] = 15900000
        self.reject('off-budget land')

    def test_nplh_subset_cannot_be_added_to_psh_homes(self):
        self.data['operations']['psh_losp_units'] += 19
        self.reject('partition')

    def test_full_year_support_cannot_replace_opening_year_disbursement(self):
        self.data['operations']['losp_schedule']['first_year_months'] = 12
        self.reject('opening-year')

    def test_discrepancy_is_preserved_instead_of_corrected(self):
        result = v.calculate(self.data)
        self.assertEqual(result['capital']['2023']['source_rows_minus_reported_total_usd'], -1)
        self.data['finance'][2]['sources_usd']['mohcd_loan'] += 1
        self.assertNotEqual(v.calculate(self.data), v.load('checks.json'))


if __name__ == '__main__':
    unittest.main()
