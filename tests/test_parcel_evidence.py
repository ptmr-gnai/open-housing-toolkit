#!/usr/bin/env python3
"""Offline tests for the parcel evidence module. No network access."""
import copy, hashlib, json, pathlib, sys, tempfile, time, unittest
from contextlib import contextmanager
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import collect
import parcel_evidence as pe

BBL = '2012340056'
OTHER_BBL = '2012340057'

BODIES = {
    'pluto_%s' % BBL: [{'bbl': BBL, 'bin': '2012345', 'address': '123 MAIN ST',
                        'owner1': 'ACME HOLDINGS LLC', 'owner2': None, 'lotarea': 5000,
                        'zoningdist': 'R8A'}],
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
        {'document_id': 'D1', 'party_name': 'ACME HOLDINGS LLC', 'party_role': 'GRANTEE'},
        {'document_id': 'D1', 'party_name': 'OLD OWNER LLC', 'party_role': 'GRANTOR'},
        {'document_id': 'D2', 'party_name': 'ACME HOLDINGS LLC', 'party_role': 'MORTGAGEE'},
    ],
    'dof_sales_%s' % BBL: [
        {'bbl': BBL, 'bin': '2012345', 'address': '123 MAIN ST', 'sale_date': '2020-01-15',
         'sale_price': '500000'},
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
        return record
    return fetcher


@contextmanager
def run_ctx(bodies=None, budget=None):
    """Run a fake collection in a temp dir; yields (run_dir, run, package)."""
    bodies = bodies if bodies is not None else copy.deepcopy(BODIES)
    tmp = tempfile.TemporaryDirectory()
    try:
        run_dir = pathlib.Path(tmp.name) / 'run-test'
        run, _ = pe.run_collection(BBL, run_dir, budget=budget,
                                   fetcher=make_fake_fetcher(bodies))
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
            self.assertEqual(len(run['requests']), 5)
            self.assertTrue((run_dir / 'run.json').exists())
            self.assertTrue((run_dir / 'package.json').exists())
            self.assertEqual(len(package['records']), 6)  # 4 ACRIS + PLUTO + 1 sale

    def test_deeds_distinguished_from_mortgages(self):
        with run_ctx() as (_, _, package):
            families = {r['record_id']: r['instrument_family'] for r in package['records']
                        if r['kind'] == 'recorded_instrument'}
            self.assertEqual(families['acris:D1'], 'deed')
            self.assertEqual(families['acris:D2'], 'mortgage')
            self.assertEqual(families['acris:D3'], 'other')
            self.assertEqual(families['acris:D4'], 'unclassified')
            raw = {r['record_id']: r['doc_type_raw'] for r in package['records']
                   if r['kind'] == 'recorded_instrument'}
            self.assertEqual(raw['acris:D1'], 'DEED')
            self.assertEqual(raw['acris:D2'], 'MTGE')

    def test_other_parcels_from_same_records(self):
        with run_ctx() as (_, _, package):
            self.assertEqual(len(package['other_parcels']), 1)
            other = package['other_parcels'][0]
            self.assertEqual(other['bbl'], OTHER_BBL)
            self.assertEqual(other['referenced_by'], ['acris:D3'])

    def test_conflict_owner_label(self):
        bodies = copy.deepcopy(BODIES)
        bodies['pluto_%s' % BBL][0]['owner1'] = 'DIFFERENT OWNER LLC'
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
            self.assertIn('parties_missing', kinds)     # D3, D4 have no parties rows
            self.assertIn('coverage', kinds)            # latest document date bound
            master_missing = [u for u in package['unknowns'] if u['kind'] == 'master_missing']
            self.assertIn('D4', master_missing[0]['description'])

    def test_party_role_codes_are_unknown_not_guessed(self):
        bodies = copy.deepcopy(BODIES)
        bodies['acris_parties_%s' % BBL] = [
            {'document_id': 'D1', 'name': 'ACME HOLDINGS LLC', 'party_type': '2'},
            {'document_id': 'D1', 'name': 'OLD OWNER LLC', 'party_type': '1'},
        ]
        with run_ctx(bodies=bodies) as (_, _, package):
            kinds = {u['kind'] for u in package['unknowns']}
            self.assertIn('party_role', kinds)
            self.assertEqual([c['kind'] for c in package['conflicts']], [])  # no owner guess

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
            for record in package['records']:
                self.assertNotIn('beneficial_owner', record)
                self.assertNotIn('current_owner', record)


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
    def test_parse_bbl(self):
        self.assertEqual(pe.parse_bbl('2028710002'), ('2', '02871', '0002'))
        self.assertEqual(pe.bbl_from_parts('2', '2871', '2'), '2028710002')
        for bad in ('', '12345', '6028710002', '20287100021', '2A28710002'):
            with self.assertRaises(ValueError):
                pe.parse_bbl(bad)

    def test_classify_doc_type(self):
        cases = {'DEED': 'deed', 'DEED OF TRUST': 'deed', 'MTGE': 'mortgage', 'MTG': 'mortgage',
                 'MTG RFRG': 'mortgage', 'MORTGAGE': 'mortgage', 'SAT': 'release',
                 'REL': 'release', 'AGMT': 'other', 'AL&R': 'other', 'LEAS': 'other',
                 None: 'unclassified', '': 'unclassified'}
        for code, expected in cases.items():
            self.assertEqual(pe.classify_doc_type(code), expected, code)

    def test_plan_phase2_empty_without_document_ids(self):
        self.assertEqual(pe.plan_phase2(BBL, []), [])
        self.assertEqual(len(pe.plan_phase2(BBL, ['D1'])), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
