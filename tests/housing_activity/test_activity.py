"""Development-activity check: classification, coverage gaps, failures and tamper checks (offline). MIT."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import urllib.parse

from housing_activity import engine

LOT_A, LOT_B, LOT_C = '2031780001', '2028540044', '2028290045'


def fake_fetcher(failing=()):
    def fetch(url):
        q = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
        dataset = urllib.parse.urlsplit(url).path.split('/')[-1].replace('.json', '')
        if dataset in failing:
            return 503, b'busy', 'HTTP 503'
        if q.get('$select', '').startswith('count(*)'):
            rows = 0 if dataset == 'w9ak-ipjd' else 1000
            return 200, json.dumps([{'rows': str(rows)}]).encode(), None
        if dataset == 'rbx6-tga4':
            rows = [{'bbl': LOT_A, 'work_type': 'Full Demolition', 'permit_status': 'Signed-off', 'issued_date': '2025-12-16T00:00:00.000',
                     'job_filing_number': 'X1', 'job_description': 'Full demolition to a high one story building'},
                    {'bbl': LOT_B, 'work_type': 'Construction Fence', 'permit_status': 'Permit Issued', 'issued_date': '2024-07-25T00:00:00.000',
                     'job_filing_number': 'X2', 'job_description': 'PROPOSED 8FT CONSTRUCTION FENCE'},
                    {'bbl': LOT_C, 'work_type': 'Sidewalk Shed', 'permit_status': 'Permit Issued', 'issued_date': '2025-01-01T00:00:00.000',
                     'job_filing_number': 'X3', 'job_description': 'Facade shed'},
                    {'bbl': LOT_C, 'work_type': 'Foundation', 'permit_status': 'Signed-off', 'issued_date': '2019-01-01T00:00:00.000',
                     'job_filing_number': 'X4', 'job_description': 'Old foundation work outside the window'}]
            return 200, json.dumps(rows).encode(), None
        return 200, b'[]', None
    return fetch


class Activity(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_check(self, name, **kw):
        return engine.collect(self.tmp / name, bbls=[LOT_A, LOT_B, LOT_C], as_of='2026-11-16', fetcher=fake_fetcher(**kw))

    def test_classifies_activity_and_reports_coverage_gap(self):
        result = self.run_check('ok')
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['active'], [LOT_A])
        data = json.loads((self.tmp / 'ok/activity.json').read_text())
        status = {l['bbl']: l['status'] for l in data['lots']}
        self.assertEqual(status, {LOT_A: 'active_development', LOT_B: 'site_preparation', LOT_C: 'none_found'})
        self.assertEqual(data['coverage_gaps'], ['DOB NOW: Build – Job Application Filings (BRONX)'])
        self.assertIn('Full Demolition', next(l for l in data['lots'] if l['bbl'] == LOT_A)['latest'])

    def test_failed_source_is_not_none_found(self):
        self.run_check('partial', failing=('ipu4-2q9a',))
        data = json.loads((self.tmp / 'partial/activity.json').read_text())
        self.assertEqual(data['run_status'], 'partial')
        status = {l['bbl']: l['status'] for l in data['lots']}
        self.assertEqual(status[LOT_C], 'not_checked')
        self.assertEqual(status[LOT_A], 'active_development')

    def test_tampered_response_fails_verify(self):
        self.run_check('tamper')
        body = next((self.tmp / 'tamper/sources').glob('*dob_now_permits.json'))
        body.write_text('[]')
        with self.assertRaises(ValueError):
            engine.verify(self.tmp / 'tamper')

    def test_rejects_bad_bbl_and_existing_output(self):
        with self.assertRaises(ValueError):
            engine.collect(self.tmp / 'bad', bbls=['12345'], fetcher=fake_fetcher())
        self.run_check('once')
        with self.assertRaises(ValueError):
            self.run_check('once')


if __name__ == '__main__':
    unittest.main()
