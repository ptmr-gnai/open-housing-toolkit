#!/usr/bin/env python3
"""Parcel evidence module: bounded public ownership/transaction evidence.

For one BBL, collects ACRIS real-property records (deeds, mortgages and other
recorded instruments), DOF sales rows, the PLUTO parcel row and the ACRIS
Document Control Codes mapping dataset into a separate run directory, then
assembles a structured evidence package with exact claim locators, conflicts
and unknowns.

Document-type and party-role mappings are data-driven from the NYC Open Data
"ACRIS - Document Control Codes" dataset (7isb-wh4c, published by NYC DOF);
the raw mapping rows are retained in the run with receipts. Where the mapping
dataset is absent (older runs), a keyword fallback is used and flagged.

Collection budget: 150 requests, 50 MiB, 90 minutes (configurable), at most
2 retries per request, sequential (1 concurrent), bounded per-request reads,
Retry-After honored. Retries and error-response bytes count against the
budget. A run is 'complete' only if every planned source returned ok.

This module does not establish beneficial ownership or complete title
research. Recorded grantee evidence is not a current-owner conclusion.
Instrument amounts are recorded instrument amounts, never sale prices.
Stdlib only. MIT.
"""
import argparse, datetime, email.utils, hashlib, json, pathlib, re, time, urllib.error, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
BUDGET_DEFAULTS = {'max_requests': 150, 'max_bytes': 50 * 1024 * 1024, 'max_seconds': 90 * 60}
ACRIS_LEGALS = '8h5j-fqxa'
ACRIS_MASTER = 'bnx9-e6tj'
ACRIS_PARTIES = '636b-3b5g'
DOF_SALES = 'w2pb-icbu'
PLUTO = '64uk-42ks'
DOC_CODES = '7isb-wh4c'
TERMS = 'https://opendata.cityofnewyork.us/overview/#termsofuse'
USER_AGENT = 'OpenHousingToolkit/0.2 (public research)'
PER_REQUEST_BYTE_CAP = 10 * 1024 * 1024
MAX_RETRIES = 2
RETRYABLE_STATUS = {429, 500, 502, 503, 504}
BACKOFF_CAP_SECONDS = 10
HTTP_TIMEOUT_SECONDS = 55
CLASS_FAMILY = {
    'DEEDS AND OTHER CONVEYANCES': 'deed',
    'MORTGAGES & INSTRUMENTS': 'mortgage',
    'UCC AND FEDERAL LIENS': 'lien',
    'OTHER DOCUMENTS': 'other',
}
PARTY_PLACEHOLDERS = {'PARTY 1', 'PARTY 2', 'PARTY 3', 'PARTY ONE', 'PARTY TWO', 'PARTY THREE'}
LIMITS_ACRIS = ('ACRIS real property records for exact borough/block/lot or document_id. '
                'NYC boroughs excluding Staten Island; records from 1966 onward; good_through dates vary. '
                'Index rows are not native document images and not a current title opinion.')
LIMITS_SALES = ('DOF sales rows for exact BBL from the NYC Citywide Annualized Calendar Sales Update. '
                'Annualized update feed; absence of a row is not proof of no sale.')
LIMITS_PLUTO = ('PLUTO row for exact BBL. Tax-roll attributes; owner label is not legal ownership. '
                'Parcel fields may lag underlying changes.')
LIMITS_DOC_CODES = ('ACRIS Document Type and Class Code mappings for codes in the ACRIS Real and '
                    'Personal Property Master Datasets (NYC Open Data 7isb-wh4c, published by NYC DOF). '
                    'Mapping reference data; vintage per dataset update, not per recording.')
