"""Execute and verify one discrete, source-bound workflow. MIT."""
from pathlib import Path
import shutil
from .contracts import digest, dumps, load, save, validate_request
from . import model, packet, router

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / 'workflows/parcel-investigation.json'

def implementation():
    files = sorted((ROOT/'housing_workflow').glob('*.py')) + sorted((ROOT/'housing_workflow').glob('*.json')) + [WORKFLOW]
    files += sorted((ROOT/'skills').glob('*/SKILL.md'))
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in files}

def safe(root, name):
    p = root / name
    if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('Package path escapes run directory')
    return p

def fresh(folder):
    if folder.exists() and any(folder.iterdir()):raise ValueError('Use a new empty output directory; previous evidence is preserved.')
    folder.mkdir(parents=True,exist_ok=True)

def validate_evidence(req, receipts, folder):
    validate_request(req)
    ids=[r['id'] for r in receipts]
    expected=set(router.REGISTRY) | ({'address_resolution'} if req.get('address') else set())
    if len(ids)!=len(set(ids)) or set(ids)!=expected:raise ValueError('Missing, duplicate or unexpected source receipts')
    parcel=req.get('bbl')
    if not parcel:
        resolution=next(r for r in receipts if r['id']=='address_resolution')
        if resolution['status']!='ok' or resolution['url']!=router.address_url(req['address']):raise ValueError('Address resolution binding changed')
        data=load(safe(folder,resolution['body_path']))
        if len(data)!=1:raise ValueError('Ambiguous parcel resolution')
        parcel=router.bbl(str(int(float(data[0]['bbl']))))
    for r in receipts:
        if r['id']!='address_resolution':
            if r['requested_bbl']!=parcel or r['url']!=router.parcel_url(r['id'],parcel):raise ValueError('Source query is for a different parcel or adapter')
        if r['status'] not in {'ok','failed'}:raise ValueError('Unsupported source status')
        if r['body_path']:
            expected_body='sources/'+r['id']+'.json'
            if r['body_path']!=expected_body:raise ValueError('Unexpected source body path')
            raw=safe(folder,r['body_path']).read_bytes()
            if digest(raw)!=r['sha256'] or len(raw)!=r['bytes']:raise ValueError('Source hash mismatch: '+r['id'])
        if r['status']=='ok':
            data=load(safe(folder,r['body_path']))
            if r.get('http_status')!=200 or not isinstance(data,list) or not all(isinstance(x,dict) for x in data):raise ValueError('Invalid successful source')
            if r['returned_rows']!=len(data) or r['truncated']!=(len(data)>router.LIMIT):raise ValueError('Invalid coverage accounting')
            if any(str(int(float(x.get('bbl','0'))))!=parcel for x in data):raise ValueError('Source parcel identity mismatch')
            if r['id']=='pluto' and len(data)!=1:raise ValueError('Expected exactly one PLUTO tax lot')
    return parcel

def validate_claims(ir, receipts, folder):
    claims=ir['claims']; by_id={c['id']:c for c in claims}; sources={r['id']:r for r in receipts}
    if len(by_id)!=len(claims):raise ValueError('Duplicate claim ID')
    done=set();active=set()
    def visit(cid):
        if cid in active:raise ValueError('Claim dependency cycle')
        if cid not in by_id:raise ValueError('Unknown claim dependency')
        if cid in done:return
        active.add(cid);c=by_id[cid]
        if c['kind'] not in {'fact','assumption','calculation','judgment','unknown'}:raise ValueError('Untyped claim')
        for dep in c['inputs']:visit(dep)
        if c['kind']=='unknown' and (c['value'] is not None or not c['rationale']):raise ValueError('Unknown promoted to known')
        if c['kind']=='assumption' and not c['rationale']:raise ValueError('Unexplained assumption')
        if c['kind']=='fact' and not c['references']:raise ValueError('Uncited fact')
        for ref in c['references']:
            r=sources[ref['source_id']]
            if r['status']!='ok' or r['sha256']!=ref['sha256']:raise ValueError('Fact references unavailable/version-mismatched evidence')
            value=load(safe(folder,r['body_path']))
            for token in ref['pointer'].strip('/').split('/') if ref['pointer'] else []:
                value=value[int(token)] if isinstance(value,list) else value[token]
            if c['kind']=='fact' and c['value']!=value:raise ValueError('Citation value mismatch')
            if c['formula']=='len_source_array' and c['value']!=len(value):raise ValueError('Row-count mismatch')
        if c['kind']=='calculation' and c['formula']!='len_source_array':
            actual=model.calculate(c['formula'],[by_id[i]['value'] for i in c['inputs']])
            if c['value']!=actual:raise ValueError('Calculation mismatch')
        active.remove(cid);done.add(cid)
    for cid in by_id:visit(cid)

