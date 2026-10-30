"""Small explicit model: evidence, uncertainty and optional area arithmetic. MIT."""
from decimal import Decimal, InvalidOperation
from pathlib import Path
from .contracts import Claim, Kind, digest, load, validate_request

UNKNOWNS = {
    'current_use':'Current occupancy, leases, lawful use and displacement implications are not established by these records.',
    'title':'Title, site control and owner willingness have not been investigated.',
    'entitlement':'Applicable zoning text, special districts, amendments, approvals and legal capacity are not determined.',
    'physical_fit':'Survey, envelope, access, egress, layouts and geotechnical fit are not validated.',
    'environment':'Environmental requirements, studies and satisfaction status have not been reconciled.',
    'finance':'Complete development cost, affordability program, capital sources and commitments are not modeled.',
    'transit':'Walked access, service reliability, accessibility and job access are not modeled.',
    'process_coverage':'This is a partial playbook. The complete practitioner process and all material requirements are not known.'
}

def number(value):
    try:
        v = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError('Non-numeric calculation input') from exc
    if not v.is_finite():raise ValueError('Non-finite calculation input')
    return v

def calculate(formula, values):
    v = [number(x) for x in values]
    if formula == 'subtract': answer = v[0] - v[1]
    elif formula == 'multiply': answer = v[0] * v[1]
    elif formula == 'divide':
        if v[1] <= 0:raise ValueError('Non-positive calculation denominator')
        answer = v[0] / v[1]
    else:raise ValueError('Unknown formula')
    return float(answer)

def fact_unit(field):
    if field in {'lotarea','bldgarea'}:return 'square feet as recorded'
    if 'dwelling_units' in field or field in {'unitsres','unitstotal'}:return 'units as recorded; source definition applies'
    return 'source value'

def build(req, parcel, receipts, root):
    validate_request(req)
    claims = []
    signals = []
    source_states = []
    def add(c):claims.append(c);return c.id
    for receipt in receipts:
        sid = receipt['id']
        source_states.append({'source':sid, 'status':receipt['status'], 'returned_rows':receipt['returned_rows'], 'truncated':receipt['truncated'], 'limits':receipt['limits'], 'retrieved_at':receipt['retrieved_at']})
        if receipt['status'] != 'ok':
            add(Claim('source.'+sid+'.unknown',Kind.UNKNOWN, sid+' evidence unavailable',None,'unknown',rationale=receipt.get('error','Failed collection')))
            continue
        raw = (root / receipt['body_path']).read_bytes()
        if digest(raw) != receipt['sha256']:raise ValueError('Source bytes changed: ' + sid)
        data = load(root / receipt['body_path'])
        if sid == 'address_resolution':continue
        add(Claim(sid+'.returned_rows',Kind.CALCULATION,sid+' returned rows in this exact-BBL query',len(data),'returned rows; not projects or total population',references=[{'source_id':sid,'pointer':'','sha256':receipt['sha256']}],formula='len_source_array',rationale='Bounded query; see truncation and source limits.'))
        for index,row in enumerate(data):
            if str(int(float(row.get('bbl','0')))) != parcel:raise ValueError('Parcel mismatch while modeling')
            for key,value in sorted(row.items()):
                claim_id = sid+'.'+str(index)+'.'+key
                add(Claim(claim_id,Kind.FACT,sid+' row '+str(index)+' '+key,value,fact_unit(key),references=[{'source_id':sid,'pointer':'/'+str(index)+'/'+key,'sha256':receipt['sha256']}]))
                if sid.startswith('dob_') and key in {'existing_dwelling_units','proposed_dwelling_units'}:
                    try:positive = number(value) > 0
                    except ValueError:positive = False
                    if positive:signals.append(claim_id)
        if receipt['truncated']:
            add(Claim('source.'+sid+'.coverage',Kind.UNKNOWN,sid+' complete query coverage',None,'unknown',rationale='Row cap reached; retained rows are a bounded sample, not a complete history.'))
    scenario = req.get('scenario')
    if scenario:
        units={'gross_area_sf':'gross sf','nonresidential_gross_sf':'gross sf','residential_net_efficiency':'share','average_net_home_sf':'net sf per home-equivalent'}
        for key,unit in units.items():
            add(Claim('scenario.'+key,Kind.ASSUMPTION,key,scenario[key]['value'],unit,rationale=scenario[key]['rationale']))
        def calc(i,label,formula,inputs,unit):
            by_id={c.id:c for c in claims}
            add(Claim(i,Kind.CALCULATION,label,calculate(formula,[by_id[x].value for x in inputs]),unit,inputs=inputs,formula=formula,rationale='User-stated area budget; not a verified design or entitlement.'))
        calc('scenario.residential_gross_sf','Residential gross area allocation','subtract',['scenario.gross_area_sf','scenario.nonresidential_gross_sf'],'gross sf')
        calc('scenario.residential_net_sf','Residential net area allowance','multiply',['scenario.residential_gross_sf','scenario.residential_net_efficiency'],'net sf')
        calc('scenario.home_equivalents','Area-budget home-equivalents','divide',['scenario.residential_net_sf','scenario.average_net_home_sf'],'home-equivalents; not a feasible unit count')
        if any(c.id == 'pluto.0.lotarea' for c in claims):
            try:
                if number(next(c.value for c in claims if c.id=='pluto.0.lotarea')) > 0:
                    calc('scenario.gross_to_recorded_lot_ratio','Proposed gross area / recorded lot area','divide',['scenario.gross_area_sf','pluto.0.lotarea'],'gross-to-lot ratio; NOT zoning FAR')
            except ValueError:pass
    else:
        add(Claim('scenario.unspecified',Kind.UNKNOWN,'No development scenario supplied',None,'unknown',rationale='Evidence gathering is useful without inventing a building program.'))
    for key,reason in UNKNOWNS.items():
        add(Claim('unknown.'+key,Kind.UNKNOWN,key,None,'unknown',rationale=reason))
    if signals:
        basis=signals + (['pluto.0.unitsres'] if any(c.id=='pluto.0.unitsres' for c in claims) else [])
        add(Claim('review.housing_signals',Kind.JUDGMENT,'Reconcile heterogeneous housing evidence','reconciliation_needed','unreviewed author policy',inputs=basis,rationale='DOB historical existing/proposed units and PLUTO recorded units are different observations. Preserve all positive signals; obtain approved plans, certificates and current-use evidence before concluding occupancy or displacement. No units are summed across filings.'))
    add(Claim('review.next_diligence',Kind.JUDGMENT,'Questions for practitioner review','Review current-use evidence, entitlement pathway, physical constraints and capital structure.','unreviewed author policy',inputs=['unknown.current_use','unknown.entitlement','unknown.physical_fit','unknown.finance'],rationale='A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.'))
    return {'version':'0.2.0','workflow':'parcel-investigation','process_status':'partial_playbook_under_development','resolved_bbl':parcel,'question':req['question'],'scenario_name':scenario['name'] if scenario else None,'request_sha256':digest((root/'request.json').read_bytes()),'claims':[c.to_dict() for c in claims],'sources':source_states,'housing_signal_claims':signals,'interpretation_review':'pending','scope':'Current retrieved records, exact tax-lot match; no complete historical reconstruction or professional clearance.'}
