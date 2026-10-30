"""Run retained research checks as separate offline processes. MIT."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from housing_common.local_outputs import checkout_snapshot,assert_checkout_unchanged
VALIDATORS = [
    'scripts/check_onboarding.py',
    'examples/live-lot-trial/verify.py',
    'research/community-benefit/validate.py',
    'examples/street-placement/verify.py',
    'examples/geometry-render/verify.py',
    'research/source-audit/validate.py',
    'research/jerome-brief/validate.py',
    'research/benchmark-case-search/validate_inputs.py',
    'scripts/validate_retrospective_portable.py',
    'research/eligibility-gates/validate.py',
    'research/requirement-coverage/validate_coverage.py',
    'scripts/validate_conclusion_portable.py',
    'scripts/validate_backtest_portable.py',
    'research/grand-concourse-calibration/validate.py',
]
TEST_DIRS = [
    'tests/housing_rer',
    'tests/housing_benefit',
    'tests/housing_geometry',
    'tests/housing_recipe',
    'tests/housing_render',
    'tests/housing_workflow',
    'tests/scripts',
    'research/jerome-brief/tests',
    'research/benchmark-case-search/tests',
    'research/retrospective-run/tests',
    'research/eligibility-gates/tests',
    'research/requirement-coverage/tests',
    'research/grand-concourse-calibration/tests',
]

if __name__ == '__main__':
    before=checkout_snapshot()
    try:
        for path in VALIDATORS:
            print('Validate: ' + path, flush=True)
            subprocess.run([sys.executable, path], cwd=ROOT, check=True)
        for path in TEST_DIRS:
            print('Test: ' + path, flush=True)
            subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', path, '-v'], cwd=ROOT, check=True)
    finally:
        assert_checkout_unchanged(before)
