"""Invert desired housing programs into required area and financial diagnostics. MIT.

Discovery admission remains independent. All modeled programs and prices are
explicit scenarios. Failed and unknown targets remain in the complete trial set.
"""
from collections import Counter
import copy
from decimal import Decimal as D,ROUND_CEILING,localcontext
from housing_underwriting.model import evaluate as underwrite,validate as validate_template,keys,dec,integer,basis,serial,money

PATHS=['housing_permitted_by_general_use_rule','rezoning_path','special_or_unresolved_review']
LANES=['other_nonhousing_review','public_or_institutional_use_review','park_or_recreation_review','infrastructure_review']
MODES=['fixed','per_home','per_gross_sf','per_lot_sf']


def validate(req,template):
    validate_template(template)
    keys(req,['version','id','question','program_grid','land_price_per_lot_sf_values','scaling','targets','detail_limit','basis'],'site-search request')
    import re
    if req['version']!='1.0' or not isinstance(req['id'],str) or not re.fullmatch('[a-z0-9-]{1,80}',req['id']):raise ValueError('Unsupported search id/version')
    if not isinstance(req['question'],str) or not req['question'].strip():raise ValueError('Search question required')
    basis(req['basis'])
    if not set(req['basis']['reference_ids'])<={x['id'] for x in template['references']}:raise ValueError('Search basis cites an unknown template reference')
    if req['basis']['kind'] in ['reported_input','source_derived_input'] and not req['basis']['reference_ids']:raise ValueError('Attributed search basis requires a source reference')
    integer(req['detail_limit'],1,10,'detailed model count')
    grid=req['program_grid'];keys(grid,['homes','net_sf_per_home','net_efficiency','residential_share_of_gross','gross_per_zoning_sf'],'program grid')
    if not isinstance(grid['homes'],list) or not 1<=len(grid['homes'])<=10 or len(set(grid['homes']))!=len(grid['homes']):raise ValueError('Choose 1 to 10 unique program home counts')
    for h in grid['homes']:integer(h,1,1000,'program homes')
    dec(grid['net_sf_per_home'],'Net sf/home',D('100'),D('3000'))
    dec(grid['net_efficiency'],'Net efficiency',D('.1'),D('1'));dec(grid['residential_share_of_gross'],'Residential share',D('.1'),D('1'));dec(grid['gross_per_zoning_sf'],'Gross/zoning sf conversion',D('.5'),D('2'))
    prices=req['land_price_per_lot_sf_values']
    if not isinstance(prices,list) or not 1<=len(prices)<=10 or len(set(prices))!=len(prices):raise ValueError('Choose 1 to 10 unique assumed land prices')
    numeric_prices=[dec(p,'Assumed land price per lot sf',D(0),D(10000)) for p in prices]
    if len(set(numeric_prices))!=len(numeric_prices):raise ValueError('Choose numerically unique land-price scenarios')
    scale=req['scaling'];keys(scale,['reference_lot_area_sf','fixed_capital','income','expenses','replacement_reserve','below_line','sources'],'template scaling')
    dec(scale['reference_lot_area_sf'],'Reference lot area',D('.01'))
    expected={x['category'] for x in template['capital']['lines'] if x['measure']=='fixed' and x['category']!='land'}
    if not isinstance(scale['fixed_capital'],dict) or set(scale['fixed_capital'])!=expected:raise ValueError('Declare scaling for every fixed capital line except overridden land')
    maps=[scale['fixed_capital']]
    for group in ['income','expenses','below_line']:
        if not isinstance(scale[group],dict) or set(scale[group])!={x['id'] for x in template['operations'][group]}:raise ValueError('Declare scaling for every '+group+' line')
        maps.append(scale[group])
    if not isinstance(scale['sources'],dict) or set(scale['sources'])!={x['id'] for x in template['sources']}:raise ValueError('Declare scaling for each source amount')
    maps.append(scale['sources'])
    if scale['replacement_reserve'] not in MODES or any(v not in MODES for m in maps for v in m.values()):raise ValueError('Unsupported scaling mode')
    targets=req['targets'];keys(targets,['allowed_zoning_paths','allowed_review_lanes','max_station_straight_line_m','require_lot_point_outside_ibz','require_no_active_linked_zap','require_no_positive_returned_housing_signal','max_required_zoning_far','max_unallocated_capital_per_home_usd','max_monthly_scheduled_tenant_rent_usd','tenant_rent_stream_ids','tenant_rent_cap_scope','minimum_cashflow_usd'],'search targets')
    for key,allowed in [('allowed_zoning_paths',PATHS),('allowed_review_lanes',LANES)]:
        values=targets[key]
        if not isinstance(values,list) or not values or len(values)!=len(set(values)) or not set(values)<=set(allowed):raise ValueError('Unsupported or empty '+key)
    for key in ['require_lot_point_outside_ibz','require_no_active_linked_zap','require_no_positive_returned_housing_signal']:
        if type(targets[key]) is not bool:raise ValueError('Explicit boolean needed for '+key)
    for key in ['max_station_straight_line_m','max_required_zoning_far','max_unallocated_capital_per_home_usd','max_monthly_scheduled_tenant_rent_usd']:
        if targets[key] is not None:dec(targets[key],key,D(0))
    dec(targets['minimum_cashflow_usd'],'Minimum cash flow',D('-1e12'))
    if targets['tenant_rent_cap_scope'] not in ['year_one','all_projection_years']:raise ValueError('Declare tenant rent cap scope')
    rent_ids=targets['tenant_rent_stream_ids']
    if not isinstance(rent_ids,list) or not rent_ids or len(rent_ids)!=len(set(rent_ids)) or not set(rent_ids)<={x['id'] for x in template['operations']['income']}:raise ValueError('Choose valid tenant-rent income stream ids')
    return req


