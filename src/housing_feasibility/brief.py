"""The run brief: the user's goal in their words, what they provided, every decision, and agent notes. MIT.

The agent starts it before any work and appends to it as the user decides things.
Entries are never edited; a changed mind is a new decision. The report reads it so
the goal and the path to the result are the user's, not the agent's paraphrase.

Every field has a size limit so the report stays readable. Anything that does not
fit (caveats, friction, ideas, concerns) goes in an agent note, which the report
prints in its own appendix.
"""
from datetime import date
from pathlib import Path
import json
import re

PERSONAS = {'housing_agency', 'developer', 'community', 'other'}
STEPS = ['search', 'activity', 'select', 'research', 'massing', 'financing', 'render', 'report', 'other']
NOTE_KINDS = {
    'friction': 'A command, guide or tool was unclear or failed',
    'data_issue': 'A source looked wrong, stale, missing or contradictory',
    'assumption_concern': 'An input or method the user should question',
    'idea': 'Something that would make this analysis or the toolkit better',
}
LIMITS = {'goal': 1000, 'provided_label': 40, 'provided_value': 160, 'proposed': 280, 'answer': 600,
          'note': 300, 'notes': 12}
OVERFLOW = ' Put anything longer in an agent note: housing_feasibility brief note --kind ... --text ...'


def _text(value, name, limit):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('%s must be non-empty text' % name)
    if len(value) > limit:
        raise ValueError('%s is %d characters; the limit is %d.%s' % (name, len(value), limit, OVERFLOW))


def _steps(value):
    steps = [s.strip() for s in str(value).split(',') if s.strip()]
    if not steps or any(s not in STEPS for s in steps) or len(set(steps)) != len(steps):
        raise ValueError('step must be one or more of %s, comma-separated' % ', '.join(STEPS))
    return steps


def decision_steps(decision):
    return _steps(decision['step'])


def validate(brief):
    required = {'version', 'goal', 'persona', 'provided', 'decisions'}
    if not isinstance(brief, dict) or not required <= set(brief) or set(brief) - required - {'extends', 'notes'}:
        raise ValueError('Brief fields: version, goal, persona, provided, decisions (and optional extends, notes)')
    for item in brief.get('extends', []):
        if not isinstance(item, dict) or set(item) != {'title', 'evidence_fingerprint', 'prepared_on'}:
            raise ValueError('Each extends item needs title, evidence_fingerprint, prepared_on')
    if brief['version'] != '1.0':
        raise ValueError('Brief version must be "1.0"')
    _text(brief['goal'], 'goal', LIMITS['goal'])
    if brief['persona'] not in PERSONAS:
        raise ValueError('persona must be one of ' + ', '.join(sorted(PERSONAS)))
    for item in brief['provided']:
        if not isinstance(item, dict) or set(item) != {'label', 'value'}:
            raise ValueError('Each provided item needs label and value')
        _text(item['label'], 'provided label', LIMITS['provided_label'])
        _text(item['value'], 'provided value', LIMITS['provided_value'])
    for d in brief['decisions']:
        if not isinstance(d, dict) or set(d) != {'step', 'proposed', 'answer', 'decided_on'}:
            raise ValueError('Each decision needs step, proposed, answer, decided_on')
        _steps(d['step'])
        _text(d['proposed'], 'proposed', LIMITS['proposed'])
        _text(d['answer'], 'answer', LIMITS['answer'])
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d['decided_on'])):
            raise ValueError('decided_on must be a date like 2026-11-16')
    notes = brief.get('notes', [])
    if len(notes) > LIMITS['notes']:
        raise ValueError('At most %d agent notes; keep the ones a reviewer needs' % LIMITS['notes'])
    for n in notes:
        if not isinstance(n, dict) or set(n) != {'kind', 'step', 'text'}:
            raise ValueError('Each note needs kind, step, text')
        if n['kind'] not in NOTE_KINDS:
            raise ValueError('note kind must be one of ' + ', '.join(NOTE_KINDS))
        _steps(n['step'])
        _text(n['text'], 'note', LIMITS['note'])
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
    """One decision per user answer; an answer that covers several steps lists them all, e.g. massing,financing."""
    brief = _load(path)
    steps = ','.join(_steps(step))
    for d in brief['decisions']:
        if d['answer'] == answer and d['proposed'] == proposed:
            raise ValueError('This answer is already recorded; record one decision with several steps, e.g. --step massing,financing,render')
    brief['decisions'].append({'step': steps, 'proposed': proposed, 'answer': answer,
                               'decided_on': decided_on or date.today().isoformat()})
    _save(path, brief)
    return {'status': 'recorded', 'decisions': len(brief['decisions'])}


def note(path, kind, text, step='other'):
    """The agent's own outlet: friction, data issues, assumption concerns and ideas, printed in an appendix."""
    brief = _load(path)
    brief.setdefault('notes', []).append({'kind': kind, 'step': ','.join(_steps(step)), 'text': text})
    _save(path, brief)
    return {'status': 'recorded', 'notes': len(brief['notes'])}
