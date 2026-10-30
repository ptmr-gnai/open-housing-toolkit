"""Local source router. Public allowlisted APIs only; no hosted proxy required. MIT."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from .contracts import bbl, digest, load, save

REGISTRY_PATH = Path(__file__).with_name('sources.json')
REGISTRY = load(REGISTRY_PATH)
LIMIT = 500
TERMS = 'https://opendata.cityofnewyork.us/overview/#termsofuse'

def url_for(source, where, limit=LIMIT + 1):
    definition = REGISTRY[source]
    query = {'$where':where, '$select':','.join(definition['fields']), '$order':definition['order'], '$limit':str(limit)}
    return 'https://data.cityofnewyork.us/resource/' + definition['dataset'] + '.json?' + urllib.parse.urlencode(query)

def parcel_url(source, parcel):
    parcel = bbl(parcel)
    where = 'bbl=' + (parcel if REGISTRY[source]['bbl_type'] == 'number' else "'" + parcel + "'")
    return url_for(source, where)

def address_url(address):
    address = ' '.join(address.upper().strip().split())
    substitutions = {'AVENUE':'AVE', 'STREET':'ST', 'HIGHWAY':'HWY', 'BOULEVARD':'BLVD', 'ROAD':'RD'}
    contracted = ' '.join(substitutions.get(w, w) for w in address.split())
    reverse = {v:k for k,v in substitutions.items()}
    expanded = ' '.join(reverse.get(w, w) for w in address.split())
    variants = sorted({address, contracted, expanded})
    literals = ','.join("'" + x.replace("'", "''") + "'" for x in variants)
    return url_for('pluto', "borough='BX' AND upper(address) IN (" + literals + ")", 2)

def request_bytes(url):
    request = urllib.request.Request(url, headers={'User-Agent':'OpenHousingToolkit/0.2 public-research'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(8_000_001)
            if len(data) > 8_000_000:
                raise ValueError('Response exceeded bounded byte budget')
            return response.status, data
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(8_000_000)

def fetch(source, url, folder, parcel=None, transport=request_bytes):
    folder.mkdir(parents=True, exist_ok=True)
    receipt = {'id':source, 'url':url, 'publisher':REGISTRY[source]['publisher'], 'catalog_url':REGISTRY[source]['catalog'], 'terms_url':TERMS,
               'retrieved_at':datetime.now(timezone.utc).isoformat(), 'limits':REGISTRY[source]['limits'], 'requested_bbl':parcel,
               'status':'failed', 'body_path':None, 'sha256':None, 'returned_rows':None, 'truncated':False}
    try:
        status, body = transport(url)
        path = folder / (source + '.json')
        path.write_bytes(body)
        receipt.update(http_status=status, body_path='sources/' + path.name, sha256=digest(body), bytes=len(body))
        data = json.loads(body)
        if status != 200 or not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError('Expected a successful JSON array of API records')
        if any(not row.get('bbl') for row in data):
            raise ValueError('Source row lacks parcel identity')
        if parcel and any(str(int(float(row['bbl']))) != parcel for row in data):
            raise ValueError('Source returned a different parcel')
        receipt.update(status='ok', returned_rows=len(data), truncated=len(data) > LIMIT)
    except (OSError, ValueError, TypeError, OverflowError) as exc:
        receipt['error'] = type(exc).__name__ + ': ' + str(exc)
    return receipt

def collect(req, out, transport=request_bytes):
    records = []
    parcel = req.get('bbl')
    if not parcel:
        receipt = fetch('pluto', address_url(req['address']), out / 'sources', transport=transport)
        receipt['id'] = 'address_resolution'
        # Preserve resolver separately; the parcel query must not overwrite its bytes.
        if receipt['body_path']:
            old = out / receipt['body_path']; new = old.with_name('address_resolution.json'); old.rename(new)
            receipt['body_path'] = 'sources/address_resolution.json'
        records.append(receipt)
        save(out / 'receipts.json', records)
        rows = load(out / receipt['body_path']) if receipt['status'] == 'ok' else []
        if len(rows) != 1:
            raise ValueError('Address resolution failed or is ambiguous. Supply the Bronx BBL; resolver receipt saved.')
        parcel = bbl(str(int(float(rows[0]['bbl']))))
    def one(source):return fetch(source, parcel_url(source, parcel), out / 'sources', parcel, transport)
    with ThreadPoolExecutor(max_workers=4) as pool:
        records.extend(pool.map(one, REGISTRY))
    save(out / 'receipts.json', records)
    return parcel, records
