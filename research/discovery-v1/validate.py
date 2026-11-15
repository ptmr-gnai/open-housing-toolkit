"""Read-only replay of retained real discovery cases. MIT."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'src'))
from housing_discovery.common import digest, load
from housing_discovery.engine import differences, verify
from housing_discovery.screen import evaluate


def main():
    cases = Path(__file__).parent/'cases'
    for name in ['jerome-deep','hunts-deep','jerome-far8']:
        assert verify(cases/name)['status']=='passed'
    findings=load(cases/'findings.json')
    parents={p:cases/f'{p}-deep/handoff/screen/parent' for p in ['jerome','hunts']}
    screens={'jerome-far6':parents['jerome'],'hunts-far6':parents['hunts'],
             'jerome-auto':parents['jerome'].parent,'hunts-auto':parents['hunts'].parent,
             'jerome-far8':cases/'jerome-far8'}
    for key,path in screens.items():
        assert load(path/'ir.json')['counts']==findings['counts'][key],key
    inv=load(parents['jerome']/'evidence/inventory.json')
    public=evaluate(inv,load(ROOT/'config/discovery/jerome-public-review.json'))
    assert public['counts']==findings['counts']['jerome-public']
    for p in ['jerome','hunts']:
        assert digest((parents[p]/'evidence/manifest.json').read_bytes())==findings['source_manifest_sha256'][p]
        assert load(cases/f'{p}-deep/handoff/selection.json')['bbls']==findings['deep_followups'][p]
        ir=load(screens[p+'-auto']/'ir.json')
        for row in ir['lots']:
            if row['shortlisted']:
                assert row['recorded_residential_units']==0 and row['matches_use_focus']
    assert differences(parents['jerome'],cases/'jerome-far8')==load(cases/'far-sensitivity.json')
    assert differences(parents['jerome'],parents['jerome'].parent)==load(cases/'auto-focus-comparison.json')
    print('Discovery case replay passed: 3,164 lots; two auto-focus cases; three deeper investigations; same-source sensitivity.')


if __name__=='__main__':main()
