"""Bounded monthly NYC zoning-tax-lot reconciliation with no entitlement claim. MIT."""
from collections import Counter
from pathlib import Path
import copy
import re
import shutil
from housing_common import site_inputs
from housing_common.public_sources import PublicJSON,same_query
from housing_common.local_outputs import ROOT
from housing_common.packages import digest,dumps,load,save,fresh
from housing_discovery.common import bbl

PROVIDERS={'nyztl':{'metadata_url':'https://data.cityofnewyork.us/api/views/fdkv-4t4z.json','records_url':'https://data.cityofnewyork.us/resource/fdkv-4t4z.json','metadata_shape':'object','records_shape':'array'}}
FIELDS=['bbl']+[f'zoning_district_{n}' for n in range(1,5)]+[f'commercial_overlay_{n}' for n in range(1,3)]+[f'special_district_{n}' for n in range(1,4)]+['limited_height_district','zoning_map_number','zoning_map_code']


def queries(ids):return [{'$select':','.join(FIELDS),'$where':'bbl in ('+','.join(ids[i:i+100])+')','$order':'bbl','$limit':'101'} for i in range(0,len(ids),100)]


def implementation():
    paths=sorted(Path(__file__).parent.glob('*.py'))+sorted(Path(__file__).parent.glob('*.json'))+[ROOT/'src/housing_common'/n for n in ['site_inputs.py','public_sources.py','local_outputs.py','packages.py']]
    paths+=[ROOT/'src/housing_discovery/common.py']
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def seal(folder):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'kind':'zoning-review','version':'1.0.0','implementation':implementation(),'files':files})


