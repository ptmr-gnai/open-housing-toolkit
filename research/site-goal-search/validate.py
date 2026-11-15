"""Read-only package and numerical sensitivity replay. MIT."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from housing_underwriting.engine import load,digest
from housing_site_search import engine,comparison,area_handoff,pipeline_handoff,model
from housing_geometry.engine import verify as geometry_verify
BASE=Path(__file__).parent/'cases'
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
