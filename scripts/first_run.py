"""Offline, fail-closed onboarding across independent verified modules. MIT."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(out: Path) -> None:
    if sys.version_info < (3, 11):
        raise ValueError('Python 3.11+ is required')
    out = out.resolve()
    # Never write into immutable input/code directories, even if a child is absent.
    if out == ROOT or (out.is_relative_to(ROOT) and not out.is_relative_to(ROOT / 'runs')):
        raise ValueError('Within the checkout, choose an output under runs/')
    if out.exists():
        raise ValueError('Output already exists; choose a new directory')
    out.mkdir(parents=True)
    commands = [
        ['housing_workflow', 'demo', '--out', str(out / 'parcel')],
        ['housing_workflow', 'verify', '--run', str(out / 'parcel')],
        ['housing_recipe', 'build', '--from-run', str(out / 'parcel'), '--recipe',
         str(ROOT / 'recipes/area-budget.json'), '--out', str(out / 'recipe')],
        ['housing_recipe', 'verify', '--run', str(out / 'recipe')],
        ['housing_benefit', 'build', '--analysis', str(out / 'recipe'), '--references',
         str(ROOT / 'examples/affordability-inputs/reference-source'), '--input',
         str(ROOT / 'examples/affordability-inputs/request.json'), '--out', str(out / 'comparison')],
        ['housing_benefit', 'verify', '--run', str(out / 'comparison')],
        ['housing_rer', 'build', '--comparison', str(out / 'comparison'), '--input',
         str(ROOT / 'examples/rer-inputs/request.json'), '--out', str(out / 'rer')],
        ['housing_rer', 'verify', '--run', str(out / 'rer')],
    ]
    results = []
    for i, command in enumerate(commands, 1):
        args = [sys.executable, '-m', *command]
        print(f'{i}/{len(commands)}: {command[0]} {command[1]}', flush=True)
        result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
        log = f'{i:02d}-{command[0]}-{command[1]}.log'
        (out / log).write_text(result.stdout + result.stderr)
        results.append({'command': args, 'returncode': result.returncode, 'log': log})
        # Execution ledger is diagnostic, not a new provenance-verification layer.
        (out / 'steps.json').write_text(json.dumps(results, indent=2) + '\n')
        if result.returncode:
            raise ValueError(f'Stopped at {command[0]} {command[1]}; inspect {out / log}. Use a new output for retry.')
    (out / 'README.md').write_text('''# First-run walkthrough

All four modules built and verified. This index records technical execution,
not professional acceptance. See steps.json and the individual execution logs.

Read in sequence:

1. [Parcel evidence](parcel/packet.html) ([Markdown](parcel/packet.md)). Cached
   real-source records; no current collection or finding of vacancy.
2. [Area recipe](recipe/packet.html) ([Markdown](recipe/packet.md)). 34
   home-equivalents; no feasible unit count or zoning capacity established.
3. [Housing offers](comparison/packet.html) ([Markdown](comparison/packet.md)).
   Independently assumed 24/36 homes; 16/8 meet the lower-profile cost-and-bedroom
   test. No eligibility, delivery, ranking or reconciliation to the area budget.
4. [RER preparation](rer/packet.html) ([Markdown](rer/packet.md)). Separate
   five-section illustrative drafts, instruction map and missing-data states.
   These are incomplete drafts, not official forms or compliance findings.

Each module retains typed IR, inputs and its own verifiable manifest. The comparison
retains the newly built recipe as context; its program assumptions are not derived
from it. Historical 2025 affordability references are not current 2026 program rules.
The sample RER preparation date remains its supplied 2026-10-29, not today's date.
Earlier packet text describing queries refers to retained collection, not this run.
Geometry, image generation, live collection and expert review were not executed.
Start with the short final index/coverage and follow individual claims into the
longer evidence packets. See docs/first-run.md in the checkout for reading and
manual community-data acquisition guidance.

Next: identify a real practitioner question and supplied inputs; use the start-here
skill's module map. Missing EDDE/community data, program definitions, applicability
and applicant interpretation remain substantive work, not template defaults.
''')
    print(f'Completed. Open {out / "README.md"} and {out / "rer/packet.html"}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        run(args.out)
        return 0
    except (ValueError, OSError) as exc:
        print(f'Blocked: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
