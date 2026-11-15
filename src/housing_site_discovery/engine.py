"""Compose verified evidence, independent discovery and explicit follow-up. MIT."""
from pathlib import Path
import shutil
from . import context, evidence, model, packet
from .common import digest, fresh, guidance, load, save, seal, validate_request, verify_files


def build(source,request,out,context_source=None):
    source=Path(source);evidence.verify(source);validate_request(request)
    inv=load(source/'inventory/inventory.json');supp=load(source/'zoning-records.json')
    pack=guidance(load(Path(__file__).with_name('guidance.json')))
    public_context=None
    if context_source is not None:
        context_source=Path(context_source);context.verify(context_source)
        origin=load(context_source/'universe.json')
        if digest((source/'manifest.json').read_bytes())!=origin['evidence_manifest_sha256'] or origin['scope']!=inv['scope'] or origin['bbls']!=[model.bbl(x['row']['bbl']) for x in inv['records']['pluto']]:raise ValueError('Context and discovery evidence differ')
        public_context=load(context_source/'context.json')
    ir=model.evaluate(inv,supp,request,pack,public_context)
    out=fresh(out);shutil.copytree(source,out/'evidence')
    if context_source is not None:shutil.copytree(context_source,out/'public-context')
    save(out/'request.json',request);save(out/'guidance.json',pack);save(out/'ir.json',ir)
    save(out/'origin.json',{'evidence_manifest_sha256':digest((source/'manifest.json').read_bytes()),'mode':'discovery_from_retained_evidence'})
    for name,content in packet.project(ir,request,pack).items():(out/name).write_text(content)
    seal(out,'discovery');return verify(out)


def followup_requests(ir,selected):
    if not isinstance(selected,list) or not selected or len(selected)>10 or len(selected)!=len(set(selected)):
        raise ValueError('Choose 1 to 10 unique BBLs explicitly')
    by_id={x['bbl']:x for x in ir['lots']}
    if any(b not in by_id or not by_id[b]['in_recorded_nonhousing_set'] for b in selected):
        raise ValueError('Follow-up requires lots from the verified recorded-nonhousing set')
    reqs=[]
    for identity in selected:
        if not identity.startswith('2'):raise ValueError('The current deeper parcel workflow supports Bronx lots only')
        row=by_id[identity]
        reqs.append({'version':'0.2.0','bbl':identity,'question':f"Nonhousing discovery follow-up for {row['address']} ({identity}), general zoning path {row['zoning_path']['path']}: reconcile current operations, historical housing signals, zoning exceptions, site control and unresolved constraints. No development program or vacancy finding is supplied.",'scenario':None})
    return reqs


def handoff(source,selected,out):
    source=Path(source);verify(source)
    if load(source/'manifest.json')['kind']!='discovery':raise ValueError('Select from a verified discovery package')
    reqs=followup_requests(load(source/'ir.json'),selected)
    out=fresh(out);shutil.copytree(source,out/'discovery')
    save(out/'selection.json',{'bbls':selected,'method':'Explicit user or analyst selection; no automatic universal site score'})
    save(out/'requests.json',reqs);seal(out,'site-handoff');return verify(out)


def deepen(source,out):
    source=Path(source);verify(source)
    if load(source/'manifest.json')['kind']!='site-handoff':raise ValueError('Provide a verified site handoff')
    from housing_workflow.engine import run
    out=fresh(out);shutil.copytree(source,out/'handoff')
    for req in load(source/'requests.json'):run(req,out/req['bbl'])
    seal(out,'site-investigation');return verify(out)


