"""Preserve reviewed search lineage while reusing evidence-only parcel handoffs. MIT."""
from pathlib import Path
import shutil
from housing_common import site_inputs
from housing_common.packages import digest,load,save,fresh
from housing_site_discovery import engine as sites
from . import engine as search

SELECTION_MEANING='Explicit evidence-only selection; full reviewed search and financial assumptions are retained, not replaced with the earlier broad inventory.'
HANDOFF_TEXT='# Selected search evidence handoff\n\nFull zoning/dwelling/public-context review and models: [search packet](search/packet.md).\n\nExisting supported evidence-only requests: [site handoff](site-handoff/requests.json). No modeled program is supplied to the parcel workflow.\n'
DEEP_TEXT='# Search and deeper evidence\n\n[Reviewed search and financial scenarios](handoff/search/packet.md) remain attached to the selected lots. Fresh known-lot outputs are under parcel-investigation/; inspect every source status there. Existing historical review and a fresh request can have different coverage.\n'


def implementation():return search.implementation()


def seal(folder,kind):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':kind,'implementation':implementation(),'files':files})


def handoff(folder,selected,out):
    folder=Path(folder);search.verify(folder)
    result=load(folder/'results.json');matched={x['bbl'] for x in result['trials'] if x['status']=='matches_declared_targets'}
    if not isinstance(selected,list) or not selected or len(selected)!=len(set(selected)) or not set(selected)<=matched:raise ValueError('Choose unique matching BBLs; other nonhousing lots remain available through broad discovery')
    out=fresh(out);shutil.copytree(folder,out/'search')
    sites.handoff(site_inputs.original_discovery(folder/'discovery'),selected,out/'site-handoff')
    save(out/'selection.json',{'bbls':selected,'search_manifest_sha256':digest((folder/'manifest.json').read_bytes()),'meaning':SELECTION_MEANING})
    (out/'packet.md').write_text(HANDOFF_TEXT)
    seal(out,'search-handoff');return verify(out)


def deepen(folder,out):
    folder=Path(folder);verify(folder)
    if load(folder/'manifest.json')['kind']!='search-handoff':raise ValueError('Provide a verified search handoff')
    out=fresh(out);shutil.copytree(folder,out/'handoff')
    sites.deepen(folder/'site-handoff',out/'parcel-investigation')
    save(out/'origin.json',{'handoff_manifest_sha256':digest((folder/'manifest.json').read_bytes())})
    (out/'packet.md').write_text(DEEP_TEXT)
    seal(out,'search-investigation');return verify(out)


def verify(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json');kind=m.get('kind')
    if kind not in ['search-handoff','search-investigation'] or m.get('version')!='1.0.0' or m.get('implementation')!=implementation():raise ValueError('Unknown or changed search handoff implementation')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Search-handoff file inventory changed')
    for name,sha in m['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Search-handoff artifact changed: '+name)
    if kind=='search-handoff':
        search.verify(folder/'search');sites.verify(folder/'site-handoff')
        selection=load(folder/'selection.json');result=load(folder/'search/results.json')
        expected_selection={'bbls':load(folder/'site-handoff/selection.json')['bbls'],'search_manifest_sha256':digest((folder/'search/manifest.json').read_bytes()),'meaning':SELECTION_MEANING}
        if selection!=expected_selection or (folder/'packet.md').read_text()!=HANDOFF_TEXT:raise ValueError('Search-handoff metadata or packet differs from replay')
        matched={x['bbl'] for x in result['trials'] if x['status']=='matches_declared_targets'}
        if not set(selection['bbls'])<=matched or selection['bbls']!=load(folder/'site-handoff/selection.json')['bbls'] or selection['search_manifest_sha256']!=digest((folder/'search/manifest.json').read_bytes()):raise ValueError('Search-handoff selection differs')
        original=site_inputs.original_discovery(folder/'search/discovery')
        if digest((original/'manifest.json').read_bytes())!=digest((folder/'site-handoff/discovery/manifest.json').read_bytes()):raise ValueError('Search-handoff base discovery differs')
        return {'status':'passed','selected_bbls':selection['bbls'],'retains_full_search_reviews':True,'packet':str(folder/'packet.md')}
    if (folder/'packet.md').read_text()!=DEEP_TEXT:raise ValueError('Search investigation summary differs from replay')
    verify(folder/'handoff');sites.verify(folder/'parcel-investigation')
    if load(folder/'origin.json')!={'handoff_manifest_sha256':digest((folder/'handoff/manifest.json').read_bytes())}:raise ValueError('Search investigation handoff differs')
    if digest((folder/'handoff/site-handoff/manifest.json').read_bytes())!=digest((folder/'parcel-investigation/handoff/manifest.json').read_bytes()):raise ValueError('Deeper evidence differs from selected handoff')
    return {'status':'passed','selected_bbls':load(folder/'handoff/selection.json')['bbls'],'retains_full_search_reviews':True,'packet':str(folder/'packet.md')}
