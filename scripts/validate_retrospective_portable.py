"""Relocate the recorded 2019-input boundary without rewriting its frozen record. MIT."""
import importlib.util
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'research/retrospective-run'
OLD_INPUTS = PurePosixPath('/workspace/bronx-housing-probe/research/benchmark-case-search/inputs')
INPUTS = ROOT / 'research/benchmark-case-search/inputs'
spec = importlib.util.spec_from_file_location('frozen_retrospective_validator', CASE / 'validate.py')
legacy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(legacy)

def recorded_input_name(recorded_path):
    # Bind to the exact recorded root, not any path sharing a basename or suffix.
    path = PurePosixPath(recorded_path)
    if '..' in path.parts:
        raise ValueError('Traversal in recorded input path')
    try:
        relative = path.relative_to(OLD_INPUTS)
    except ValueError as exc:
        raise ValueError('Recorded path outside original input boundary') from exc
    if len(relative.parts) != 1:
        raise ValueError('Recorded input must be an immediate file')
    return relative.name

def validate():
    pre = json.loads((CASE / 'precommit.json').read_text())
    for name, digest in pre['files'].items():
        if legacy.digest(ROOT / name) != digest:
            raise ValueError('Input changed: ' + name)
    if legacy.digest(CASE / 'rubric.json') != pre['rubric_sha256']:
        raise ValueError('Rubric changed after precommit')
    result = legacy.validate_claims(json.loads((CASE / 'claims.json').read_text()))
    allowed = {p.name: legacy.digest(p) for p in INPUTS.iterdir() if p.is_file()}
    for read in json.loads((CASE / 'access-log.json').read_text())['reads']:
        name = recorded_input_name(read['file'])
        if name not in allowed or allowed[name] != read['sha256']:
            raise ValueError('Recorded input missing or hash mismatch')
    freeze = json.loads((CASE / 'freeze.json').read_text())
    legacy.check_frozen(CASE, freeze['files'])
    for name, key in [('validate.py', 'validator_sha256'), ('freeze.py', 'freeze_code_sha256')]:
        if legacy.digest(CASE / name) != freeze[key]:
            raise ValueError('Frozen validation code changed')
    result.update(technical_boundary='pass', historical_path_relocation='exact original input root mapped to current checkout; same bytes', access_enforcement='self-reported original reads, not OS sandbox', semantic_accuracy='requires evaluator review', practitioner_utility='not_tested', historical_certification='blocked')
    return result

if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
