"""The run brief: the user's goal in their words, what they provided, and every decision. MIT.

The agent starts it before any work and appends to it as the user decides things.
Entries are never edited; a changed mind is a new decision. The report reads it so
the goal and the path to the result are the user's, not the agent's paraphrase.
"""
from datetime import date
from pathlib import Path
import json
import re

PERSONAS = {'housing_agency', 'developer', 'community', 'other'}
STEPS = ['search', 'select', 'research', 'massing', 'financing', 'render', 'report', 'other']


def _text(value, name, limit=4000):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError('%s must be non-empty text' % name)


def validate(brief):
    required = {'version', 'goal', 'persona', 'provided', 'decisions'}
    if not isinstance(brief, dict) or not required <= set(brief) or set(brief) - required - {'extends'}:
        raise ValueError('Brief fields: version, goal, persona, provided, decisions (and optional extends)')
    for item in brief.get('extends', []):
        if not isinstance(item, dict) or set(item) != {'title', 'evidence_fingerprint', 'prepared_on'}:
            raise ValueError('Each extends item needs title, evidence_fingerprint, prepared_on')
    if brief['version'] != '1.0':
        raise ValueError('Brief version must be "1.0"')
    _text(brief['goal'], 'goal')
    if brief['persona'] not in PERSONAS:
        raise ValueError('persona must be one of ' + ', '.join(sorted(PERSONAS)))
    for item in brief['provided']:
        if not isinstance(item, dict) or set(item) != {'label', 'value'}:
            raise ValueError('Each provided item needs label and value')
        _text(item['label'], 'provided label', 200)
        _text(item['value'], 'provided value')
    for d in brief['decisions']:
        if not isinstance(d, dict) or set(d) != {'step', 'proposed', 'answer', 'decided_on'}:
            raise ValueError('Each decision needs step, proposed, answer, decided_on')
        if d['step'] not in STEPS:
            raise ValueError('step must be one of ' + ', '.join(STEPS))
        _text(d['proposed'], 'proposed')
        _text(d['answer'], 'answer')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d['decided_on'])):
            raise ValueError('decided_on must be a date like 2026-11-16')
    return brief


def _load(path):
    return validate(json.loads(Path(path).read_text()))


def _save(path, brief):
    validate(brief)
    Path(path).write_text(json.dumps(brief, indent=2, ensure_ascii=False) + '\n')


def start(out, goal, persona, provided=()):
    out = Path(out)
    if out.exists():
        raise ValueError('A brief already exists at %s; add to it instead' % out)
    out.parent.mkdir(parents=True, exist_ok=True)
    brief = {'version': '1.0', 'goal': goal, 'persona': persona,
             'provided': [_pair(p) for p in provided], 'decisions': []}
    _save(out, brief)
    return {'status': 'started', 'brief': str(out)}


def _pair(text):
    if '=' not in text:
        raise ValueError('Provided items look like "Label=value"')
    label, value = text.split('=', 1)
    return {'label': label.strip(), 'value': value.strip()}


def provide(path, items):
    brief = _load(path)
    brief['provided'] += [_pair(p) for p in items]
    _save(path, brief)
    return {'status': 'recorded', 'provided': len(brief['provided'])}


def decide(path, step, proposed, answer, decided_on=None):
    brief = _load(path)
    brief['decisions'].append({'step': step, 'proposed': proposed, 'answer': answer,
                               'decided_on': decided_on or date.today().isoformat()})
    _save(path, brief)
    return {'status': 'recorded', 'decisions': len(brief['decisions'])}