def legacy_difference(source,legacy):
    new=load(source/'ir.json');old=load(legacy/'ir.json')
    original=source/'evidence/inventory/manifest.json'
    old_original=legacy/('parent/evidence/manifest.json' if load(legacy/'manifest.json')['kind']=='focus' else 'evidence/manifest.json')
    if digest(original.read_bytes())!=digest(old_original.read_bytes()):raise ValueError('Comparison requires the exact same original inventory')
    previous={x['bbl']:x for x in old['lots']}
    if set(previous)!={x['bbl'] for x in new['lots']}:raise ValueError('Comparison lot universe changed')
    added=[]
    for row in new['lots']:
        prior=previous[row['bbl']]
        if row['in_recorded_nonhousing_set'] and prior['hold_reasons']:
            added.append({'bbl':row['bbl'],'address':row['address'],'zoning_path':row['zoning_path']['path'],
                          'old_hold_reasons':prior['hold_reasons'],'recorded_residential_far':row['recorded_residential_far']})
    return {'interpretation':'Method correction on the same original universe; a later zoning supplement is retained separately. Counts are not viable sites.',
            'old_counts':old['counts'],'new_counts':new['counts'],'new_nonhousing_previously_held':added}


def compare_legacy(source,legacy,out):
    source,legacy=Path(source),Path(legacy);verify(source)
    from housing_discovery.engine import verify as old_verify
    old_verify(legacy)
    result=legacy_difference(source,legacy);out=fresh(out)
    shutil.copytree(source,out/'discovery');shutil.copytree(legacy,out/'legacy')
    save(out/'comparison.json',result);seal(out,'legacy-comparison');return verify(out)


def verify(folder):
    folder=Path(folder);kind=load(folder/'manifest.json')['kind']
    if kind=='evidence':return evidence.verify(folder)
    if kind=='context':return context.verify(folder)
    verify_files(folder,kind)
    if kind=='discovery':
        evidence.verify(folder/'evidence')
        req=validate_request(load(folder/'request.json'));pack=guidance(load(folder/'guidance.json'))
        if pack!=load(Path(__file__).with_name('guidance.json')):raise ValueError('Unrecognized guidance snapshot')
        public_context=None
        if (folder/'public-context').exists():
            context.verify(folder/'public-context')
            origin=load(folder/'public-context/universe.json');inv=load(folder/'evidence/inventory/inventory.json')
            if origin['evidence_manifest_sha256']!=digest((folder/'evidence/manifest.json').read_bytes()) or origin['scope']!=inv['scope'] or origin['bbls']!=[model.bbl(x['row']['bbl']) for x in inv['records']['pluto']]:raise ValueError('Retained context evidence differs')
            public_context=load(folder/'public-context/context.json')
        expected=model.evaluate(load(folder/'evidence/inventory/inventory.json'),load(folder/'evidence/zoning-records.json'),req,pack,public_context)
        if expected!=load(folder/'ir.json'):raise ValueError('Discovery differs from recomputation')
        if load(folder/'origin.json')!={'evidence_manifest_sha256':digest((folder/'evidence/manifest.json').read_bytes()),'mode':'discovery_from_retained_evidence'}:
            raise ValueError('Discovery origin changed')
        for name,content in packet.project(expected,req,pack).items():
            if (folder/name).read_text()!=content:raise ValueError('Discovery projection differs: '+name)
        return {'status':'passed',**expected['counts'],'packet':str(folder/'packet.html'),'professional_review':'pending'}
    if kind=='site-handoff':
        verify(folder/'discovery')
        if followup_requests(load(folder/'discovery/ir.json'),load(folder/'selection.json')['bbls'])!=load(folder/'requests.json'):
            raise ValueError('Selected follow-up requests changed')
        return {'status':'passed','requests':len(load(folder/'requests.json'))}
    if kind=='site-investigation':
        verify(folder/'handoff')
        from housing_workflow.engine import verify as parcel_verify
        reqs=load(folder/'handoff/requests.json')
        for req in reqs:
            parcel_verify(folder/req['bbl'])
            if load(folder/req['bbl']/'request.json')!=req:raise ValueError('Parcel request differs from selected handoff')
        return {'status':'passed','investigations':len(reqs)}
    if kind=='legacy-comparison':
        verify(folder/'discovery')
        from housing_discovery.engine import verify as old_verify
        old_verify(folder/'legacy')
        if legacy_difference(folder/'discovery',folder/'legacy')!=load(folder/'comparison.json'):raise ValueError('Legacy comparison differs from replay')
        return {'status':'passed','new_nonhousing_previously_held':len(load(folder/'comparison.json')['new_nonhousing_previously_held'])}
    raise ValueError('Unsupported site-discovery package kind')
