"""Compose inventory, scenario screening, comparisons and candidate handoffs. MIT."""
from pathlib import Path
import shutil
from . import collection, packet, screen, focus as use_focus
from .common import digest, fresh, load, save, seal, validate_request, verify_files


def build(inventory_folder, request, out):
    collection.verify(inventory_folder)
    validate_request(request)
    inv = load(Path(inventory_folder)/'inventory.json')
    ir = screen.evaluate(inv,request)
    out = fresh(out)
    shutil.copytree(inventory_folder,out/'evidence')
    save(out/'request.json',request);save(out/'inventory.json',inv);save(out/'ir.json',ir)
    save(out/'origin.json',{'inventory_manifest_sha256':digest((Path(inventory_folder)/'manifest.json').read_bytes()),'mode':'screen_from_saved_inventory'})
    for name,content in packet.project(ir,request).items():
        (out/name).write_text(content)
    seal(out,'screen')
    return verify(out)


def verify(folder):
    folder = Path(folder)
    m = load(folder/'manifest.json')
    if m['kind']=='inventory':return collection.verify(folder)
    verify_files(folder,m['kind'])
    if m['kind']=='screen':
        collection.verify(folder/'evidence')
        inv = load(folder/'evidence/inventory.json')
        if inv != load(folder/'inventory.json') or load(folder/'origin.json')['inventory_manifest_sha256'] != digest((folder/'evidence/manifest.json').read_bytes()):
            raise ValueError('Screen origin changed')
        ir = screen.evaluate(inv,load(folder/'request.json'))
        if ir != load(folder/'ir.json'):
            raise ValueError('Screen differs from recomputation')
        for name,content in packet.project(ir,load(folder/'request.json')).items():
            if (folder/name).read_text()!=content:raise ValueError('Screen projection changed: '+name)
        return {'status':'passed',**ir['counts'],'packet':str(folder/'packet.html'),'professional_review':'pending'}
    if m['kind']=='comparison':
        verify(folder/'left');verify(folder/'right')
        expected = differences(folder/'left',folder/'right')
        if load(folder/'comparison.json')!=expected:raise ValueError('Comparison differs from replay')
        if (folder/'packet.md').read_text()!=comparison_text(expected):raise ValueError('Comparison summary changed')
        return {'status':'passed','changed_lots':len(expected['changed_lots'])}
    if m['kind']=='focus':
        verify(folder/'parent')
        request=load(folder/'request.json')
        if request!=load(folder/'parent/request.json'):raise ValueError('Focus changed source scenario')
        ir=use_focus.apply(load(folder/'parent/ir.json'),load(folder/'focus.json'),request['selection']['top_n'])
        if ir!=load(folder/'ir.json'):raise ValueError('Use focus differs from replay')
        for name,content in packet.project(ir,request).items():
            if (folder/name).read_text()!=content:raise ValueError('Focus projection changed')
        return {'status':'passed',**ir['counts'],'packet':str(folder/'packet.html')}
    if m['kind']=='handoff':
        verify(folder/'screen')
        expected = handoff_requests(load(folder/'screen/ir.json'),load(folder/'selection.json')['bbls'])
        if load(folder/'requests.json')!=expected:raise ValueError('Candidate handoff changed')
        return {'status':'passed','requests':len(expected)}
    if m['kind']=='deep-investigation':
        verify(folder/'handoff')
        from housing_workflow.engine import verify as verify_parcel
        reqs = load(folder/'handoff/requests.json')
        for req in reqs:
            verify_parcel(folder/req['bbl'])
            if load(folder/req['bbl']/'request.json') != req:raise ValueError('Deep parcel differs from selected handoff')
        return {'status':'passed','investigations':len(reqs)}
    raise ValueError('Unsupported discovery package')


def focus(source,spec,out):
    source=Path(source);verify(source)
    if load(source/'manifest.json')['kind']!='screen':raise ValueError('Focus starts from a verified scenario screen')
    request=load(source/'request.json')
    ir=use_focus.apply(load(source/'ir.json'),spec,request['selection']['top_n'])
    out=fresh(out);shutil.copytree(source,out/'parent')
    save(out/'request.json',request);save(out/'focus.json',spec);save(out/'ir.json',ir)
    for name,content in packet.project(ir,request).items():(out/name).write_text(content)
    seal(out,'focus');return verify(out)


