"""Typed conditional comparisons. All narratives consume the same claim graph. MIT."""
from .contracts import Claim, Kind as K, Unit as U, validate_request
from .methods import evaluate
from housing_workflow.contracts import digest

LIMITS=[
 'Hypothetical household profiles, not observed beneficiaries; no eligibility or availability determination.',
 'Cost threshold and exact bedroom match are diagnostic criteria, not an agency affordability or compliance certification.',
 'All program quantities and restriction durations are explicit assumptions; restrictions are proposed, delivery unknown.',
 'No established future no-action baseline; no project-attributable benefit, net new homes or causal rent/displacement estimate.',
 'Existing occupancy and direct losses unresolved; zero recorded homes does not establish no displacement.',
 'No transit-access, public-resource, financing, geometric-fit or emissions model executed by this module.',
 'Historical reference values in the declared price year, not a current rent forecast or inflation-adjusted projection.'
]


def compile_model(req,reference,analysis,analysis_sha,request_sha,reference_sha):
    validate_request(req)
    if req['site_bbl']!=analysis['resolved_bbl']:raise ValueError('Program and verified analysis parcel mismatch')
    if req['price_year']!=reference['income_year'] or req['price_year']!=reference['rent_year']:
        raise ValueError('Request price year and reference schedule vintages differ; no automatic inflation or mixing')
    base={c['id']:c for c in analysis['claims']}
    if base.get('unknown.current_use',{}).get('kind')!='unknown':raise ValueError('Current-use evidence requires a reviewed adapter; cannot clear occupancy here')
    claims=[];by_id={}
    def add(c):
        c=c.to_dict()
        if c['id'] in by_id:raise ValueError('Duplicate claim ID')
        claims.append(c);by_id[c['id']]=c;return c['id']
    def assumed(cid,label,value,unit,rationale,inputs=()):
        return add(Claim(cid,K.ASSUMPTION,label,value,unit,tuple(inputs),rationale=rationale))
    def calc(cid,label,method,inputs):
        value,unit=evaluate(method,[by_id[i] for i in inputs])
        return add(Claim(cid,K.CALCULATION,label,value,unit,tuple(inputs),method=method,rationale='Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.'))
    add(Claim('site.bbl',K.FACT,'Site identity from verified upstream analysis',req['site_bbl'],U.STATUS,references=({'file':'analysis-run/ir.json','pointer':'/resolved_bbl','sha256':analysis_sha},)))
    for row in reference['rows']:
        add(Claim('reference.'+row['id'],K.FACT,'Historical rounded '+row['quantity']+' at '+str(row['ami_percent'])+'% AMI',row['value'],U.USD_YEAR if row['household_size'] else U.USD_MONTH,references=(row['reference'],)))
    threshold=assumed('policy.cost_threshold_percent','Illustrative housing-cost threshold',req['cost_threshold_percent']['value'],U.PERCENT,req['cost_threshold_percent']['rationale'])
    add(Claim('review.no_action',K.UNKNOWN,'Future without-intervention baseline',None,U.STATUS,rationale=req['no_action']['rationale']))
    add(Claim('review.occupancy',K.UNKNOWN,'Existing occupancy and direct losses',None,U.STATUS,rationale=req['occupancy']['rationale'],references=({'file':'analysis-run/ir.json','sha256':analysis_sha,'upstream_claim':'unknown.current_use'},)))
    add(Claim('review.access',K.UNKNOWN,'Transit opportunity access',None,U.STATUS,rationale='No network-access result imported or calculated in this slice. Station proximity is not job access.'))
    rows={r['id']:r for r in reference['rows']};profiles=[]
    for p in req['profiles']:
        r=rows.get(p['income_reference_id'])
        if r is None or r['quantity']!='annual_income_usd' or r['household_size']!=p['household_size']:
            raise ValueError('Household income reference has wrong definition/household size')
        prefix='profile.'+p['id']
        income=assumed(prefix+'.annual_income_usd','Hypothetical annual household income',r['value'],U.USD_YEAR,p['rationale'],['reference.'+r['id']])
        bedroom=assumed(prefix+'.bedrooms','Exact bedroom category for this comparison',p['bedrooms'],U.BEDROOMS,p['rationale'])
        budget=calc(prefix+'.monthly_budget','Illustrative monthly housing-cost budget','housing.monthly_budget@1',[income,threshold])
        profiles.append({**p,'annual_income_claim':income,'bedroom_claim':bedroom,'monthly_budget_claim':budget,'population_status':'hypothetical_not_observed'})
    programs=[]
    for program in req['programs']:
        prefix='program.'+program['id'];bins=[]
        total=assumed(prefix+'.declared_homes','Explicit proposed program total',program['total_homes']['value'],U.HOMES,program['total_homes']['rationale'])
        add(Claim(prefix+'.delivery',K.UNKNOWN,'Program delivery and realization',None,U.STATUS,rationale=program['delivery']['rationale']))
        assumed(prefix+'.commitment','Restriction commitment status','proposed',U.STATUS,'Only an illustrative proposed offer. No binding legal instrument or achieved affordability certified.')
        for b in program['bins']:
            bid=prefix+'.'+b['id'];refs={}
            for key,unit in [('homes',U.HOMES),('monthly_rent_usd',U.USD_MONTH),('tenant_utilities_usd',U.USD_MONTH),('restriction_years',U.YEARS)]:
                refs[key]=assumed(bid+'.'+key,key,b[key]['value'],unit,b[key]['rationale'])
            refs['bedrooms']=assumed(bid+'.bedrooms','Proposed bedroom category',b['bedrooms'],U.BEDROOMS,'Explicit illustrative offer category, not a reviewed floor plan or household-suitability determination.')
            refs['gross_monthly']=calc(bid+'.gross_monthly_cost','Rent plus assumed tenant-paid utilities','housing.gross_monthly_cost@1',[refs['monthly_rent_usd'],refs['tenant_utilities_usd']])
            refs['annual_cost']=calc(bid+'.annual_cost','Annualized housing cost','housing.annualize@1',[refs['gross_monthly']])
            assessments=[]
            for p in profiles:
                pid=p['id'];aid=bid+'.for_'+pid
                burden=calc(aid+'.burden_percent','Illustrative housing-cost burden','housing.cost_burden_percent@1',[refs['annual_cost'],p['annual_income_claim']])
                cost=calc(aid+'.cost_test','Annual cost at or below stated income threshold','housing.within_threshold@1',[refs['annual_cost'],p['annual_income_claim'],threshold])
                bed=calc(aid+'.bedroom_test','Exact bedroom category matches','housing.bedroom_match@1',[refs['bedrooms'],p['bedroom_claim']])
                both=calc(aid+'.cost_and_bedroom_test','Both diagnostic conditions met; not eligibility','housing.cost_and_bedroom_match@1',[cost,bed])
                assessments.append({'profile_id':pid,'burden_claim':burden,'cost_test_claim':cost,'bedroom_test_claim':bed,'combined_test_claim':both})
            bins.append({'id':b['id'],'claims':refs,'assessments':assessments})
        sum_id=calc(prefix+'.sum_homes','Sum of explicit offer bins','housing.sum_homes@1',[b['claims']['homes'] for b in bins])
        if by_id[sum_id]['value']!=by_id[total]['value']:raise ValueError('Home totals differ')
        counts=[]
        for p in profiles:
            inputs=[]
            for b in bins:
                a=next(a for a in b['assessments'] if a['profile_id']==p['id']);inputs += [b['claims']['homes'],a['combined_test_claim']]
            cid=calc(prefix+'.for_'+p['id']+'.cost_test_homes','Homes meeting cost threshold and exact bedroom category; not eligibility','housing.selected_homes@1',inputs)
            counts.append({'profile_id':p['id'],'homes_claim':cid})
        programs.append({'id':program['id'],'label':program['label'],'total_claim':total,'bins':bins,'profile_counts':counts,'commitment_status':'proposed','delivery':'unknown'})
    comparisons=[]
    a,b=programs
    comparisons.append({'metric':'explicit_total_homes','claim':calc('comparison.total_homes_difference','Second program minus first: explicit total homes','housing.difference@1',[b['total_claim'],a['total_claim']])})
    for p in profiles:
        aa=next(c for c in a['profile_counts'] if c['profile_id']==p['id']);bb=next(c for c in b['profile_counts'] if c['profile_id']==p['id'])
        cid=calc('comparison.for_'+p['id']+'.cost_test_homes_difference','Second minus first: homes meeting diagnostic conditions','housing.difference@1',[bb['homes_claim'],aa['homes_claim']])
        comparisons.append({'metric':'cost_test_homes','profile_id':p['id'],'claim':cid})
    return {'version':'0.1.0','module':'housing-program-comparison','site_bbl':req['site_bbl'],'question':req['question'],'objective':req['objective'],
            'price_year':req['price_year'],'basis':req['basis'],'request_sha256':request_sha,'analysis_sha256':analysis_sha,'reference_bundle_sha256':reference_sha,
            'claims':claims,'profiles':profiles,'programs':programs,'comparisons':comparisons,'overall_ranking':None,
            'professional_review':'pending','project_attributable_benefit':'not_estimated','eligibility':'not_determined',
            'reference_scope':reference['scope'],'limitations':LIMITS}


