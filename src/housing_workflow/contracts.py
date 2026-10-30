"""Typed records and bounded input contracts. MIT."""
from dataclasses import asdict, dataclass, field
from enum import Enum
import hashlib
import json
import math
import re
from typing import Any

class Kind(str, Enum):
    FACT = 'fact'
    ASSUMPTION = 'assumption'
    CALCULATION = 'calculation'
    JUDGMENT = 'judgment'
    UNKNOWN = 'unknown'

@dataclass
class Claim:
    id: str
    kind: Kind
    label: str
    value: Any
    unit: str
    inputs: list[str] = field(default_factory=list)
    references: list[dict] = field(default_factory=list)
    formula: str | None = None
    rationale: str | None = None

    def to_dict(self):
        d = asdict(self)
        d['kind'] = self.kind.value
        return d

def dumps(value):
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + '\n'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def save(path, value):
    path.write_text(dumps(value))

def load(path):
    return json.loads(path.read_text())

def bbl(value):
    if not isinstance(value, str) or not re.fullmatch(r'2[0-9]{9}', value):
        raise ValueError('This slice needs a 10-digit Bronx BBL beginning with 2.')
    return value

def validate_request(req):
    if not isinstance(req, dict) or set(req) - {'version', 'bbl', 'address', 'question', 'scenario'}:
        raise ValueError('Unsupported request field or request type')
    if req.get('version') != '0.2.0':
        raise ValueError('Unsupported request version')
    if bool(req.get('bbl')) == bool(req.get('address')):
        raise ValueError('Supply exactly one of bbl or address.')
    if req.get('bbl'): bbl(req['bbl'])
    if req.get('address') and (not isinstance(req['address'], str) or not 3 <= len(req['address']) <= 160):
        raise ValueError('Address must be a Bronx street address, 3–160 characters.')
    if not isinstance(req.get('question'), str) or not req['question'].strip() or len(req['question']) > 2000:
        raise ValueError('Provide the decision/question this packet should support.')
    scenario = req.get('scenario')
    if scenario is not None:
        if not isinstance(scenario, dict) or set(scenario) != {'name', 'gross_area_sf', 'nonresidential_gross_sf', 'residential_net_efficiency', 'average_net_home_sf'}:
            raise ValueError('Scenario must provide exactly the named area-budget inputs.')
        if not isinstance(scenario['name'], str) or not scenario['name'].strip():
            raise ValueError('Name the scenario.')
        for k in ['gross_area_sf', 'nonresidential_gross_sf', 'residential_net_efficiency', 'average_net_home_sf']:
            item = scenario[k]
            if not isinstance(item, dict) or set(item) != {'value', 'rationale'}:
                raise ValueError('Each scenario input needs value and rationale: ' + k)
            v = item['value']
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
                raise ValueError('Finite numeric scenario input required: ' + k)
            if not isinstance(item['rationale'], str) or not item['rationale'].strip():
                raise ValueError('Explain scenario input: ' + k)
        s = {k:v['value'] for k,v in scenario.items() if k != 'name'}
        if not 0 < s['gross_area_sf'] <= 10_000_000 or not 0 <= s['nonresidential_gross_sf'] < s['gross_area_sf']:
            raise ValueError('Area allocation is inconsistent.')
        if not 0 < s['residential_net_efficiency'] <= 1 or not 0 < s['average_net_home_sf'] <= s['gross_area_sf']:
            raise ValueError('Efficiency or average home size is inconsistent.')
    return req