def _build_trial_request(template,req,lot,homes,land_price,trial_id):
    """All transforms are declared; no market prices or legal envelope are inferred."""
    grid=req['program_grid'];scale=req['scaling'];area=D(str(lot['recorded_lot_area_sf']))
    gross=(D(homes)*dec(grid['net_sf_per_home'])/dec(grid['net_efficiency'])/dec(grid['residential_share_of_gross'])).quantize(D('.01'),rounding=ROUND_CEILING)
    factors={'fixed':D(1),'per_home':D(homes)/template['program']['homes'],
             'per_gross_sf':gross/dec(template['program']['gross_area_sf']),
             'per_lot_sf':area/dec(scale['reference_lot_area_sf'])}
    out=copy.deepcopy(template);out['id']=trial_id;out['question']=req['question']+' BBL '+lot['bbl']+'.'
    new_basis={'kind':'analyst_assumption','rationale':req['basis']['rationale']+' Program scaling and land prices are scenario transforms, not observed conditions.','reference_ids':[]}
    out['basis']=new_basis;out['program']={'homes':homes,'gross_area_sf':serial(gross),'basis':new_basis}
    out['debt']['basis']=new_basis
    for line in out['capital']['lines']:
        line['basis']=new_basis
        if line['category']=='land':line.update(measure='fixed',usd=serial(money(area*land_price)),basis=new_basis)
        elif line['measure']=='fixed':line.update(usd=serial(money(dec(line['usd'])*factors[scale['fixed_capital'][line['category']]])),basis=new_basis)
    for group in ['income','expenses','below_line']:
        for line in out['operations'][group]:line.update(annual_usd=serial(money(dec(line['annual_usd'])*factors[scale[group][line['id']]])),basis=new_basis)
    reserve=out['operations']['replacement_reserve'];reserve.update(annual_usd=serial(money(dec(reserve['annual_usd'])*factors[scale['replacement_reserve']])),basis=new_basis)
    for source in out['sources']:source.update(status='proposed',amount_usd=serial(money(dec(source['amount_usd'])*factors[scale['sources'][source['id']]])),basis=new_basis)
    # Dollar debt caps, appraisals and other debt service remain fixed input assumptions;
    # the search contract explicitly discloses this, rather than scaling a commitment.
    return out


def build_trial_request(template,req,lot,homes,land_price,trial_id):
    with localcontext() as ctx:
        ctx.prec=40
        return _build_trial_request(template,req,lot,homes,land_price,trial_id)


