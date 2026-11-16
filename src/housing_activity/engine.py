"""Development-activity check: is anything already being built or cleared on these lots? MIT.

Collects recent permits and filings for a set of NYC tax lots from four public
datasets (sources.json), keeps every response with a SHA-256 receipt, and classifies
each lot deterministically:

  active_development  a strong signal inside the window: full demolition, foundation,
                      earth work or excavation support permit; a new-building filing
                      or permit; an HPD new-construction project start
  site_preparation    only a construction-fence permit inside the window
  none_found          nothing qualifying returned (not proof that nothing is planned)
  not_checked         a source failed for this lot; the run is then 'partial'

`verify` recomputes the classification from the retained responses.
"""
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import hashlib
import json
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

from housing_common.local_outputs import ROOT, destination

VERSION = '1.0.0'
HERE = Path(__file__).resolve().parent
SOURCES = json.loads((HERE / 'sources.json').read_text())
BASE = 'https://data.cityofnewyork.us/resource/%s.json'
BATCH = 60
LIMIT = 5000
BOROUGH_NAMES = {'1': 'MANHATTAN', '2': 'BRONX', '3': 'BROOKLYN', '4': 'QUEENS', '5': 'STATEN ISLAND'}
STATUS_ORDER = ['active_development', 'site_preparation', 'none_found', 'not_checked']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def dumps(value):
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + '\n'


def save(path, value):
    Path(path).write_text(dumps(value))


def implementation():
    files = sorted(HERE.glob('*.py')) + sorted(HERE.glob('*.json'))
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in files}


def inventory(folder):
    folder = Path(folder)
    return {str(p.relative_to(folder)): digest(p.read_bytes()) for p in sorted(folder.rglob('*'))
            if p.is_file() and p != folder / 'manifest.json' and '__pycache__' not in p.parts}


# ---------------------------------------------------------------- queries

def queries(bbls, since):
    """Deterministic list of (source, params) covering every lot, plus per-borough coverage counts."""
    out = []
    for source in SOURCES:
        for boro in sorted({BOROUGH_NAMES[b[0]] for b in bbls}):
            out.append((source, {'$select': 'count(*) AS rows', '$where': "upper(borough)='%s'" % boro, '$coverage': boro}))
    for source, cfg in SOURCES.items():
        fields = ','.join(cfg['fields'])
        stamp = since.isoformat() + 'T00:00:00'
        if cfg['key'] in ('bbl_text', 'bbl_number'):
            for i in range(0, len(bbls), BATCH):
                chunk = bbls[i:i + BATCH]
                values = ','.join(("'%s'" % b) if cfg['key'] == 'bbl_text' else b for b in chunk)
                out.append((source, {'$select': fields, '$where': "bbl in (%s) and %s >= '%s'" % (values, cfg['date_field'], stamp),
                                     '$order': 'bbl,%s' % cfg['date_field'], '$limit': str(LIMIT)}))
        else:
            blocks = {}
            for b in bbls:
                blocks.setdefault(BOROUGH_NAMES[b[0]], set()).add(b[1:6])
            for borough, items in sorted(blocks.items()):
                items = sorted(items)
                for i in range(0, len(items), BATCH):
                    values = ','.join("'%s'" % x for x in items[i:i + BATCH])
                    out.append((source, {'$select': fields,
                                         '$where': "borough='%s' and block in (%s) and %s >= '%s'" % (borough, values, cfg['date_field'], since.isoformat()),
                                         '$order': 'block,lot,%s' % cfg['date_field'], '$limit': str(LIMIT)}))
    return out


def _context():
    return ssl.create_default_context()


def fetch(url):
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'OpenHousingToolkit-Activity/1.0', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, context=_context(), timeout=60) as response:
                return response.status, response.read(16 * 1024 * 1024 + 1), None
        except urllib.error.HTTPError as exc:
            last = (exc.code, exc.read(1024 * 64), 'HTTP %s' % exc.code)
            if exc.code not in (429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, OSError) as exc:
            last = (None, b'', str(getattr(exc, 'reason', exc)))
        time.sleep(1 + attempt)
    return last


