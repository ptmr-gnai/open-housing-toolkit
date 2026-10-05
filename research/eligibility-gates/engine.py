"""Small, closed requirement DSL. Matching evidence is not agency approval. MIT."""
import calendar
import datetime as dt
import hashlib
import json
import pathlib
import re
import jsonschema

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[1]
KINDS = {'all', 'any', 'eq', 'gte', 'in', 'within_years'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def norm(value):
    return ' '.join(value.split())


def local_file(name):
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Path escapes repository')
    return path


def compile_case(case, sources):
    """Reject bad provenance/rule types before evaluating any credential."""
    schema_file = BASE / 'schemas/gates.schema.json'
    try:
        jsonschema.Draft202012Validator(json.loads(schema_file.read_text())).validate(case)
    except jsonschema.ValidationError as error:
        raise ValueError('DSL schema: ' + error.message) from error
    dt.date.fromisoformat(case['cutoff'])
    docs = {d['id']: d for d in sources['sources']}
    ids = [g['id'] for g in case['gates']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate gate id')
    for doc in docs.values():
        if doc['case'] != case['id']:
            continue
        for file_key, hash_key in [('pdf', 'pdf_sha256'), ('text', 'text_sha256')]:
            if sha(local_file(doc[file_key]).read_bytes()) != doc[hash_key]:
                raise ValueError('Changed source bytes')
        if doc['issue_date'] > case['cutoff']:
            raise ValueError('Post-cutoff source')
        for key in ['pdf_creation', 'pdf_modified']:
            date = dt.datetime.strptime(doc[key], '%a %b %d %H:%M:%S %Y %Z').date()
            if date > dt.date.fromisoformat(case['cutoff']):
                raise ValueError('Post-cutoff PDF export')
    bound_values = {}
    for gate in case['gates']:
        if gate['kind'] not in {'experience', 'review'}:
            raise ValueError('Unsupported gate kind')
        if not gate['citations'] or not gate['owner'] or not gate['next_action']:
            raise ValueError('Untraced requirement or missing responsibility')
        for citation in gate['citations']:
            doc = docs[citation['source_id']]
            if doc['case'] != case['id']:
                raise ValueError('Cross-case source leakage')
            page = citation['pdf_page']
            if type(page) != int or not 1 <= page <= doc['pages']:
                raise ValueError('Invalid PDF page')
            text = local_file(doc['text']).read_text().split('\f')[page - 1]
            if len(norm(citation['quote'])) < 12 or norm(citation['quote']) not in norm(text):
                raise ValueError('Quote not on cited page')
        bindings = {}
        for binding in gate.get('bindings', []):
            quote = gate['citations'][binding['citation_index']]['quote']
            matches = list(re.finditer(binding['regex'], norm(quote)))
            if len(matches) != 1:
                raise ValueError('Ambiguous numeric binding')
            raw = matches[0].group(1)
            value = {'seven': 7}.get(raw, int(raw) if raw.isdigit() else None)
            if value is None or value != binding['value']:
                raise ValueError('Numeric rule disagrees with source')
            if binding['id'] in bindings:
                raise ValueError('Duplicate numeric binding')
            bindings[binding['id']] = value

        def check(expression):
            op = expression['op']
            if op not in KINDS:
                raise ValueError('Unknown DSL operator')
            if op in {'all', 'any'}:
                if not expression['args']:
                    raise ValueError('Empty Boolean expression')
                for child in expression['args']:
                    check(child)
                return
            if not isinstance(expression.get('field'), str):
                raise ValueError('Missing input field')
            if op in {'gte', 'within_years'}:
                if type(expression['value']) != int or expression['value'] < 1:
                    raise ValueError('Invalid numeric threshold')
                if bindings.get(expression.get('binding')) != expression['value']:
                    raise ValueError('Unbound numeric rule')
            if op == 'in' and not set(expression['values']).issubset(expression['domain']):
                raise ValueError('Rule enum outside declared domain')
        if gate['kind'] == 'experience':
            check(gate['where'])
            if gate['on_no_match'] not in {'fail', 'agency_review'}:
                raise ValueError('Unsupported no-match route')
            if gate['on_no_match'] == 'agency_review' and not gate.get('discretion_citation'):
                raise ValueError('Untraced discretion route')
            if gate.get('discretion_citation') not in [None, *range(len(gate['citations']))]:
                raise ValueError('Invalid discretion locator')
        bound_values[gate['id']] = bindings
    if set(case['coverage']['threshold_gate_ids']) != set(ids):
        raise ValueError('Missing gate in declared inventory')
    compiled = {'case': case, 'sources': [d for d in sources['sources'] if d['case'] == case['id']],
                'engine_sha256': sha(pathlib.Path(__file__).read_bytes()),
                'schema_sha256': sha(schema_file.read_bytes()),
                'release_policy_sha256': sha((BASE / 'check.py').read_bytes())}
    return {'case': case, 'fingerprint': fingerprint(compiled), 'bindings': bound_values}


def combine(op, values):
    if op == 'all':
        return False if False in values else None if None in values else True
    return True if True in values else None if None in values else False


def compare(expression, facts, cutoff):
    op = expression['op']
    if op in {'all', 'any'}:
        return combine(op, [compare(x, facts, cutoff) for x in expression['args']])
    value = facts.get(expression['field'])
    if value is None:
        return None
    if op == 'eq':
        expected = expression['value']
        if type(value) is not type(expected):
            raise ValueError('Wrong fact type')
        return value == expected
    if op == 'gte':
        if type(value) != int or value < 0:
            raise ValueError('Unit count must be a nonnegative integer')
        return value >= expression['value']
    if op == 'in':
        if not isinstance(value, str):
            raise ValueError('Wrong enum fact type')
        if value not in expression['domain']:
            raise ValueError('Unknown credential enum')
        return value in expression['values']
    if op == 'within_years':
        end = dt.date.fromisoformat(cutoff)
        date = dt.date.fromisoformat(value)
        year = end.year - expression['value']
        start = dt.date(year, end.month, min(end.day, calendar.monthrange(year, end.month)[1]))
        return start <= date <= end
    raise ValueError('Unknown DSL operator')


def evidence_review(item, compiled, profile):
    """Bind an attested review to facts, source bytes and exact rule version."""
    review = item.get('review', {})
    if review.get('status') != 'accepted':
        return False
    if not review.get('reviewer'):
        raise ValueError('Missing reviewer attribution')
    if review.get('requirements_fingerprint') != compiled['fingerprint']:
        raise ValueError('Stale credential review: rules changed')
    payload = {k: v for k, v in item.items() if k != 'review'}
    if review.get('payload_fingerprint') != fingerprint(payload):
        raise ValueError('Stale credential review: facts changed')
    evidence = item.get('evidence')
    if not evidence:
        raise ValueError('Reviewed credential has no evidence')
    raw = local_file(evidence['file']).read_bytes()
    if sha(raw) != evidence['sha256']:
        raise ValueError('Credential evidence changed')
    try:
        synthetic_content = json.loads(raw).get('artifact_kind') == 'synthetic_test_evidence'
    except (ValueError, AttributeError, UnicodeDecodeError):
        synthetic_content = False
    synthetic_path = 'fixtures' in pathlib.Path(evidence['file']).parts
    if (evidence['synthetic'] or synthetic_content or synthetic_path) and profile['kind'] != 'synthetic':
        raise ValueError('Synthetic credential cannot support actual profile')
    return True


def evaluate(compiled, profile):
    case = compiled['case']
    if profile['kind'] not in {'actual', 'synthetic'}:
        raise ValueError('Unknown profile kind')
    results = []
    for gate in case['gates']:
        witnesses = []
        base_status = 'unknown'
        reason = 'No accepted evidence supplied'
        if gate['kind'] == 'review':
            decision = profile.get('decisions', {}).get(gate['id'], {})
            if evidence_review(decision, compiled, profile):
                base_status = decision['verdict']
                if base_status not in {'pass', 'fail', 'unknown'}:
                    raise ValueError('Invalid review verdict')
                reason = 'Attested scoped review; agency judgment still separate'
        else:
            collection = profile.get('collections', {}).get(gate['collection'], {})
            values = []
            for item in collection.get('records', []):
                if not evidence_review(item, compiled, profile):
                    values.append(None)
                    continue
                verdict = compare(gate['where'], item['facts'], case['cutoff'])
                values.append(verdict)
                if verdict is True:
                    witnesses.append(item['id'])
            if True in values:
                base_status = 'pass'
                reason = 'Accepted evidence contains a matching witness'
            elif None not in values and collection.get('scope_complete') is True:
                scope = collection.get('scope_review', {})
                if evidence_review(scope, compiled, profile):
                    if scope.get('facts', {}).get('record_set_fingerprint') != fingerprint(collection.get('records', [])) or scope.get('facts', {}).get('complete') is not True:
                        raise ValueError('Scope review does not bind complete history')
                    base_status = 'fail'
                    reason = 'Accepted complete history contains no matching witness'
            else:
                reason = 'Incomplete history or unknown/unreviewed credential fields'
        status = base_status
        if gate.get('on_no_match') == 'agency_review' and base_status == 'fail':
            status = 'unknown'
            reason = 'Base criterion unmet; agency permits justified experience for review, not automatic acceptance'
        results.append({'id': gate['id'], 'label': gate['label'], 'status': status,
                        'base_status': base_status, 'reason': reason, 'witnesses': witnesses,
                        'owner': gate['owner'], 'next_action': gate['next_action'],
                        'citations': gate['citations']})
    blockers = [r['id'] for r in results if r['status'] != 'pass']
    if case['coverage']['full_submission_inventory_review'] != 'accepted':
        blockers.append('coverage.full_submission_inventory')
    if profile['kind'] == 'synthetic':
        blockers.append('synthetic_profile_not_actual_evidence')
    return {'case_id': case['id'], 'cutoff': case['cutoff'], 'profile_id': profile['id'],
            'profile_kind': profile['kind'], 'requirements_fingerprint': compiled['fingerprint'],
            'gates': results, 'submission_readiness_claim_allowed': not blockers,
            'blocking_gates': blockers, 'low_cost_exploration_allowed': True,
            'agency_approval': False,
            'limits': ['Attested review attribution is not authenticated by this prototype.',
                       'Exact quote and byte checks do not certify interpretation or completeness.',
                       'Historical inclusive seven-year window is an explicit analyst convention.',
                       'Agency retains discretion; this evaluates declared rules, not selection.']}
