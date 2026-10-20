#!/usr/bin/env python3
"""Parcel evidence module: bounded public ownership/transaction evidence.

For one BBL, collects ACRIS real-property records (deeds, mortgages and other
recorded instruments), DOF sales rows and the PLUTO parcel row into a separate
run directory, then assembles a structured evidence package with exact claim
locators, conflicts and unknowns.

Collection budget: 150 requests, 50 MiB, 90 minutes (configurable).
This module does not establish beneficial ownership or complete title research.
Stdlib only. MIT.
"""
import argparse, datetime, hashlib, json, pathlib, re, time, urllib.parse

import collect

ROOT = pathlib.Path(__file__).resolve().parent
BUDGET_DEFAULTS = {'max_requests': 150, 'max_bytes': 50 * 1024 * 1024, 'max_seconds': 90 * 60}
ACRIS_LEGALS = '8h5j-fqxa'
ACRIS_MASTER = 'bnx9-e6tj'
ACRIS_PARTIES = '636b-3b5g'
DOF_SALES = 'w2pb-icbu'
PLUTO = '64uk-42ks'
TERMS = 'https://opendata.cityofnewyork.us/overview/#termsofuse'
LIMITS_ACRIS = ('ACRIS real property records for exact borough/block/lot or document_id. '
                'NYC boroughs excluding Staten Island; records from 1966 onward; good_through dates vary. '
                'Index rows are not native document images and not a current title opinion.')
LIMITS_SALES = ('DOF sales rows for exact BBL from the NYC Citywide Annualized Calendar Sales Update. '
                'Annualized update feed; absence of a row is not proof of no sale.')
LIMITS_PLUTO = ('PLUTO row for exact BBL. Tax-roll attributes; owner label is not legal ownership. '
                'Parcel fields may lag underlying changes.')
NON_CLAIMS = [
    'This package is not a title opinion. It does not establish beneficial ownership, current site control, or complete title research.',
    'ACRIS coverage: NYC boroughs excluding Staten Island; records from 1966 onward; good_through dates vary; native document images not retrieved.',
    'DOF sales dataset is an annualized update feed; absence of a row is not proof of no sale.',
    'PLUTO owner label is a tax-roll label, not legal ownership.',
    'doc_type classification is a keyword-based triage aid, not legal interpretation of the instrument.',
]


class BudgetExceeded(Exception):
    def __init__(self, which):
        super().__init__('collection budget exceeded: ' + which)
        self.which = which


class Budget:
    """Hard limits on requests, bytes and wall-clock time for one collection run."""

    def __init__(self, max_requests=BUDGET_DEFAULTS['max_requests'],
                 max_bytes=BUDGET_DEFAULTS['max_bytes'],
                 max_seconds=BUDGET_DEFAULTS['max_seconds'], clock=time.monotonic):
        self.max_requests, self.max_bytes, self.max_seconds = max_requests, max_bytes, max_seconds
        self.clock = clock
        self.requests = 0
        self.bytes = 0
        self.started_at = None

    def start(self):
        self.started_at = self.clock()

    def elapsed(self):
        return 0.0 if self.started_at is None else self.clock() - self.started_at

    def charge_request(self):
        self.requests += 1
        self.check_time()
        if self.requests > self.max_requests:
            raise BudgetExceeded('requests')

    def charge_bytes(self, n):
        self.bytes += int(n)
        self.check_time()
        if self.bytes > self.max_bytes:
            raise BudgetExceeded('bytes')

    def check_time(self):
        if self.elapsed() > self.max_seconds:
            raise BudgetExceeded('time')

    def exhausted(self):
        if self.requests >= self.max_requests:
            return 'requests'
        if self.bytes >= self.max_bytes:
            return 'bytes'
        if self.started_at is not None and self.elapsed() >= self.max_seconds:
            return 'time'
        return None

    def snapshot(self):
        return {'max_requests': self.max_requests, 'max_bytes': self.max_bytes,
                'max_seconds': self.max_seconds, 'requests': self.requests,
                'bytes': self.bytes, 'elapsed_seconds': round(self.elapsed(), 3),
                'exhausted': self.exhausted()}


def parse_bbl(bbl):
    """10-digit BBL -> (borough, block, lot) as zero-padded strings. Raises ValueError."""
    if not re.fullmatch(r'[1-5][0-9]{9}', bbl or ''):
        raise ValueError('BBL must be 10 digits with borough 1-5: %r' % (bbl,))
    return bbl[0], bbl[1:6], bbl[6:]


