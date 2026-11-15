"""Compose verified discovery with a verified financial template. MIT."""
from pathlib import Path
import shutil
from housing_underwriting import engine as underwriting
from housing_site_discovery import engine as discovery
from housing_common import site_inputs
from housing_common.local_outputs import ROOT
from housing_underwriting.engine import digest,load,save,dumps,fresh
from .model import evaluate,build_trial_request
from .packet import project


def implementation():
    paths=sorted(Path(__file__).parent.glob('*.py'))+sorted(Path(__file__).parent.glob('*.json'))
    skill=ROOT/'skills/goal-seek-housing-sites/SKILL.md'
    if skill.exists():paths+=[skill]+sorted((skill.parent/'references').glob('*.md'))
    paths+=[ROOT/'src/housing_common/site_inputs.py',ROOT/'src/housing_common/packages.py']
    return {**underwriting.implementation(),**{str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}}


def seal(folder):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':'site-search','implementation':implementation(),'files':files})


def verify_files(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('kind')!='site-search' or m.get('version')!='1.0.0' or m.get('implementation')!=implementation():raise ValueError('Unknown or changed site-search implementation')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Search file inventory changed')
    for name,sha in m['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Changed or escaping search file: '+name)


def input_state(source,template):
    source,template=Path(source),Path(template);ir=site_inputs.state(source);underwriting.verify(template)
    return ir,load(template/'request.json')


def trial_request(ir,template,req,row):
    from .model import dec
    lot=next(x for x in ir['lots'] if x['bbl']==row['bbl'])
    return build_trial_request(template,req,lot,row['proposed_homes'],dec(row['assumed_land_usd_per_lot_sf']),row['id'])


def build(source,template,req,out):
    ir,base=input_state(source,template);result=evaluate(ir,base,req);out=fresh(out)
    shutil.copytree(source,out/'discovery');shutil.copytree(template,out/'underwriting-template')
    save(out/'request.json',req);save(out/'results.json',result)
    save(out/'origin.json',{'discovery_manifest_sha256':digest((Path(source)/'manifest.json').read_bytes()),'underwriting_template_manifest_sha256':digest((Path(template)/'manifest.json').read_bytes())})
    by_id={x['id']:x for x in result['trials']}
    source_files={x['id']:out/'underwriting-template'/x['body_path'] for x in load(out/'underwriting-template/references.json') if x['retention']=='retained_bytes'}
    for identity in result['detailed_trial_ids']:
        model=trial_request(ir,base,req,by_id[identity]);underwriting.build(model,out/'models'/identity,source_files)
    for name,body in project(req,result).items():(out/name).write_text(body)
    seal(out);return verify(out)


def verify(folder):
    folder=Path(folder);verify_files(folder);ir,base=input_state(folder/'discovery',folder/'underwriting-template')
    origin={'discovery_manifest_sha256':digest((folder/'discovery/manifest.json').read_bytes()),'underwriting_template_manifest_sha256':digest((folder/'underwriting-template/manifest.json').read_bytes())}
    if load(folder/'origin.json')!=origin:raise ValueError('Search origin changed')
    req=load(folder/'request.json');result=evaluate(ir,base,req)
    if load(folder/'results.json')!=result:raise ValueError('Search differs from recomputation')
    by_id={x['id']:x for x in result['trials']}
    for identity in result['detailed_trial_ids']:
        underwriting.verify(folder/'models'/identity)
        if load(folder/'models'/identity/'references.json')!=load(folder/'underwriting-template/references.json'):raise ValueError('Detailed model reference lineage differs from retained template')
        if load(folder/'models'/identity/'request.json')!=trial_request(ir,base,req,by_id[identity]):raise ValueError('Detailed model differs from selected trial')
    for name,body in project(req,result).items():
        if (folder/name).read_text()!=body:raise ValueError('Search projection changed: '+name)
    return {'status':'passed',**result['counts'],'packet':str(folder/'packet.html'),'professional_review':'pending'}


def handoff(folder,selected,out):
    """Preserve the complete reviewed search while delegating parcel evidence."""
    from . import pipeline_handoff
    return pipeline_handoff.handoff(folder,selected,out)
