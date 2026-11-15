"""Reuse a verified lot inventory; collect all available recorded zoning fields. MIT."""
from pathlib import Path
import shutil
from housing_discovery import collection
from .common import bbl, digest, fresh, load, number, save, seal, transport_request, validate_request, verify_files

FIELDS=['bbl','borough','version','address','bldgclass','landuse','unitsres','resarea',
        'zonedist1','zonedist2','zonedist3','zonedist4','overlay1','overlay2',
        'spdist1','spdist2','spdist3','splitzone','ltdheight','zonemap','zoningdate',
        'residfar','affresfar','bldgarea','lotarea','ownername','ownertype',
        'transitzone','mih_opt1','mih_opt2','mih_opt3','mih_opt4','latitude','longitude']
COMPARE=['borough','version','address','bldgclass','landuse','unitsres','zonedist1','zonedist2',
         'spdist1','splitzone','residfar','affresfar','lotarea','ownername','transitzone','latitude','longitude']
NUMERIC={'unitsres','residfar','affresfar','lotarea','latitude','longitude'}
CHUNK=100


def queries(ids):
    return [{'$select':','.join(FIELDS),'$where':'bbl in ('+','.join(ids[i:i+CHUNK])+')',
             '$order':'bbl','$limit':'101'} for i in range(0,len(ids),CHUNK)]


def metadata_ok(meta):
    fields={x.get('fieldName'):x.get('dataTypeName') for x in meta.get('columns',[])}
    return set(FIELDS)<=set(fields) and fields.get('bbl')=='number'


def derive(folder):
    folder=Path(folder);inv=load(folder/'inventory/inventory.json')
    req=validate_request(load(folder/'request.json'))
    if inv['scope']!=req['scope']:raise ValueError('Inventory geography differs from request')
    original={bbl(x['row']['bbl']):x for x in inv['records']['pluto']};ids=list(original)
    receipts=load(folder/'receipts.json')
    if [r['id'] for r in receipts]!=[str(i) for i in range(len(receipts))]:raise ValueError('Duplicate or missing receipt ids')
    if [r['params'] for r in receipts]!=[None]+queries(ids)+[None]:raise ValueError('Zoning supplement does not cover the exact inventory')
    rows={};metas=[];failed=[]
    for receipt in receipts:
        if receipt['provider']!='pluto' or not collection.same_query(receipt['url'],collection.url('pluto',receipt['params'])):
            raise ValueError('Non-allowlisted zoning supplement query')
        if 'body_path' in receipt:
            if receipt['body_path']!=f'sources/{receipt["id"]}-pluto.json':raise ValueError('Unexpected body path')
            body=(folder/receipt['body_path']).read_bytes()
            if digest(body)!=receipt['sha256'] or len(body)!=receipt['bytes']:raise ValueError('Supplement bytes differ from receipt')
        if receipt['status']!='ok':failed.append(receipt['id']);continue
        data=load(folder/receipt['body_path'])
        if receipt['params'] is None:
            if not isinstance(data,dict) or not metadata_ok(data):raise ValueError('Required recorded zoning fields unavailable')
            metas.append(data);continue
        if not isinstance(data,list) or len(data)>=101:raise ValueError('Supplement is malformed or truncated')
        requested=receipt['params']['$where'][8:-1].split(',')
        for index,row in enumerate(data):
            identity=bbl(row['bbl'])
            if identity not in requested or identity in rows:raise ValueError('Unexpected or duplicate supplement lot')
            changes=[]
            for key in COMPARE:
                left,right=original[identity]['row'].get(key),row.get(key)
                if (number(left)!=number(right) if key in NUMERIC else left!=right):changes.append(key)
            rows[identity]={'row':row,'changed_since_inventory':changes,
                            'reference':{'body_path':receipt['body_path'],'pointer':'/'+str(index),
                                         'receipt_id':receipt['id'],'sha256':receipt['sha256']}}
    stable=len(metas)==2 and metas[0].get('rowsUpdatedAt')==metas[1].get('rowsUpdatedAt')
    return {'version':'1.0','scope':inv['scope'],'primary_complete':inv['primary_complete'],
            'returned_lots':len(rows),'missing_bbls':sorted(set(ids)-set(rows)),
            'complete':not failed and stable and len(rows)==len(original),
            'metadata_stable':stable,'failed_receipts':failed,
            'map_coverage':'Recorded PLUTO zoning fields only; no fresh parcel-polygon/zoning-polygon intersection. Official map, sub-10%-area pieces and applicable text remain review items.',
            'records':rows}


def _enrich(req,inventory,out,ca_file):
    save(out/'request.json',req)
    if Path(inventory).resolve()!= (out/'inventory').resolve():shutil.copytree(inventory,out/'inventory')
    f=collection.Fetcher(out,ca_file,max_requests=250)
    f.fetch('pluto')
    ids=[bbl(x['row']['bbl']) for x in load(out/'inventory/inventory.json')['records']['pluto']]
    for query in queries(ids):f.fetch('pluto',query)
    f.fetch('pluto')
    save(out/'zoning-records.json',derive(out));seal(out,'evidence')
    return verify(out)


def enrich(inventory,req,out,ca_file=None):
    validate_request(req);collection.verify(inventory)
    if load(Path(inventory)/'inventory.json')['scope']!=req['scope']:raise ValueError('Changed geography needs a new inventory')
    out=fresh(out)
    return _enrich(req,inventory,out,ca_file)


def collect(req,out,ca_file=None):
    validate_request(req);out=fresh(out)
    collection.collect(transport_request(req),out/'inventory',ca_file)
    return _enrich(req,out/'inventory',out,ca_file)


def verify(folder):
    folder=Path(folder);verify_files(folder,'evidence');collection.verify(folder/'inventory')
    expected=derive(folder)
    if expected!=load(folder/'zoning-records.json'):raise ValueError('Zoning supplement differs from replay')
    return {'status':'passed','inventory':len(load(folder/'inventory/inventory.json')['records']['pluto']),
            'zoning_supplement_complete':expected['complete'],'returned_zoning_records':expected['returned_lots']}
