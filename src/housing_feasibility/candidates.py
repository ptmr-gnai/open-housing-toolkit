"""Rank an area search's candidates for discussion. A browsing order, not a viability score. MIT."""
import csv
import json
from pathlib import Path

GOOD_CLASSES = ('K', 'G', 'E', 'F', 'V', 'O')
PUBLIC_LANES = {'public_or_institutional_use_review', 'park_or_recreation_review', 'infrastructure_review'}
METHOD = ('Privately used recorded-nonhousing lots with commercial, garage, industrial, office or vacant building '
          'classes and at least {min_lot} sf of lot area, sorted by unused recorded residential floor area '
          '((recorded residential FAR - built FAR) x lot area), then by straight-line distance to the nearest station. '
          'A browsing order for discussion, not viability, availability or a zoning finding.')


def _pluto_rows(folder):
    for inv in [folder / 'evidence/inventory/inventory.json'] + sorted(folder.parent.glob('*/inventory/inventory.json')):
        if inv.exists():
            rows = {}
            for rec in json.loads(inv.read_text())['records'].get('pluto', []):
                rows[str(rec['row'].get('bbl', '')).split('.')[0]] = rec['row']
            return rows
    return {}


def _f(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def rank(folder, min_lot_sf=5000, include_public=False):
    """Return (method, candidates) for a verified discovery package folder."""
    folder = Path(folder)
    pluto = _pluto_rows(folder)
    out = []
    with (folder / 'all-lots.csv').open(newline='') as handle:
        for r in csv.DictReader(handle):
            if r['current_use_category'] != 'recorded_nonhousing' or r['building_class'][:1] not in GOOD_CLASSES:
                continue
            lot = _f(r['recorded_lot_area_sf'])
            if lot < min_lot_sf or (r['review_lane'] in PUBLIC_LANES and not include_public):
                continue
            p = pluto.get(r['bbl'], {})
            built, far = _f(p.get('builtfar')), _f(r['recorded_residential_far'])
            unused = round(max(far - built, 0), 2)
            out.append({'bbl': r['bbl'], 'address': r['address'], 'building_class': r['building_class'],
                        'lot_area_sf': int(lot), 'existing_floors': _f(p.get('numfloors'), None),
                        'built_far': built, 'recorded_residential_far': far,
                        'recorded_affordable_residential_far': _f(r.get('recorded_affordable_residential_far'), None),
                        'unused_residential_far': unused, 'unused_residential_floor_area_sf': int(unused * lot),
                        'zoning_path': r['zoning_path'], 'review_lane': r['review_lane'],
                        'nearest_station': r['nearest_station_name'] or None,
                        'station_m': round(_f(r['nearest_station_straight_line_m'], 9999)),
                        'owner_label': r['recorded_owner_label'], 'flags': [f for f in r['flags'].split('; ') if f]})
    out.sort(key=lambda x: (-x['unused_residential_floor_area_sf'], x['station_m'], x['bbl']))
    for i, row in enumerate(out, 1):
        row['rank'] = i
    return METHOD.format(min_lot=int(min_lot_sf)), out
