"""Read-only package and numerical sensitivity replay. MIT."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from housing_underwriting.engine import load,digest
from housing_site_search import engine,comparison,area_handoff,pipeline_handoff,model
from housing_geometry import engine as geometry
import json,math
BASE=Path(__file__).parent/'cases'
# Floating-point area sums can differ in the last few bits between CPU architectures
# (the retained case was built on Apple Silicon; CI runs on x86-64 Linux).
FLOAT_REL_TOL=1e-9
FLOAT_DERIVED={'geometry.json','packet.html','visual-handoff.json'}


def close(a,b):
    if isinstance(a,float) or isinstance(b,float):
        return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isclose(a,b,rel_tol=FLOAT_REL_TOL,abs_tol=1e-6)
    if isinstance(a,dict):return isinstance(b,dict) and a.keys()==b.keys() and all(close(a[k],b[k]) for k in a)
    if isinstance(a,list):return isinstance(b,list) and len(a)==len(b) and all(close(x,y) for x,y in zip(a,b))
    return a==b


def geometry_verify(folder):
    """Exact replay where the platform reproduces the retained bytes; otherwise require
    unchanged retained files, the same implementation, byte-identical non-numeric
    outputs and a recomputed geometry that agrees within FLOAT_REL_TOL."""
    try:return geometry.verify(folder)
    except ValueError as exc:
        if 'Geometry output differs' not in str(exc):raise
    m=load(folder/'manifest.json')
    assert m['implementation']==geometry.implementation() and m['files']==geometry.inventory(folder)
    fresh=geometry.compile_run(folder)
    for name,content in fresh.items():
        if name not in FLOAT_DERIVED:assert (folder/name).read_bytes()==content.encode(),name
    assert close(json.loads(fresh['geometry.json']),load(folder/'geometry.json'))
    handoff=load(folder/'visual-handoff.json')
    assert handoff['geometry_ir_sha256']==digest((folder/'geometry.json').read_bytes())
    assert close({**json.loads(fresh['visual-handoff.json']),'geometry_ir_sha256':None},{**handoff,'geometry_ir_sha256':None})
    print('Geometry: retained bytes intact; replay on this CPU agrees within relative tolerance '+str(FLOAT_REL_TOL)+'.')
    return {'status':'passed'}


verifiers={'cost-comparison':comparison.verify,'hunts':engine.verify,'area-handoff':area_handoff.verify,'deeper-evidence':pipeline_handoff.verify,'geometry':geometry_verify}
for name,record in load(BASE/'case-manifests.json').items():
    folder=BASE/name
    assert digest((folder/'manifest.json').read_bytes())==record['manifest_sha256']
    assert verifiers[name](folder)['status']=='passed'
left=BASE/'cost-comparison/left'
for copy in [BASE/'area-handoff/search',BASE/'deeper-evidence/handoff/search']:
    assert (copy/'manifest.json').read_bytes()==(left/'manifest.json').read_bytes()
for record in load(BASE/'sensitivities.json'):
    folder=BASE/record['baseline_case']
    result=model.evaluate(load(folder/'discovery/ir.json'),record['financial_request'],record['search_request'])
    assert result['counts']==record['expected_counts']
    assert result['detailed_trial_ids']==record['expected_detail_ids']
for folder,expected in [(left,61),(BASE/'hunts',29)]:
    result=load(folder/'results.json')
    assert result['counts']['lots_by_status']['matches_declared_targets']==expected
assert load(BASE/'cost-comparison/right/results.json')['counts']['lots_by_status'].get('matches_declared_targets',0)==0
print('Site goal search: five complete packages, unchanged reviewed ancestry, 61/29 conditional matching lots, cost challenge and four numerical sensitivities passed.')