# ---------------------------------------------------------------- collect / build

def normalize_bbls(values):
    out = []
    for v in values:
        b = str(v).split('.')[0].strip()
        if not re.fullmatch(r'[1-5][0-9]{9}', b):
            raise ValueError('Expected 10-digit NYC BBLs, got %r' % v)
        out.append(b)
    return sorted(set(out))


def lots_from_discovery(folder, ranked_only=True):
    """Candidate BBLs (and labels) from a verified area search."""
    from housing_site_discovery.engine import verify
    folder = Path(folder)
    verify(folder)
    if ranked_only:
        from housing_feasibility.candidates import rank
        _, rows = rank(folder)
        return [{'bbl': r['bbl'], 'address': r['address']} for r in rows]
    import csv
    with (folder / 'all-lots.csv').open(newline='') as handle:
        return [{'bbl': r['bbl'], 'address': r['address']} for r in csv.DictReader(handle)
                if r['current_use_category'] == 'recorded_nonhousing']


def collect(out, bbls=None, discovery=None, since_years=3, as_of=None, all_nonhousing=False, fetcher=fetch):
    out = destination(out) if Path(out).resolve().is_relative_to(ROOT) else Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty')
    lots = []
    if discovery:
        lots += lots_from_discovery(discovery, ranked_only=not all_nonhousing)
    lots += [{'bbl': b, 'address': None} for b in normalize_bbls(bbls or [])]
    seen, unique = set(), []
    for lot in lots:
        if lot['bbl'] not in seen:
            seen.add(lot['bbl'])
            unique.append(lot)
    if not unique:
        raise ValueError('No lots to check: give --discovery or --bbl')
    as_of = date.fromisoformat(as_of) if as_of else datetime.now(timezone.utc).date()
    since = as_of - timedelta(days=round(365.25 * since_years))
    request = {'version': '1.0', 'as_of': as_of.isoformat(), 'since': since.isoformat(), 'since_years': since_years,
               'lots': unique, 'discovery': {'name': Path(discovery).name,
                                             'manifest_sha256': digest((Path(discovery) / 'manifest.json').read_bytes())} if discovery else None}
    out.mkdir(parents=True, exist_ok=True)
    (out / 'sources').mkdir()
    save(out / 'request.json', request)
    receipts = []
    for n, (source, params) in enumerate(queries([l['bbl'] for l in unique], since)):
        params = dict(params)
        coverage = params.pop('$coverage', None)
        url = BASE % SOURCES[source]['dataset'] + '?' + urllib.parse.urlencode(params)
        status, body, error = fetcher(url)
        name = 'sources/%03d-%s.json' % (n, source)
        (out / name).write_bytes(body or b'')
        rows = None
        if status == 200 and not error:
            try:
                parsed = json.loads(body)
                rows = len(parsed) if isinstance(parsed, list) else None
                if rows is None:
                    error = 'Unexpected response shape'
            except ValueError:
                error = 'Response is not JSON'
        receipts.append({'id': n, 'source': source, 'coverage_borough': coverage, 'dataset': SOURCES[source]['dataset'], 'url': url, 'params': params,
                         'body_path': name, 'sha256': digest(body or b''), 'bytes': len(body or b''), 'http_status': status,
                         'status': 'ok' if rows is not None else 'failed', 'error': error, 'rows': rows,
                         'possibly_truncated': rows == LIMIT, 'retrieved_at': datetime.now(timezone.utc).isoformat()})
    save(out / 'receipts.json', receipts)
    write_outputs(out)
    save(out / 'manifest.json', {'version': VERSION, 'module': 'development-activity', 'implementation': implementation(),
                                 'files': inventory(out),
                                 'validation_scope': 'Retained responses bound by SHA-256; classification recomputed from them. '
                                                     'Not a site visit, title search or zoning determination.'})
    return verify(out)


