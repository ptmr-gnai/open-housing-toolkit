#!/usr/bin/env python3
"""Offline tests for the parcel evidence module. No network access."""
import copy, hashlib, json, pathlib, sys, tempfile, time, unittest, urllib.error
from contextlib import contextmanager
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import collect
import parcel_evidence as pe

BBL = '2012340056'
OTHER_BBL = '2012340057'

BODIES = {
    'pluto_%s' % BBL: [{'bbl': BBL, 'bin': '2012345', 'address': '123 MAIN ST',
                        'ownername': 'ACME HOLDINGS LLC', 'zonedist1': 'R8A',
                        'lotarea': 5000, 'appbbl': BBL, 'condono': None,
                        'unitsres': 0, 'numfloors': 3, 'bldgclass': 'V1'}],
    'acris_legal_%s' % BBL: [
        {'document_id': 'D1', 'record_type': 'L', 'borough': '2', 'block': '01234', 'lot': '56',
         'street_number': '123', 'street_name': 'MAIN ST', 'good_through_date': '2020-01-31T00:00:00.000'},
        {'document_id': 'D2', 'record_type': 'L', 'borough': '2', 'block': '01234', 'lot': '56',
         'street_number': '123', 'street_name': 'MAIN ST', 'good_through_date': '2021-01-31T00:00:00.000'},
        {'document_id': 'D3', 'record_type': 'L', 'borough': '2', 'block': '01234', 'lot': '57',
         'street_number': '125', 'street_name': 'MAIN ST', 'good_through_date': '2019-05-31T00:00:00.000'},
        {'document_id': 'D4', 'record_type': 'L', 'borough': '2', 'block': '01234', 'lot': '56',
         'street_number': '123', 'street_name': 'MAIN ST', 'good_through_date': '2018-03-31T00:00:00.000'},
    ],
    'acris_master_%s' % BBL: [
        {'document_id': 'D1', 'crfn': 'C1', 'doc_type': 'DEED', 'document_date': '2020-01-15T00:00:00.000',
         'document_amt': '500000.00', 'recorded_datetime': '2020-01-20T00:00:00.000',
         'good_through_date': '2020-01-31T00:00:00.000'},
        {'document_id': 'D2', 'crfn': 'C2', 'doc_type': 'MTGE', 'document_date': '2021-01-10T00:00:00.000',
         'document_amt': '400000.00', 'recorded_datetime': '2021-01-12T00:00:00.000',
         'good_through_date': '2021-01-31T00:00:00.000'},
        {'document_id': 'D3', 'crfn': 'C3', 'doc_type': 'AGMT', 'document_date': '2019-05-01T00:00:00.000',
         'document_amt': '0.00', 'recorded_datetime': '2019-05-02T00:00:00.000',
         'good_through_date': '2019-05-31T00:00:00.000'},
    ],
    'acris_parties_%s' % BBL: [
        {'document_id': 'D1', 'party_type': '1', 'name': 'OLD OWNER LLC'},
        {'document_id': 'D1', 'party_type': '2', 'name': 'ACME HOLDINGS LLC'},
        {'document_id': 'D2', 'party_type': '1', 'name': 'ACME HOLDINGS LLC'},
        {'document_id': 'D2', 'party_type': '2', 'name': 'SOME BANK'},
        {'document_id': 'D3', 'party_type': '1', 'name': 'SOME PARTY'},
    ],
    'dof_sales_%s' % BBL: [
        {'bbl': BBL, 'bin': '2012345', 'address': '123 MAIN ST',
         'borough': '2', 'block': '01234', 'lot': '0056', 'apartment_number': None,
         'sale_date': '2020-01-15', 'sale_price': '500000',
         'building_class_category': '01 ONE FAMILY DWELLINGS'},
    ],
    'acris_doc_codes': [
        {'record_type': 'D', 'doc__type': 'DEED', 'doc__type_description': 'DEED',
         'class_code_description': 'DEEDS AND OTHER CONVEYANCES',
         'party1_type': 'GRANTOR/SELLER', 'party2_type': 'GRANTEE/BUYER'},
        {'record_type': 'D', 'doc__type': 'MTGE', 'doc__type_description': 'MORTGAGE',
         'class_code_description': 'MORTGAGES & INSTRUMENTS',
         'party1_type': 'MORTGAGOR/BORROWER', 'party2_type': 'MORTGAGEE/LENDER'},
        {'record_type': 'D', 'doc__type': 'AGMT', 'doc__type_description': 'AGREEMENT',
         'class_code_description': 'MORTGAGES & INSTRUMENTS',
         'party1_type': 'PARTY 1', 'party2_type': 'PARTY 2'},
    ],
}


def make_fake_fetcher(bodies):
    def fetcher(source, budget, run_dir):
        budget.charge_request()
        sid = source['source_id']
        body = bodies.get(sid)
        if body is None:
            raise AssertionError('unexpected source requested: %s' % sid)
        data = json.dumps(body).encode()
        cache = pathlib.Path(run_dir) / 'cache'
        cache.mkdir(parents=True, exist_ok=True)
        (cache / (sid + '.body')).write_bytes(data)
        record = {'id': sid, 'url': source['url'], 'publisher': source['publisher'],
                  'retrieved_at': '2026-01-01T00:00:00+00:00', 'coverage_limits': source['limits'],
                  'terms_url': source.get('terms'), 'status': 'ok', 'http_status': 200,
                  'content_type': 'application/json', 'last_modified': None,
                  'cache_path': 'cache/%s.body' % sid, 'bytes': len(data),
                  'sha256': hashlib.sha256(data).hexdigest()}
        (cache / (sid + '.source.json')).write_text(json.dumps(record, indent=2) + '\n')
        with (cache / 'collection-attempts.jsonl').open('a') as ledger:
            ledger.write(json.dumps(record, sort_keys=True) + '\n')
        return record
    return fetcher


