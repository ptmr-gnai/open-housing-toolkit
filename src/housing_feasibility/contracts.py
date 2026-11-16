"""Report request and report shape checks (standard library). MIT."""
import re

REQUEST_KEYS = {'version', 'title', 'base_case', 'prepared_on', 'prepared_by'}
REPORT_KEYS = {'version', 'module', 'request', 'brief', 'process', 'provenance', 'headline', 'site', 'search', 'ownership', 'zoning',
               'massing', 'development_budget', 'operating_pro_forma', 'debt_sizing', 'sensitivity',
               'program_reconciliation', 'render', 'open_items', 'sources', 'inputs', 'non_claims'}


def validate_request(req):
    if not isinstance(req, dict):
        raise ValueError('Report request must be a JSON object')
    missing, extra = REQUEST_KEYS - set(req), set(req) - REQUEST_KEYS
    if missing or extra:
        raise ValueError('Report request fields: missing %s, unexpected %s' % (sorted(missing), sorted(extra)))
    if req['version'] != '1.1':
        raise ValueError('Report request version must be "1.1" (the goal and persona now live in brief.json)')
    for key in ('title', 'base_case', 'prepared_by'):
        if not isinstance(req[key], str) or not req[key].strip() or len(req[key]) > 2000:
            raise ValueError(key + ' must be a non-empty string')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(req['prepared_on'])):
        raise ValueError('prepared_on must be a date like 2026-11-16')
    return req


def validate_report(report):
    if set(report) != REPORT_KEYS:
        raise ValueError('Report sections changed: ' + ', '.join(sorted(set(report) ^ REPORT_KEYS)))
    for key in ('brief', 'process', 'provenance', 'site', 'zoning', 'development_budget', 'operating_pro_forma', 'debt_sizing', 'sensitivity', 'headline'):
        if not isinstance(report[key], dict):
            raise ValueError('Missing required section: ' + key)
    for key in ('massing', 'open_items', 'sources', 'inputs', 'program_reconciliation'):
        if not isinstance(report[key], list):
            raise ValueError('Section must be a list: ' + key)
    return report
