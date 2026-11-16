"""Read-only replay of the retained ownership evidence packages. MIT.

Rebuilds each derived package from its retained raw receipts with the current
housing_ownership code and requires an identical result. No network, no writes.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from housing_ownership import engine  # noqa: E402

DERIVED = pathlib.Path(__file__).parent / 'derived-20261020T033000Z'
runs = sorted(p for p in DERIVED.iterdir() if p.is_dir())
assert len(runs) == 3, runs
for run in runs:
    rebuilt = engine.build_package(run)
    assert rebuilt == json.loads((run / 'package.json').read_text()), 'Package differs on replay: ' + run.name
print('Ownership evidence: 3 retained packages replay identically from raw ACRIS, DOF and PLUTO receipts.')
