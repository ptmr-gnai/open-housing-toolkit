"""Massing-grounded concept: prompt and elevation from the massing, review gates, report and bundle. MIT."""
import json
from pathlib import Path
import shutil
import struct
import tempfile
import unittest
import zlib

from housing_common.local_outputs import ROOT
from housing_concept import engine

MASSING = ROOT / 'examples/grounded-massing/allocation-sensitivity'


def png(color=(200, 0, 0)):
    raw = b'\x00' + bytes(color)
    chunk = lambda t, d: struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')


class Concept(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        (self.tmp / 'photo.png').write_bytes(png())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def prepare(self, name='c'):
        return engine.prepare(MASSING, self.tmp / 'photo.png', self.tmp / name, 'brick', 'shops', 'Google Street View', 'June 2026')

    def review(self, **status):
        checks = {k: {'status': status.get(k, 'consistent'), 'note': ''} for k in engine.CHECKS}
        path = self.tmp / ('review-%s.json' % len(list(self.tmp.glob('review-*'))))
        path.write_text(json.dumps({'reviewer': 'test', 'checks': checks}))
        return path

    def test_prompt_is_compiled_from_massing_numbers_only(self):
        result = self.prepare()
        self.assertEqual(result['stage'], 'prompt_prepared')
        prompt = (self.tmp / 'c/prompt.txt').read_text()
        geometry = json.loads((MASSING / 'geometry.json').read_text())
        self.assertIn('%d stories' % len(geometry['floors']), prompt)
        self.assertIn('no part of them remains', prompt)
        self.assertNotIn('white-and-blue', prompt)
        self.assertTrue((self.tmp / 'c/elevation.png').read_bytes().startswith(b'\x89PNG'))

    def test_attach_verifies_and_rejects_bad_reviews(self):
        self.prepare()
        with self.assertRaisesRegex(ValueError, 'regenerate'):
            engine.attach(self.tmp / 'c', self.tmp / 'photo.png', 'test', self.review(story_count='not_consistent'))
        long_note = self.review()
        data = json.loads(long_note.read_text())
        data['checks']['story_count']['note'] = 'x' * 200
        long_note.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, '160'):
            engine.attach(self.tmp / 'c', self.tmp / 'photo.png', 'test', long_note)
        (self.tmp / 'gen.png').write_bytes(png((0, 0, 200)))
        result = engine.attach(self.tmp / 'c', self.tmp / 'gen.png', 'Codex image_gen', self.review())
        self.assertEqual(result['stage'], 'generated_and_reviewed')
        (self.tmp / 'c/prompt.txt').write_text('make it 20 stories\n')
        with self.assertRaises(ValueError):
            engine.verify(self.tmp / 'c')

    def test_report_shows_grounded_render_and_bundle_withholds_photo(self):
        from housing_feasibility import brief as briefs, engine as report
        from housing_underwriting import engine as underwriting
        self.prepare()
        (self.tmp / 'gen.png').write_bytes(png((0, 0, 200)))
        engine.attach(self.tmp / 'c', self.tmp / 'gen.png', 'Codex image_gen', self.review())
        req = underwriting.load(ROOT / 'config/underwriting/rental-60-base.json')
        req['id'] = 'base'
        underwriting.build(req, self.tmp / 'uw', {})
        briefs.start(self.tmp / 'brief.json', 'Test goal', 'developer')
        request = {'version': '1.1', 'title': 'Test', 'base_case': 'base', 'prepared_on': '2026-11-16', 'prepared_by': 'unit test'}
        report.build(request, self.tmp / 'r', ROOT / 'examples/parcel-investigation', [self.tmp / 'uw'], massing=[MASSING],
                     render=self.tmp / 'c', brief=self.tmp / 'brief.json')
        data = json.loads((self.tmp / 'r/report.json').read_text())
        self.assertEqual(data['render']['kind'], 'massing_grounded')
        self.assertEqual(data['render']['story_status'], 'matches_massing')
        self.assertIn('What the picture was built from', (self.tmp / 'r/report.html').read_text())
        bundled = report.bundle(self.tmp / 'r', self.tmp / 'b.zip')
        self.assertEqual(bundled['withheld'], ['inputs/render/inputs/reference.png'])


if __name__ == '__main__':
    unittest.main()