NON_CLAIMS = [
    'This package is not a title opinion. It does not establish beneficial ownership, current site control, or complete title research.',
    'ACRIS coverage: NYC boroughs excluding Staten Island; records from 1966 onward; good_through dates vary; native document images not retrieved.',
    'DOF sales dataset is an annualized update feed; absence of a row is not proof of no sale.',
    'PLUTO owner label is a tax-roll label, not legal ownership.',
    'Recorded grantee evidence identifies parties of recorded instruments; it is not a current-owner conclusion.',
    'Instrument amounts (document_amt) are recorded instrument amounts, never sale prices; DOF sale_price is the only sale-price field.',
    'doc_type classification uses the NYC DOF ACRIS Document Control Codes dataset (7isb-wh4c) where available; the keyword fallback is flagged per record.',
    'ACRIS legals are queried by exact BBL; documents in which this parcel appears only as a secondary legal are not collected. other_parcels reflects only documents collected in this run.',
    'DOF sales rows for condo buildings are unit-level sales associated with the condo billing/map BBL; their block/lot identify the unit lot, not the mapped parcel lot, and they are not whole-property sales.',
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


class SessionBudget:
    """Cumulative budget shared across documentation, discovery and collection
    in one session. File-backed so separate CLI invocations share the ledger.
    Wall-clock based (monotonic clocks do not compare across processes)."""

    def __init__(self, path, max_requests=BUDGET_DEFAULTS['max_requests'],
                 max_bytes=BUDGET_DEFAULTS['max_bytes'], max_seconds=BUDGET_DEFAULTS['max_seconds']):
        self.path = pathlib.Path(path)
        self.max_requests, self.max_bytes, self.max_seconds = max_requests, max_bytes, max_seconds
        self.entries = []
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.max_requests = data.get('max_requests', self.max_requests)
            self.max_bytes = data.get('max_bytes', self.max_bytes)
            self.max_seconds = data.get('max_seconds', self.max_seconds)
            self.requests = data.get('requests', 0)
            self.bytes = data.get('bytes', 0)
            self.started_at_epoch = data.get('started_at_epoch', time.time())
            self.entries = data.get('entries', [])
        else:
            self.requests = 0
            self.bytes = 0
            self.started_at_epoch = time.time()
            self._save()

    def elapsed(self):
        return time.time() - self.started_at_epoch

    def check(self):
        if self.requests > self.max_requests:
            raise BudgetExceeded('session requests')
        if self.bytes > self.max_bytes:
            raise BudgetExceeded('session bytes')
        if self.elapsed() > self.max_seconds:
            raise BudgetExceeded('session time')

    def charge(self, label, requests=0, nbytes=0):
        # Mutate, append the durable per-attempt entry, persist, THEN check.
        # If the check raises, the file already holds the truthful accounting.
        self.requests += int(requests)
        self.bytes += int(nbytes)
        self.entries.append({'label': label, 'requests': int(requests), 'bytes': int(nbytes),
                             'at': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        self._save()
        self.check()

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({
            'max_requests': self.max_requests, 'max_bytes': self.max_bytes,
            'max_seconds': self.max_seconds,
            'started_at': datetime.datetime.fromtimestamp(self.started_at_epoch, datetime.timezone.utc).isoformat(),
            'started_at_epoch': self.started_at_epoch,
            'requests': self.requests, 'bytes': self.bytes,
            'elapsed_seconds': round(self.elapsed(), 3), 'entries': self.entries},
            indent=2, sort_keys=True) + '\n')

    def snapshot(self):
        return {'max_requests': self.max_requests, 'max_bytes': self.max_bytes,
                'max_seconds': self.max_seconds, 'requests': self.requests,
                'bytes': self.bytes, 'elapsed_seconds': round(self.elapsed(), 3),
                'entries': self.entries}


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
        {'source_id': 'acris_doc_codes', 'url': soql_url(DOC_CODES, "record_type='D'", limit=10000),
         'publisher': 'NYC Department of Finance (ACRIS Document Control Codes)',
         'limits': LIMITS_DOC_CODES, 'terms': TERMS},
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


class BoundedReader:
    """Reads a stream in chunks, charging each received chunk to the run
    budget and enforcing the per-request cap plus the remaining run/session
    byte and time allowances DURING the read (not after a full response).
    When any allowance is exhausted it stops reading and returns the partial
    body received so far with a stop reason; received bytes are never lost."""

    def __init__(self, stream, byte_cap, budget, session=None):
        self.stream, self.byte_cap = stream, byte_cap
        self.budget, self.session = budget, session
        self.total = 0
        self.stop = None  # None | 'cap' | 'budget' | 'time'

    def read_all(self):
        chunks = []
        while self.stop is None:
            remaining = self.byte_cap - self.total
            if self.budget is not None:
                remaining = min(remaining, self.budget.max_bytes - self.budget.bytes)
                if self.budget.elapsed() > self.budget.max_seconds:
                    self.stop = 'time'
                    break
            if self.session is not None:
                # Session bytes are charged per attempt (after the read), so
                # subtract this attempt's in-flight bytes from the allowance.
                remaining = min(remaining, self.session.max_bytes - self.session.bytes - self.total)
                if self.session.elapsed() > self.session.max_seconds:
                    self.stop = 'time'
                    break
            if remaining <= 0:
                self.stop = 'budget'
                break
            chunk = self.stream.read(min(65536, remaining))
            if not chunk:
                break
            self.total += len(chunk)
            chunks.append(chunk)
            try:
                if self.budget is not None:
                    self.budget.charge_bytes(len(chunk))
            except BudgetExceeded as exc:
                self.stop = 'time' if exc.which == 'time' else 'budget'
                break
            if self.total >= self.byte_cap:
                self.stop = 'cap'
        return b''.join(chunks)


def transport_urllib(url, timeout=HTTP_TIMEOUT_SECONDS, byte_cap=PER_REQUEST_BYTE_CAP,
                     budget=None, session=None):
    """Default transport. Returns (status, headers, body, stop). HTTP error
    responses are returned (not raised) so the retry logic can see status and
    body; network/timeout errors raise. Reads are bounded per chunk by
    byte_cap and by the remaining run/session byte and time allowances;
    partial bodies are retained, never discarded. The socket timeout is capped
    by the remaining run/session time so a slow stream cannot overshoot the
    wall-clock budget."""
    if budget is not None and budget.started_at is not None:
        timeout = min(timeout, max(budget.max_seconds - budget.elapsed(), 1.0))
    if session is not None:
        timeout = min(timeout, max(session.max_seconds - session.elapsed(), 1.0))
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        response = urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as exc:
        reader = BoundedReader(exc, byte_cap, budget, session)
        body = reader.read_all()
        return exc.code, dict(exc.headers or {}), body, reader.stop
    with response:
        reader = BoundedReader(response, byte_cap, budget, session)
        body = reader.read_all()
        return response.status, dict(response.headers or {}), body, reader.stop


def _retry_delay(headers, attempt):
    """Full server Retry-After (numeric seconds or HTTP-date), never shortened.
    Falls back to capped exponential backoff when absent or unparseable."""
    raw = headers.get('Retry-After') or headers.get('retry-after')
    if raw:
        try:
            return max(float(raw), 0.0)
        except ValueError:
            try:
                when = email.utils.parsedate_to_datetime(raw)
                if when.tzinfo is None:
                    when = when.replace(tzinfo=datetime.timezone.utc)
                return max((when - datetime.datetime.now(datetime.timezone.utc)).total_seconds(), 0.0)
            except (TypeError, ValueError):
                pass
    return min(2.0 ** (attempt - 1), BACKOFF_CAP_SECONDS)


def _write_record(source, root, body, headers, status_code, error=None, attempt=None):
    root = pathlib.Path(root)
    cache_dir = root / 'cache'
    cache_dir.mkdir(parents=True, exist_ok=True)
    source_id = source['source_id']
    record = {'id': source_id, 'url': source['url'], 'publisher': source['publisher'],
              'retrieved_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'coverage_limits': source['limits'], 'terms_url': source.get('terms'),
              'source_updated_at': None, 'attempt': attempt}
    if error is None:
        path = cache_dir / (source_id + '.body')
        path.write_bytes(body)
        record.update(status='ok', http_status=status_code,
                      content_type=headers.get('Content-Type') or headers.get('content-type'),
                      last_modified=headers.get('Last-Modified') or headers.get('last-modified'),
                      cache_path=str(path.relative_to(root)), bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest())
        try:
            data = json.loads(body)
            if isinstance(data, dict):
                record['source_updated_at'] = data.get('rowsUpdatedAt') or data.get('viewLastModified')
                record['dataset_name'] = data.get('name')
        except (ValueError, UnicodeDecodeError):
            pass
    else:
        record.update(status='failed', http_status=status_code, error=error)
        if body:
            # Unique per-attempt path so earlier error/partial bodies are never overwritten.
            suffix = '.attempt-%d.error' % attempt if attempt else '.error'
            err_path = cache_dir / (source_id + suffix)
            err_path.write_bytes(body)
            record.update(error_body_path=str(err_path.relative_to(root)),
                          error_bytes=len(body), error_sha256=hashlib.sha256(body).hexdigest())
    (cache_dir / (source_id + '.source.json')).write_text(json.dumps(record, indent=2) + '\n')
    with (cache_dir / 'collection-attempts.jsonl').open('a') as ledger:
        ledger.write(json.dumps(record, sort_keys=True) + '\n')
    return record


def bounded_fetch(source, budget, root, session=None, transport=transport_urllib,
                  max_retries=MAX_RETRIES, timeout=HTTP_TIMEOUT_SECONDS,
                  byte_cap=PER_REQUEST_BYTE_CAP, sleep=time.sleep):
    """Fetch one source with bounded reads, bounded retries and full receipts.

    Every attempt (including retries) charges one request to the run and
    session budgets. Received bytes are charged per chunk by the transport's
    BoundedReader (run budget) and once per attempt to the session ledger;
    error and partial bodies are charged and retained, never lost. Retries
    only on network errors and 429/5xx, honoring the server's full
    Retry-After; if the full delay cannot fit in the remaining run/session
    time the fetch stops instead of retrying late. Failures are records,
    never exceptions. Cached ok receipts are reused only after hash
    verification; a changed cached body fails closed and is re-fetched.
    """
    root = pathlib.Path(root)
    record_path = root / 'cache' / (source['source_id'] + '.source.json')
    if record_path.exists():
        existing = json.loads(record_path.read_text())
        if existing.get('status') == 'ok' and existing.get('url') == source['url']:
            body_path = root / existing.get('cache_path', '')
            try:
                if hashlib.sha256(body_path.read_bytes()).hexdigest() == existing.get('sha256'):
                    return existing
            except (OSError, TypeError):
                pass
            # tampered or missing cached body: fail closed, re-fetch below
    attempt = 0
    while True:
        attempt += 1
        budget.charge_request()
        if session:
            session.charge(source['source_id'] + ' attempt %d' % attempt, requests=1)
        error, status_code, body, headers, stop = None, None, b'', {}, None
        bytes_before = budget.bytes
        try:
            status_code, headers, body, stop = transport(source['url'], timeout=timeout,
                                                         byte_cap=byte_cap, budget=budget,
                                                         session=session)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            error = '%s: %s' % (type(exc).__name__, exc)
        # Reconcile: the transport's BoundedReader charges received bytes per
        # chunk; guarantee the full received body is charged even if a custom
        # transport did not charge.
        if budget.bytes - bytes_before < len(body):
            budget.charge_bytes(len(body) - (budget.bytes - bytes_before))
        if stop is not None:
            error = 'read stopped: %s (%d bytes received and retained)' % (stop, len(body))
        elif error is None and status_code != 200:
            error = 'HTTP %s' % status_code
        if session and body:
            try:
                session.charge(source['source_id'] + ' attempt %d bytes' % attempt, nbytes=len(body))
            except BudgetExceeded:
                pass  # session exhausted; the record below is still written, then we stop
        record = _write_record(source, root, body, headers, status_code, error=error, attempt=attempt)
        if error is None:
            return record
        if error.startswith('HTTP'):
            retryable = status_code in RETRYABLE_STATUS
        else:
            # network/timeout errors retry; cap/budget/time stops do not
            retryable = stop is None
        if not retryable or attempt > max_retries:
            return record
        delay = _retry_delay(headers, attempt)
        remaining = budget.max_seconds - budget.elapsed()
        if session:
            remaining = min(remaining, session.max_seconds - session.elapsed())
        if delay > remaining:
            return record  # cannot honor the full Retry-After within the deadline; stop
        sleep(delay)


def make_fetcher(session=None, **kwargs):
    def fetcher(source, budget, run_dir):
        return bounded_fetch(source, budget, run_dir, session=session, **kwargs)
    return fetcher


def run_collection(bbl, run_dir, budget=None, fetcher=None):
    """Fetch all planned sources for one BBL into run_dir; write run.json.

    Returns (run_record, budget). Stops cleanly on BudgetExceeded or fetch
    failure; whatever was fetched is still packaged by build_package.
    Status is 'complete' only if every planned source returned ok; otherwise
    'partial' (some ok), 'failed' (none ok) or 'budget_exhausted'.
    """
    run_dir = pathlib.Path(run_dir)
    (run_dir / 'cache').mkdir(parents=True, exist_ok=True)
    budget = budget or Budget()
    fetcher = fetcher or make_fetcher()
    budget.start()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    requests, errors, document_ids = [], [], []
    budget_exhausted = False
    for phase in (plan_phase1(bbl), None):
        sources = phase if phase is not None else plan_phase2(bbl, document_ids)
        for source in sources:
            try:
                record = fetcher(source, budget, run_dir)
            except BudgetExceeded as exc:
                budget_exhausted = True
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
        if budget_exhausted:
            break
    planned = [s['source_id'] for s in plan_phase1(bbl)]
    if document_ids:
        planned += [s['source_id'] for s in plan_phase2(bbl, document_ids)]
    ok_ids = {r['source_id'] for r in requests if r['status'] == 'ok'}
    if budget_exhausted:
        status = 'budget_exhausted'
    elif ok_ids == set(planned) and len(requests) == len(planned):
        status = 'complete'
    elif ok_ids:
        status = 'partial'
    else:
        status = 'failed'
    run = {'run_id': run_dir.name, 'bbl': bbl, 'started_at': started,
           'ended_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'status': status, 'budget': budget.snapshot(), 'requests': requests, 'errors': errors}
    (run_dir / 'run.json').write_text(json.dumps(run, indent=2, sort_keys=True) + '\n')
    return run, budget


def classify_doc_type(code):
    """Keyword-based fallback triage of ACRIS doc_type codes. Used only when
    the ACRIS Document Control Codes source is unavailable; flagged as
    classification_basis='keyword_fallback'. Not legal interpretation."""
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
    if hashlib.sha256(body).hexdigest() != record.get('sha256'):
        raise ValueError('Changed cached source body for %s; refusing to use unverified evidence' % source_id)
    return record, json.loads(body)


def _locator(source_id, row, fields):
    return {'source_id': source_id, 'row': row, 'fields': sorted(fields)}


def _norm_name(name):
    return re.sub(r'\s+', ' ', (name or '').upper()).strip()


def _query_limit(url):
    try:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url or '').query)
        if '$limit' in q:
            return int(q['$limit'][0])
    except (ValueError, IndexError):
        pass
    return None


DOC_SOURCES = [
    {'source_id': 'acris_doc_codes', 'url': soql_url(DOC_CODES, "record_type='D'", limit=10000),
     'publisher': 'NYC Department of Finance (ACRIS Document Control Codes)',
     'limits': LIMITS_DOC_CODES, 'terms': TERMS},
    {'source_id': 'acris_doc_codes_metadata',
     'url': 'https://data.cityofnewyork.us/api/views/%s.json' % DOC_CODES,
     'publisher': 'NYC Open Data (Socrata dataset metadata)',
     'limits': 'Socrata dataset metadata: name, description, column descriptions, rowsUpdatedAt.',
     'terms': TERMS},
    {'source_id': 'acris_master_metadata',
     'url': 'https://data.cityofnewyork.us/api/views/%s.json' % ACRIS_MASTER,
     'publisher': 'NYC Open Data (Socrata dataset metadata)',
     'limits': 'Socrata dataset metadata: name, description, column descriptions, rowsUpdatedAt.',
     'terms': TERMS},
    {'source_id': 'acris_parties_metadata',
     'url': 'https://data.cityofnewyork.us/api/views/%s.json' % ACRIS_PARTIES,
     'publisher': 'NYC Open Data (Socrata dataset metadata)',
     'limits': 'Socrata dataset metadata: name, description, column descriptions, rowsUpdatedAt.',
     'terms': TERMS},
    {'source_id': 'acris_legals_metadata',
     'url': 'https://data.cityofnewyork.us/api/views/%s.json' % ACRIS_LEGALS,
     'publisher': 'NYC Open Data (Socrata dataset metadata)',
     'limits': 'Socrata dataset metadata: name, description, column descriptions, rowsUpdatedAt.',
     'terms': TERMS},
]


def collect_documentation(docs_dir, session=None, budget=None, fetcher=None):
    """Fetch the authoritative mapping documentation into docs_dir with
    receipts (raw bodies, source records, attempt ledger). Writes docs.json
    summarizing receipts and field-level mapping evidence."""
    docs_dir = pathlib.Path(docs_dir)
    (docs_dir / 'cache').mkdir(parents=True, exist_ok=True)
    budget = budget or Budget()
    fetcher = fetcher or make_fetcher(session=session)
    budget.start()
    receipts = []
    for source in DOC_SOURCES:
        try:
            record = fetcher(source, budget, docs_dir)
        except BudgetExceeded as exc:
            receipts.append({'source_id': source['source_id'], 'status': 'budget_exhausted',
                             'error': str(exc)})
            break
        except Exception as exc:
            receipts.append({'source_id': source['source_id'], 'status': 'failed',
                             'error': '%s: %s' % (type(exc).__name__, exc)})
            continue
        receipts.append({'source_id': record.get('id'), 'status': record.get('status'),
                         'url': record.get('url'), 'retrieved_at': record.get('retrieved_at'),
                         'sha256': record.get('sha256'), 'bytes': record.get('bytes'),
                         'source_updated_at': record.get('source_updated_at'),
                         'dataset_name': record.get('dataset_name'), 'error': record.get('error')})
    mapping_evidence = {}
    for field, source_id, field_name in (('doc_type', 'acris_master_metadata', 'doc_type'),
                                         ('party_role', 'acris_parties_metadata', 'party_type')):
        rec_path = docs_dir / 'cache' / (source_id + '.source.json')
        if not rec_path.exists():
            continue
        rec = json.loads(rec_path.read_text())
        if rec.get('status') != 'ok':
            continue
        meta = json.loads((docs_dir / rec['cache_path']).read_text())
        col = next((c for c in meta.get('columns', []) if c.get('fieldName') == field_name), None)
        mapping_evidence[field] = {
            'field': field_name,
            'official_description': col.get('description') if col else None,
            'dataset_name': meta.get('name'),
            'dataset_vintage': rec.get('source_updated_at'),
            'mapping_dataset': '7isb-wh4c (ACRIS - Document Control Codes)',
        }
    docs = {'fetched_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'receipts': receipts, 'mapping_evidence': mapping_evidence,
            'budget': budget.snapshot()}
    (docs_dir / 'docs.json').write_text(json.dumps(docs, indent=2, sort_keys=True) + '\n')
    return docs


def discover_address(borough, address, out_dir, session=None, budget=None, fetcher=None):
    """PLUTO address lookup for parcel selection. Writes a receipt and a
    discovery JSON with candidate BBLs. Charged to the session budget."""
    slug = re.sub(r'[^a-z0-9]+', '_', '%s_%s' % (borough, address)).strip('_')
    source = {'source_id': 'pluto_discover_%s' % slug,
              'url': soql_url(PLUTO, "borocode='%s' AND address like '%s%%'" % (borough, address), limit=20),
              'publisher': 'NYC Department of City Planning', 'limits': LIMITS_PLUTO, 'terms': TERMS}
    out_dir = pathlib.Path(out_dir)
    (out_dir / 'cache').mkdir(parents=True, exist_ok=True)
    budget = budget or Budget()
    fetcher = fetcher or make_fetcher(session=session)
    budget.start()
    record = fetcher(source, budget, out_dir)
    rows = []
    if record.get('status') == 'ok':
        rows = json.loads((out_dir / record['cache_path']).read_text())
    candidates = [{'bbl': r.get('bbl'), 'address': r.get('address'), 'owner1': r.get('owner1'),
                   'lotarea': r.get('lotarea'), 'zoningdist': r.get('zoningdist')} for r in rows]
    result = {'borough': borough, 'address': address, 'status': record.get('status'),
              'candidates': candidates, 'budget': budget.snapshot(),
              'receipt_source_id': source['source_id']}
    (out_dir / ('discovery-%s.json' % slug)).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    return result


def build_package(run_dir):
    """Assemble the evidence package from a run directory. Pure and deterministic."""
    run_dir = pathlib.Path(run_dir)
    run = json.loads((run_dir / 'run.json').read_text())
    bbl = run['bbl']
    borough, block, lot = parse_bbl(bbl)
    sources, records, unknowns, conflicts = [], [], [], []
    unknown_keys = set()

    def add_unknown(kind, description, key=None):
        key = key or kind
        if key in unknown_keys:
            return
        unknown_keys.add(key)
        n = len([u for u in unknowns if u['kind'] == kind])
        unknowns.append({'id': 'unknown.%s.%d' % (kind, n), 'kind': kind, 'description': description})

    for source_id in ('pluto_%s' % bbl, 'acris_legal_%s' % bbl, 'acris_master_%s' % bbl,
                      'acris_parties_%s' % bbl, 'dof_sales_%s' % bbl, 'acris_doc_codes'):
        record, rows = _load_rows(run_dir, source_id)
        if record is None:
            add_unknown('source_missing', 'No source record for %s; it was not fetched in this run.' % source_id)
            continue
        entry = {k: record.get(k) for k in
                 ('id', 'url', 'publisher', 'retrieved_at', 'status', 'http_status',
                  'content_type', 'last_modified', 'cache_path', 'bytes', 'sha256',
                  'coverage_limits', 'terms_url', 'error')}
        if rows is not None:
            limit = _query_limit(record.get('url'))
            entry['row_count'] = len(rows)
            entry['limit'] = limit
            entry['possibly_truncated'] = bool(limit is not None and len(rows) >= limit)
        sources.append(entry)
        if rows is None:
            add_unknown('source_failed', 'Source %s did not return ok status: %s'
                        % (source_id, record.get('error') or record.get('status')))

    codes_record, codes_rows = _load_rows(run_dir, 'acris_doc_codes')
    code_map = {}
    if codes_rows:
        for i, row in enumerate(codes_rows):
            code = (row.get('doc__type') or '').strip().upper()
            if code:
                code_map.setdefault(code, (i, row))
    mapping_available = bool(codes_rows)
    if not mapping_available:
        add_unknown('doc_codes_missing',
                    'ACRIS Document Control Codes source not ok in this run; instrument families use the '
                    'flagged keyword fallback and party roles are not identified.')

    pluto_record, pluto_rows = _load_rows(run_dir, 'pluto_%s' % bbl)
    pluto_row = pluto_rows[0] if pluto_rows else None
    if pluto_row is None:
        if pluto_rows is not None:
            add_unknown('pluto_empty',
                        'PLUTO returned an empty successful result for BBL %s in this run; absence is not proof '
                        'the parcel is unmapped.' % bbl)
        else:
            add_unknown('pluto_missing',
                        'No usable PLUTO source for BBL %s in this run (not fetched or failed); parcel identity '
                        'is not established.' % bbl)
    else:
        pluto_fields = ('bbl', 'bin', 'address', 'ownername', 'zonedist1', 'lotarea',
                        'appbbl', 'condono', 'unitsres', 'numfloors', 'bldgclass')
        records.append({'record_id': 'pluto:%s' % bbl, 'kind': 'parcel_identity',
                        'fields': {k: pluto_row.get(k) for k in pluto_fields},
                        'owner_label_note': ('ownername is a tax-roll label from the current PLUTO extract; it is '
                                             'not legal ownership and not a current-owner conclusion.'),
                        'locators': [_locator('pluto_%s' % bbl, 0, list(pluto_fields))]})

    legal_record, legal_rows = _load_rows(run_dir, 'acris_legal_%s' % bbl)
    if legal_rows is None:
        # Source failed or was not fetched; source_failed/source_missing
        # unknowns are already recorded. Unavailable evidence is not an empty
        # successful result.
        legal_rows = []
    elif not legal_rows:
        add_unknown('acris_empty', 'ACRIS legals returned an empty successful result for BBL %s in the dataset '
                                   'window (1966 onward, Staten Island excluded); absence is not proof of no '
                                   'records.' % bbl)
    master_record, master_rows = _load_rows(run_dir, 'acris_master_%s' % bbl)
    master_by_id = {row.get('document_id'): (i, row) for i, row in enumerate(master_rows or [])}
    parties_record, parties_rows = _load_rows(run_dir, 'acris_parties_%s' % bbl)
    parties_by_id = {}
    for i, row in enumerate(parties_rows or []):
        parties_by_id.setdefault(row.get('document_id'), []).append((i, row))

    other_parcels = {}
    latest_deed = None
    latest_doc = None
    doc_dates = []
    recorded_grantees = []

    for i, lrow in enumerate(legal_rows):
        doc_id = lrow.get('document_id')
        m_idx, mrow = master_by_id.get(doc_id, (None, None))
        p_rows = parties_by_id.get(doc_id, [])
        code_idx, crow = (None, None)
        if mrow is not None:
            code_idx, crow = code_map.get((mrow.get('doc_type') or '').strip().upper(), (None, None))
        if mrow is None:
            family, basis = 'unclassified', None
            add_unknown('master_missing',
                        'ACRIS legal row for document_id %s has no master row in this run.' % doc_id,
                        key='master_missing:%s' % doc_id)
        elif mapping_available and crow is None:
            family, basis = 'unclassified', 'acris_control_codes'
            add_unknown('doc_type_unmapped',
                        'ACRIS doc_type code %r for document_id %s is not in the Document Control Codes '
                        'dataset in this run.' % (mrow.get('doc_type'), doc_id),
                        key='doc_type_unmapped:%s' % doc_id)
        elif mapping_available:
            family = CLASS_FAMILY.get((crow.get('class_code_description') or '').strip(), 'other')
            basis = 'acris_control_codes'
        else:
            family, basis = classify_doc_type(mrow.get('doc_type')), 'keyword_fallback'
        party_roles = {}
        if crow is not None:
            for n in (1, 2, 3):
                role = (crow.get('party%d_type' % n) or '').strip()
                if role and role.upper() not in PARTY_PLACEHOLDERS:
                    party_roles[str(n)] = role
        if not p_rows:
            add_unknown('parties_missing',
                        'No ACRIS parties rows for document_id %s in this run.' % doc_id,
                        key='parties_missing:%s' % doc_id)
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
        if crow is not None:
            locators.append(_locator('acris_doc_codes', code_idx,
                                     [f for f in ('doc__type', 'doc__type_description', 'class_code_description') if f in crow]))
        party_entries = []
        for i2, prow in p_rows:
            pt = str(prow.get('party_type') or '').strip()
            role = party_roles.get(pt)
            if role is None:
                if pt in ('1', '2', '3'):
                    add_unknown('party_role_unspecified',
                                'Document %s: control-codes party slot %s has no specific role (placeholder or '
                                'absent); party name preserved without a role.' % (doc_id, pt),
                                key='party_role_unspecified:%s:%s' % (doc_id, pt))
                else:
                    add_unknown('party_role_unmapped',
                                'Document %s: parties row party_type code %r is not a 1-3 slot; role not identified.'
                                % (doc_id, pt),
                                key='party_role_unmapped:%s:%s' % (doc_id, pt))
            entry = {'name': prow.get('name'), 'party_type': pt, 'role': role,
                     'locator': _locator('acris_parties_%s' % bbl, i2, list(prow.keys()))}
            party_entries.append(entry)
            locators.append(entry['locator'])
            if family == 'deed' and role and 'GRANTEE' in role.upper() and prow.get('name'):
                recorded_grantees.append({'name': prow.get('name'), 'document_id': doc_id,
                                          'document_date': mrow.get('document_date') if mrow else None,
                                          'role': role,
                                          'locators': [entry['locator'],
                                                       _locator('acris_doc_codes', code_idx,
                                                                [f for f in ('doc__type', 'party1_type',
                                                                             'party2_type', 'party3_type') if f in crow])]})
        if p_rows:
            raw['parties'] = [row for _, row in p_rows]
        record = {'record_id': 'acris:%s' % doc_id, 'kind': 'recorded_instrument',
                  'instrument_family': family, 'classification_basis': basis,
                  'doc_type_raw': mrow.get('doc_type') if mrow else None,
                  'doc_type_description': crow.get('doc__type_description') if crow else None,
                  'doc_class': crow.get('class_code_description') if crow else None,
                  'dates': dates,
                  'instrument_amount': mrow.get('document_amt') if mrow else None,
                  'instrument_amount_note': ('Recorded instrument amount from ACRIS master; not a sale price.'
                                             if mrow else None),
                  'parties': party_entries, 'parcels': parcels, 'locators': locators, 'raw': raw}
        records.append(record)
        if mrow and mrow.get('document_date'):
            doc_dates.append(mrow['document_date'])
            if latest_doc is None or mrow['document_date'] > latest_doc:
                latest_doc = mrow['document_date']
        if family == 'deed' and mrow and mrow.get('document_date'):
            if latest_deed is None or mrow['document_date'] > latest_deed['document_date']:
                latest_deed = mrow
                latest_deed['_doc_id'] = doc_id
                latest_deed['_grantee'] = next((e['name'] for e in party_entries
                                                if e['role'] and 'GRANTEE' in e['role'].upper()), None)

    sales_record, sales_rows = _load_rows(run_dir, 'dof_sales_%s' % bbl)
    unit_sales = 0
    for i, srow in enumerate(sales_rows or []):
        raw_bbl = None
        if srow.get('borough') and srow.get('block') and srow.get('lot'):
            try:
                raw_bbl = bbl_from_parts(srow.get('borough'), srow.get('block'), srow.get('lot'))
            except ValueError:
                raw_bbl = None
        unit = srow.get('apartment_number')
        scope = 'unit' if (unit or (raw_bbl is not None and raw_bbl != bbl)) else 'parcel'
        if scope == 'unit':
            unit_sales += 1
        records.append({'record_id': 'dof_sales:%s:%d' % (bbl, i), 'kind': 'sale',
                        'scope': scope,
                        'unit': unit,
                        'raw_bbl': raw_bbl,
                        'raw': srow,
                        'fields': {k: srow.get(k) for k in
                                   ('bbl', 'bin', 'borough', 'block', 'lot', 'apartment_number', 'address',
                                    'sale_date', 'sale_price', 'building_class_category')},
                        'sale_price_note': ('Reported sale price for the scoped unit/parcel; a reported price, '
                                            'never an instrument amount.'),
                        'locators': [_locator('dof_sales_%s' % bbl, i, sorted(srow.keys()))]})
    if unit_sales:
        add_unknown('unit_sales_scope',
                    '%d of %d DOF sales rows are unit-level (condo) sales: their block/lot identify the unit lot, '
                    'not the mapped parcel lot %s. They are associated with the condo billing/map BBL %s and are '
                    'not whole-property sales of the mapped parcel; they are not aggregated or corroborated as '
                    'whole-property sales.' % (unit_sales, len(sales_rows or []), lot, bbl),
                    key='unit_sales_scope')
    if sales_rows is not None and not sales_rows:
        add_unknown('sales_empty', 'DOF sales returned an empty successful result for BBL %s in the dataset '
                                   'window; absence is not proof of no sale.' % bbl)

    if pluto_row and latest_deed and latest_deed.get('_grantee'):
        pluto_owner = _norm_name(pluto_row.get('ownername'))
        grantee = _norm_name(latest_deed.get('_grantee'))
        if pluto_owner and grantee and pluto_owner != grantee:
            conflicts.append({'id': 'conflict.owner_label', 'kind': 'owner_label_mismatch',
                              'description': 'PLUTO tax-roll owner label %r differs from recorded grantee of latest '
                                             'deed (%s) %r. Tax-roll label and deed party are not reconciled; neither '
                                             'establishes current ownership.'
                                             % (pluto_row.get('ownername'), latest_deed.get('_doc_id'),
                                                latest_deed.get('_grantee')),
                              'evidence': [_locator('pluto_%s' % bbl, 0, ['ownername']),
                                           _locator('acris_master_%s' % bbl,
                                                    master_by_id.get(latest_deed['_doc_id'], (None, None))[0],
                                                    ['document_date'])]})
    if latest_doc:
        add_unknown('coverage',
                    'Latest ACRIS document date in this run is %s; no evidence of instruments recorded after '
                    'that date, and good_through dates vary by record.' % latest_doc)

    retrieved = sorted(s.get('retrieved_at') for s in sources if s.get('retrieved_at'))
    date_bounds = {
        'earliest_document_date': min(doc_dates) if doc_dates else None,
        'latest_document_date': max(doc_dates) if doc_dates else None,
        'retrieved_at_range': [retrieved[0], retrieved[-1]] if retrieved else None,
        'dataset_last_modified': {s['id']: s['last_modified'] for s in sources if s.get('last_modified')},
    }
    ownership_evidence = {
        'recorded_grantees': recorded_grantees,
        'current_owner': {'status': 'unknown',
                          'reason': ('A defensible current-owner conclusion requires a complete chain of title from '
                                     'the latest recorded conveyance to the present, including unrecorded interests, '
                                     'liens, corrections and any post-recording transfers. This package contains '
                                     'index rows only and does not perform that research; the recorded grantee '
                                     'evidence above is not a current-owner conclusion.')},
    }
    mapping_provenance = None
    if codes_record is not None:
        mapping_provenance = {
            'mapping_source': 'NYC Open Data: ACRIS - Document Control Codes (7isb-wh4c), published by NYC DOF',
            'receipt': codes_record.get('cache_path'),
            'url': codes_record.get('url'),
            'retrieved_at': codes_record.get('retrieved_at'),
            'sha256': codes_record.get('sha256'),
            'fields': {'doc_type': 'doc__type -> doc__type_description, class_code_description',
                       'party_role': 'parties.party_type N -> partyN_type of the doc__type row'},
            'class_family_derivation': CLASS_FAMILY,
        }

    records.sort(key=lambda r: r['record_id'])
    package = {'package_version': '0.3', 'parcel': {'bbl': bbl, 'borough': borough, 'block': block, 'lot': lot},
               'run_id': run['run_id'], 'run_status': run['status'], 'budget': run['budget'],
               'sources': sources, 'records': records,
               'other_parcels': [other_parcels[k] for k in sorted(other_parcels)],
               'conflicts': conflicts, 'unknowns': unknowns,
               'ownership_evidence': ownership_evidence, 'date_bounds': date_bounds,
               'mapping_provenance': mapping_provenance,
               'limitations': list(NON_CLAIMS), 'non_claims': list(NON_CLAIMS)}
    return package


def write_package(run_dir):
    run_dir = pathlib.Path(run_dir)
    package = build_package(run_dir)
    (run_dir / 'package.json').write_text(json.dumps(package, indent=2, sort_keys=True) + '\n')
    return package


def main(argv=None):
    parser = argparse.ArgumentParser(description='Collect bounded parcel ownership/transaction evidence.')
    parser.add_argument('--bbl', help='10-digit BBL to collect')
    parser.add_argument('--replay', help='Rebuild the package from an existing run (no requests, no writes)')
    parser.add_argument('--collect-docs', action='store_true',
                        help='Fetch ACRIS mapping documentation receipts into <out>/docs')
    parser.add_argument('--discover-address', help='PLUTO address lookup for parcel selection')
    parser.add_argument('--borough', default='2', help='Borough for --discover-address (1-5)')
    parser.add_argument('--out', default=str(ROOT / 'runs'), help='Runs root directory')
    parser.add_argument('--run-id', help='Run directory name (default: timestamped)')
    parser.add_argument('--session-budget',
                        help='Path to a shared session budget file (documentation + discovery + runs)')
    parser.add_argument('--budget-requests', type=int, default=BUDGET_DEFAULTS['max_requests'])
    parser.add_argument('--budget-bytes', type=int, default=BUDGET_DEFAULTS['max_bytes'])
    parser.add_argument('--budget-seconds', type=int, default=BUDGET_DEFAULTS['max_seconds'])
    args = parser.parse_args(argv)
    if args.replay:
        package = build_package(pathlib.Path(args.replay))
        print(json.dumps({'run_id': package['run_id'], 'run_status': package['run_status'],
                          'records': len(package['records']), 'conflicts': len(package['conflicts']),
                          'unknowns': len(package['unknowns'])}))
        return 0
    session = None
    if args.session_budget:
        session = SessionBudget(args.session_budget, args.budget_requests, args.budget_bytes,
                                args.budget_seconds)
    if args.collect_docs:
        docs_dir = pathlib.Path(args.out) / 'docs'
        budget = Budget(args.budget_requests, args.budget_bytes, args.budget_seconds)
        docs = collect_documentation(docs_dir, session=session, budget=budget)
        print(json.dumps({'docs_dir': str(docs_dir),
                          'receipts': sum(1 for r in docs['receipts'] if r.get('status') == 'ok'),
                          'failed': sum(1 for r in docs['receipts'] if r.get('status') != 'ok'),
                          'session': session.snapshot() if session else None}))
        return 0
    if args.discover_address:
        out_dir = pathlib.Path(args.out) / 'discovery'
        budget = Budget(args.budget_requests, args.budget_bytes, args.budget_seconds)
        result = discover_address(args.borough, args.discover_address, out_dir, session=session, budget=budget)
        print(json.dumps(result))
        return 0
    if not args.bbl:
        parser.error('one of --bbl, --replay, --collect-docs or --discover-address is required')
    parse_bbl(args.bbl)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    run_id = args.run_id or ('run-%s-%s' % (stamp, args.bbl))
    run_dir = pathlib.Path(args.out) / run_id
    if run_dir.exists():
        raise SystemExit('run directory already exists: %s' % run_dir)
    budget = Budget(args.budget_requests, args.budget_bytes, args.budget_seconds)
    fetcher = make_fetcher(session=session)
    run, _ = run_collection(args.bbl, run_dir, budget=budget, fetcher=fetcher)
    package = write_package(run_dir)
    print(json.dumps({'run_id': run_id, 'status': run['status'], 'budget': run['budget'],
                      'session': session.snapshot() if session else None,
                      'records': len(package['records']), 'other_parcels': len(package['other_parcels']),
                      'conflicts': len(package['conflicts']), 'unknowns': len(package['unknowns'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