def make_failing_fetcher(bodies, fail_source):
    base = make_fake_fetcher(bodies)

    def fetcher(source, budget, run_dir):
        if source['source_id'] == fail_source:
            budget.charge_request()
            cache = pathlib.Path(run_dir) / 'cache'
            cache.mkdir(parents=True, exist_ok=True)
            record = {'id': source['source_id'], 'url': source['url'],
                      'publisher': source['publisher'],
                      'retrieved_at': '2026-01-01T00:00:00+00:00',
                      'coverage_limits': source['limits'], 'terms_url': source.get('terms'),
                      'status': 'failed', 'http_status': 500, 'error': 'HTTP 500'}
            (cache / (source['source_id'] + '.source.json')).write_text(json.dumps(record, indent=2) + '\n')
            with (cache / 'collection-attempts.jsonl').open('a') as ledger:
                ledger.write(json.dumps(record, sort_keys=True) + '\n')
            return record
        return base(source, budget, run_dir)
    return fetcher


@contextmanager
def run_ctx(bodies=None, budget=None, fetcher=None):
    """Run a fake collection in a temp dir; yields (run_dir, run, package)."""
    bodies = bodies if bodies is not None else copy.deepcopy(BODIES)
    tmp = tempfile.TemporaryDirectory()
    try:
        run_dir = pathlib.Path(tmp.name) / 'run-test'
        run, _ = pe.run_collection(BBL, run_dir, budget=budget,
                                   fetcher=fetcher or make_fake_fetcher(bodies))
        package = pe.write_package(run_dir)
        yield run_dir, run, package
    finally:
        tmp.cleanup()


class BudgetTests(unittest.TestCase):
    def test_request_limit(self):
        b = pe.Budget(max_requests=3)
        b.start()
        for _ in range(3):
            b.charge_request()
        with self.assertRaises(pe.BudgetExceeded) as ctx:
            b.charge_request()
        self.assertEqual(ctx.exception.which, 'requests')
        self.assertEqual(b.snapshot()['exhausted'], 'requests')

    def test_byte_limit(self):
        b = pe.Budget(max_bytes=25 * 1024 * 1024)
        b.start()
        b.charge_bytes(10 * 1024 * 1024)
        b.charge_bytes(10 * 1024 * 1024)
        with self.assertRaises(pe.BudgetExceeded) as ctx:
            b.charge_bytes(10 * 1024 * 1024)
        self.assertEqual(ctx.exception.which, 'bytes')

    def test_time_limit(self):
        now = [1000.0]
        b = pe.Budget(max_seconds=10, clock=lambda: now[0])
        b.start()
        now[0] = 1011.0
        with self.assertRaises(pe.BudgetExceeded) as ctx:
            b.charge_request()
        self.assertEqual(ctx.exception.which, 'time')

    def test_defaults_are_proposed_budget(self):
        self.assertEqual(pe.BUDGET_DEFAULTS, {'max_requests': 150,
                                              'max_bytes': 50 * 1024 * 1024,
                                              'max_seconds': 90 * 60})

    def test_snapshot_fields(self):
        b = pe.Budget()
        b.start()
        snap = b.snapshot()
        for key in ('max_requests', 'max_bytes', 'max_seconds', 'requests', 'bytes',
                    'elapsed_seconds', 'exhausted'):
            self.assertIn(key, snap)
        self.assertIsNone(snap['exhausted'])