def _lot_key(source, row):
    if SOURCES[source]['key'] == 'borough_block':
        boro = {v: k for k, v in BOROUGH_NAMES.items()}.get(str(row.get('borough', '')).upper())
        try:
            return '%s%05d%04d' % (boro, int(row['block']), int(row['lot'])) if boro else None
        except (KeyError, ValueError):
            return None
    return str(row.get('bbl', '')).split('.')[0] or None


def _signal(source, row):
    cfg = SOURCES[source]
    for field, values in cfg['strong'].items():
        if row.get(field) in values:
            return 'strong'
    pattern = cfg.get('strong_description')
    if pattern and row.get('work_type') not in cfg.get('ignore_description_for', []) and \
            re.search(pattern, (row.get('job_description') or '').upper()):
        return 'strong'
    for field, values in cfg['preparation'].items():
        if row.get(field) in values:
            return 'preparation'
    return None


def _describe(source, row):
    if source == 'dob_now_permits':
        cfg = SOURCES[source]
        nb = row.get('work_type') not in cfg['strong']['work_type'] and row.get('work_type') not in cfg.get('ignore_description_for', []) \
            and re.search(cfg['strong_description'], (row.get('job_description') or '').upper())
        return '%s permit%s (%s)' % (row.get('work_type'), ' for a new building' if nb else '', row.get('permit_status'))
    if source == 'dob_now_filings':
        units = row.get('proposed_dwelling_units')
        return '%s filing (%s)%s' % (row.get('job_type'), row.get('filing_status'), ', %s proposed homes' % units if units else '')
    if source == 'dob_bis_permits':
        return 'Legacy %s permit %s (%s)' % (row.get('job_type'), row.get('permit_type'), row.get('permit_status'))
    return 'HPD %s project "%s" (%s units)' % (row.get('reporting_construction_type'), row.get('project_name'), row.get('total_units'))


def classify(folder):
    folder = Path(folder)
    request, receipts = load(folder / 'request.json'), load(folder / 'receipts.json')
    since = request['since']
    lots = {l['bbl']: {'bbl': l['bbl'], 'address': l['address'], 'signals': []} for l in request['lots']}
    failed_sources = sorted({r['source'] for r in receipts if r['status'] != 'ok'})
    coverage = {}
    for r in receipts:
        if r.get('coverage_borough') and r['status'] == 'ok':
            body = (folder / r['body_path']).read_bytes()
            if digest(body) != r['sha256']:
                raise ValueError('Retained response changed: ' + r['body_path'])
            rows = json.loads(body)
            coverage.setdefault(r['source'], {})[r['coverage_borough']] = int(rows[0].get('rows', 0)) if rows else 0
    gaps = sorted('%s (%s)' % (SOURCES[src]['title'], boro) for src, boros in coverage.items() for boro, n in boros.items() if n == 0)
    for r in receipts:
        if r['status'] != 'ok' or r.get('coverage_borough'):
            continue
        body = (folder / r['body_path']).read_bytes()
        if digest(body) != r['sha256']:
            raise ValueError('Retained response changed: ' + r['body_path'])
        for i, row in enumerate(json.loads(body)):
            key = _lot_key(r['source'], row)
            kind = _signal(r['source'], row)
            day = str(row.get(SOURCES[r['source']]['date_field']) or '')[:10]
            if key not in lots or not kind or day < since:
                continue
            lots[key]['signals'].append({'kind': kind, 'source': r['source'], 'date': day, 'what': _describe(r['source'], row),
                                         'description': (row.get('job_description') or '')[:300] or None,
                                         'reference': row.get('job_filing_number') or row.get('job__') or row.get('project_id'),
                                         'locator': {'receipt': r['id'], 'row': i}})
    out = []
    for lot in lots.values():
        lot['signals'].sort(key=lambda s: (s['date'], s['source'], s['what']), reverse=True)
        kinds = {s['kind'] for s in lot['signals']}
        if 'strong' in kinds:
            status = 'active_development'
        elif 'preparation' in kinds:
            status = 'site_preparation'
        elif failed_sources:
            status = 'not_checked'
        else:
            status = 'none_found'
        rank_kind = {'strong': 0, 'preparation': 1}
        latest = min(lot['signals'], key=lambda x: (rank_kind[x['kind']], [-ord(c) for c in x['date']])) if lot['signals'] else None
        units = [s['what'] for s in lot['signals'] if 'proposed homes' in s['what']]
        lot.update({'status': status, 'latest': latest and '%s, %s' % (latest['what'], latest['date']),
                    'proposed_homes_note': units[0] if units else None})
        out.append(lot)
    out.sort(key=lambda l: (STATUS_ORDER.index(l['status']), l['bbl']))
    counts = {s: sum(1 for l in out if l['status'] == s) for s in STATUS_ORDER}
    return {'version': VERSION, 'as_of': request['as_of'], 'since': since, 'lots_checked': len(out),
            'run_status': 'partial' if failed_sources else 'complete', 'failed_sources': failed_sources,
            'source_coverage': coverage, 'coverage_gaps': gaps,
            'truncated_queries': [r['id'] for r in receipts if r.get('possibly_truncated')],
            'counts': counts, 'lots': out,
            'method': ('Recent permits and filings since %s from DOB NOW approved permits, DOB NOW job filings, legacy DOB permits '
                       'and HPD affordable production. Strong signals: full demolition, foundation, earth work or excavation-support '
                       'permits; permits whose description names a new building; new-building filings; HPD new-construction starts. '
                       'Site preparation: construction fence only.' % since),
            'limits': ['A signal shows recorded activity, not what will be built or whether it will finish.',
                       'none_found is not proof that nothing is planned: filings can lag, use another lot number, or sit in other systems.',
                       'Sidewalk sheds and scaffolds are ignored because facade work uses them too.']}