def differences(left,right):
    l,r = load(left/'ir.json'),load(right/'ir.json')
    def inventory_manifest(path):
        return path/('parent/evidence/manifest.json' if load(path/'manifest.json')['kind']=='focus' else 'evidence/manifest.json')
    if digest(inventory_manifest(left).read_bytes()) != digest(inventory_manifest(right).read_bytes()):
        raise ValueError('Sensitivity comparison requires the exact same retained inventory')
    left_rows,right_rows = {x['bbl']:x for x in l['lots']},{x['bbl']:x for x in r['lots']}
    if set(left_rows)!=set(right_rows):raise ValueError('Comparison lot universe changed')
    changes=[]
    for identity in sorted(left_rows):
        a,b=left_rows[identity],right_rows[identity]
        keys=['rank_in_screen_pool','shortlisted','hold_reasons','additional_zoning_area_proxy_sf','additional_home_equivalents']
        delta={key:{'before':a[key],'after':b[key]} for key in keys if a[key]!=b[key]}
        if delta:changes.append({'bbl':identity,'address':a['address'],'changes':delta})
    return {'left_request':load(left/'request.json'),'right_request':load(right/'request.json'),
            'left_counts':l['counts'],'right_counts':r['counts'],
            'entered_shortlist':sorted(set(r['shortlist'])-set(l['shortlist'])),
            'left_shortlist':sorted(set(l['shortlist'])-set(r['shortlist'])),
            'changed_lots':changes,'meaning':'Same-source sensitivity; no causal housing or welfare effect is inferred.'}


def comparison_text(result):
    return '# Discovery sensitivity comparison\n\n'+result['meaning']+'\n\n'+f"Left screen pool: {result['left_counts']['screen_pool']}; right screen pool: {result['right_counts']['screen_pool']}.\n\n"+'Entered shortlist: '+', '.join(result['entered_shortlist'])+'\n\nLeft shortlist: '+', '.join(result['left_shortlist'])+'\n\nComplete changed values and reasons are in comparison.json.\n'


def compare(left,right,out):
    left,right=Path(left),Path(right);verify(left);verify(right)
    result=differences(left,right)
    out=fresh(out);shutil.copytree(left,out/'left');shutil.copytree(right,out/'right')
    save(out/'comparison.json',result);(out/'packet.md').write_text(comparison_text(result));seal(out,'comparison')
    return verify(out)


def handoff_requests(ir,selected):
    if not isinstance(selected,list) or not selected or len(selected)!=len(set(selected)) or not set(selected)<=set(ir['shortlist']):
        raise ValueError('Choose unique BBLs from the verified shortlist')
    by_id={x['bbl']:x for x in ir['lots']}
    requests=[]
    for identity in selected:
        if not identity.startswith('2'):raise ValueError('The current deeper parcel workflow supports Bronx lots only')
        row=by_id[identity]
        requests.append({'version':'0.2.0','bbl':identity,'question':f"Discovery follow-up for {row['address']} ({identity}): reconcile public records, existing-use and historical housing signals, pipeline and the unresolved inputs behind this conditional discovery candidate. Do not infer vacancy, availability, rezoning eligibility or financial feasibility.",'scenario':None})
    return requests


def handoff(source,out,top=3):
    source=Path(source);verify(source)
    if type(top) is not int or not 1<=top<=10:raise ValueError('Choose 1 to 10 deeper investigations')
    ir=load(source/'ir.json');selected=ir['shortlist'][:top]
    requests=handoff_requests(ir,selected)
    out=fresh(out);shutil.copytree(source,out/'screen')
    save(out/'selection.json',{'bbls':selected,'method':'first N from declared deterministic screen, not practitioner acceptance'})
    save(out/'requests.json',requests)
    seal(out,'handoff');return verify(out)


def deepen(source,out):
    source=Path(source);verify(source)
    if load(source/'manifest.json')['kind']!='handoff':raise ValueError('Provide a verified handoff package')
    from housing_workflow.engine import run as run_parcel
    requests=load(source/'requests.json')
    out=fresh(out);shutil.copytree(source,out/'handoff')
    for req in requests:
        run_parcel(req,out/req['bbl'])
    seal(out,'deep-investigation');return verify(out)