class CollectionTests(unittest.TestCase):
    def test_run_writes_run_and_package(self):
        with run_ctx() as (run_dir, run, package):
            self.assertEqual(run['status'], 'complete')
            self.assertEqual(len(run['requests']), 6)  # 4 phase-1 (incl. doc codes) + 2 phase-2
            self.assertTrue((run_dir / 'run.json').exists())
            self.assertTrue((run_dir / 'package.json').exists())
            self.assertEqual(len(package['records']), 6)  # 4 ACRIS + PLUTO + 1 sale

    def test_deeds_distinguished_from_mortgages(self):
        with run_ctx() as (_, _, package):
            families = {r['record_id']: r['instrument_family'] for r in package['records']
                        if r['kind'] == 'recorded_instrument'}
            self.assertEqual(families['acris:D1'], 'deed')
            self.assertEqual(families['acris:D2'], 'mortgage')
            self.assertEqual(families['acris:D3'], 'mortgage')  # AGMT: MORTGAGES & INSTRUMENTS class
            self.assertEqual(families['acris:D4'], 'unclassified')
            d1 = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            self.assertEqual(d1['classification_basis'], 'acris_control_codes')
            self.assertEqual(d1['doc_class'], 'DEEDS AND OTHER CONVEYANCES')
            self.assertEqual(d1['doc_type_description'], 'DEED')
            self.assertEqual(d1['doc_type_raw'], 'DEED')

    def test_doc_type_unmapped_is_unknown(self):
        bodies = copy.deepcopy(BODIES)
        bodies['acris_master_%s' % BBL][0]['doc_type'] = 'ZZZZ'
        with run_ctx(bodies=bodies) as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('doc_type_unmapped', kinds)
            d1 = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            self.assertEqual(d1['instrument_family'], 'unclassified')

    def test_keyword_fallback_when_doc_codes_missing(self):
        bodies = copy.deepcopy(BODIES)
        del bodies['acris_doc_codes']
        with run_ctx(bodies=bodies) as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('doc_codes_missing', kinds)
            d1 = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            self.assertEqual(d1['instrument_family'], 'deed')
            self.assertEqual(d1['classification_basis'], 'keyword_fallback')
            self.assertIsNone(package['mapping_provenance'])
            self.assertEqual(package['ownership_evidence']['recorded_grantees'], [])

    def test_party_roles_identified_from_control_codes(self):
        with run_ctx() as (_, _, package):
            oe = package['ownership_evidence']
            self.assertEqual(oe['current_owner']['status'], 'unknown')
            self.assertIn('chain of title', oe['current_owner']['reason'])
            grantees = oe['recorded_grantees']
            self.assertEqual(len(grantees), 1)
            self.assertEqual(grantees[0]['name'], 'ACME HOLDINGS LLC')
            self.assertEqual(grantees[0]['role'], 'GRANTEE/BUYER')
            self.assertEqual(grantees[0]['document_id'], 'D1')
            d1 = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            roles = {p['party_type']: p['role'] for p in d1['parties']}
            self.assertEqual(roles['1'], 'GRANTOR/SELLER')
            self.assertEqual(roles['2'], 'GRANTEE/BUYER')
            d2 = [r for r in package['records'] if r['record_id'] == 'acris:D2'][0]
            roles2 = {p['party_type']: p['role'] for p in d2['parties']}
            self.assertEqual(roles2['1'], 'MORTGAGOR/BORROWER')
            self.assertEqual(roles2['2'], 'MORTGAGEE/LENDER')

    def test_party_type_out_of_range_is_unknown(self):
        bodies = copy.deepcopy(BODIES)
        bodies['acris_parties_%s' % BBL].append(
            {'document_id': 'D1', 'party_type': '7', 'name': 'MYSTERY PARTY'})
        with run_ctx(bodies=bodies) as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('party_role_unmapped', kinds)
            d1 = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            mystery = [p for p in d1['parties'] if p['party_type'] == '7'][0]
            self.assertIsNone(mystery['role'])
            self.assertEqual(mystery['name'], 'MYSTERY PARTY')

    def test_party_role_placeholder_is_unknown(self):
        with run_ctx() as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('party_role_unspecified', kinds)  # D3 AGMT slot 1 is 'PARTY 1'
            d3 = [r for r in package['records'] if r['record_id'] == 'acris:D3'][0]
            self.assertIsNone(d3['parties'][0]['role'])

    def test_instrument_amount_never_sale_price(self):
        with run_ctx() as (_, _, package):
            for r in package['records']:
                if r['kind'] == 'recorded_instrument':
                    self.assertIn('instrument_amount', r)
                    self.assertNotIn('sale_price', r)
                    self.assertNotIn('amount', r)
                    if r['instrument_amount'] is not None:
                        self.assertIn('not a sale price', r['instrument_amount_note'] or '')
                if r['kind'] == 'sale':
                    self.assertIn('sale_price', r['fields'])
                    self.assertNotIn('instrument_amount', r)
            deed = [r for r in package['records'] if r['record_id'] == 'acris:D1'][0]
            sale = [r for r in package['records'] if r['kind'] == 'sale'][0]
            self.assertEqual(deed['instrument_amount'], '500000.00')
            self.assertEqual(sale['fields']['sale_price'], '500000')

    def test_truncation_flag(self):
        with run_ctx() as (_, _, package):
            pluto = [s for s in package['sources'] if s['id'].startswith('pluto_')][0]
            self.assertFalse(pluto['possibly_truncated'])
            self.assertEqual(pluto['row_count'], 1)
            self.assertEqual(pluto['limit'], 10)
        bodies = copy.deepcopy(BODIES)
        bodies['pluto_%s' % BBL] = [{'bbl': BBL, 'owner1': 'X', 'lotarea': 1} for _ in range(10)]
        with run_ctx(bodies=bodies) as (_, _, package):
            pluto = [s for s in package['sources'] if s['id'].startswith('pluto_')][0]
            self.assertTrue(pluto['possibly_truncated'])
            self.assertEqual(pluto['row_count'], 10)

    def test_date_bounds(self):
        with run_ctx() as (_, _, package):
            db = package['date_bounds']
            self.assertEqual(db['earliest_document_date'], '2019-05-01T00:00:00.000')
            self.assertEqual(db['latest_document_date'], '2021-01-10T00:00:00.000')
            self.assertIsNotNone(db['retrieved_at_range'])

    def test_mapping_provenance(self):
        with run_ctx() as (_, _, package):
            mp = package['mapping_provenance']
            self.assertIsNotNone(mp)
            self.assertIn('7isb-wh4c', mp['mapping_source'])
            self.assertEqual(len(mp['sha256']), 64)
            self.assertIn('doc_type', mp['fields'])
            self.assertIn('party_role', mp['fields'])

    def test_other_parcels_from_same_records(self):
        with run_ctx() as (_, _, package):
            self.assertEqual(len(package['other_parcels']), 1)
            other = package['other_parcels'][0]
            self.assertEqual(other['bbl'], OTHER_BBL)
            self.assertEqual(other['referenced_by'], ['acris:D3'])

    def test_conflict_owner_label(self):
        bodies = copy.deepcopy(BODIES)
        bodies['pluto_%s' % BBL][0]['ownername'] = 'DIFFERENT OWNER LLC'
        with run_ctx(bodies=bodies) as (_, _, package):
            kinds = [c['kind'] for c in package['conflicts']]
            self.assertIn('owner_label_mismatch', kinds)
            conflict = [c for c in package['conflicts'] if c['kind'] == 'owner_label_mismatch'][0]
            self.assertEqual(len(conflict['evidence']), 2)

    def test_no_conflict_when_owner_matches(self):
        with run_ctx() as (_, _, package):
            self.assertEqual(package['conflicts'], [])

    def test_unknowns_recorded(self):
        with run_ctx() as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('master_missing', kinds)      # D4 has no master row
            self.assertIn('parties_missing', kinds)     # D4 has no parties rows
            self.assertIn('coverage', kinds)            # latest document date bound
            master_missing = [u for u in package['unknowns'] if u['kind'] == 'master_missing']
            self.assertIn('D4', master_missing[0]['description'])

    def test_partial_run_status_on_failed_source(self):
        bodies = copy.deepcopy(BODIES)
        fetcher = make_failing_fetcher(bodies, 'dof_sales_%s' % BBL)
        with run_ctx(bodies=bodies, fetcher=fetcher) as (run_dir, run, package):
            self.assertEqual(run['status'], 'partial')
            self.assertEqual(package['run_status'], 'partial')
            receipt = run_dir / 'cache' / ('dof_sales_%s.source.json' % BBL)
            self.assertTrue(receipt.exists())
            self.assertEqual(json.loads(receipt.read_text())['status'], 'failed')
            ledger = (run_dir / 'cache' / 'collection-attempts.jsonl').read_text().strip().splitlines()
            self.assertTrue(any('"status": "failed"' in line for line in ledger))

    def test_failed_run_status_when_nothing_ok(self):
        bodies = copy.deepcopy(BODIES)

        def all_fail(source, budget, run_dir):
            budget.charge_request()
            cache = pathlib.Path(run_dir) / 'cache'
            cache.mkdir(parents=True, exist_ok=True)
            record = {'id': source['source_id'], 'url': source['url'],
                      'publisher': source['publisher'],
                      'retrieved_at': '2026-01-01T00:00:00+00:00',
                      'coverage_limits': source['limits'], 'terms_url': source.get('terms'),
                      'status': 'failed', 'http_status': 500, 'error': 'HTTP 500'}
            (cache / (source['source_id'] + '.source.json')).write_text(json.dumps(record, indent=2) + '\n')
            return record
        with run_ctx(bodies=bodies, fetcher=all_fail) as (_, run, package):
            self.assertEqual(run['status'], 'failed')
            self.assertEqual(package['run_status'], 'failed')

    def test_locators_resolve_to_raw_rows(self):
        with run_ctx() as (run_dir, _, package):
            sources = {s['id']: s for s in package['sources']}
            for record in package['records']:
                for loc in record['locators']:
                    source = sources[loc['source_id']]
                    body = json.loads((run_dir / source['cache_path']).read_text())
                    row = body[loc['row']]
                    for field in loc['fields']:
                        self.assertIn(field, row)
            for grantee in package['ownership_evidence']['recorded_grantees']:
                for loc in grantee['locators']:
                    source = sources[loc['source_id']]
                    body = json.loads((run_dir / source['cache_path']).read_text())
                    row = body[loc['row']]
                    for field in loc['fields']:
                        self.assertIn(field, row)
            for conflict in package['conflicts']:
                for loc in conflict['evidence']:
                    self.assertIn(loc['source_id'], sources)

    def test_budget_exhaustion_mid_run(self):
        with run_ctx(budget=pe.Budget(max_requests=2)) as (_, run, package):
            self.assertEqual(run['status'], 'budget_exhausted')
            self.assertEqual(run['budget']['exhausted'], 'requests')
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('source_missing', kinds)  # unfetched sources are unknowns, not silent

    def test_existing_evidence_untouched(self):
        repo = pathlib.Path(__file__).resolve().parents[1]
        before = {str(p.relative_to(repo)) for p in (repo / 'cache').rglob('*') if p.is_file()}
        out_outputs = {str(p.relative_to(repo)) for p in (repo / 'outputs').rglob('*') if p.is_file()}
        with run_ctx():
            pass
        after = {str(p.relative_to(repo)) for p in (repo / 'cache').rglob('*') if p.is_file()}
        after_outputs = {str(p.relative_to(repo)) for p in (repo / 'outputs').rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(out_outputs, after_outputs)

    def test_package_deterministic(self):
        with run_ctx() as (run_dir, _, _):
            first = (run_dir / 'package.json').read_bytes()
            second = json.dumps(pe.build_package(run_dir), indent=2, sort_keys=True).encode() + b'\n'
            self.assertEqual(first, second)

    def test_non_claims_present(self):
        with run_ctx() as (_, _, package):
            self.assertTrue(any('not a title opinion' in c for c in package['non_claims']))
            self.assertTrue(any('never sale prices' in c for c in package['non_claims']))
            self.assertTrue(any('not a current-owner conclusion' in c for c in package['non_claims']))
            for record in package['records']:
                self.assertNotIn('beneficial_owner', record)
                self.assertNotIn('current_owner', record)


def make_transport(script):
    """Fake transport. Script entries: ('ok', body) | ('http', status, headers, body)
    | ('raise', exception). Repeats the last entry when exhausted. Returns
    (transport, calls). Mimics the real transport: charges received bytes to
    the run budget (as BoundedReader does) and returns
    (status, headers, body, stop)."""
    calls = []

    def transport(url, timeout=55, byte_cap=10 * 1024 * 1024, budget=None, session=None):
        calls.append(url)
        outcome = script[min(len(calls) - 1, len(script) - 1)]
        if outcome[0] == 'ok':
            body = outcome[1]
            stop = None
            if budget is not None:
                try:
                    budget.charge_bytes(len(body))
                except pe.BudgetExceeded:
                    stop = 'budget'
            return 200, {'Content-Type': 'application/json'}, body, stop
        if outcome[0] == 'http':
            body = outcome[3]
            stop = None
            if budget is not None:
                try:
                    budget.charge_bytes(len(body))
                except pe.BudgetExceeded:
                    stop = 'budget'
            return outcome[1], outcome[2], body, stop
        raise outcome[1]
    return transport, calls


SOURCE = {'source_id': 't', 'url': 'https://example.invalid/t.json',
          'publisher': 'p', 'limits': 'l'}
BODY = b'[{"x": 1}]'


class BoundedFetchTests(unittest.TestCase):
    def _fetch(self, script, max_requests=150, max_bytes=50 * 1024 * 1024,
               max_seconds=90 * 60, byte_cap=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name)
        transport, calls = make_transport(script)
        sleeps = []
        budget = pe.Budget(max_requests=max_requests, max_bytes=max_bytes,
                           max_seconds=max_seconds)
        budget.start()
        kwargs = {'transport': transport, 'sleep': sleeps.append}
        if byte_cap is not None:
            kwargs['byte_cap'] = byte_cap
        try:
            record = pe.bounded_fetch(SOURCE, budget, root, **kwargs)
        except pe.BudgetExceeded:
            record = None
        return root, record, budget, calls, sleeps

    def test_retry_with_retry_after_then_success(self):
        root, record, budget, calls, sleeps = self._fetch([
            ('http', 429, {'Retry-After': '1'}, b'rate limited'),
            ('http', 429, {'Retry-After': '2'}, b'rate limited'),
            ('ok', BODY),
        ])
        self.assertEqual(record['status'], 'ok')
        self.assertEqual(budget.requests, 3)          # retries count as requests
        self.assertEqual(len(calls), 3)
        self.assertEqual(sleeps, [1.0, 2.0])          # Retry-After honored
        self.assertTrue((root / 'cache' / 't.attempt-1.error').exists())  # error bodies retained per attempt
        self.assertEqual(json.loads((root / 'cache' / 't.source.json').read_text())['status'], 'ok')

    def test_retry_exhausted_gives_failed_record(self):
        root, record, budget, calls, sleeps = self._fetch(
            [('http', 429, {'Retry-After': '1'}, b'x')])
        self.assertEqual(record['status'], 'failed')
        self.assertEqual(budget.requests, 3)          # 1 + 2 retries, then stop
        self.assertEqual(len(calls), 3)
        self.assertIn('HTTP 429', record['error'])
        self.assertTrue((root / 'cache' / 't.attempt-1.error').exists())
        self.assertTrue((root / 'cache' / 't.attempt-3.error').exists())

    def test_no_retry_on_404(self):
        root, record, budget, calls, sleeps = self._fetch([('http', 404, {}, b'not found')])
        self.assertEqual(record['status'], 'failed')
        self.assertEqual(budget.requests, 1)
        self.assertEqual(len(calls), 1)
        self.assertEqual(sleeps, [])

    def test_timeout_retries_then_success(self):
        root, record, budget, calls, sleeps = self._fetch([
            ('raise', urllib.error.URLError('timed out')),
            ('raise', urllib.error.URLError('timed out')),
            ('ok', BODY),
        ])
        self.assertEqual(record['status'], 'ok')
        self.assertEqual(budget.requests, 3)
        self.assertEqual(sleeps, [1.0, 2.0])          # exponential backoff

    def test_oversized_response_no_retry(self):
        def transport(url, timeout=55, byte_cap=100, budget=None, session=None):
            return 200, {}, b'x' * 100, 'cap'
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name)
        budget = pe.Budget()
        budget.start()
        sleeps = []
        record = pe.bounded_fetch(SOURCE, budget, root, transport=transport, sleep=sleeps.append)
        self.assertEqual(record['status'], 'failed')
        self.assertIn('cap', record['error'])
        self.assertEqual(budget.requests, 1)
        self.assertEqual(sleeps, [])

    def test_error_bodies_charge_bytes(self):
        root, record, budget, calls, sleeps = self._fetch(
            [('http', 500, {}, b'x' * 100)], max_bytes=150)
        self.assertEqual(record['status'], 'failed')   # partial body retained, not lost
        self.assertEqual(budget.bytes, 200)            # error bodies counted
        self.assertEqual(budget.requests, 2)
        self.assertIn('budget', record['error'])
        self.assertTrue((root / 'cache' / 't.attempt-2.error').exists())

    def test_long_numeric_retry_after_honored_in_full(self):
        root, record, budget, calls, sleeps = self._fetch([
            ('http', 429, {'Retry-After': '120'}, b'rate limited'),
            ('ok', BODY),
        ])
        self.assertEqual(record['status'], 'ok')
        self.assertEqual(sleeps, [120.0])              # full 120s, never shortened

    def test_retry_after_exceeding_deadline_stops(self):
        # 90-second budget, 120-second Retry-After: cannot honor in full, so stop.
        root, record, budget, calls, sleeps = self._fetch([
            ('http', 429, {'Retry-After': '120'}, b'rate limited'),
            ('ok', BODY),
        ], max_seconds=90)
        self.assertEqual(record['status'], 'failed')
        self.assertEqual(len(calls), 1)
        self.assertEqual(sleeps, [])

    def test_http_date_retry_after_honored(self):
        from datetime import datetime, timedelta, timezone
        from email.utils import format_datetime
        when = datetime.now(timezone.utc) + timedelta(seconds=90)
        root, record, budget, calls, sleeps = self._fetch([
            ('http', 429, {'Retry-After': format_datetime(when)}, b'rate limited'),
            ('ok', BODY),
        ])
        self.assertEqual(record['status'], 'ok')
        self.assertTrue(85 <= sleeps[0] <= 90)

    def test_request_cap_counts_retries(self):
        root, record, budget, calls, sleeps = self._fetch([
            ('http', 429, {}, b'x'), ('http', 429, {}, b'x'), ('ok', BODY)
        ], max_requests=3)
        self.assertEqual(record['status'], 'ok')
        self.assertEqual(budget.requests, 3)
        # a further fetch must be refused
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ok_transport, _ = make_transport([('ok', BODY)])
        with self.assertRaises(pe.BudgetExceeded):
            pe.bounded_fetch({'source_id': 't2', 'url': 'https://example.invalid/t2.json',
                              'publisher': 'p', 'limits': 'l'},
                             budget, pathlib.Path(tmp.name),
                             transport=ok_transport, sleep=lambda s: None)

    def test_cache_reuse_no_charge(self):
        root, record, budget, calls, sleeps = self._fetch([('ok', BODY)])
        self.assertEqual(record['status'], 'ok')
        budget2 = pe.Budget()
        budget2.start()
        record2 = pe.bounded_fetch(SOURCE, budget2, root,
                                   transport=make_transport([('ok', b'different')])[0],
                                   sleep=lambda s: None)
        self.assertEqual(record2['sha256'], record['sha256'])
        self.assertEqual(budget2.requests, 0)         # cache hit: no request charged

    def test_session_charged_requests_and_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            session = pe.SessionBudget(pathlib.Path(tmp) / 'session.json')
            transport, _ = make_transport([('ok', BODY)])
            budget = pe.Budget()
            budget.start()
            record = pe.bounded_fetch(SOURCE, budget, root, session=session,
                                      transport=transport, sleep=lambda s: None)
            self.assertEqual(record['status'], 'ok')
            self.assertEqual(session.requests, 1)
            self.assertEqual(session.bytes, len(BODY))