def lot_targets(lot,targets):
    failed=[];unknown=[]
    if lot['zoning_path']['path'] not in targets['allowed_zoning_paths']:failed.append('zoning_path_outside_declared_search')
    if lot['review_lane'] not in targets['allowed_review_lanes']:failed.append('review_lane_outside_declared_search')
    context=lot.get('public_context',{})
    station=context.get('nearest_station')
    if targets['max_station_straight_line_m'] is not None:
        if not station or station.get('straight_line_m') is None:unknown.append('station_proximity_unknown')
        elif D(str(station['straight_line_m']))>dec(targets['max_station_straight_line_m']):failed.append('outside_declared_station_point_distance')
    if targets['require_lot_point_outside_ibz']:
        relation=context.get('industrial_zone_point_relation','unknown')
        if relation in ['inside','boundary_review']:failed.append('industrial_policy_area_point_review')
        elif relation!='outside_returned_polygons':unknown.append('industrial_policy_area_point_unknown')
    if targets['require_no_positive_returned_housing_signal']:
        status=lot.get('dwelling_review',{}).get('status')
        if status=='positive_returned_housing_signal':failed.append('positive_returned_housing_signal_requires_reconciliation')
        elif status!='no_positive_returned_housing_signal':unknown.append('historical_housing_signal_coverage_unknown')
    if targets['require_no_active_linked_zap']:
        if 'active_or_on_hold_zap_project_review' in lot['flags']:failed.append('active_linked_zap_project')
        if any(x in lot['flags'] for x in ['application_status_unresolved','zap_bbl_context_incomplete','zap_projects_context_incomplete']):unknown.append('linked_zap_status_or_coverage_unknown')
    return failed,unknown


def evaluate(discovery,template,req):
    validate(req,template)
    with localcontext() as ctx:
        ctx.prec=40
        return _evaluate(discovery,template,req)


