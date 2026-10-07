"""Receipt and review-evidence checks, not a backtest score. MIT."""
import hashlib,json,pathlib
BASE=pathlib.Path(__file__).resolve().parent
ROOT=BASE.parents[1]
def load(path):return json.loads(path.read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def validate():
    manifest=load(BASE/'manifest.json')
    for name,h in manifest['files'].items():
        if sha(ROOT/name)!=h:raise ValueError('Changed review/reference artifact: '+name)
    receipts=load(BASE/'receipts.json')
    for r in receipts:
        if r['status']=='retained':
            if sha(BASE/r['file'])!=r['sha256']:raise ValueError('Changed source body: '+r['id'])
            if sha(BASE/r['text_file'])!=r['text_sha256']:raise ValueError('Changed derived text: '+r['id'])
    checks={'hpd_425_selection.text':['April 28, 2016','241'],
            'hdc_425_opening.text':['Nov 2, 2022','277','$178 million'],
            'nyserda_425.text':['310,758','$121,942,998','$392.41'],
            'cpc_425_map.text':['November 29, 2017','C4-4','C6-3'],
            'wsfssh_fischer.text':['105','2025']}
    for name,anchors in checks.items():
        text=(BASE/'cache'/name).read_text()
        if any(a not in text for a in anchors):raise ValueError('Missing reference anchor: '+name)
    d=load(BASE/'review-disposition.json');b=load(ROOT/'research/conclusion-probe/outputs/baseline.json')
    if d['reviewed_packet_basis']!=b['basis_fingerprint']:raise ValueError('Review basis changed')
    e=d['findings'][0]['evidence']
    if sha(ROOT/e['file'])!=e['sha256'] or load(ROOT/e['file'])[e['row']]!=e['exact_record']:raise ValueError('Omitted-record evidence changed')
    v=lambda k:b['claims']['scenario.2028710002.A.'+k]['value']
    calc=d['findings'][1]['calculation']
    if abs(calc['baseline_non_debt_capital']-(v('ex_land_cost')-v('illustrative_loan')))>0.01:raise ValueError('Capital base mismatch')
    if abs(calc['total_non_debt_capital_under_fixed_assumed_loan_and_rent']-(v('ex_land_cost')-v('illustrative_loan')+v('additional_non_debt_capital')))>0.01:raise ValueError('Capital total mismatch')
    shells=[r for r in receipts if r.get('substantive_case_evidence') is False]
    if len(shells)!=2:raise ValueError('Login/award boundary changed')
    if d['human_review']!='pending' or d['backtest_executed_in_this_slice'] is not False:raise ValueError('Unsupported review/backtest promotion')
    return {'request_receipts':len(receipts),'retained_responses':sum(r['status']=='retained' for r in receipts),
            'substantive_reference_documents':sum(r.get('substantive_case_evidence') is True for r in receipts),
            'review':'fresh_context_AI_requires_revision','human_review':'pending','new_backtest':'not_executed','integrity':'pass'}
if __name__=='__main__':print(json.dumps(validate(),indent=2))
