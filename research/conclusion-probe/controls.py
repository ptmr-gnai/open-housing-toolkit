"""Explicitly synthetic perturbations of copied snapshots. MIT."""
import copy, pathlib, shutil, tempfile
from conclusion_engine import ROOT, BASE, load, write, sha, build, compare
from pipeline import bbl

def snapshot(folder):
    folder = pathlib.Path(folder)
    shutil.copytree(ROOT/'cache',folder/'cache')
    shutil.copy2(ROOT/'probe.json',folder/'probe.json')
    return folder

def mutate(folder, source_id, change, description, update_receipt=True):
    receipt_path = folder/'cache'/(source_id+'.source.json')
    receipt = load(receipt_path); body = folder/receipt['cache_path']
    data = load(body); change(data); write(body,data)
    if update_receipt:
        receipt.update(kind='synthetic',parent_sha256=receipt['sha256'],parent_url=receipt['url'],
                       parent_retrieved_at=receipt['retrieved_at'],url='fixture://conclusion-probe/'+description,
                       retrieved_at=None,sha256=sha(body.read_bytes()),bytes=body.stat().st_size,
                       mutation=description,coverage_limits='SYNTHETIC fault control on a copied cached snapshot; not new site evidence.')
        write(receipt_path,receipt)

def competing(folder, field='unitsres', value=48, version='26v2'):
    path = folder/'competing.json'
    write(path,{'synthetic':True,'subject_bbl':'2028710002','field':field,'value':value,'version':version})
    return {'receipt':{'id':'competing_control','kind':'synthetic','cache_path':'competing.json','sha256':sha(path.read_bytes()),
                       'url':'fixture://conclusion-probe/competing','publisher':'Synthetic test author','retrieved_at':None}}

def run_control(control, baseline):
    ident = control['id']; config = load(ROOT/'probe.json'); rival = None
    with tempfile.TemporaryDirectory() as d:
        folder = snapshot(d)
        if ident in ['higher_cost','lower_cost']:
            config['assumptions']['hard_cost_per_gsf']['value'] = control['value']
        elif ident in ['smaller_lot','positive_units','unreceipted_source_change']:
            def change(rows):
                row = next(r for r in rows if bbl(r.get('bbl')) == '2028710002')
                if ident=='positive_units': row['unitsres']=str(control['value'])
                else: row['lotarea']=str(float(row['lotarea'])*control.get('factor',0.8))
            mutate(folder,'pluto_universe',change,ident,ident!='unreceipted_source_change')
        elif ident in ['contradictory_units','different_vintage_units']:
            rival=competing(folder,value=control['value'],version='26v2' if ident=='contradictory_units' else '25v1')
        elif ident in ['missing_occupancy_gate','missing_finance_gate']:
            config['required_gates'].remove('current_occupancy_and_leases' if ident=='missing_occupancy_gate' else 'full_cost_and_financing')
        elif ident=='missing_historical_passage':
            mutate(folder,'dob_bis_2028710002',lambda rows:rows[3].pop('job_description'),'missing_historical_passage')
        elif ident!='baseline': raise ValueError('Unknown control')
        try:
            result=build(folder,config,rival,baseline['basis_fingerprint'])
        except ValueError as error:
            return {'id':ident,'expected':control['expect'],'status':'rejected','error':str(error),'synthetic_control':ident!='baseline'},None
    result['control_id']=ident
    result['synthetic_input']=result['synthetic_input'] or ident!='baseline'
    return {'id':ident,'expected':control['expect'],'status':'evaluated','disposition':result['disposition'],
            'synthetic_control':ident!='baseline','diff':compare(baseline,result),
            'release':result['release'],'metrics':metrics(result)},result

def metrics(result):
    c=result['claims'];p='scenario.2028710002.A.'
    return {name:c[p+name]['value'] for name in ['gross_sf','units','ex_land_cost','debt_support_rent_month','additional_non_debt_capital']}

def expected_response(control, baseline):
    ident=control['id']; m=control.get('metrics',{}); b=metrics(baseline)
    if ident=='baseline': return control['disposition']=='investigate_current_uses_and_leases' and control['diff']['prior_judgment_basis']=='matches'
    if ident=='higher_cost':
        return abs(m['debt_support_rent_month']/b['debt_support_rent_month']-1.5)<1e-10 and m['units']==b['units'] and control['disposition']==baseline['disposition'] and not control['release']['acquisition_or_design_clearance']
    if ident=='lower_cost':
        return m['additional_non_debt_capital']==0 and control['disposition']==baseline['disposition'] and not control['release']['acquisition_or_design_clearance']
    if ident=='smaller_lot':
        return abs(m['gross_sf']/b['gross_sf']-0.8)<1e-10 and m['units']<b['units'] and control['diff']['prior_judgment_basis']=='stale'
    if ident=='positive_units': return control['disposition']=='reassess_resident_impacts_before_design' and control['diff']['prior_judgment_basis']=='stale'
    if ident=='contradictory_units': return control['disposition']=='hold_for_source_reconciliation' and not control['release']['investigation_conclusion']
    if ident=='different_vintage_units': return control['disposition']=='hold_for_temporal_reconciliation' and not control['release']['investigation_conclusion']
    if ident in ['missing_occupancy_gate','missing_finance_gate']: return control['status']=='rejected' and 'Required gate inventory' in control['error']
    if ident=='missing_historical_passage': return control['disposition']=='hold_for_missing_evidence' and not control['release']['investigation_conclusion']
    if ident=='unreceipted_source_change': return control['status']=='rejected' and 'Source cache hash mismatch' in control['error']
    return False
