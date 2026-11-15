"""Allowlisted Socrata collection with receipts, paging and explicit coverage. MIT."""
from datetime import datetime, timezone
import json
from pathlib import Path
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from .common import bbl, digest, dumps, fresh, load, save, seal, validate_request, verify_files
from housing_common.local_outputs import destination

REGISTRY = load(Path(__file__).with_name('providers.json'))
PAGE = 1000
CHUNK = 100


def predicate(scope):
    w,s,e,n = scope['bbox']
    return f"borough='{scope['borough']}' AND longitude>={w} AND longitude<={e} AND latitude>={s} AND latitude<={n}"


def url(provider, params=None):
    dataset = REGISTRY[provider]['dataset']
    return ('https://data.cityofnewyork.us/api/views/'+dataset+'.json' if params is None
            else 'https://data.cityofnewyork.us/resource/'+dataset+'.json?'+urllib.parse.urlencode(params))


def same_query(actual, expected):
    a,b = urllib.parse.urlsplit(actual),urllib.parse.urlsplit(expected)
    return ((a.scheme,a.netloc,a.path,a.fragment)==(b.scheme,b.netloc,b.path,b.fragment)
            and sorted(urllib.parse.parse_qsl(a.query,keep_blank_values=True))==sorted(urllib.parse.parse_qsl(b.query,keep_blank_values=True)))


