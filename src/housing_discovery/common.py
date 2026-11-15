"""Strict input and immutable local package helpers. MIT."""
import hashlib
import json
import math
from pathlib import Path
from housing_common.local_outputs import ROOT, destination


def dumps(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False) + '\n'


def load(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    Path(path).write_text(dumps(value))


def digest(body):
    return hashlib.sha256(body).hexdigest()


def number(value):
    if value is None or value == '' or isinstance(value, bool):
        return None
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None


def bbl(value):
    n = number(value)
    if n is None or n != int(n) or not 1000000000 <= n < 6000000000:
        raise ValueError('Invalid BBL')
    return str(int(n))


def keys(obj, expected, label):
    if not isinstance(obj, dict) or set(obj) != set(expected):
        raise ValueError('Unknown or missing ' + label + ' fields')


def validate_request(req):
    keys(req, ['version', 'id', 'question', 'scope', 'scenario', 'selection'], 'request')
    if req['version'] != '1.0' or not isinstance(req['id'], str) or not req['id'].strip():
        raise ValueError('Unsupported discovery request')
    if not isinstance(req['question'], str) or not req['question'].strip():
        raise ValueError('Question required')
    scope = req['scope']
    keys(scope, ['borough', 'bbox'], 'scope')
    if scope['borough'] not in ['BX', 'BK', 'MN', 'QN', 'SI']:
        raise ValueError('Unsupported borough')
    if not isinstance(scope['bbox'], list) or len(scope['bbox']) != 4:
        raise ValueError('bbox must be [west,south,east,north]')
    w, s, e, n = scope['bbox']
    if any(type(x) not in [int, float] or not math.isfinite(x) for x in [w,s,e,n]):
        raise ValueError('Finite bbox numbers required')
    if not (-74.3 <= w < e <= -73.6 and 40.45 <= s < n <= 41.0 and e-w <= .1 and n-s <= .1):
        raise ValueError('Use a bounded NYC bbox (maximum .1 degree per side)')
    sc = req['scenario']
    keys(sc, ['label', 'proposed_residential_far', 'gross_per_zoning_sf', 'residential_share', 'net_efficiency', 'net_sf_per_home_equivalent', 'rationale'], 'scenario')
    for name, upper in [('proposed_residential_far', 20), ('gross_per_zoning_sf', 2), ('residential_share',1), ('net_efficiency',1), ('net_sf_per_home_equivalent',3000)]:
        v = sc[name]
        if type(v) not in [int, float] or not math.isfinite(v) or not 0 < v <= upper:
            raise ValueError('Invalid scenario value: '+name)
    if not all(isinstance(sc[x],str) and sc[x].strip() for x in ['label','rationale']):
        raise ValueError('Scenario label and rationale required')
    sel = req['selection']
    keys(sel, ['min_lot_area_sf','max_lot_area_sf','min_additional_area_proxy_sf','max_recorded_residential_units','mission','hold_active_applications','top_n'], 'selection')
    for key in ['min_lot_area_sf','max_lot_area_sf','min_additional_area_proxy_sf']:
        if type(sel[key]) not in [int,float] or not math.isfinite(sel[key]) or sel[key] < 0:
            raise ValueError('Invalid selection threshold: '+key)
    if sel['min_lot_area_sf'] > sel['max_lot_area_sf']:
        raise ValueError('Reversed area bounds')
    cap = sel['max_recorded_residential_units']
    if cap is not None and (type(cap) is not int or cap < 0):
        raise ValueError('Housing-unit threshold must be null or nonnegative integer')
    if sel['mission'] not in ['private_redevelopment','public_or_institutional_review','all_with_flags']:
        raise ValueError('Unsupported mission')
    if type(sel['hold_active_applications']) is not bool or type(sel['top_n']) is not int or not 1 <= sel['top_n'] <= 50:
        raise ValueError('Invalid pipeline policy or shortlist limit')
    return req


def fresh(path):
    path = destination(path)
    path.mkdir(parents=True, exist_ok=False)
    return path


def implementation(kind):
    module = Path(__file__).parent
    paths = ([module/name for name in ['__init__.py','common.py','collection.py','providers.json']]
             if kind == 'inventory' else sorted(module.glob('*.py')) + sorted(module.glob('*.json')))
    paths += [ROOT/'src/housing_common/local_outputs.py']
    skill = ROOT/'skills/discover-housing-sites/SKILL.md'
    if skill.exists() and kind != 'inventory':
        paths += [skill] + sorted((skill.parent/'references').glob('*.md'))
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def seal(folder, kind):
    files = {str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p != folder/'manifest.json'}
    save(folder/'manifest.json', {'version':'1.0.0','kind':kind,'implementation':implementation(kind),'files':files})


def verify_files(folder, kind):
    folder = Path(folder).resolve()
    m = load(folder/'manifest.json')
    if m['version'] != '1.0.0' or m['kind'] != kind or m['implementation'] != implementation(kind):
        raise ValueError('Unknown or changed discovery implementation')
    actual = {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual != set(m['files']) | {'manifest.json'}:
        raise ValueError('Package file inventory changed')
    for name, expected in m['files'].items():
        p = folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes()) != expected:
            raise ValueError('Changed or escaping package file: '+name)
    return m
