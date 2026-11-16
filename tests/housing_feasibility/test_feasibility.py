"""Feasibility report: assembly from verified packages, gates and tamper checks. MIT."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from housing_common.local_outputs import ROOT
from housing_feasibility import engine
from housing_feasibility.contracts import validate_request
from housing_underwriting import engine as underwriting
from housing_feasibility import brief as briefs

EVIDENCE = ROOT / 'examples/parcel-investigation'
MASSING = ROOT / 'examples/grounded-massing/allocation-sensitivity'
RENDER = ROOT / 'examples/site-concept/with-analysis'
OWNERSHIP = ROOT / 'research/ownership-evidence/derived-20261020T033000Z/run-20261020T020741Z-2028710002'
OTHER_LOT = ROOT / 'examples/jerome-evidence-only'
DISCOVERY = ROOT / 'research/nonhousing-discovery/cases/jerome'
REQUEST = {'version': '1.1', 'title': 'Site feasibility: test', 'base_case': 'base', 'prepared_on': '2026-11-16',
           'prepared_by': 'unit test'}


class Report(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp()).resolve()
        base = underwriting.load(ROOT / 'config/underwriting/rental-60-base.json')
        base['id'] = 'base'
        cheaper = copy.deepcopy(base)
        cheaper['id'] = 'cheaper'
        for line in cheaper['capital']['lines']:
            if line['category'] == 'hard_costs':
                line['usd'] = '360'
        cls.brief = cls.tmp / 'brief.json'
        briefs.start(cls.brief, 'Could this lot hold apartments over shops?', 'developer', ['Address=1240 Edward L Grant Hwy'])
        briefs.decide(cls.brief, 'financing', 'Base and a cheaper hard-cost case', 'Go ahead', '2026-11-16')
        cls.uw = []
        for req in (base, cheaper):
            out = cls.tmp / ('uw-' + req['id'])
            underwriting.build(req, out, {})
            cls.uw.append(out)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def build(self, name, **kw):
        args = dict(evidence=EVIDENCE, underwriting=self.uw, massing=[MASSING], ownership=OWNERSHIP, render=RENDER, brief=self.brief)
        args.update(kw)
        return engine.build(kw.pop('request', REQUEST), self.tmp / name, **{k: v for k, v in args.items() if k != 'request'})

    def test_full_report_builds_verifies_and_has_standard_sections(self):
        result = self.build('full')
        self.assertEqual(result['status'], 'passed')
        report = json.loads((self.tmp / 'full/report.json').read_text())
        self.assertEqual(report['site']['bbl'], '2028710002')
        budget = report['development_budget']
        self.assertEqual(budget['base_case_id'], 'base')
        uses = sum(float(u['amount_usd']) for u in budget['uses'])
        self.assertAlmostEqual(uses, float(budget['total_uses_usd']), places=2)
        sources = sum(float(s['amount_usd']) for s in budget['sources'])
        self.assertAlmostEqual(max(float(budget['total_uses_usd']) - sources, 0), float(budget['gap_usd']), places=2)
        scenarios = {s['id']: s for s in report['sensitivity']['scenarios']}
        self.assertEqual(scenarios['cheaper']['hard_cost_per_gross_sf_usd'], '360.00')
        self.assertEqual(len(report['sensitivity']['scenarios']), 2)
        self.assertTrue(report['ownership']['latest_recorded_deed'])
        self.assertEqual(report['render']['stage'], 'generated_and_reviewed')
        self.assertTrue(any('lot area' in c['formula'] for c in report['zoning']['capacity_calculations']))
        html = (self.tmp / 'full/report.html').read_text()
        for heading in ('Brief', 'How we got here', 'Development budget (sources and uses)', 'Operating pro forma',
                        'Sensitivity', 'Open items', 'Every financing scenario', 'Decisions'):
            self.assertIn(heading, html)
        self.assertIn('Could this lot hold apartments over shops?', html)
        self.assertEqual(report['brief']['decisions'][0]['answer'], 'Go ahead')
        steps = {st['step']: st['status'] for st in report['process']['steps']}
        self.assertEqual((steps['search'], steps['ownership'], steps['render']), ('not_run', 'ran', 'ran'))
        self.assertIsNone(report['search'])

    def test_search_block_lists_candidates_and_selection(self):
        brief = self.tmp / 'brief-search.json'
        briefs.start(brief, 'Which lots near Jerome Avenue could become housing, and why?', 'housing_agency')
        briefs.decide(brief, 'select', 'Top-ranked candidate', 'Take the first one, it is the biggest', '2026-11-16')
        engine.build(REQUEST, self.tmp / 'search', EVIDENCE, self.uw, discovery=DISCOVERY, brief=brief)
        report = json.loads((self.tmp / 'search/report.json').read_text())
        search = report['search']
        self.assertEqual(search['selected']['rank'], 1)
        self.assertEqual(len(search['all_candidates']), search['candidates_count'])
        self.assertEqual(search['selected']['why_user_words'], ['Take the first one, it is the biggest'])
        html = (self.tmp / 'search/report.html').read_text()
        self.assertIn('All candidates from the area search', html)
        self.assertIn('Area search', html)

    def test_bundle_withholds_source_photo_and_verifies_elsewhere(self):
        import struct
        import zipfile
        import zlib
        from housing_render.engine import prepare
        from housing_render.contracts import load as rload
        def png():
            raw = b'\x00\xff\x00\x00'
            chunk = lambda t, d: struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
            return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')
        photo = self.tmp / 'street.png'
        photo.write_bytes(png())
        scene = rload(ROOT / 'examples/site-concept/scene.json')
        scene['reference']['availability'] = 'local_file'
        prepare(scene, rload(ROOT / 'examples/site-concept/scenario.json'), self.tmp / 'render-local', None, photo)
        engine.build(REQUEST, self.tmp / 'withphoto', EVIDENCE, self.uw, render=self.tmp / 'render-local', brief=self.brief)
        result = engine.bundle(self.tmp / 'withphoto', self.tmp / 'b.zip')
        self.assertEqual(result['withheld'], ['inputs/render/inputs/reference.png'])
        with zipfile.ZipFile(self.tmp / 'b.zip') as z:
            names = z.namelist()
            self.assertIn('README.md', names)
            self.assertNotIn('report/inputs/render/inputs/reference.png', names)
            z.extractall(self.tmp / 'unzipped')
        verified = engine.verify(self.tmp / 'unzipped/report')
        self.assertEqual(verified['inputs_checked_by_hash_only'], ['inputs/render'])
        self.assertEqual(verified['evidence_fingerprint'], result['evidence_fingerprint'])
        html = self.tmp / 'withphoto/report.html'
        self.assertTrue(engine.verify_html(html, self.tmp / 'unzipped/report')['html_matches_bundle'])
        self.assertIn('github.com/ptmr-gnai/open-housing-toolkit', html.read_text())
        from housing_feasibility.__main__ import main
        import contextlib, io
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            main(['show', '--html', str(html), '--section', 'headline'])
        self.assertEqual(json.loads(buffer.getvalue())['bbl'], '2028710002')
        ready = engine.continue_from(self.tmp / 'unzipped/report', self.tmp / 'continued')
        self.assertIsNone(ready['reusable_inputs']['render'])
        brief = json.loads((self.tmp / 'continued/brief.json').read_text())
        self.assertEqual(brief['extends'][0]['evidence_fingerprint'], result['evidence_fingerprint'])

    def test_activity_flags_site_and_leads_open_items(self):
        import sys
        sys.path.insert(0, str(ROOT / 'tests/housing_activity'))
        import test_activity
        from housing_activity import engine as activity
        test_activity.LOT_A = '2028710002'
        fetch = test_activity.fake_fetcher()
        def patched(url):
            status, body, err = fetch(url)
            return status, body.replace(b'2031780001', b'2028710002'), err
        activity.collect(self.tmp / 'act', bbls=['2028710002'], as_of='2026-11-16', fetcher=patched)
        engine.build(REQUEST, self.tmp / 'withact', EVIDENCE, self.uw, brief=self.brief, activity=self.tmp / 'act')
        report = json.loads((self.tmp / 'withact/report.json').read_text())
        self.assertEqual(report['site']['development_activity']['status'], 'active_development')
        self.assertEqual(report['open_items'][0]['area'], 'current activity')
        steps = {st['step']: st['status'] for st in report['process']['steps']}
        self.assertEqual(steps['activity'], 'ran')

    def test_tampered_report_fails(self):
        self.build('tamper')
        path = self.tmp / 'tamper/report.json'
        data = json.loads(path.read_text())
        data['headline']['base_gap_usd'] = '0.00'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'changed'):
            engine.verify(self.tmp / 'tamper')

    def test_tampered_input_fails(self):
        self.build('input')
        target = next((self.tmp / 'input/inputs/underwriting').iterdir()) / 'results.json'
        target.write_text(target.read_text().replace('"homes": 60', '"homes": 61'))
        with self.assertRaises(ValueError):
            engine.verify(self.tmp / 'input')

    def test_other_lot_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'different tax lot'):
            self.build('mixed', evidence=OTHER_LOT)

    def test_unknown_base_case_is_rejected(self):
        bad = dict(REQUEST, base_case='missing')
        with self.assertRaisesRegex(ValueError, 'Base case'):
            engine.build(bad, self.tmp / 'nobase', EVIDENCE, self.uw, brief=self.brief)

    def test_minimal_report_and_no_overwrite(self):
        result = engine.build(REQUEST, self.tmp / 'minimal', EVIDENCE, self.uw[:1], brief=self.brief)
        self.assertEqual(result['status'], 'passed')
        with self.assertRaisesRegex(ValueError, 'never overwritten'):
            engine.build(REQUEST, self.tmp / 'minimal', EVIDENCE, self.uw[:1], brief=self.brief)

    def test_brief_is_required_and_append_only(self):
        with self.assertRaisesRegex(ValueError, 'brief is required'):
            engine.build(REQUEST, self.tmp / 'nobrief', EVIDENCE, self.uw[:1])
        with self.assertRaisesRegex(ValueError, 'already exists'):
            briefs.start(self.brief, 'x', 'developer')
        with self.assertRaises(ValueError):
            briefs.decide(self.brief, 'dreaming', 'x', 'y')

    def test_request_contract(self):
        with self.assertRaises(ValueError):
            validate_request(dict(REQUEST, version='1.0'))
        with self.assertRaises(ValueError):
            validate_request(dict(REQUEST, extra=1))


if __name__ == '__main__':
    unittest.main()
