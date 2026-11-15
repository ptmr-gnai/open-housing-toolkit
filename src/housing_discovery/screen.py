"""Deterministic scenario screening; every lot retains a route and reasons. MIT."""
from collections import Counter, defaultdict
from .common import bbl, number, validate_request

ACTIVE = {'Active','On-Hold'}
TERMINAL = {'Complete','Record Closed','Withdrawn-Other','Terminated','Terminated-Applicant Unresponsive'}


def evaluate(inventory, request):
    validate_request(request)
    if inventory['scope'] != request['scope']:
        raise ValueError('Changed geography requires a new inventory')
    if not inventory['primary_complete']:
        raise ValueError('Incomplete inventory cannot produce a ranked shortlist')
    sc, sel = request['scenario'], request['selection']
    projects = {x['row']['project_id']:x for x in inventory['records']['zap_projects']}
    links, uses = defaultdict(list), defaultdict(list)
    for x in inventory['records']['zap_bbl']:
        links[bbl(x['row']['bbl'])].append(x)
    for x in inventory['records']['colp']:
        uses[bbl(x['row']['bbl'])].append(x)
    rows = []
    for item in inventory['records']['pluto']:
        raw = item['row']; identity = bbl(raw['bbl'])
        values = {k:number(raw.get(k)) for k in ['lotarea','residfar','affresfar','unitsres']}
        unknown = [k for k,v in values.items() if v is None or v < 0]
        flags, holds = [], []
        public_signal = (str(raw.get('landuse','')).split('.')[0] in ['8','9']
                         or str(raw.get('bldgclass',''))[:1] in ['W','I','M','N','P','Q','Y','U','T']
                         or (str(raw.get('landuse','')).split('.')[0] == '7' and not str(raw.get('bldgclass','')).startswith('G'))
                         or bool(uses[identity]))
        if public_signal:
            flags.append('public_or_institutional_use_signal_not_title_finding')
        if raw.get('zonedist1') == 'PARK':
            flags.append('recorded_park_zoning_requires_separate_review')
            holds.append('parkland_review_not_ordinary_redevelopment')
        if str(raw.get('bldgclass',''))[:1] in ['U','T'] or (str(raw.get('landuse','')).split('.')[0]=='7' and not str(raw.get('bldgclass','')).startswith('G')):
            flags.append('infrastructure_use_replacement_or_retention_unresolved')
        if sel['max_recorded_residential_units']==0 and values['unitsres'] in [None,0] and str(raw.get('bldgclass',''))[:1] in ['H','S','A','B','C','D','R']:
            flags.append('residential_like_use_despite_zero_or_missing_recorded_homes')
            holds.append('occupancy_review_before_zero_homes_screen_advances')
        if str(raw.get('bldgclass','')).startswith('G') and str(raw.get('landuse','')).split('.')[0]=='7':
            flags.append('auto_use_in_transportation_landuse_group_requires_current_use_review')
        if not raw.get('ownername'):
            flags.append('recorded_owner_missing')
        for field,flag in [('spdist1','special_district'),('landmark','landmark'),('histdist','historic_district'),('edesignum','environmental_designation')]:
            if raw.get(field):
                flags.append(flag+'_review_needed')
        if raw.get('splitzone') in [True,'true','Y'] or raw.get('zonedist2'):
            flags.append('multiple_or_split_zoning_review_needed')
        if raw.get('irrlotcode') in [True,'true','Y']:
            flags.append('irregular_lot_review_needed')
        if number(raw.get('pfirm15_flag')) == 1:
            flags.append('recorded_flood_flag_review_needed')
        contexts = []
        seen = set()
        for link in links[identity]:
            pid = link['row'].get('project_id')
            if pid in seen:
                continue
            seen.add(pid)
            project = projects.get(pid)
            status = project['row'].get('project_status') if project else None
            if status in ACTIVE:
                flags.append('active_or_on_hold_zap_application')
                if sel['hold_active_applications']:
                    holds.append('pipeline_review_before_advancement')
            elif status not in TERMINAL:
                flags.append('unresolved_application_status')
                holds.append('unresolved_application_status')
            if link['row'].get('validated') not in [True,'true','Y','Yes']:
                flags.append('zap_link_validation_requires_review')
            contexts.append({'project_id':pid,'project':project,'parcel_link_reference':link['reference']})
        for provider,complete in inventory['context_complete'].items():
            if not complete:
                flags.append(provider+'_coverage_unknown')
                holds.append('context_collection_incomplete')
        if unknown:
            holds.append('missing_numeric_inputs:'+','.join(unknown))
        if not raw.get('bldgclass') or not raw.get('landuse'):
            holds.append('existing_use_classification_missing')
        area = values['lotarea']
        current = max(values['residfar'],values['affresfar']) if not any(k in unknown for k in ['residfar','affresfar']) else None
        if current is not None and values['affresfar'] > values['residfar']:
            flags.append('affordable_far_used_only_as_conservative_recorded_proxy_not_applicability')
        proposed = sc['proposed_residential_far']
        area_gain = max(0,area*(proposed-current)) if current is not None and area is not None and area >= 0 else None
        equivalent = (area_gain * sc['gross_per_zoning_sf'] * sc['residential_share'] * sc['net_efficiency'] / sc['net_sf_per_home_equivalent'] if area_gain is not None else None)
        if area is not None and not sel['min_lot_area_sf'] <= area <= sel['max_lot_area_sf']:
            holds.append('outside_declared_lot_size_range')
        if sel['max_recorded_residential_units'] is not None and values['unitsres'] is not None and values['unitsres'] > sel['max_recorded_residential_units']:
            holds.append('recorded_homes_exceed_declared_screen')
        if sel['mission']=='private_redevelopment' and public_signal:
            holds.append('different_mission_public_or_institutional_review')
        if sel['mission']=='public_or_institutional_review' and not public_signal:
            holds.append('outside_public_or_institutional_mission')
        if area_gain is not None and area_gain < sel['min_additional_area_proxy_sf']:
            holds.append('insufficient_increment_under_declared_scenario')
        eligible = not holds
        rows.append({'bbl':identity,'address':raw.get('address'),'recorded_owner':raw.get('ownername'),
                     'recorded_building_class':raw.get('bldgclass'),'recorded_landuse':raw.get('landuse'),
                     'recorded_zoning':raw.get('zonedist1'),'recorded_special_district':raw.get('spdist1'),
                     'recorded_lot_area_sf':area,'recorded_residential_units':values['unitsres'],
                     'recorded_residential_far':values['residfar'],'recorded_affordable_residential_far':values['affresfar'],
                     'baseline_recorded_far_proxy':current,'proposed_far_assumption':proposed,
                     'additional_zoning_area_proxy_sf':round(area_gain,2) if area_gain is not None else None,
                     'additional_home_equivalents':round(equivalent,3) if equivalent is not None else None,
                     'recorded_transit_zone':raw.get('transitzone'),'latitude':number(raw.get('latitude')),'longitude':number(raw.get('longitude')),
                     'public_or_institutional_signal':public_signal,'colp_use_records':uses[identity],
                     'zap_projects':contexts,'flags':sorted(set(flags)),'hold_reasons':sorted(set(holds)),
                     'route':'scenario_screen_shortlist_pool' if eligible else 'held_for_reason_or_different_mission',
                     'pluto_reference':item['reference'],'scenario_reference':'request.json#/scenario',
                     'net_new_homes':None,'current_occupancy':None,'site_control':None,'rezoning_eligibility':None,'financial_feasibility':None,
                     'rent_stabilization_status':None,'subsidized_housing_status':None,'parcel_assembly':None,'walk_and_job_access':None,
                     'next_review':'Reconcile applicable zoning/envelope, existing uses, site control, pipeline and economics with practitioners.'})
    ranked = sorted([x for x in rows if not x['hold_reasons']], key=lambda x:(-x['additional_zoning_area_proxy_sf'],x['bbl']))
    shortlist = [x['bbl'] for x in ranked[:sel['top_n']]]
    rank = {x['bbl']:i for i,x in enumerate(ranked,1)}
    for row in rows:
        row['rank_in_screen_pool'] = rank.get(row['bbl'])
        row['shortlisted'] = row['bbl'] in shortlist
    return {'version':'1.0.0','request_id':request['id'],'question':request['question'],'scope':inventory['scope'],
            'evidence_mode':'screened_from_retained_inventory_not_fresh_collection',
            'coverage':{k:v for k,v in inventory.items() if k!='records'},
            'methods':{'increment':'max(0, recorded lot sf * (assumed proposed residential FAR - max(recorded residential FAR, recorded affordable residential FAR)))',
                       'home_equivalents':'increment * assumed gross/zoning conversion * residential share * net efficiency / average net sf; fractional arithmetic, not net new or buildable homes',
                       'rank':'Descending incremental zoning-area proxy, BBL tie-break; not community benefit, feasibility or likelihood of approval.'},
            'limits':['No future No-Action forecast; recorded FAR is not a legally reconciled envelope.',
                      'No cadastral polygon intersection, parcel assemblage, walking/job access, displacement estimate, market underwriting or approval prediction in v1.',
                      'Zero recorded homes and a COLP NO USE label do not establish vacancy or availability.',
                      'Tax-lot joins may miss historic lot changes; application rows do not establish constructed outcomes.'],
            'counts':{'inventory':len(rows),'screen_pool':len(ranked),'shortlist':len(shortlist),
                      'held':len(rows)-len(ranked),'by_hold_reason':dict(sorted(Counter(r for x in rows for r in x['hold_reasons']).items()))},
            'shortlist':shortlist,'lots':sorted(rows,key=lambda x:x['bbl'])}
