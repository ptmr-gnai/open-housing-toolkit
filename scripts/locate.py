#!/usr/bin/env python3
"""Turn plain place descriptions into toolkit inputs. MIT.

    .venv/bin/python scripts/locate.py lookup "1337 Jerome Ave, Bronx"
    .venv/bin/python scripts/locate.py area --station "170 St" --routes 4 --out runs/my-search/request.json
    .venv/bin/python scripts/locate.py area "1337 Jerome Ave, Bronx" --radius-m 400 --out ...
    .venv/bin/python scripts/locate.py area --lat 40.84 --lon -73.915 --borough BX --out ...

`lookup` resolves a street address or named place (not intersections or
neighborhoods) with NYC Planning's public GeoSearch service and prints the match,
borough and tax lot (BBL). `area` builds a lot-discovery request: a square around
an address, a subway station (MTA station list) or explicit coordinates, sized by
--radius-m. Matches are suggestions; confirm the printed place with the user.
Uses only the standard library; writes only the --out file (which must not exist).
"""
import argparse
import json
import math
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

GEOSEARCH = 'https://geosearch.planninglabs.nyc/v2/search'
STATIONS = 'https://data.ny.gov/resource/39hk-dx4f.json'
STATION_BOROUGHS = {'Bx': 'BX', 'Bk': 'BK', 'M': 'MN', 'Q': 'QN', 'SI': 'SI'}
BOROUGHS = {'Bronx': 'BX', 'Brooklyn': 'BK', 'Manhattan': 'MN', 'Queens': 'QN', 'Staten Island': 'SI'}
QUESTION = ('Which recorded nonhousing sites could support housing, and which general '
            'zoning path and follow-up questions apply?')


def search(text, size=5):
    url = GEOSEARCH + '?' + urllib.parse.urlencode({'text': text, 'size': size})
    req = urllib.request.Request(url, headers={'User-Agent': 'OpenHousingToolkit-Locate/1.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        features = json.load(response).get('features', [])
    matches = []
    for f in features:
        p = f.get('properties', {})
        lon, lat = f['geometry']['coordinates']
        bbl = ((p.get('addendum') or {}).get('pad') or {}).get('bbl')
        matches.append({'label': p.get('label'), 'borough': BOROUGHS.get(p.get('borough')),
                        'borough_name': p.get('borough'), 'bbl': bbl, 'lat': lat, 'lon': lon,
                        'confidence': p.get('confidence')})
    return matches


def stations(name, routes=None):
    words = name.upper().replace("'", "''")
    url = STATIONS + '?' + urllib.parse.urlencode({'$where': "upper(stop_name) like '%" + words + "%'", '$limit': 50})
    req = urllib.request.Request(url, headers={'User-Agent': 'OpenHousingToolkit-Locate/1.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        rows = json.load(response)
    found = []
    for r in rows:
        served = set((r.get('daytime_routes') or '').split())
        if routes and not set(routes.upper().split()) & served:
            continue
        found.append({'label': '%s station (%s), %s' % (r['stop_name'], r.get('daytime_routes', ''), r.get('borough')),
                      'borough': STATION_BOROUGHS.get(r.get('borough')), 'lat': float(r['gtfs_latitude']),
                      'lon': float(r['gtfs_longitude']), 'bbl': None})
    return found


def bbox(lat, lon, radius_m):
    dlat = radius_m / 111320.0
    dlon = radius_m / (111320.0 * math.cos(math.radians(lat)))
    return [round(lon - dlon, 6), round(lat - dlat, 6), round(lon + dlon, 6), round(lat + dlat, 6)]


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:60] or 'area'


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest='command', required=True)
    lk = sub.add_parser('lookup', help='resolve an address or place')
    lk.add_argument('text')
    ar = sub.add_parser('area', help='write a lot-discovery request around a place')
    ar.add_argument('text', nargs='?', help='street address or named place')
    ar.add_argument('--station', help='subway station name, e.g. "170 St"')
    ar.add_argument('--routes', help='narrow a station name by routes, e.g. "4" or "B D"')
    ar.add_argument('--lat', type=float)
    ar.add_argument('--lon', type=float)
    ar.add_argument('--borough', choices=sorted(set(BOROUGHS.values())))
    ar.add_argument('--radius-m', type=float, default=400,
                    help='half-width of the square in meters (default 400; 100-1500)')
    ar.add_argument('--question', default=QUESTION)
    ar.add_argument('--out', required=True, type=Path)
    a = ap.parse_args()

    if a.command == 'area' and a.station:
        matches = stations(a.station, a.routes)
        if len(matches) > 1:
            print(json.dumps({'status': 'ambiguous', 'options': [m['label'] for m in matches],
                              'hint': 'Add --routes with the lines serving the intended station.'}, indent=2))
            return 1
    elif a.command == 'area' and a.lat is not None:
        if a.lon is None or not a.borough:
            raise ValueError('--lat needs --lon and --borough.')
        matches = [{'label': 'point %.5f, %.5f' % (a.lat, a.lon), 'borough': a.borough,
                    'borough_name': a.borough, 'lat': a.lat, 'lon': a.lon, 'bbl': None}]
    elif a.text:
        matches = search(a.text)
    else:
        raise ValueError('Give an address/place, --station or --lat/--lon/--borough.')
    if not matches:
        print(json.dumps({'status': 'not_found', 'text': a.text,
                          'hint': 'Try a street address with borough, a subway station (--station) or coordinates.'}, indent=2))
        return 1
    if a.command == 'lookup':
        print(json.dumps({'status': 'ok', 'best': matches[0], 'alternatives': matches[1:]}, indent=2))
        return 0

    best = matches[0]
    if not best['borough']:
        raise ValueError('The best match is outside the five NYC boroughs: %s' % best['label'])
    if not 100 <= a.radius_m <= 1500:
        raise ValueError('Choose --radius-m between 100 and 1500 meters.')
    if a.out.exists():
        raise ValueError('Output already exists; choose a new path: %s' % a.out)
    request = {'version': '1.0', 'id': slug(best['label'] or 'area'), 'question': a.question,
               'scope': {'borough': best['borough'], 'bbox': bbox(best['lat'], best['lon'], a.radius_m)},
               'display_per_group': 5}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(request, indent=2) + '\n')
    print(json.dumps({'status': 'ok', 'center': best['label'], 'borough': best.get('borough_name', best['borough']),
                      'square_side_m': round(2 * a.radius_m), 'request': str(a.out),
                      'note': 'Lots are included when their recorded point falls inside the square.',
                      'alternatives': [m['label'] for m in matches[1:]]}, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': str(exc)}, indent=2))
        raise SystemExit(2)