def validate_claims(ir):
    by_id={c['id']:c for c in ir['claims']}
    if len(by_id)!=len(ir['claims']):raise ValueError('Duplicate claim ID')
    active=set();done=set()
    def visit(cid):
        if cid in active:raise ValueError('Claim dependency cycle')
        if cid not in by_id:raise ValueError('Missing claim dependency')
        if cid in done:return
        active.add(cid);c=by_id[cid];kind=K(c['kind']);unit=U(c['unit'])
        if kind!=K.UNKNOWN:
            value=c['value']
            if unit in {U.USD_MONTH,U.USD_YEAR,U.PERCENT}:
                import re
                pattern=r'(0|[1-9][0-9]*)(\.[0-9]{1,6})?' if unit==U.PERCENT else r'(0|[1-9][0-9]*)(\.[0-9]{1,2})?'
                if not isinstance(value,str) or not re.fullmatch(pattern,value):raise ValueError('Invalid decimal quantity type')
            elif unit in {U.HOMES,U.YEARS,U.BEDROOMS} and type(value)!=int:raise ValueError('Invalid integer quantity type')
            elif unit==U.BOOLEAN and type(value)!=bool:raise ValueError('Invalid boolean quantity type')
            elif unit==U.STATUS and not isinstance(value,str):raise ValueError('Invalid status quantity type')
        for dep in c['inputs']:visit(dep)
        if kind==K.FACT and not c['references']:raise ValueError('Uncited fact')
        if kind==K.ASSUMPTION and not c['rationale']:raise ValueError('Unexplained assumption')
        if kind==K.UNKNOWN and (c['value'] is not None or not c['rationale']):raise ValueError('Unknown promoted to known')
        if kind==K.CALCULATION:
            actual,expected=evaluate(c['method'],[by_id[i] for i in c['inputs']])
            if type(actual)!=type(c['value']) or actual!=c['value'] or expected!=unit:raise ValueError('Calculation/type mismatch')
        elif c['method'] is not None:raise ValueError('Non-calculation has a method')
        active.remove(cid);done.add(cid)
    for cid in by_id:visit(cid)
