"""Bounded, source-bound DOB review without changing discovery admission. MIT."""
from collections import Counter
from datetime import datetime,timezone
import json
from pathlib import Path
import shutil
import time
import ssl
import urllib.error
import urllib.parse
import urllib.request
from housing_common.local_outputs import ROOT
from housing_site_discovery import engine as discovery
from housing_discovery.collection import same_query
from housing_site_discovery.common import bbl,digest,dumps,fresh,load,number,save
from . import packet

REGISTRY=load(Path(__file__).with_name('sources.json'))
CHUNK=25
CAP=2001


def safe_path(folder,name):
    relative=Path(name)
    if relative.is_absolute() or '..' in relative.parts:raise ValueError('Escaping review path')
    path=folder/relative
    if path.is_symlink() or not path.resolve().is_relative_to(folder.resolve()):raise ValueError('Escaping review path')
    return path


def implementation():
    paths=sorted(Path(__file__).parent.glob('*.py'))+sorted(Path(__file__).parent.glob('*.json'))+[ROOT/'src/housing_workflow/sources.json',ROOT/'src/housing_common/local_outputs.py']
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def seal(folder):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':'dwelling-review','implementation':implementation(),'files':files})


def verify_files(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('version')!='1.0.0' or m.get('kind')!='dwelling-review' or m.get('implementation')!=implementation():raise ValueError('Unknown or changed dwelling-review implementation')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Review package inventory changed')
    for name,sha in m['files'].items():
        path=folder/name
        if path.is_symlink() or not path.resolve().is_relative_to(folder) or digest(path.read_bytes())!=sha:raise ValueError('Changed or escaping review file: '+name)


def params(provider,ids):
    join=REGISTRY[provider]['join']
    if join=='borough_block_lot':
        clause=' OR '.join('(boroid='+x[0]+' AND block='+str(int(x[1:6]))+' AND lot='+str(int(x[6:]))+')' for x in ids)
    else:clause='bbl in ('+','.join(("'"+x+"'") if join=='bbl_text' else x for x in ids)+')'
    return {'$select':','.join(REGISTRY[provider]['fields']),'$where':clause,'$limit':str(CAP)}


def row_bbl(provider,row):
    if REGISTRY[provider]['join']!='borough_block_lot':return bbl(row.get('bbl'))
    values=[number(row.get(k)) for k in ['boroid','block','lot']]
    if any(x is None or x!=int(x) for x in values):raise ValueError('Invalid registration borough/block/lot')
    borough,block,lot=map(int,values)
    if not 1<=borough<=5 or not 1<=block<=99999 or not 1<=lot<=9999:raise ValueError('Invalid registration borough/block/lot')
    return bbl(borough*1000000000+block*10000+lot)


def url(provider,query=None):
    dataset=REGISTRY[provider]['dataset']
    return ('https://data.cityofnewyork.us/api/views/'+dataset+'.json' if query is None else
            'https://data.cityofnewyork.us/resource/'+dataset+'.json?'+urllib.parse.urlencode(query))


def raw_import(folder):
    """Validate retained original bytes; ignore/recompute all original derived outputs."""
    imported=folder/'imported';m=load(imported/'manifest.json')
    known=load(Path(__file__).with_name('legacy-imports.json'))['allowed_implementations']
    if m.get('kind')!='dwelling-review' or m.get('version')!='1.0.0' or m.get('implementation') not in known+[implementation()]:
        raise ValueError('Unrecognized raw capture implementation; no generic stale-package bypass')
    actual={str(p.relative_to(imported)) for p in imported.rglob('*') if p.is_file()}
    expected={name for name in m['files'] if not name.startswith('discovery/')}|{'manifest.json'}
    if actual!=expected:raise ValueError('Imported capture inventory differs from original manifest')
    for name,sha in m['files'].items():
        relative=Path(name)
        if relative.is_absolute() or '..' in relative.parts:raise ValueError('Escaping imported capture path')
        path=safe_path(folder,name) if name.startswith('discovery/') else safe_path(imported,name)
        if path.is_symlink() or digest(path.read_bytes())!=sha:raise ValueError('Imported capture bytes differ from original manifest: '+name)
    return load(imported/'receipts.json')


def signature(provider,query):
    # A complete uncapped result's universe is unchanged by row ordering. The
    # original exact URL/order remains recorded and validated on imported receipts.
    return dumps([provider,{k:v for k,v in query.items() if k!='$order'} if query is not None else None])


def split(subset,capped=False):
    if capped or len(subset)<=5:
        middle=len(subset)//2;return [subset[:middle],subset[middle:]]
    return [subset[i:i+5] for i in range(0,len(subset),5)]


class Fetcher:
    def __init__(self,folder,ca_file,budget,imported=None,offline=False):
        self.folder=folder;self.context=ssl.create_default_context(cafile=ca_file);self.budget=budget;self.attempts=0;self.receipts=[]
        (folder/'sources').mkdir()
        self.cache={}
        imported=imported or []
        failed_providers={r['provider'] for r in imported if r['status']!='ok'}
        for row in imported:
            if offline or (row['status']=='ok' and not (row['params'] is None and row['provider'] in failed_providers)):
                self.cache.setdefault(signature(row['provider'],row['params']),[]).append(row)

    def fetch(self,provider,query=None):
        cached=self.cache.get(signature(provider,query))
        if cached:
            original=cached.pop(0);row={**original,'id':str(len(self.receipts)),'imported_receipt_id':original['id']}
            if original.get('body_path'):row['body_path']='imported/'+original['body_path']
            self.receipts.append(row);save(self.folder/'receipts.json',self.receipts)
            return load(safe_path(self.folder,row['body_path'])) if row['status']=='ok' else None
        row={'id':str(len(self.receipts)),'provider':provider,'url':url(provider,query),'params':query,
             'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'failed'}
        body=None
        if self.attempts>=self.budget:row['error']='Session HTTP request budget reached'
        else:
            self.attempts+=1
            time.sleep(.15)
            try:
                req=urllib.request.Request(row['url'],headers={'User-Agent':'OpenHousingToolkit-DwellingReview/1.0','Accept':'application/json'})
                with urllib.request.urlopen(req,context=self.context,timeout=10) as response:
                    body=response.read(16*1024*1024+1)
                    if len(body)>16*1024*1024:raise ValueError('Source response exceeds16MiB')
                    row['http_status']=response.status
                data=json.loads(body)
                if not isinstance(data,dict if query is None else list):raise ValueError('Unexpected source response shape')
                row['status']='ok'
            except urllib.error.HTTPError as exc:
                body=exc.read(1024*1024);row.update(error=str(exc),http_status=exc.code)
            except (OSError,ValueError) as exc:row['error']=str(exc)
        if body is not None:
            path=f'sources/{row["id"]}-{provider}.json';(self.folder/path).write_bytes(body);row.update(body_path=path,sha256=digest(body),bytes=len(body))
        self.receipts.append(row);save(self.folder/'receipts.json',self.receipts)
        return data if row['status']=='ok' else None


def collect(source,out,ca_file=None,max_requests=160,reuse_capture=None,offline=False):
    source=Path(source);discovery.verify(source)
    if load(source/'manifest.json')['kind']!='discovery':raise ValueError('Start with a verified broad discovery package')
    if type(max_requests) is not int or not 4<=max_requests<=500:raise ValueError('Use an explicit HTTP budget from4to500')
    out=fresh(out);shutil.copytree(source,out/'discovery');save(out/'origin.json',{'discovery_manifest_sha256':digest((source/'manifest.json').read_bytes())})
    imported=None
    if reuse_capture is not None:
        original=Path(reuse_capture)
        if any(path.is_symlink() for path in original.rglob('*')):raise ValueError('Import source symlinks are unsupported')
        shutil.copytree(original,out/'imported',ignore=lambda path,names:{'discovery'} if Path(path).resolve()==original.resolve() else set())
        imported=raw_import(out)
        save(out/'capture-mode.json',{'mode':'retained_raw_offline_replay' if offline else 'retained_raw_replay_with_live_recovery','source_capture_manifest_sha256':digest((original/'manifest.json').read_bytes())})
    else:save(out/'capture-mode.json',{'mode':'live_collection','source_capture_manifest_sha256':None})
    ir=load(source/'ir.json');ids=[r['bbl'] for r in ir['lots'] if r['in_recorded_nonhousing_set']]
    f=Fetcher(out,ca_file,0 if offline else max_requests,imported,offline)
    def batch(provider,subset):
        rows=f.fetch(provider,params(provider,subset))
        if (rows is None and len(subset)>5) or (rows is not None and len(rows)>=CAP and len(subset)>1):
            for child in split(subset,capped=rows is not None):batch(provider,child)
    for provider in REGISTRY:
        f.fetch(provider)
        for start in range(0,len(ids),CHUNK):batch(provider,ids[start:start+CHUNK])
        f.fetch(provider)
    review=derive(out);save(out/'review.json',review);enriched=augment(ir,review);save(out/'ir.json',enriched)
    for name,content in packet.project(enriched,review).items():(out/name).write_text(content)
    seal(out);return verify(out)


def recover(capture,out,ca_file=None,max_requests=160,offline=False):
    capture=Path(capture)
    # Full raw-byte validation happens in the new package after copying. Base
    # discovery is independently verified; prior derived claims are not reused.
    return collect(capture/'discovery',out,ca_file,max_requests,capture,offline)


def metadata_valid(provider,meta):
    if not isinstance(meta,dict) or meta.get('id')!=REGISTRY[provider]['dataset'] or type(meta.get('rowsUpdatedAt')) is not int:return False
    fields={x.get('fieldName'):x.get('dataTypeName') for x in meta.get('columns',[])}
    if not set(REGISTRY[provider]['fields'])<=set(fields):return False
    if REGISTRY[provider]['join']=='borough_block_lot':return all(fields.get(k)=='number' for k in ['boroid','block','lot'])
    return fields.get('bbl')==('number' if REGISTRY[provider]['join']=='bbl_number' else 'text')


def receipt_vintage(folder,receipt,provider):
    capture=folder;record=receipt
    for _ in range(10):
        if 'imported_receipt_id' not in record:break
        capture=capture/'imported';originals={r['id']:r for r in load(capture/'receipts.json')}
        if record['imported_receipt_id'] not in originals:raise ValueError('Missing nested import receipt')
        record=originals[record['imported_receipt_id']]
    else:raise ValueError('Raw import ancestry exceeds ten captures')
    rows=[r for r in load(capture/'receipts.json') if r['provider']==provider and r['params'] is None and r['status']=='ok']
    metas=[load(safe_path(capture,r['body_path'])) for r in rows]
    valid=len(metas)==2 and all(metadata_valid(provider,m) for m in metas) and metas[0]['rowsUpdatedAt']==metas[1]['rowsUpdatedAt']
    return valid,metas[0].get('rowsUpdatedAt') if metas else None


def derive(folder):
    folder=Path(folder);ir=load(folder/'discovery/ir.json');ids=[r['bbl'] for r in ir['lots'] if r['in_recorded_nonhousing_set']]
    receipts=load(folder/'receipts.json')
    if [r['id'] for r in receipts]!=[str(i) for i in range(len(receipts))]:raise ValueError('Missing or duplicate review receipts')
    imported=raw_import(folder) if (folder/'imported').exists() else None
    originals={r['id']:r for r in imported or []}
    capture_mode=load(folder/'capture-mode.json') if (folder/'capture-mode.json').exists() else {'mode':'live_collection','source_capture_manifest_sha256':None}
    if imported is not None and (capture_mode.get('mode') not in ['retained_raw_replay_with_live_recovery','retained_raw_offline_replay'] or capture_mode.get('source_capture_manifest_sha256')!=digest((folder/'imported/manifest.json').read_bytes())):raise ValueError('Raw import mode/origin differs')
    cursor=0;lots={identity:{'coverage_by_source':{},'positive_signals':[]} for identity in ids};source_coverage={}
    def read(provider,query):
        nonlocal cursor
        if cursor>=len(receipts):raise ValueError('Review query coverage is incomplete')
        r=receipts[cursor];cursor+=1
        actual_query=r['params']
        if 'imported_receipt_id' in r:
            original=originals.get(r['imported_receipt_id'])
            if original is None:raise ValueError('Unknown imported receipt')
            expected={**original,'id':r['id'],'imported_receipt_id':original['id']}
            if original.get('body_path'):expected['body_path']='imported/'+original['body_path']
            if r!=expected:raise ValueError('Imported receipt differs from retained original')
            if actual_query is not None and actual_query.get('$order') not in [None,'bbl,'+REGISTRY[provider]['order']]:raise ValueError('Unexpected imported row ordering')
            actual_query={k:v for k,v in actual_query.items() if k!='$order'} if actual_query is not None else None
        if r['provider']!=provider or actual_query!=query or not same_query(r['url'],url(provider,r['params'])):raise ValueError('Review query identity differs from the declared universe')
        if r['status'] not in ['ok','failed']:raise ValueError('Unknown review source status')
        if 'body_path' in r:
            if 'imported_receipt_id' not in r and r['body_path']!=f'sources/{r["id"]}-{provider}.json':raise ValueError('Review body path differs')
            raw=safe_path(folder,r['body_path']).read_bytes()
            if digest(raw)!=r['sha256'] or len(raw)!=r['bytes']:raise ValueError('Review body differs from receipt')
        if r['status']!='ok':return r,None
        data=load(safe_path(folder,r['body_path']))
        if not isinstance(data,dict if query is None else list):raise ValueError('Invalid review response shape')
        return r,data
    for provider in REGISTRY:
        before_receipt,before=read(provider,None);leaf_ids={}
        def batch(subset):
            receipt,rows=read(provider,params(provider,subset))
            if rows is not None and any(not isinstance(x,dict) or row_bbl(provider,x) not in subset for x in rows):
                raise ValueError('Review returned a different parcel or malformed row')
            if (rows is None and len(subset)>5) or (rows is not None and len(rows)>=CAP and len(subset)>1):
                for child in split(subset,capped=rows is not None):batch(child)
                return
            for identity in subset:
                selected=[(index,row) for index,row in enumerate(rows or []) if row_bbl(provider,row)==identity]
                status=('failed' if rows is None else ('truncated' if len(rows)>=CAP else ('query_complete_rows' if selected else 'query_complete_empty')))
                missing_fields=(sum(1 for _,row in selected if all(number(row.get(k)) is None for k in REGISTRY[provider]['signal_fields'])) if REGISTRY[provider]['signal_fields'] else None)
                vintage_valid,vintage=receipt_vintage(folder,receipt,provider)
                coverage={'status':status,'returned_rows':len(selected),'rows_without_any_numeric_dwelling_field':missing_fields,
                          'receipt_id':receipt['id'],'metadata_stable':None,'capture_origin':'imported' if 'imported_receipt_id' in receipt else 'live','origin_metadata_stable':vintage_valid,'source_rows_updated_at':vintage}
                lots[identity]['coverage_by_source'][provider]=coverage;leaf_ids[identity]=status
                for index,row in selected:
                    if REGISTRY[provider]['presence_signal']:
                        field='registrationid' if provider=='hpd_registrations' else 'project_id'
                        lots[identity]['positive_signals'].append({'provider':provider,'field':field,'value':row.get(field),
                            'kind':'housing_registration_record' if provider=='hpd_registrations' else 'affordable_housing_program_record',
                            'job_id':row.get(field),'status':None,'filing_date':row.get('lastregistrationdate',row.get('project_start_date')),
                            'reference':{'body_path':receipt['body_path'],'pointer':'/'+str(index), 'receipt_id':receipt['id'],'sha256':receipt['sha256'],'url':receipt['url']},
                            'meaning':'HPD record linked by exact current tax-lot keys; program/registration dates and scope require review. Not proof of present occupancy, active registration or completed housing.'})
                    for field in REGISTRY[provider]['signal_fields']:
                        value=number(row.get(field))
                        if value is not None and value>0:
                            lots[identity]['positive_signals'].append({'provider':provider,'field':field,'value':value,'kind':'positive_historical_housing_unit_field',
                              'job_id':row.get('job__',row.get('job_filing_number')),'status':row.get('job_status_descrp',row.get('filing_status')),
                              'filing_date':row.get('pre__filing_date',row.get('filing_date')),
                              'reference':{'body_path':receipt['body_path'],'pointer':'/'+str(index)+'/'+field,'receipt_id':receipt['id'],'sha256':receipt['sha256'],'url':receipt['url']},
                              'meaning':'Historical/program unit-field signal; not verified current lawful housing or completed units.'})
        for start in range(0,len(ids),CHUNK):batch(ids[start:start+CHUNK])
        after_receipt,after=read(provider,None)
        stable=metadata_valid(provider,before) and metadata_valid(provider,after) and before['rowsUpdatedAt']==after['rowsUpdatedAt']
        for identity in ids:
            coverage=lots[identity]['coverage_by_source'][provider];coverage['metadata_stable']=stable and coverage['origin_metadata_stable'] and coverage['source_rows_updated_at']==(before.get('rowsUpdatedAt') if before else None)
            if not coverage['metadata_stable'] and coverage['status'].startswith('query_complete'):coverage['status']='metadata_unresolved'
        source_coverage[provider]={'metadata_stable':stable,'lots_by_status':dict(sorted(Counter(lots[i]['coverage_by_source'][provider]['status'] for i in ids).items())),
                                   'limits':REGISTRY[provider]['limits']}
    if cursor!=len(receipts):raise ValueError('Unexpected extra review queries')
    for identity,row in lots.items():
        if row['positive_signals']:status='positive_returned_housing_signal'
        elif all(c['status'].startswith('query_complete') for c in row['coverage_by_source'].values()):status='no_positive_returned_housing_signal'
        else:status='housing_signal_coverage_unknown'
        row.update(status=status,actual_current_homes=None,meaning='Bounded exact-BBL returned-field review, not proof of absence/presence of current housing. All base discovery lots remain visible.')
    return {'version':'1.0','capture_mode':capture_mode,'imported_historical_failed_receipts':sum(r['status']=='failed' for r in imported or []),'replayed_receipts':sum('imported_receipt_id' in r for r in receipts),'new_receipts':sum('imported_receipt_id' not in r for r in receipts),'reviewed_recorded_nonhousing_lots':len(ids),'source_coverage':source_coverage,
            'counts':dict(sorted(Counter(x['status'] for x in lots.values()).items())),'lots':lots,
            'limits':['Exact BBL or explicit borough/block/lot joins can miss historical lot changes, unlinked or unrecorded housing.',
                      'Historical existing/proposed units and filing status do not establish current occupancy or completed/lawful housing.',
                      'No positive returned signal is a literal query result; empty or missing numeric fields do not establish no housing.',
                      'Before/after update metadata detects some drift; these APIs are not transactional snapshots.']}


def augment(ir,review):
    import copy
    enriched=copy.deepcopy(ir);enriched['dwelling_review_counts']=review['counts']
    for row in enriched['lots']:
        record=review['lots'].get(row['bbl']);row['dwelling_review']=record
        if record:
            if record['status']=='positive_returned_housing_signal':row['flags']=sorted(set(row['flags']+['positive_historical_dwelling_signal_requires_reconciliation']))
            elif record['status']=='housing_signal_coverage_unknown':row['flags']=sorted(set(row['flags']+['dwelling_signal_query_coverage_unknown']))
    return enriched


def verify(folder):
    folder=Path(folder);verify_files(folder);discovery.verify(folder/'discovery')
    if load(folder/'origin.json')!={'discovery_manifest_sha256':digest((folder/'discovery/manifest.json').read_bytes())}:raise ValueError('Review origin differs')
    review=derive(folder)
    if review!=load(folder/'review.json'):raise ValueError('Dwelling review differs from replay')
    ir=augment(load(folder/'discovery/ir.json'),review)
    if ir!=load(folder/'ir.json'):raise ValueError('Reviewed discovery differs from recomputation')
    for name,content in packet.project(ir,review).items():
        if (folder/name).read_text()!=content:raise ValueError('Review projection differs: '+name)
    return {'status':'passed','reviewed_lots':review['reviewed_recorded_nonhousing_lots'],'housing_signal_counts':review['counts'],'packet':str(folder/'packet.html')}