def packet(result):
    lines = ['# Development activity check', '',
             'As of %s, looking back to %s. %s lots: %s.' % (result['as_of'], result['since'], result['lots_checked'],
                                                            ', '.join('%s %s' % (v, k.replace('_', ' ')) for k, v in result['counts'].items() if v)),
             '', result['method'], '']
    if result['coverage_gaps']:
        lines += ['**Coverage gap:** these published sources hold no rows for the borough checked, so they could not '
                  'contribute: %s.' % '; '.join(result['coverage_gaps']), '']
    if result['run_status'] != 'complete':
        lines += ['**Partial run:** failed sources %s; affected lots are marked not checked.' % ', '.join(result['failed_sources']), '']
    lines += ['| Lot | Address | Status | Latest signal |', '|---|---|---|---|']
    for lot in result['lots']:
        lines.append('| %s | %s | %s | %s |' % (lot['bbl'], lot['address'] or '', lot['status'].replace('_', ' '), lot['latest'] or ''))
    lines += ['', '## Limits', ''] + ['- ' + x for x in result['limits']] + ['']
    return '\n'.join(lines)


def write_outputs(folder):
    result = classify(folder)
    save(Path(folder) / 'activity.json', result)
    (Path(folder) / 'packet.md').write_text(packet(result))
    return result


def verify(folder):
    folder = Path(folder)
    manifest = load(folder / 'manifest.json')
    if manifest.get('module') != 'development-activity' or manifest.get('version') != VERSION:
        raise ValueError('Not a development-activity package')
    if manifest['implementation'] != implementation():
        raise ValueError('Built by a different version of housing_activity; collect again into a new folder')
    if manifest['files'] != inventory(folder):
        raise ValueError('Activity package files were added, removed or changed')
    result = classify(folder)
    if load(folder / 'activity.json') != result or (folder / 'packet.md').read_text() != packet(result):
        raise ValueError('Activity results differ from the retained responses')
    return {'status': 'passed', 'run_status': result['run_status'], 'lots_checked': result['lots_checked'],
            'coverage_gaps': result['coverage_gaps'],
            'counts': result['counts'], 'active': [l['bbl'] for l in result['lots'] if l['status'] == 'active_development'],
            'packet': str(folder / 'packet.md')}
