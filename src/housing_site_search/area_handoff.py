"""Explicit selected-program adapter to the existing verified parcel/area module. MIT.

The adapter preserves the search and financial model; it never infers entitlement
or promotes a selected numerical program into a verified building design.
"""
from pathlib import Path
import shutil
from housing_common.packages import digest,load,save,fresh
from housing_workflow import engine as parcel
from housing_underwriting import engine as underwriting
from . import engine as search


def selection(search_folder,identity,evidence_folder):
    ir,template=search.input_state(search_folder/'discovery',search_folder/'underwriting-template')
    req=load(search_folder/'request.json');result=load(search_folder/'results.json')
    matches=[x for x in result['trials'] if x['id']==identity]
    if len(matches)!=1:raise ValueError('Choose one existing scenario id from the verified search')
    trial=matches[0];verified=parcel.verify(evidence_folder)
    if verified['bbl']!=trial['bbl']:raise ValueError('Parcel evidence belongs to a different selected lot')
    model=search.trial_request(ir,template,req,trial)
    from .model import dec
    gross=dec(model['program']['gross_area_sf']);share=dec(req['program_grid']['residential_share_of_gross'])
    rationale='Analyst scenario selected from verified finite search '+identity+'. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately.'
    scenario={'name':identity,'gross_area_sf':{'value':float(gross),'rationale':rationale},
              'nonresidential_gross_sf':{'value':float(gross*(1-share)),'rationale':rationale+' Nonresidential share is 1 minus the explicit residential share of gross.'},
              'residential_net_efficiency':{'value':float(dec(req['program_grid']['net_efficiency'])),'rationale':rationale+' Declared net/residential-gross conversion, not a floor plan.'},
              'average_net_home_sf':{'value':float(dec(req['program_grid']['net_sf_per_home'])),'rationale':rationale+' Net sf per proposed home; the legacy area module reports fractional home-equivalents.'}}
    request={'version':'0.2.0','bbl':trial['bbl'],'question':('Selected program area handoff for '+trial['bbl']+'. '+req['question']+' The source search status is '+trial['status']+'. Treat all program dimensions as assumptions and retain the separate financial packet.')[:1900],'scenario':scenario}
    record={'trial_id':identity,'bbl':trial['bbl'],'source_search_status':trial['status'],
            'search_manifest_sha256':digest((search_folder/'manifest.json').read_bytes()),
            'parcel_evidence_manifest_sha256':digest((evidence_folder/'manifest.json').read_bytes()),
            'proposed_homes':trial['proposed_homes'],'scenario':scenario,
            'meaning':'Explicit program-to-area adapter. Existing parcel and geometry modules retain their own verification and unknowns; no feasibility or legal building program is inferred.'}
    return record,request,model


def text(record):
    return '# Selected-program area handoff\n\n'+record['meaning']+'\n\nSelected scenario: '+record['trial_id']+'. Original search status: '+record['source_search_status']+'.\n\n'+str(record['proposed_homes'])+' proposed homes are scenario inputs; the area module computes fractional home-equivalents under the supplied conversions.\n\n[Area/evidence packet](analysis/packet.md) · [Selected financial model](selected-underwriting/packet.md) · [Full search and retained sources](search/packet.md).\n\nThe existing geometry module can consume analysis/ with a separately sourced parcel polygon and explicit footprints/heights/use shares. Agreement is schematic containment/area consistency, not zoning, floor-plan or financial feasibility.\n'


def build(search_folder,identity,evidence_folder,out):
    search_folder,evidence_folder=Path(search_folder),Path(evidence_folder);search.verify(search_folder)
    record,request,model=selection(search_folder,identity,evidence_folder)
    out=fresh(out);shutil.copytree(search_folder,out/'search');shutil.copytree(evidence_folder,out/'parcel-evidence')
    parcel.replay(out/'parcel-evidence',out/'analysis',request)
    files={x['id']:out/'search/underwriting-template'/x['body_path'] for x in load(out/'search/underwriting-template/references.json') if x['retention']=='retained_bytes'}
    underwriting.build(model,out/'selected-underwriting',files)
    save(out/'selection.json',record);(out/'packet.md').write_text(text(record));seal(out);return verify(out)


def implementation():
    return {**search.implementation(),**{'parcel:'+k:v for k,v in parcel.implementation().items()}}


def seal(folder):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':'search-area-handoff','implementation':implementation(),'files':files})


def verify(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('kind')!='search-area-handoff' or m.get('version')!='1.0.0' or m.get('implementation')!=implementation():raise ValueError('Unknown or changed selected-program handoff')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Area-handoff inventory changed')
    for name,sha in m['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Area-handoff artifact changed: '+name)
    search.verify(folder/'search');record=load(folder/'selection.json')
    expected,request,model=selection(folder/'search',record['trial_id'],folder/'parcel-evidence')
    parcel.verify(folder/'analysis');underwriting.verify(folder/'selected-underwriting')
    if (folder/'analysis/replay-source-manifest.json').read_bytes()!=(folder/'parcel-evidence/manifest.json').read_bytes():raise ValueError('Area analysis replay differs from retained parcel-evidence capture')
    if record!=expected or load(folder/'analysis/request.json')!=request or load(folder/'selected-underwriting/request.json')!=model:raise ValueError('Area handoff differs from the selected model and source evidence')
    if load(folder/'selected-underwriting/references.json')!=load(folder/'search/underwriting-template/references.json'):raise ValueError('Selected financial model changed reference lineage')
    if (folder/'packet.md').read_text()!=text(record):raise ValueError('Area-handoff summary changed')
    return {'status':'passed','bbl':record['bbl'],'selected_trial':record['trial_id'],'source_search_status':record['source_search_status'],'packet':str(folder/'packet.md'),'professional_review':'pending'}
