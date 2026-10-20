#!/usr/bin/env python3
"""Regenerate evidence packages with the corrected code (v0.3) from retained
raw receipts. Writes NEW derived directories; never modifies original runs.
No network access: reuses exact raw receipts and original retrieval dates."""
import hashlib, json, pathlib, shutil, sys, datetime
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import parcel_evidence as pe

ROOT = pathlib.Path(__file__).resolve().parents[1] / 'runs'
DERIVED = ROOT / 'derived-20261020T033000Z'
ORIGINAL_COMMIT = '365e5b3'
RUNS = ['run-20261020T020741Z-2028710002', 'run-20261020T020834Z-2028430040',
        'run-20261020T031148Z-1012127503']

DERIVED.mkdir(exist_ok=True)
for run_id in RUNS:
    src = ROOT / run_id
    dst = DERIVED / run_id
    if dst.exists():
        shutil.rmtree(dst)
    (dst / 'cache').mkdir(parents=True)
    # Byte-identical copy of the original receipts (original retrieval dates).
    for f in (src / 'cache').iterdir():
        shutil.copy2(f, dst / 'cache' / f.name)
    shutil.copy2(src / 'run.json', dst / 'run.json')
    notes = ('Regenerated with corrected parcel_evidence.py (package v0.3): PLUTO '
             'ownername/zonedist1 tax-roll fields with precise locators, unit-level '
             'DOF sale scope, fail-closed cached receipt verification. Raw receipts '
             'are byte-identical copies of the original run cache; original '
             'retrieval dates preserved. No new network requests.')
    augmented = []
    # Runs 1 and 2 predate the mapping feature; augment with the retained
    # doc_codes receipt from the documentation session (exact raw receipt).
    if not (dst / 'cache' / 'acris_doc_codes.source.json').exists():
        for name in ('acris_doc_codes.body', 'acris_doc_codes.source.json'):
            shutil.copy2(ROOT / 'docs' / 'cache' / name, dst / 'cache' / name)
        rec = json.loads((dst / 'cache' / 'acris_doc_codes.source.json').read_text())
        augmented.append('acris_doc_codes receipt copied from runs/docs/cache '
                         '(retrieved %s, sha256 %s)' % (rec['retrieved_at'], rec['sha256']))
    package = pe.write_package(dst)
    lineage = {'derived_from': run_id, 'original_run_id': run_id,
               'original_commit': ORIGINAL_COMMIT,
               'regenerated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'code_version': package['package_version'],
               'notes': notes, 'augmented_with': augmented,
               'original_package_sha256': hashlib.sha256((src / 'package.json').read_bytes()).hexdigest(),
               'derived_package_sha256': hashlib.sha256((dst / 'package.json').read_bytes()).hexdigest()}
    (dst / 'lineage.json').write_text(json.dumps(lineage, indent=2) + '\n')
    # Verify receipts are byte-identical to the originals.
    for f in (src / 'cache').iterdir():
        a = hashlib.sha256(f.read_bytes()).hexdigest()
        b = hashlib.sha256((dst / 'cache' / f.name).read_bytes()).hexdigest()
        assert a == b, 'receipt differs: %s' % f.name
    print('%s: %d records, %d unknowns, %d conflicts' %
          (run_id, len(package['records']), len(package['unknowns']), len(package['conflicts'])))
print('derived packages written to', DERIVED)