class SessionBudgetTests(unittest.TestCase):
    def test_accumulates_across_instances(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'session.json'
            s1 = pe.SessionBudget(path, max_requests=5)
            s1.charge('docs', requests=2, nbytes=1000)
            s2 = pe.SessionBudget(path, max_requests=5)
            self.assertEqual(s2.requests, 2)
            self.assertEqual(s2.bytes, 1000)
            s2.charge('run', requests=3)
            with self.assertRaises(pe.BudgetExceeded):
                s2.charge('more', requests=1)
            # The rejected 6th charge is persisted before the check, so the
            # ledger holds the truthful accounting of what was attempted.
            data = json.loads(path.read_text())
            self.assertEqual(data['requests'], 6)
            self.assertEqual(len(data['entries']), 3)

    def test_exhausted_state_survives_reload(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'session.json'
            s = pe.SessionBudget(path, max_requests=2)
            s.charge('a', requests=2)
            with self.assertRaises(pe.BudgetExceeded):
                s.charge('b', requests=1)
            s2 = pe.SessionBudget(path, max_requests=2)
            self.assertEqual(s2.requests, 3)  # truthful: 3 attempts recorded
            with self.assertRaises(pe.BudgetExceeded):
                s2.charge('c', requests=1)

    def test_byte_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'session.json'
            s = pe.SessionBudget(path, max_bytes=100)
            s.charge('a', nbytes=60)
            with self.assertRaises(pe.BudgetExceeded):
                s.charge('b', nbytes=60)


class ProvenanceTests(unittest.TestCase):
    def test_cached_source_reuse_and_tamper_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            cache = root / 'cache'
            cache.mkdir()
            body = b'[{"x": 1}]'
            (cache / 't.body').write_bytes(body)
            record = {'id': 't', 'url': 'https://example.invalid/t.json', 'publisher': 'p',
                      'retrieved_at': '2026-01-01T00:00:00+00:00', 'coverage_limits': 'l',
                      'terms_url': None, 'status': 'ok', 'http_status': 200,
                      'content_type': 'application/json', 'last_modified': None,
                      'cache_path': 'cache/t.body', 'bytes': len(body),
                      'sha256': hashlib.sha256(body).hexdigest()}
            (cache / 't.source.json').write_text(json.dumps(record))
            reused = collect.fetch('t', 'https://example.invalid/t.json', 'p', 'l', root=root)
            self.assertEqual(reused['sha256'], record['sha256'])
            (cache / 't.body').write_bytes(b'[{"x": 2}]')
            with self.assertRaises(ValueError) as ctx:
                collect.fetch('t', 'https://example.invalid/t.json', 'p', 'l', root=root)
            self.assertIn('Changed cached source', str(ctx.exception))


class UnitTests(unittest.TestCase):
    def test_replay_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / 'run-x'
            run_dir.mkdir()
            (run_dir / 'run.json').write_text(json.dumps(
                {'run_id': 'run-x', 'bbl': '2028710002', 'status': 'complete',
                 'budget': {'max_requests': 150, 'max_bytes': 52428800,
                            'max_seconds': 5400, 'requests': 0, 'bytes': 0,
                            'elapsed_seconds': 0.0, 'exhausted': None}}))
            (run_dir / 'package.json').write_text('{"sentinel": true}\n')
            import io
            from contextlib import redirect_stdout
            with redirect_stdout(io.StringIO()):
                rc = pe.main(['--replay', str(run_dir)])
            self.assertEqual(rc, 0)
            self.assertEqual((run_dir / 'package.json').read_text(), '{"sentinel": true}\n')

    def test_parse_bbl(self):
        self.assertEqual(pe.parse_bbl('2028710002'), ('2', '02871', '0002'))
        self.assertEqual(pe.bbl_from_parts('2', '2871', '2'), '2028710002')
        for bad in ('', '12345', '6028710002', '20287100021', '2A28710002'):
            with self.assertRaises(ValueError):
                pe.parse_bbl(bad)

    def test_classify_doc_type_fallback(self):
        cases = {'DEED': 'deed', 'DEED OF TRUST': 'deed', 'MTGE': 'mortgage', 'MTG': 'mortgage',
                 'MTG RFRG': 'mortgage', 'MORTGAGE': 'mortgage', 'SAT': 'release',
                 'REL': 'release', 'AGMT': 'other', 'AL&R': 'other', 'LEAS': 'other',
                 None: 'unclassified', '': 'unclassified'}
        for code, expected in cases.items():
            self.assertEqual(pe.classify_doc_type(code), expected, code)

    def test_plan_phase1_includes_doc_codes(self):
        sources = pe.plan_phase1(BBL)
        ids = [s['source_id'] for s in sources]
        self.assertIn('acris_doc_codes', ids)
        self.assertEqual(len(sources), 4)

    def test_plan_phase2_empty_without_document_ids(self):
        self.assertEqual(pe.plan_phase2(BBL, []), [])
        self.assertEqual(len(pe.plan_phase2(BBL, ['D1'])), 2)

    def test_retry_delay_parsing(self):
        self.assertEqual(pe._retry_delay({'Retry-After': '7'}, 1), 7.0)
        self.assertEqual(pe._retry_delay({'Retry-After': '999'}, 1), 999.0)  # full, never shortened
        self.assertEqual(pe._retry_delay({}, 1), 1.0)
        self.assertEqual(pe._retry_delay({}, 4), 8.0)
        self.assertEqual(pe._retry_delay({}, 9), pe.BACKOFF_CAP_SECONDS)


class BoundedReaderTests(unittest.TestCase):
    """Real BoundedReader against fake streams: mid-read enforcement and
    per-chunk charging, partial bodies retained."""

    class FakeStream:
        def __init__(self, data):
            self.data, self.pos = data, 0

        def read(self, n):
            chunk = self.data[self.pos:self.pos + n]
            self.pos += len(chunk)
            return chunk

    def test_reader_stops_at_per_request_cap(self):
        budget = pe.Budget()
        budget.start()
        reader = pe.BoundedReader(self.FakeStream(b'x' * 300), 100, budget)
        body = reader.read_all()
        self.assertEqual(len(body), 100)
        self.assertEqual(reader.stop, 'cap')
        self.assertEqual(budget.bytes, 100)

    def test_reader_stops_at_remaining_run_bytes(self):
        budget = pe.Budget(max_bytes=150)
        budget.start()
        budget.charge_bytes(50)  # 100 bytes remaining
        reader = pe.BoundedReader(self.FakeStream(b'x' * 300), 10 * 1024 * 1024, budget)
        body = reader.read_all()
        self.assertEqual(len(body), 100)
        self.assertEqual(reader.stop, 'budget')
        self.assertEqual(budget.bytes, 150)

    def test_reader_stops_at_remaining_session_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            session = pe.SessionBudget(pathlib.Path(tmp) / 's.json', max_bytes=150)
            session.charge('prior', nbytes=50)
            budget = pe.Budget()
            budget.start()
            reader = pe.BoundedReader(self.FakeStream(b'x' * 300), 10 * 1024 * 1024,
                                      budget, session)
            body = reader.read_all()
            self.assertEqual(len(body), 100)
            self.assertEqual(reader.stop, 'budget')

    def test_reader_stops_on_time(self):
        clock = [0.0]
        budget = pe.Budget(max_seconds=10, clock=lambda: clock[0])
        budget.start()
        data = b'x' * 300
        pos = [0]

        class SlowStream:
            def read(self, n):
                chunk = data[pos[0]:pos[0] + min(n, 10)]
                pos[0] += len(chunk)
                clock[0] += 11  # each read overshoots the time budget
                return chunk

        reader = pe.BoundedReader(SlowStream(), 10 * 1024 * 1024, budget)
        body = reader.read_all()
        self.assertEqual(len(body), 10)  # one chunk read, then time exhausted
        self.assertEqual(reader.stop, 'time')


class TransportIntegrationTests(unittest.TestCase):
    """Real transport_urllib + BoundedReader + shared SessionBudget, with
    urlopen monkeypatched (no network)."""

    def test_real_transport_charges_run_and_session(self):
        import io
        payload = b'["a"]' * 100  # 600 bytes

        class FakeResp(io.BytesIO):
            status = 200
            headers = {'Content-Type': 'application/json'}

            def __enter__(self):
                return self

            def __exit__(self, *a):
                self.close()

        with tempfile.TemporaryDirectory() as tmp:
            session = pe.SessionBudget(pathlib.Path(tmp) / 's.json')
            budget = pe.Budget()
            budget.start()
            orig = pe.urllib.request.urlopen
            pe.urllib.request.urlopen = lambda req, timeout=None: FakeResp(payload)
            try:
                record = pe.bounded_fetch(SOURCE, budget, pathlib.Path(tmp) / 'run',
                                          session=session, sleep=lambda s: None)
            finally:
                pe.urllib.request.urlopen = orig
            self.assertEqual(record['status'], 'ok')
            self.assertEqual(budget.bytes, len(payload))
            self.assertEqual(session.bytes, len(payload))
            self.assertEqual(session.requests, 1)

    def test_real_transport_error_body_retained_and_charged(self):
        import io
        import urllib.error

        with tempfile.TemporaryDirectory() as tmp:
            session = pe.SessionBudget(pathlib.Path(tmp) / 's.json')
            budget = pe.Budget()
            budget.start()
            orig = pe.urllib.request.urlopen
            err = urllib.error.HTTPError('https://example.invalid/x.json', 503, 'unavailable',
                                         {'Retry-After': '1'}, io.BytesIO(b'server busy'))

            def raise_err(req, timeout=None):
                raise err

            pe.urllib.request.urlopen = raise_err
            try:
                status, headers, body, stop = pe.transport_urllib(
                    'https://example.invalid/x.json', budget=budget, session=session)
            finally:
                pe.urllib.request.urlopen = orig
            self.assertEqual(status, 503)
            self.assertEqual(body, b'server busy')
            self.assertEqual(budget.bytes, len(b'server busy'))


class RetainedReceiptRegressionTests(unittest.TestCase):
    """Regression fixtures based on the retained raw receipts from the live
    run for BBL 1012127503 (150 West 82nd Street, a 38-unit elevator condo
    property per the raw PLUTO/DOF receipts)."""
    RUN3 = pathlib.Path(__file__).resolve().parents[1] / 'runs' / 'run-20261020T031148Z-1012127503'

    def test_run3_pluto_ownername_and_zoning(self):
        row = json.loads((self.RUN3 / 'cache' / 'pluto_1012127503.body').read_text())[0]
        self.assertEqual(row['ownername'], '150 WEST 82ND STREET OWNER, LLC')
        self.assertEqual(row['zonedist1'], 'R8B')
        self.assertEqual(row['unitsres'], '38')
        self.assertEqual(row['condono'], '3124')

    def test_run3_dof_rows_are_unit_level(self):
        rows = json.loads((self.RUN3 / 'cache' / 'dof_sales_1012127503.body').read_text())
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertEqual(row['bbl'], '1012127503')
            self.assertEqual(row['building_class_category'], '13 CONDOS - ELEVATOR APARTMENTS')
            self.assertTrue(row.get('apartment_number'))
            self.assertNotEqual(row['lot'], '7503')  # unit lot, not the mapped parcel lot

    def test_derived_run3_package_flags_unit_scope(self):
        derived = self.RUN3.parent / 'derived-20261020T033000Z' / 'run-20261020T031148Z-1012127503'
        package = json.loads((derived / 'package.json').read_text())
        self.assertEqual(package['package_version'], '0.3')
        kinds = {u['kind'] for u in package['unknowns']}
        self.assertIn('unit_sales_scope', kinds)
        pluto = [r for r in package['records'] if r['kind'] == 'parcel_identity'][0]
        self.assertEqual(pluto['fields']['ownername'], '150 WEST 82ND STREET OWNER, LLC')
        self.assertEqual(pluto['fields']['zonedist1'], 'R8B')
        self.assertIn('tax-roll label', pluto['owner_label_note'])
        sales = [r for r in package['records'] if r['kind'] == 'sale']
        self.assertTrue(all(s['scope'] == 'unit' for s in sales))
        self.assertTrue(all('raw' in s for s in sales))
        lineage = json.loads((derived / 'lineage.json').read_text())
        self.assertEqual(lineage['original_run_id'], 'run-20261020T031148Z-1012127503')


if __name__ == '__main__':
    unittest.main(verbosity=2)