def build(folder):
    req=load(folder/'request.json'); receipts=load(folder/'receipts.json')
    parcel=validate_evidence(req,receipts,folder)
    ir=model.build(req,parcel,receipts,folder)
    validate_claims(ir,receipts,folder)
    save(folder/'workflow.json',load(WORKFLOW))
    save(folder/'ir.json',ir)
    prompt=packet.prompts(ir); prompt['model_sha256']=digest((folder/'ir.json').read_bytes())
    save(folder/'image-prompts.json',prompt)
    md,page,csv=packet.projections(ir,receipts)
    (folder/'packet.md').write_text(md)
    (folder/'packet.html').write_text(page)
    (folder/'calculation-steps.csv').write_text(csv)
    names=[str(p.relative_to(folder)) for p in sorted(folder.rglob('*')) if p.is_file() and p.name!='manifest.json']
    save(folder/'manifest.json',{'version':'0.2.0','resolved_bbl':parcel,'implementation':implementation(),'files':{n:digest(safe(folder,n).read_bytes()) for n in names},'validation_scope':'Byte bindings, typed claims, dependency arithmetic and deterministic exports; not semantic completeness or professional acceptance.'})
    return ir

def verify(folder):
    m=load(folder/'manifest.json')
    if m['implementation']!=implementation():raise ValueError('Implementation changed; this packet needs a versioned rebuild')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!=set(m['files'])|{'manifest.json'}:raise ValueError('Packet inventory changed')
    for name,h in m['files'].items():
        if digest(safe(folder,name).read_bytes())!=h:raise ValueError('Artifact hash mismatch: '+name)
    req=load(folder/'request.json');receipts=load(folder/'receipts.json');parcel=validate_evidence(req,receipts,folder)
    ir=load(folder/'ir.json');validate_claims(ir,receipts,folder)
    if ir!=model.build(req,parcel,receipts,folder):raise ValueError('Model differs from inputs and implementation')
    if load(folder/'workflow.json')!=load(WORKFLOW):raise ValueError('Workflow snapshot changed')
    prompt=packet.prompts(ir);prompt['model_sha256']=digest((folder/'ir.json').read_bytes())
    if (folder/'image-prompts.json').read_text()!=dumps(prompt):raise ValueError('Image prompt bindings changed')
    for name,text in zip(['packet.md','packet.html','calculation-steps.csv'],packet.projections(ir,receipts)):
        if (folder/name).read_text()!=text:raise ValueError('Packet projection changed: '+name)
    return {'status':'passed','bbl':parcel,'claims':len(ir['claims']),'sources':len(receipts),'professional_review':'pending','process_coverage':'partial','packet':str(folder/'packet.html')}

def collect(req,folder):
    validate_request(req);fresh(folder);save(folder/'request.json',req)
    parcel,receipts=router.collect(req,folder)
    validate_evidence(req,receipts,folder)
    return parcel

def run(req,folder):
    collect(req,folder);build(folder);return verify(folder)

def replay(source,folder,req=None):
    verify(source)
    chosen=req or load(source/'request.json');validate_request(chosen);fresh(folder)
    if req is None:shutil.copyfile(source/'request.json',folder/'request.json')
    else:save(folder/'request.json',chosen)
    shutil.copyfile(source/'receipts.json',folder/'receipts.json')
    shutil.copytree(source/'sources',folder/'sources')
    build(folder);return verify(folder)