def verify_files(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('kind')!='zoning-review' or m.get('version')!='1.0.0' or m.get('implementation')!=implementation():raise ValueError('Unknown or changed zoning-review implementation')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Zoning-review file inventory changed')
    for name,sha in m['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Changed or escaping zoning-review file: '+name)


def derive(folder):
    folder=Path(folder);parent=load(folder/'parent/ir.json');ids=[x['bbl'] for x in parent['lots']]
    receipts=load(folder/'receipts.json');expected=[None]+queries(ids)+[None]
    if len(receipts)!=len(expected) or [r['id'] for r in receipts]!=list(map(str,range(len(expected)))) or [r['params'] for r in receipts]!=expected:raise ValueError('Zoning query inventory differs from the exact upstream lot universe')
    expected_bodies={r['body_path'] for r in receipts if 'body_path' in r}
    actual_bodies={str(p.relative_to(folder)) for p in (folder/'sources').rglob('*') if p.is_file()}
    if actual_bodies!=expected_bodies:raise ValueError('Zoning source file inventory differs from receipts')
    records={};coverage={};meta=[];versions=[]
    client=PublicJSON.__new__(PublicJSON);client.providers=PROVIDERS
    for r,params in zip(receipts,expected):
        if r['provider']!='nyztl' or not same_query(r['url'],client.url('nyztl',params)):raise ValueError('Non-allowlisted zoning query')
        if 'body_path' in r:
            if r['body_path']!='sources/'+r['id']+'-nyztl.json':raise ValueError('Unexpected zoning source path')
            body=(folder/r['body_path']).read_bytes()
            if digest(body)!=r['sha256'] or len(body)!=r['bytes']:raise ValueError('Zoning source receipt changed')
        if params is None:
            valid=False;data=load(folder/r['body_path']) if r['status']=='ok' else None
            if isinstance(data,dict):
                columns={x.get('fieldName'):x.get('dataTypeName') for x in data.get('columns',[])}
                valid=set(FIELDS)<=set(columns) and columns.get('bbl')=='number' and data.get('id')=='fdkv-4t4z'
                match=re.search(r'Current version:\s*([0-9]{8})',data.get('description',''),re.I);versions.append(match.group(1) if match else None)
            else:versions.append(None)
            meta.append({'valid':valid,'rows_updated_at':data.get('rowsUpdatedAt') if data else None});continue
        batch=params['$where'][len('bbl in ('):-1].split(',')
        data=load(folder/r['body_path']) if r['status']=='ok' else None
        if not isinstance(data,list):
            for identity in batch:coverage[identity]='query_failed_or_malformed'
            continue
        if len(data)>=101:
            for identity in batch:coverage[identity]='batch_row_cap_requires_review'
            continue
        seen={}
        for i,row in enumerate(data):
            if not isinstance(row,dict):raise ValueError('Malformed zoning row')
            identity=bbl(row.get('bbl'))
            if identity not in batch:raise ValueError('Zoning response includes an unrequested BBL')
            seen[identity]=seen.get(identity,0)+1
            records[identity]={'row':row,'reference':{'body_path':r['body_path'],'receipt_id':r['id'],'pointer':'/'+str(i),'sha256':r['sha256']}}
        for identity in batch:coverage[identity]='one_returned_record' if seen.get(identity)==1 else ('no_returned_record' if identity not in seen else 'multiple_returned_records')
    stable=len(meta)==2 and all(x['valid'] for x in meta) and meta[0]['rows_updated_at']==meta[1]['rows_updated_at'] and meta[0]['rows_updated_at'] is not None and versions[0]==versions[1] and versions[0] is not None
    return {'dataset':'fdkv-4t4z','source_version':versions[0] if versions else None,'metadata_stable':stable,
            'coverage_by_bbl':coverage,'records':records,'coverage_counts':dict(sorted(Counter(coverage.values()).items())),
            'meaning':'Published monthly NYC zoning-by-tax-lot records, not a new cadastral intersection or a professional entitlement determination.'}


def apply(parent,review):
    ir=copy.deepcopy(parent)
    for lot in ir['lots']:
        identity=lot['bbl'];item=review['records'].get(identity);coverage=review['coverage_by_bbl'][identity]
        status='unresolved';differences=[];districts=[];specials=[];overlays=[]
        if item and coverage=='one_returned_record':
            raw=item['row'];districts=[raw[k].strip().upper() for k in [f'zoning_district_{n}' for n in range(1,5)] if raw.get(k)]
            specials=[raw[k].strip().upper() for k in [f'special_district_{n}' for n in range(1,4)] if raw.get(k)]
            overlays=[raw[k].strip().upper() for k in [f'commercial_overlay_{n}' for n in range(1,3)] if raw.get(k)]
            original=lot['zoning_path']
            if set(districts)!=set(original['recorded_districts']):differences.append('districts_differ')
            if set(specials)!=set(str(x).upper() for x in original['recorded_special_districts']):differences.append('special_districts_differ')
            if set(overlays)!=set(str(x).upper() for x in original.get('recorded_overlays',[])):differences.append('commercial_overlays_differ')
            if raw.get('limited_height_district'):differences.append('monthly_source_limited_height_requires_review')
            if not districts:differences.append('monthly_source_districts_missing')
            status='sources_differ_or_require_review' if differences else 'recorded_sources_agree_on_compared_fields'
        if not review['metadata_stable']:status='unresolved'
        lot['zoning_record_review']={'status':status,'query_coverage':coverage,'source_version':review['source_version'],
                                    'recorded_districts':districts,'recorded_special_districts':specials,'recorded_overlays':overlays,
                                    'differences':differences,'reference':item['reference'] if item else None,
                                    'meaning':review['meaning']}
        if status!='recorded_sources_agree_on_compared_fields':
            lot['zoning_path']['path']='special_or_unresolved_review'
            lot['zoning_path']['review_reasons']=sorted(set(lot['zoning_path']['review_reasons']+['monthly_zoning_source_reconciliation_required']))
            lot['flags']=sorted(set(lot['flags']+['monthly_zoning_source_review']))
    ir['zoning_record_review_coverage']={k:v for k,v in review.items() if k not in ['records','coverage_by_bbl']}
    non=[x for x in ir['lots'] if x['in_recorded_nonhousing_set']]
    ir['counts']['nonhousing_by_zoning_path']=dict(sorted(Counter(x['zoning_path']['path'] for x in non).items()))
    ir['counts']['nonhousing_by_zoning_record_review']=dict(sorted(Counter(x['zoning_record_review']['status'] for x in non).items()))
    return ir


def project(ir):
    counts=ir['counts'].get('nonhousing_by_zoning_record_review',{})
    lines=['# Monthly zoning-record reconciliation','',ir['zoning_record_review_coverage']['meaning'],'',f"Source version: {ir['zoning_record_review_coverage']['source_version']}. Metadata stable: {ir['zoning_record_review_coverage']['metadata_stable']}.",'', 'Recorded nonhousing lot review states:']+['- '+k+': '+str(v) for k,v in counts.items()]
    lines+=['','Differences are retained for reconciliation rather than choosing one source silently. Agreement on these fields does not establish full zoning applicability or a lawful envelope. Earlier source paths and dwelling reviews remain unchanged under parent/.','', '[Earlier discovery/review packet](parent/packet.md). Full per-lot source fields and differences are in ir.json; raw responses and exact queries are in sources/ and receipts.json.']
    return '\n'.join(lines)+'\n'


def html_project(ir):
    import html
    text=project(ir)
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zoning record review</title><style>body{font:16px/1.5 system-ui;max-width:1000px;margin:30px auto;padding:0 20px}pre{white-space:pre-wrap;overflow-wrap:anywhere}</style><h1>Monthly zoning-record reconciliation</h1><pre>'+html.escape(text)+'</pre><p><a href="parent/packet.html">Earlier discovery/review packet</a></p></html>'


def origin(folder):
    result={'parent_manifest_sha256':digest((folder/'parent/manifest.json').read_bytes()),'mode':'live_collection'}
    if (folder/'raw-capture-manifest.json').exists():
        result.update(mode='retained_raw_capture_replay',raw_capture_manifest_sha256=digest((folder/'raw-capture-manifest.json').read_bytes()))
        old=load(folder/'raw-capture-manifest.json')
        if old.get('kind')!='zoning-review' or old.get('version')!='1.0.0':raise ValueError('Unsupported raw zoning capture kind')
        known=load(Path(__file__).with_name('legacy-captures.json'))['allowed_implementations']
        if old.get('implementation') not in known+[implementation()]:raise ValueError('Unrecognized raw zoning-capture implementation')
        for name in ['receipts.json']+[str(p.relative_to(folder)) for p in sorted((folder/'sources').glob('*.json'))]:
            if digest((folder/name).read_bytes())!=old.get('files',{}).get(name):raise ValueError('Replayed zoning source differs from retained raw capture')
    return result


def replay(parent,capture,out):
    # Import only raw responses/queries, not the old IR or its interpretation.
    # Old implementation bindings are not represented as current verification.
    ir=site_inputs.state(parent);capture=Path(capture);manifest=load(capture/'manifest.json')
    if manifest.get('kind')!='zoning-review' or manifest.get('version')!='1.0.0':raise ValueError('Unsupported raw zoning capture')
    known=load(Path(__file__).with_name('legacy-captures.json'))['allowed_implementations']
    if manifest.get('implementation') not in known+[implementation()]:raise ValueError('Unrecognized raw zoning-capture implementation')
    receipts=load(capture/'receipts.json');expected={r['body_path'] for r in receipts if 'body_path' in r}
    actual={str(p.relative_to(capture)) for p in (capture/'sources').rglob('*') if p.is_file()}
    if actual!=expected or (capture/'sources').is_symlink():raise ValueError('Raw source inventory or symlink differs from receipts')
    for path in (capture/'sources').rglob('*'):
        if path.is_symlink() or not path.resolve().is_relative_to(capture.resolve()):raise ValueError('Raw source path escapes capture')
    for name in ['receipts.json']+[str(p.relative_to(capture)) for p in sorted((capture/'sources').glob('*.json'))]:
        path=capture/name
        if path.is_symlink() or not path.resolve().is_relative_to(capture.resolve()) or digest(path.read_bytes())!=manifest.get('files',{}).get(name):raise ValueError('Raw source capture bytes changed')
    out=fresh(out);shutil.copytree(parent,out/'parent');shutil.copytree(capture/'sources',out/'sources')
    shutil.copyfile(capture/'receipts.json',out/'receipts.json');shutil.copyfile(capture/'manifest.json',out/'raw-capture-manifest.json')
    save(out/'origin.json',origin(out));return finalize(out)


def collect(parent,out,ca_file=None):
    ir=site_inputs.state(parent);out=fresh(out);shutil.copytree(parent,out/'parent')
    save(out/'origin.json',origin(out))
    ids=[x['bbl'] for x in ir['lots']];client=PublicJSON(out,PROVIDERS,ca_file,max_attempts=160)
    for params in [None]+queries(ids)+[None]:client.fetch('nyztl',params)
    return finalize(out)


def finalize(folder):
    folder=Path(folder)
    if (folder/'manifest.json').exists():raise ValueError('A completed zoning review cannot be finalized again')
    site_inputs.verify(folder/'parent');review=derive(folder);ir=apply(load(folder/'parent/ir.json'),review)
    save(folder/'zoning-records.json',review);save(folder/'ir.json',ir);(folder/'packet.md').write_text(project(ir));(folder/'packet.html').write_text(html_project(ir));seal(folder);return verify(folder)


def verify(folder):
    folder=Path(folder);verify_files(folder);site_inputs.verify(folder/'parent')
    if load(folder/'origin.json')!=origin(folder):raise ValueError('Zoning review parent changed')
    review=derive(folder);ir=apply(load(folder/'parent/ir.json'),review)
    if load(folder/'zoning-records.json')!=review or load(folder/'ir.json')!=ir:raise ValueError('Zoning reconciliation differs from source replay')
    if (folder/'packet.md').read_text()!=project(ir) or (folder/'packet.html').read_text()!=html_project(ir):raise ValueError('Zoning review packet changed')
    return {'status':'passed','inventory':len(ir['lots']),'metadata_stable':review['metadata_stable'],'source_version':review['source_version'],'nonhousing_by_review':ir['counts']['nonhousing_by_zoning_record_review']}