class Fetcher:
    def __init__(self, folder, ca_file=None, max_requests=100):
        self.folder = folder
        (folder/'sources').mkdir()
        self.receipts = []
        self.context = ssl.create_default_context(cafile=ca_file)
        self.max_requests = max_requests
        self.attempts = 0

    def fetch(self, provider, params=None):
        uri = url(provider, params)
        record = {'id':str(len(self.receipts)), 'provider':provider,'url':uri,'params':params,
                  'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'failed','attempts':[]}
        self.receipts.append(record)
        body = None
        for retry in range(2):
            if self.attempts >= self.max_requests:
                record['error'] = 'Session request budget reached'
                break
            self.attempts += 1
            try:
                request = urllib.request.Request(uri, headers={'User-Agent':'OpenHousingToolkit-Discovery/1.0','Accept':'application/json'})
                with urllib.request.urlopen(request, timeout=30, context=self.context) as response:
                    body = response.read(16*1024*1024 + 1)
                    if len(body) > 16*1024*1024:
                        raise ValueError('Source response exceeds 16 MiB limit')
                    record['attempts'].append({'http_status':response.status})
                    record['http_status'] = response.status
                parsed = json.loads(body)
                if (params is None and not isinstance(parsed,dict)) or (params is not None and (not isinstance(parsed,list) or not all(isinstance(x,dict) for x in parsed))):
                    raise ValueError('Unexpected source JSON shape')
                record['status'] = 'ok'
                break
            except urllib.error.HTTPError as exc:
                body = exc.read(1024*1024)
                record['attempts'].append({'http_status':exc.code})
                record['error'] = f'HTTP {exc.code}'
                if retry == 0 and exc.code in [429,500,502,503,504]:
                    wait = exc.headers.get('Retry-After','1')
                    if wait.isdigit() and int(wait) <= 5:
                        time.sleep(max(1,int(wait)))
                        continue
                break
            except (OSError,ValueError) as exc:
                record['error'] = str(exc)
                break
        if body is not None:
            name = f'sources/{record["id"]}-{provider}.json'
            (self.folder/name).write_bytes(body)
            record.update(body_path=name,sha256=digest(body),bytes=len(body))
        save(self.folder/'receipts.json', self.receipts)
        if record['status'] != 'ok':
            return None
        record.pop('error',None)
        save(self.folder/'receipts.json', self.receipts)
        return parsed


def _check_metadata(provider, meta):
    if meta is None:
        return False
    available = {c.get('fieldName'):c.get('dataTypeName') for c in meta.get('columns',[])}
    if not set(REGISTRY[provider]['fields']) <= set(available):
        raise ValueError('Provider schema changed: '+provider)
    key = 'project_id' if provider == 'zap_projects' else 'bbl'
    if available.get(key) != ('text' if key == 'project_id' else 'number'):
        raise ValueError('Provider join-key type changed: '+provider)
    return True


def derive(folder):
    req = validate_request(load(folder/'request.json'))
    receipts = load(folder/'receipts.json')
    if [r['id'] for r in receipts] != [str(i) for i in range(len(receipts))]:
        raise ValueError('Missing or duplicated receipt identities')
    records = {p:[] for p in REGISTRY}
    metadata = {p:[] for p in REGISTRY}
    pluto_pages = []
    complete_context = {p:True for p in REGISTRY if p != 'pluto'}
    for r in receipts:
        provider = r['provider']
        if provider not in REGISTRY or not same_query(r['url'],url(provider,r['params'])):
            raise ValueError('Receipt is not an allowlisted source request')
        if 'body_path' in r:
            if r['body_path'] != f'sources/{r["id"]}-{provider}.json':
                raise ValueError('Unexpected source-body path')
            body = (folder/r['body_path']).read_bytes()
            if digest(body) != r['sha256'] or len(body) != r['bytes']:
                raise ValueError('Source receipt mismatch')
        if r['status'] != 'ok':
            if provider in complete_context:
                complete_context[provider] = False
            continue
        data = load(folder/r['body_path'])
        if r['params'] is None:
            _check_metadata(provider,data)
            metadata[provider].append(data)
        elif '$select' in r['params'] and r['params']['$select'].startswith('count('):
            continue
        else:
            if len(data) >= int(r['params'].get('$limit','2001')):
                if provider in complete_context:
                    complete_context[provider] = False
            for i,row in enumerate(data):
                records[provider].append({'row':row,'reference':{'receipt_id':r['id'],'body_path':r['body_path'],'pointer':'/'+str(i),'sha256':r['sha256']}})
            if provider == 'pluto':
                pluto_pages.append(r)
    ids = []
    for item in records['pluto']:
        row = item['row']; identity = bbl(row.get('bbl'))
        ids.append(identity)
        if row.get('borough') != req['scope']['borough']:
            raise ValueError('Parcel outside requested borough')
        w,s,e,n = req['scope']['bbox']
        try:
            if not w <= float(row['longitude']) <= e or not s <= float(row['latitude']) <= n:
                raise ValueError('Parcel point outside scope')
        except (KeyError,TypeError):
            raise ValueError('Missing source point in point-defined inventory')
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate parcel BBL in inventory')
    for provider in ['zap_bbl','colp']:
        expected_queries = [{'$select':','.join(REGISTRY[provider]['fields']),
                             '$where':'bbl in ('+','.join(ids[i:i+CHUNK])+')',
                             '$order':'bbl,project_id' if provider=='zap_bbl' else 'bbl',
                             '$limit':'2001'} for i in range(0,len(ids),CHUNK)]
        actual_queries = [r['params'] for r in receipts if r['provider']==provider and r['params'] is not None]
        if actual_queries != expected_queries:
            raise ValueError('Context collection does not cover the declared inventory: '+provider)
        if any(bbl(x['row'].get('bbl')) not in set(ids) for x in records[provider]):
            raise ValueError('Context returned a lot outside inventory')
    project_ids = sorted({x['row']['project_id'] for x in records['zap_bbl'] if x['row'].get('project_id')})
    expected_queries = [{'$select':','.join(REGISTRY['zap_projects']['fields']),
                         '$where':'project_id in ('+','.join("'"+p.replace("'","''")+"'" for p in project_ids[i:i+CHUNK])+')',
                         '$order':'project_id','$limit':'2001'} for i in range(0,len(project_ids),CHUNK)]
    if [r['params'] for r in receipts if r['provider']=='zap_projects' and r['params'] is not None] != expected_queries:
        raise ValueError('Project lookup coverage differs from returned parcel links')
    returned_ids = [x['row'].get('project_id') for x in records['zap_projects']]
    if set(returned_ids) != set(project_ids) or len(returned_ids) != len(set(returned_ids)):
        complete_context['zap_projects'] = False
    counts = [r for r in receipts if r['provider']=='pluto' and r['params'] and r['params'].get('$select')=='count(*) as n']
    count_values = [int(load(folder/r['body_path'])[0]['n']) for r in counts if r['status']=='ok']
    expected_where = predicate(req['scope'])
    if any(r['params']['$where'] != expected_where for r in counts):
        raise ValueError('Inventory count scope mismatch')
    expected_cursor = None
    for r in pluto_pages:
        expected = expected_where + (f' AND bbl>{expected_cursor}' if expected_cursor else '')
        if r['params'] != {'$select':','.join(REGISTRY['pluto']['fields']), '$where':expected,'$order':'bbl','$limit':str(PAGE)}:
            raise ValueError('Inventory pagination query mismatch')
        rows = load(folder/r['body_path'])
        if rows:
            values = [int(bbl(x['bbl'])) for x in rows]
            if values != sorted(set(values)):
                raise ValueError('Unstable primary-key page order')
            expected_cursor = str(values[-1])
    primary = (len(count_values)==2 and count_values[0]==count_values[1]==len(ids)
               and len(metadata['pluto'])==2
               and metadata['pluto'][0].get('rowsUpdatedAt')==metadata['pluto'][1].get('rowsUpdatedAt')
               and all(r['status']=='ok' for r in receipts if r['provider']=='pluto'))
    for p in complete_context:
        complete_context[p] = complete_context[p] and bool(metadata[p])
    for p in complete_context:
        queried = [r for r in receipts if r['provider']==p and r['params'] is not None]
        if ids and not queried and p != 'zap_projects':
            complete_context[p] = False
    return {'scope':req['scope'],'scope_definition':'PLUTO recorded point lies in closed bbox; not every polygon intersecting it. Unlocated lots cannot be spatially assigned.',
            'query':expected_where,'count_before':count_values[0] if count_values else None,
            'count_after':count_values[-1] if len(count_values)>1 else None,'returned_lots':len(ids),
            'primary_complete':primary,'context_complete':complete_context,
            'consistency':'Count and metadata-update checks; not a transactional API snapshot.',
            'records':records}


def collect(req, out, ca_file=None, max_lots=10000):
    validate_request(req)
    out = fresh(out); save(out/'request.json',req)
    f = Fetcher(out,ca_file)
    where = predicate(req['scope'])
    meta = f.fetch('pluto'); _check_metadata('pluto',meta)
    count = f.fetch('pluto',{'$select':'count(*) as n','$where':where})
    total = int(count[0]['n']) if count else None
    identities = []
    if total is not None and total <= max_lots and meta:
        cursor = None
        while len(identities) < total:
            page = f.fetch('pluto',{'$select':','.join(REGISTRY['pluto']['fields']), '$where':where+(f' AND bbl>{cursor}' if cursor else ''),'$order':'bbl','$limit':str(PAGE)})
            if not page:
                break
            identities += [bbl(row['bbl']) for row in page]
            cursor = identities[-1]
    else:
        save(out/'collection-note.json',{'reason':'Missing primary source or inventory exceeds configured lot cap','max_lots':max_lots})
    f.fetch('pluto',{'$select':'count(*) as n','$where':where})
    f.fetch('pluto')
    for p in ['zap_bbl','zap_projects','colp']:
        _check_metadata(p,f.fetch(p))
    projects = set()
    for start in range(0,len(identities),CHUNK):
        subset = identities[start:start+CHUNK]
        clause = 'bbl in ('+','.join(subset)+')'
        links = f.fetch('zap_bbl',{'$select':','.join(REGISTRY['zap_bbl']['fields']),'$where':clause,'$order':'bbl,project_id','$limit':'2001'})
        for row in links or []:
            if row.get('project_id'):
                projects.add(row['project_id'])
        f.fetch('colp',{'$select':','.join(REGISTRY['colp']['fields']),'$where':clause,'$order':'bbl','$limit':'2001'})
    projects = sorted(projects)
    for start in range(0,len(projects),CHUNK):
        quoted = ["'"+p.replace("'","''")+"'" for p in projects[start:start+CHUNK]]
        f.fetch('zap_projects',{'$select':','.join(REGISTRY['zap_projects']['fields']),'$where':'project_id in ('+','.join(quoted)+')','$order':'project_id','$limit':'2001'})
    return finalize(out)


def finalize(folder):
    """Recover a finished raw collection that has no completed manifest yet."""
    folder=destination(folder)
    if (folder/'manifest.json').exists():
        raise ValueError('Completed inventories are read-only')
    save(folder/'inventory.json',derive(folder))
    seal(folder,'inventory')
    return verify(folder)


def verify(folder):
    folder = Path(folder)
    verify_files(folder,'inventory')
    if load(folder/'inventory.json') != derive(folder):
        raise ValueError('Inventory differs from source replay')
    inv = load(folder/'inventory.json')
    return {'status':'passed','primary_complete':inv['primary_complete'],'lots':inv['returned_lots'],'context_complete':inv['context_complete']}
