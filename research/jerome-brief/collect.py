"""Use the bounded audit collector with an independent immutable case snapshot. MIT."""
import concurrent.futures,importlib.util,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_audit',ROOT.parent/'source-audit'/'audit.py')
audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit);audit.ROOT=ROOT
if __name__=='__main__':
    requests=json.loads((ROOT/'requests.json').read_text())
    if any((ROOT/'cache'/(r['id']+'.receipt.json')).exists() for r in requests):raise SystemExit('Snapshot exists; create a new versioned directory for refresh rather than overwriting reviewed sources.')
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for r in pool.map(audit.collect,requests):print(json.dumps(r),flush=True)
