#!/usr/bin/env python3
"""Public source collection with byte-level provenance; stdlib only. MIT."""
import argparse, concurrent.futures, datetime, hashlib, json, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent

def fetch(source_id, url, publisher, limits, terms=None, refresh=False):
    """Save body unchanged. Failures are records, never empty successful datasets."""
    base = ROOT / 'cache'
    base.mkdir(exist_ok=True)
    record_path=base/(source_id+'.source.json')
    if record_path.exists():
        previous=json.loads(record_path.read_text())
        if previous.get('status')=='ok' and not refresh:
            if previous['url']!=url:
                raise ValueError('Source ID already binds a different URL; use a new ID or explicit --refresh: '+source_id)
            if hashlib.sha256((ROOT/previous['cache_path']).read_bytes()).hexdigest()!=previous['sha256']:
                raise ValueError('Changed cached source: '+source_id)
            return previous
        history=base/'history'/source_id
        history.mkdir(parents=True,exist_ok=True)
        stamp=previous['retrieved_at'].replace(':','_')
        if previous.get('status')=='ok':
            body=(ROOT/previous['cache_path']).read_bytes()
            old_path=history/(previous['sha256']+'.body')
            old_path.write_bytes(body)
            previous['cache_path']=str(old_path.relative_to(ROOT))
        (history/(stamp+'.source.json')).write_text(json.dumps(previous,indent=2)+'\n')
    record = {'id': source_id, 'url': url, 'publisher': publisher,
              'retrieved_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'coverage_limits': limits, 'terms_url': terms,
              'source_updated_at': None}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'OpenHousingProbe/0.1 (public research)'})
        with urllib.request.urlopen(req, timeout=55) as response:
            body = response.read()
            record.update(status='ok', http_status=response.status,
                          content_type=response.headers.get('Content-Type'),
                          last_modified=response.headers.get('Last-Modified'))
        path = base / (source_id + '.body')
        path.write_bytes(body)
        record.update(cache_path=str(path.relative_to(ROOT)), bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest())
        try:
            data = json.loads(body)
            if isinstance(data, dict):
                record['source_updated_at'] = data.get('rowsUpdatedAt') or data.get('viewLastModified')
                record['dataset_name'] = data.get('name')
        except (ValueError, UnicodeDecodeError):
            pass
    except Exception as exc:
        record.update(status='failed', error=type(exc).__name__ + ': ' + str(exc))
    record_path.write_text(json.dumps(record, indent=2) + '\n')
    with (base/'collection-attempts.jsonl').open('a') as ledger:
        ledger.write(json.dumps(record,sort_keys=True)+'\n')
    return record

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sources', help='JSON array of source request definitions')
    parser.add_argument('--refresh',action='store_true',help='Explicitly replace current source bindings, archiving prior evidence')
    args = parser.parse_args()
    definitions = json.loads(pathlib.Path(args.sources).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda source: fetch(**source,refresh=args.refresh), definitions))
    for result in results:
        print(json.dumps({key: result.get(key) for key in ['id', 'status', 'bytes', 'dataset_name', 'error']}))