def bbl_from_parts(borough, block, lot):
    """Canonical 10-digit BBL from ACRIS-style parts (which may lack zero padding)."""
    return '%s%s%s' % (str(borough or ''), str(block or '').zfill(5), str(lot or '').zfill(4))


def soql_url(dataset, where, limit=10000, order=None):
    params = {'$where': where, '$limit': str(limit)}
    if order:
        params['$order'] = order
    return 'https://data.cityofnewyork.us/resource/%s.json?' % dataset + urllib.parse.urlencode(params)


def plan_phase1(bbl):
    borough, block, lot = parse_bbl(bbl)
    block_variants = sorted({block, block.lstrip('0') or '0'})
    lot_variants = sorted({lot, lot.lstrip('0') or '0'})
    return [
        {'source_id': 'pluto_%s' % bbl, 'url': soql_url(PLUTO, "bbl='%s'" % bbl, limit=10),
         'publisher': 'NYC Department of City Planning', 'limits': LIMITS_PLUTO, 'terms': TERMS},
        {'source_id': 'acris_legal_%s' % bbl,
         'url': soql_url(ACRIS_LEGALS, "borough='%s' AND block in (%s) AND lot in (%s)"
                         % (borough, ','.join("'%s'" % v for v in block_variants),
                            ','.join("'%s'" % v for v in lot_variants)),
                         order='document_id'),
         'publisher': 'NYC Department of Finance (ACRIS)', 'limits': LIMITS_ACRIS, 'terms': TERMS},
        {'source_id': 'dof_sales_%s' % bbl, 'url': soql_url(DOF_SALES, "bbl='%s'" % bbl, order='sale_date'),
         'publisher': 'NYC Department of Finance', 'limits': LIMITS_SALES, 'terms': TERMS},
    ]


def plan_phase2(bbl, document_ids):
    if not document_ids:
        return []
    ids = ','.join("'%s'" % d for d in document_ids)
    return [
        {'source_id': 'acris_master_%s' % bbl, 'url': soql_url(ACRIS_MASTER, 'document_id in (%s)' % ids, order='document_id'),
         'publisher': 'NYC Department of Finance (ACRIS)', 'limits': LIMITS_ACRIS, 'terms': TERMS},
        {'source_id': 'acris_parties_%s' % bbl, 'url': soql_url(ACRIS_PARTIES, 'document_id in (%s)' % ids, order='document_id'),
         'publisher': 'NYC Department of Finance (ACRIS)', 'limits': LIMITS_ACRIS, 'terms': TERMS},
    ]


def real_fetch(source, budget, root):
    budget.charge_request()
    record = collect.fetch(source['source_id'], source['url'], source['publisher'],
                           source['limits'], source.get('terms'), root=root)
    if record.get('status') == 'ok':
        budget.charge_bytes(record.get('bytes', 0))
    budget.check_time()
    return record


