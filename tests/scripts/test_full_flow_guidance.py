"""Structural regression checks for agent guidance, not an agent behavior test."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class FullFlowGuidanceTests(unittest.TestCase):
    def test_entry_points_route_broad_requests_to_coordinator(self):
        for name in ('AGENTS.md', 'CLAUDE.md'):
            with self.subTest(name=name):
                text = (ROOT / name).read_text().lower()
                self.assertIn('whole-flow', text)
                self.assertIn('skills/start-here/skill.md#practitioner-guide', text)
        start = (ROOT / 'skills/start-here/SKILL.md').read_text()
        self.assertIn('references/full-flow.md', start)
        self.assertIn('Independent and evidence-only requests', start)

    def test_site_only_routes_to_early_menu_not_evidence_shortcut(self):
        entry = ' '.join((ROOT / 'AGENTS.md').read_text().lower().split())
        start = ' '.join((ROOT / 'skills/start-here/SKILL.md').read_text().lower().split())
        guide = ' '.join((ROOT / 'skills/start-here/references/full-flow.md').read_text().lower().split())
        self.assertIn('bare address or bbl with no requested outcome', entry)
        self.assertIn('explicit evidence-only', entry)
        self.assertIn('site-only address or bbl without an outcome', start)
        self.assertIn('first user-facing response', guide)
        self.assertIn('show the menu itself', guide)
        self.assertIn('which would you like to explore?', guide)
        self.assertIn("i'm not sure, help me choose", guide)
        self.assertIn('do not wait for collection before presenting it', guide)
        self.assertIn('do not ask for the address again', guide)

    def test_resume_states_and_honest_stage_boundaries_are_documented(self):
        text = ' '.join((ROOT / 'skills/start-here/references/full-flow.md').read_text().lower().split())
        for state in ('completed', 'awaiting input', 'declined', 'unsupported', 'blocked'):
            self.assertIn(state, text)
        for phrase in ('stage-status.md', 'independent ready branches', 'practitioner approval',
                       'not permitted homes', 'homeownership', 'street view screenshot',
                       'provider receipts', 'one or two consequential questions',
                       'new project or a', 'continuation', 'approved assumptions',
                       'prior location', "actual runtime", "i don't know",
                       "actually ask the question", "create it exclusively",
                       "intent and selected outcomes", "explicitly say that this runtime cannot generate"):
            self.assertIn(phrase, text)

    def test_parcel_only_guidance_returns_full_requests_to_coordinator(self):
        for path in ('skills/housing-investigation/SKILL.md',
                     'skills/housing-investigation/references/runbook.md',
                     'docs/guides/investigate-a-lot.md'):
            with self.subTest(path=path):
                self.assertIn('full-flow', (ROOT / path).read_text().lower())


if __name__ == '__main__':
    unittest.main()
