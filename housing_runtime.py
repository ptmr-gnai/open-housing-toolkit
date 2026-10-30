"""Strict replay of the one archived verifier after the public skill-layout move. MIT."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / 'archive/skill-layout-v0'
MODULES = {'housing_workflow', 'housing_recipe', 'housing_render',
           'housing_geometry', 'housing_benefit', 'housing_rer'}


def validate_archive(archive=None):
    archive=Path(archive) if archive is not None else ARCHIVE
    record = json.loads((archive / 'snapshot.json').read_text(encoding='utf-8'))
    if record.get('id') not in {'skill-layout-v0','before-local-output-safety'}:
        raise ValueError('Unsupported historical runtime')
    actual = {str(p.relative_to(archive)) for p in archive.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts
              and p.name not in {'snapshot.json', 'README.md'}}
    if actual != set(record['files']):
        raise ValueError('Historical runtime inventory changed')
    for name, expected in record['files'].items():
        path = archive / name
        if path.is_symlink() or not path.resolve().is_relative_to(archive.resolve()):
            raise ValueError('Historical runtime path escapes archive')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('Historical runtime source changed: ' + name)
    return record


def verify_historical(module, folder):
    if module not in MODULES:
        raise ValueError('Unsupported historical module')
    archives=[ARCHIVE,ROOT/'archive/before-local-output-safety']
    manifest=json.loads((Path(folder)/'manifest.json').read_text())
    implementation=manifest['implementation']
    bound=implementation.get('files',implementation)
    if not isinstance(bound,dict) or not bound:raise ValueError('Historical verification rejected unknown implementation')
    selected=None
    for archive in archives:
        record=validate_archive(archive)
        if all(record['files'].get(name)==sha for name,sha in bound.items()):
            selected=(archive,record);break
    if selected is None:raise ValueError('Historical verification rejected unknown implementation')
    archive,record=selected
    # -E/-P exclude caller PYTHONPATH/cwd while retaining installed user packages.
    # -B leaves the archived source untouched; optional geometry dependencies remain usable.
    # The original verifier compares its own implementation to the retained
    # manifest and recomputes outputs; a mismatch is never accepted by rehashing.
    code = ('import importlib,json,sys; from pathlib import Path; '
            'sys.path.insert(0,sys.argv[1]); '
            'engine=importlib.import_module(sys.argv[2]+".engine"); '
            'print(json.dumps(engine.verify(Path(sys.argv[3]))))')
    result = subprocess.run([sys.executable, '-E', '-P', '-B', '-c', code,
                             str(archive), module, str(Path(folder).resolve())],
                            cwd=archive, capture_output=True, text=True)
    if result.returncode:
        raise ValueError('Historical verification rejected the package: ' + result.stderr[-2000:])
    report = json.loads(result.stdout)
    if report.get('status') != 'passed':
        raise ValueError('Historical verifier did not report success')
    return {**report, 'verification_runtime': 'archived-'+record['id']}