def run_collection(bbl, run_dir, budget=None, fetcher=None):
    """Fetch all planned sources for one BBL into run_dir; write run.json.

    Returns (run_record, budget). Stops cleanly on BudgetExceeded or fetch
    failure; whatever was fetched is still packaged by build_package.
    """
    run_dir = pathlib.Path(run_dir)
    (run_dir / 'cache').mkdir(parents=True, exist_ok=True)
    budget = budget or Budget()
    fetcher = fetcher or real_fetch
    budget.start()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    requests, status, errors = [], 'complete', []
    document_ids = []
    for phase in (plan_phase1(bbl), None):
        sources = phase if phase is not None else plan_phase2(bbl, document_ids)
        for source in sources:
            try:
                record = fetcher(source, budget, run_dir)
            except BudgetExceeded as exc:
                status = 'budget_exhausted'
                errors.append(str(exc))
                break
            except Exception as exc:
                errors.append('%s: %s: %s' % (source['source_id'], type(exc).__name__, exc))
                continue
            requests.append({'source_id': record.get('id'), 'status': record.get('status'),
                             'bytes': record.get('bytes'), 'error': record.get('error')})
            if record.get('status') == 'ok' and source['source_id'].startswith('acris_legal_'):
                body = json.loads((run_dir / record['cache_path']).read_text())
                document_ids = sorted({row.get('document_id') for row in body if row.get('document_id')})
        if status == 'budget_exhausted':
            break
    run = {'run_id': run_dir.name, 'bbl': bbl, 'started_at': started,
           'ended_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'status': status, 'budget': budget.snapshot(), 'requests': requests, 'errors': errors}
    (run_dir / 'run.json').write_text(json.dumps(run, indent=2, sort_keys=True) + '\n')
    return run, budget


def classify_doc_type(code):
    """Keyword-based triage of ACRIS doc_type codes. Not legal interpretation."""
    if not code:
        return 'unclassified'
    c = str(code).strip().upper()
    if c == 'DEED' or 'DEED' in c:
        return 'deed'
    if c in ('MTGE', 'MTG') or c.startswith('MTG') or 'MORTGAGE' in c:
        return 'mortgage'
    if c in ('SAT', 'REL', 'RLS'):
        return 'release'
    return 'other'


def _load_rows(run_dir, source_id):
    record_path = run_dir / 'cache' / (source_id + '.source.json')
    if not record_path.exists():
        return None, None
    record = json.loads(record_path.read_text())
    if record.get('status') != 'ok':
        return record, None
    body = (run_dir / record['cache_path']).read_bytes()
    return record, json.loads(body)


def _locator(source_id, row, fields):
    return {'source_id': source_id, 'row': row, 'fields': sorted(fields)}


def _norm_name(name):
    return re.sub(r'\s+', ' ', (name or '').upper()).strip()


def build_package(run_dir):
    """Assemble the evidence package from a run directory. Pure and deterministic."""
    run_dir = pathlib.Path(run_dir)
    run = json.loads((run_dir / 'run.json').read_text())
    bbl = run['bbl']
    borough, block, lot = parse_bbl(bbl)
    sources, records, unknowns, conflicts = [], [], [], []

    def add_unknown(kind, description):
        n = len([u for u in unknowns if u['kind'] == kind])
        unknowns.append({'id': 'unknown.%s.%d' % (kind, n), 'kind': kind, 'description': description})

    for source_id in ('pluto_%s' % bbl, 'acris_legal_%s' % bbl, 'acris_master_%s' % bbl,
                      'acris_parties_%s' % bbl, 'dof_sales_%s' % bbl):
        record, rows = _load_rows(run_dir, source_id)
        if record is None:
            add_unknown('source_missing', 'No source record for %s; it was not fetched in this run.' % source_id)
            continue
        sources.append({k: record.get(k) for k in
                        ('id', 'url', 'publisher', 'retrieved_at', 'status', 'http_status',
                         'content_type', 'last_modified', 'cache_path', 'bytes', 'sha256',
                         'coverage_limits', 'terms_url', 'error')})
        if rows is None:
            add_unknown('source_failed', 'Source %s did not return ok status: %s'
                        % (source_id, record.get('error') or record.get('status')))

    pluto_record, pluto_rows = _load_rows(run_dir, 'pluto_%s' % bbl)
    pluto_row = pluto_rows[0] if pluto_rows else None
    if pluto_row is None:
        add_unknown('pluto_missing', 'No PLUTO row for BBL %s in this run.' % bbl)
    else:
        records.append({'record_id': 'pluto:%s' % bbl, 'kind': 'parcel_identity',
                        'fields': {k: pluto_row.get(k) for k in
                                   ('bbl', 'bin', 'address', 'owner1', 'owner2', 'lotarea', 'zoningdist')},
                        'locators': [_locator('pluto_%s' % bbl, 0, ['bbl', 'owner1', 'lotarea'])]})

    legal_record, legal_rows = _load_rows(run_dir, 'acris_legal_%s' % bbl)
    legal_rows = legal_rows or []
    if not legal_rows:
        add_unknown('acris_empty', 'No ACRIS legal rows for BBL %s in the dataset window '
                                   '(1966 onward, Staten Island excluded); absence is not proof of no records.' % bbl)
    master_record, master_rows = _load_rows(run_dir, 'acris_master_%s' % bbl)
    master_by_id = {row.get('document_id'): (i, row) for i, row in enumerate(master_rows or [])}
    parties_record, parties_rows = _load_rows(run_dir, 'acris_parties_%s' % bbl)
    parties_by_id = {}
    for i, row in enumerate(parties_rows or []):
        parties_by_id.setdefault(row.get('document_id'), []).append((i, row))

    other_parcels = {}
    latest_deed = None
    latest_doc = None
    parties_role_unrecognized = False
    for i, lrow in enumerate(legal_rows):
        doc_id = lrow.get('document_id')
        m_idx, mrow = master_by_id.get(doc_id, (None, None))
        p_rows = parties_by_id.get(doc_id, [])
        family = classify_doc_type(mrow.get('doc_type')) if mrow else 'unclassified'
        if mrow is None:
            add_unknown('master_missing', 'ACRIS legal row for document_id %s has no master row in this run.' % doc_id)
        elif family == 'unclassified':
            add_unknown('doc_type_unclassified', 'Unrecognized ACRIS doc_type code %r for document_id %s.'
                        % (mrow.get('doc_type'), doc_id))
        if not p_rows:
            add_unknown('parties_missing', 'No ACRIS parties rows for document_id %s in this run.' % doc_id)
        elif not any(any('role' in k.lower() for k in row.keys()) for _, row in p_rows):
            parties_role_unrecognized = True
        dates = {}
        if mrow:
            dates = {'document_date': mrow.get('document_date'), 'recorded_datetime': mrow.get('recorded_datetime')}
        dates['good_through_date_legal'] = lrow.get('good_through_date')
        if mrow and mrow.get('good_through_date') and lrow.get('good_through_date') \
                and mrow.get('good_through_date') != lrow.get('good_through_date'):
            conflicts.append({'id': 'conflict.good_through.%s' % doc_id, 'kind': 'good_through_date_mismatch',
                              'description': 'good_through_date differs between ACRIS legals and master for document_id %s.' % doc_id,
                              'evidence': [_locator('acris_legal_%s' % bbl, i, ['good_through_date']),
                                           _locator('acris_master_%s' % bbl, m_idx, ['good_through_date'])]})
        parcels = [{'bbl': bbl_from_parts(lrow.get('borough'), lrow.get('block'), lrow.get('lot')),
                    'street': ' '.join(x for x in [lrow.get('street_number'), lrow.get('street_name')] if x)}]
        for p in parcels:
            if p['bbl'] != bbl:
                other_parcels.setdefault(p['bbl'], {'bbl': p['bbl'], 'street': p['street'], 'referenced_by': []})
                other_parcels[p['bbl']]['referenced_by'].append('acris:%s' % doc_id)
        locators = [_locator('acris_legal_%s' % bbl, i, ['document_id', 'borough', 'block', 'lot', 'street_number', 'street_name'])]
        raw = {'legal': lrow}
        if mrow is not None:
            locators.append(_locator('acris_master_%s' % bbl, m_idx,
                                     ['document_id', 'doc_type', 'document_date', 'document_amt', 'recorded_datetime']))
            raw['master'] = mrow
        if p_rows:
            raw['parties'] = [row for _, row in p_rows]
            locators.extend(_locator('acris_parties_%s' % bbl, i2, list(row.keys())) for i2, row in p_rows)
        record = {'record_id': 'acris:%s' % doc_id, 'kind': 'recorded_instrument',
                  'instrument_family': family, 'doc_type_raw': mrow.get('doc_type') if mrow else None,
                  'dates': dates, 'amount': mrow.get('document_amt') if mrow else None,
                  'parcels': parcels, 'locators': locators, 'raw': raw}
        records.append(record)
        if mrow and mrow.get('document_date'):
            if latest_doc is None or mrow['document_date'] > latest_doc:
                latest_doc = mrow['document_date']
        if family == 'deed' and mrow and mrow.get('document_date'):
            if latest_deed is None or mrow['document_date'] > latest_deed['document_date']:
                latest_deed = mrow
                latest_deed['_doc_id'] = doc_id
                latest_deed['_grantor_grantee'] = _party_names(p_rows)

    sales_record, sales_rows = _load_rows(run_dir, 'dof_sales_%s' % bbl)
    for i, srow in enumerate(sales_rows or []):
        records.append({'record_id': 'dof_sales:%s:%d' % (bbl, i), 'kind': 'sale',
                        'fields': {k: srow.get(k) for k in ('bbl', 'bin', 'address', 'sale_date', 'sale_price')},
                        'locators': [_locator('dof_sales_%s' % bbl, i, ['bbl', 'sale_date', 'sale_price'])]})
    if sales_rows is not None and not sales_rows:
        add_unknown('sales_empty', 'No DOF sales rows for BBL %s in the dataset window; absence is not proof of no sale.' % bbl)

    if pluto_row and latest_deed:
        pluto_owner = _norm_name(pluto_row.get('owner1'))
        grantee = _norm_name(latest_deed.get('_grantor_grantee'))
        if pluto_owner and grantee and pluto_owner != grantee:
            conflicts.append({'id': 'conflict.owner_label', 'kind': 'owner_label_mismatch',
                              'description': 'PLUTO owner label %r differs from grantee of latest deed (%s) %r. '
                                             'Tax-roll label and deed party are not reconciled; neither establishes current ownership.'
                                             % (pluto_row.get('owner1'), latest_deed.get('_doc_id'), latest_deed.get('_grantor_grantee')),
                              'evidence': [_locator('pluto_%s' % bbl, 0, ['owner1']),
                                           _locator('acris_master_%s' % bbl,
                                                    master_by_id.get(latest_deed['_doc_id'], (None, None))[0],
                                                    ['document_date'])]})
    if parties_role_unrecognized:
        unknowns.append({'id': 'unknown.party_role', 'kind': 'party_role',
                         'description': 'ACRIS parties rows in this run carry party_type codes (e.g. 1, 2) but no '
                                        'verified role field; grantor/grantee roles are not identified. Party names are '
                                        'preserved in record raw data with locators.'})
    if latest_doc:
        unknowns.append({'id': 'unknown.coverage', 'kind': 'coverage',
                         'description': 'Latest ACRIS document date in this run is %s; no evidence of instruments '
                                        'recorded after that date, and good_through dates vary by record.'
                                        % latest_doc})

    records.sort(key=lambda r: r['record_id'])
    package = {'package_version': '0.1', 'parcel': {'bbl': bbl, 'borough': borough, 'block': block, 'lot': lot},
               'run_id': run['run_id'], 'run_status': run['status'], 'budget': run['budget'],
               'sources': sources, 'records': records,
               'other_parcels': [other_parcels[k] for k in sorted(other_parcels)],
               'conflicts': conflicts, 'unknowns': unknowns,
               'limitations': list(NON_CLAIMS), 'non_claims': list(NON_CLAIMS)}
    return package


def _party_names(p_rows):
    """Best-effort grantee name from parties rows; role matched by keyword."""
    for _, row in p_rows:
        for key, value in row.items():
            if 'role' in key.lower() and isinstance(value, str) and 'GRANTEE' in value.upper():
                for name_key, name_value in row.items():
                    if 'name' in name_key.lower() and name_value:
                        return name_value
    return None


def write_package(run_dir):
    run_dir = pathlib.Path(run_dir)
    package = build_package(run_dir)
    (run_dir / 'package.json').write_text(json.dumps(package, indent=2, sort_keys=True) + '\n')
    return package


def main(argv=None):
    parser = argparse.ArgumentParser(description='Collect bounded parcel ownership/transaction evidence.')
    parser.add_argument('--bbl', help='10-digit BBL to collect')
    parser.add_argument('--replay', help='Run directory to rebuild package.json from (no requests)')
    parser.add_argument('--out', default=str(ROOT / 'runs'), help='Runs root directory')
    parser.add_argument('--run-id', help='Run directory name (default: timestamped)')
    parser.add_argument('--budget-requests', type=int, default=BUDGET_DEFAULTS['max_requests'])
    parser.add_argument('--budget-bytes', type=int, default=BUDGET_DEFAULTS['max_bytes'])
    parser.add_argument('--budget-seconds', type=int, default=BUDGET_DEFAULTS['max_seconds'])
    args = parser.parse_args(argv)
    if args.replay:
        package = write_package(args.replay)
        print(json.dumps({'run_id': package['run_id'], 'records': len(package['records']),
                          'conflicts': len(package['conflicts']), 'unknowns': len(package['unknowns'])}))
        return 0
    if not args.bbl:
        parser.error('one of --bbl or --replay is required')
    parse_bbl(args.bbl)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    run_id = args.run_id or ('run-%s-%s' % (stamp, args.bbl))
    run_dir = pathlib.Path(args.out) / run_id
    if run_dir.exists():
        raise SystemExit('run directory already exists: %s' % run_dir)
    budget = Budget(args.budget_requests, args.budget_bytes, args.budget_seconds)
    run, _ = run_collection(args.bbl, run_dir, budget=budget)
    package = write_package(run_dir)
    print(json.dumps({'run_id': run_id, 'status': run['status'], 'budget': run['budget'],
                      'records': len(package['records']), 'other_parcels': len(package['other_parcels']),
                      'conflicts': len(package['conflicts']), 'unknowns': len(package['unknowns'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
