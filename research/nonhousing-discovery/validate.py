"""Read-only replay of broad discovery, source contexts and known-case challenges. MIT."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from housing_site_discovery import engine
from housing_site_discovery.common import load,number
from housing_workflow.engine import verify as verify_parcel


def main():
    cases=Path(__file__).parent/'cases';findings=load(cases/'findings.json')
    for place in ['jerome','hunts']:
        folder=cases/place
        assert engine.verify(folder)['status']=='passed'
        ir=load(folder/'ir.json');assert ir['counts']==findings[place]['counts']
        previous=ROOT/f'research/discovery-v1/cases/{place}-deep/handoff/screen/parent'
        assert engine.legacy_difference(folder,previous)==load(cases/f'{place}-method-change.json')
        reqs=engine.followup_requests(ir,findings[place]['followups'])
        assert reqs==load(cases/f'{place}-followup-requests.json')
        for req in reqs:
            parcel=cases/'parcels'/req['bbl'];assert verify_parcel(parcel)['status']=='passed'
            assert load(parcel/'request.json')==req
    # The two attractive non-auto examples must preserve their actual source challenge.
    for identity in ['2028310056','2027350020']:
        parcel=cases/'parcels'/identity
        signals=[]
        for provider in ['dob_bis','dob_now']:
            for row in load(parcel/f'sources/{provider}.json'):
                signals.extend(number(row.get(k)) for k in ['existing_dwelling_units','proposed_dwelling_units'] if number(row.get(k)) is not None and number(row.get(k))>0)
        assert signals,identity+' lost its recorded housing-history challenge'
    reviews=cases/'reviews'
    from housing_site_review.engine import verify
    for place in ['jerome','hunts']:
        assert verify(reviews/place)['status']=='passed'
        data=load(reviews/place/'review.json')
        assert data['counts']==findings[place]['housing_review_counts']
        assert data['source_coverage']==findings[place]['housing_review_source_coverage']
        assert data['capture_mode']['mode']=='retained_raw_offline_replay' and data['new_receipts']==0
        base=load(cases/place/'ir.json');reviewed=load(reviews/place/'ir.json')
        assert [(x['bbl'],x['in_recorded_nonhousing_set']) for x in base['lots']]==[(x['bbl'],x['in_recorded_nonhousing_set']) for x in reviewed['lots']]
    print('Broad discovery replay passed: 3,164 lots, 969 recorded-nonhousing, two source/method cases, four deeper source challenges and retained four-source housing reviews.')


if __name__=='__main__':main()