def _evaluate(discovery,template,req):
    all_lots=discovery['lots'];pool=[x for x in all_lots if x['in_recorded_nonhousing_set']]
    count=len(pool)*len(req['program_grid']['homes'])*len(req['land_price_per_lot_sf_values'])
    if count>25000:raise ValueError('Search exceeds 25,000 explicit lot/program/price trials; reduce grid or collect a narrower geography')
    trials=[];lot_rows=[];target=req['targets'];grid=req['program_grid']
    for lot in all_lots:
        if not lot['in_recorded_nonhousing_set']:
            lot_rows.append({'bbl':lot['bbl'],'status':'retained_other_current_use_queue','current_use_category':lot['current_use_category'],'trial_count':0});continue
        failed,unknown=lot_targets(lot,target)
        area=lot['recorded_lot_area_sf']
        if area is None or area<=0:
            lot_rows.append({'bbl':lot['bbl'],'status':'needs_review','reasons':sorted(set(unknown+['lot_area_missing_or_invalid'])),'failed_targets':failed,'trial_count':0});continue
        n=0
        for homes in sorted(grid['homes']):
            for price_index,price in enumerate(req['land_price_per_lot_sf_values']):
                identity=lot['bbl']+'-h'+str(homes)+'-p'+str(price_index)
                model=build_trial_request(template,req,lot,homes,dec(price),identity);r=underwrite(model)
                gross=dec(model['program']['gross_area_sf']);zoning=gross/dec(grid['gross_per_zoning_sf']);far=zoning/D(str(area))
                gap=D(r['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd'])/homes
                annual_rents=[sum((D(x['scheduled_usd']) for x in year['income_lines'] if x['id'] in target['tenant_rent_stream_ids']),D(0))/homes/12 for year in r['annual']]
                year_one_rent=annual_rents[0];peak_rent=max(annual_rents)
                rents=year_one_rent if target['tenant_rent_cap_scope']=='year_one' else peak_rent
                cash=min(D(x['cash_after_reserves_debt_and_below_line_usd']) for x in r['annual'])
                reasons=list(failed)
                for key,value,reason in [('max_required_zoning_far',far,'required_far_exceeds_declared_scenario_cap'),('max_unallocated_capital_per_home_usd',gap,'unallocated_capital_per_home_exceeds_target'),('max_monthly_scheduled_tenant_rent_usd',rents,'scheduled_tenant_rent_exceeds_target')]:
                    if target[key] is not None and value>dec(target[key]):reasons.append(reason)
                if cash<dec(target['minimum_cashflow_usd'],minimum=D('-1e12')):reasons.append('cashflow_below_declared_target')
                reasons.extend(r['financing_limit_breaches'])
                if r['coverage_breach_years']:reasons.append('declared_dscr_not_met_in_all_projection_years')
                status='does_not_match_declared_targets' if reasons else ('needs_review' if unknown else 'matches_declared_targets')
                station=lot.get('public_context',{}).get('nearest_station')
                trials.append({'id':identity,'bbl':lot['bbl'],'address':lot.get('address'),'status':status,
                               'failed_targets':sorted(set(reasons)),'unknown_targets':sorted(set(unknown)),
                               'proposed_homes':homes,'assumed_land_usd_per_lot_sf':price,'required_gross_area_sf':serial(gross),
                               'required_zoning_area_proxy_sf':serial(money(zoning)),
                               'required_zoning_far':serial(far.quantize(D('.000001'))),
                               'required_zoning_far_exact':serial(far),
                               'unallocated_capital_per_home_exact_usd':serial(gap),
                               'unallocated_capital_per_home_usd':serial(money(gap)),
                               'total_development_cost_usd':r['total_development_cost_usd'],
                               'modeled_primary_loan_usd':r['modeled_primary_loan_usd'],
                               'monthly_scheduled_tenant_rent_per_home_usd':serial(money(rents)),
                               'tenant_rent_target_scope':target['tenant_rent_cap_scope'],
                               'year_one_monthly_scheduled_tenant_rent_per_home_usd':serial(money(year_one_rent)),
                               'peak_monthly_scheduled_tenant_rent_per_home_usd':serial(money(peak_rent)),
                               'minimum_annual_cashflow_usd':serial(money(cash)),
                               'coverage_breach_years':r['coverage_breach_years'],
                               'zoning_path':lot['zoning_path']['path'],'review_lane':lot['review_lane'],
                               'station_straight_line_m':station.get('straight_line_m') if station else None,
                               'source_flags':lot['flags'],'professional_feasibility':None})
                n+=1
        subset=trials[-n:]
        best_status=('matches_declared_targets' if any(x['status']=='matches_declared_targets' for x in subset) else ('needs_review' if any(x['status']=='needs_review' for x in subset) else 'does_not_match_declared_targets'))
        lot_rows.append({'bbl':lot['bbl'],'status':best_status,'current_use_category':lot['current_use_category'],'trial_count':n})
    matches=[x for x in trials if x['status']=='matches_declared_targets']
    # Keep multiple program alternatives; no monetary weights or universal site score.
    # Pareto axes: smaller required FAR and capital gap, more proposed homes. Distance
    # remains an explicit filter, so missing distance cannot acquire an invented score.
    def metric(t):return (D(t['required_zoning_far_exact']),D(t['unallocated_capital_per_home_exact_usd']),-t['proposed_homes'])
    front=[]
    for row in sorted(matches,key=lambda x:(metric(x),x['bbl'],x['id'])):
        m=metric(row)
        if any(all(a<=b for a,b in zip(metric(other),m)) and any(a<b for a,b in zip(metric(other),m)) for other in front):continue
        front.append(row)
    pareto_ids={x['id'] for x in front}
    for row in trials:row['pareto_under_declared_metrics']=row['id'] in pareto_ids
    detail=sorted(front,key=lambda x:(D(x['unallocated_capital_per_home_usd']),D(x['required_zoning_far']),-x['proposed_homes'],x['bbl'],x['id']))[:req['detail_limit']]
    return {'version':'1.0.0','request_id':req['id'],'meaning':'Explicit finite scenario search, not an optimization proof, site recommendation, legal envelope or funded feasibility finding.',
            'counts':{'inventory_lots':len(all_lots),'recorded_nonhousing_lots':len(pool),'trials':len(trials),
                      'trials_by_status':dict(sorted(Counter(x['status'] for x in trials).items())),
                      'lots_by_status':dict(sorted(Counter(x['status'] for x in lot_rows).items())),
                      'pareto_scenarios':len(front)},
            'pareto_method':'Non-dominated on smaller required zoning FAR, smaller unallocated capital/home and more proposed homes, among matching scenarios only; no universal welfare weights.',
            'detailed_trial_ids':[x['id'] for x in detail],
            'limits':['Broad nonhousing discovery stays unchanged; these are user/analyst-declared search filters.',
                      'Desired whole-home programs imply required area; no FAR increment is required and no legally permitted unit count is inferred.',
                      'Land prices, construction costs, rent, efficiency and all scaling are scenario assumptions, not automatically estimated from public records.',
                      'Recorded-point station distance is not walking/job access; an outside-IBZ point does not resolve parcel-wide overlap or policy support.',
                      'Dollar appraisal/debt caps and other debt service remain fixed scenario assumptions; all template funding statuses are downgraded to proposed for the new site/program.',
                      'No result resolves occupancy, site control, parcel assembly, zoning applicability, physical fit, environmental clearance or investor returns.'],
            'lots':lot_rows,'trials':trials}
