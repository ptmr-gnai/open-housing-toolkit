"""Current-use and general residential-use paths; no capacity admission test. MIT."""
from collections import Counter, defaultdict
import re
from .common import bbl, guidance, number, validate_request
from .context import annotate

PATHS=['housing_permitted_by_general_use_rule','rezoning_path','special_or_unresolved_review']
NONRES_CONDOS={'RA','RB','RG','RK','RP','RS','RT','RW','R5','R7','R8'}
RES_CONDOS={'R1','R2','R3','R4','R6','R9','RR'}
ACCOMMODATION={'O8','RH','I1','I2','I4','I6','I7','M3','M4','P3','Y3'}
NONRES_PREFIXES=set('EFGJKLOPQTUVWYZ')


def current_use(raw):
    units,area=number(raw.get('unitsres')),number(raw.get('resarea'))
    cls=str(raw.get('bldgclass') or '').upper();use=str(raw.get('landuse') or '').split('.')[0]
    reasons=[]
    if units is not None and units>0 or area is not None and area>0:
        return 'housing_recorded',['positive_recorded_residential_units_or_area']
    if cls[:1] in set('ABCDHSN') or cls in RES_CONDOS or cls in ACCOMMODATION or use in ['1','2','3','4']:
        return 'housing_signals_require_review',['housing_or_accommodation_class_or_landuse_despite_no_positive_units']
    if units is None or units<0:
        return 'current_use_unresolved',['recorded_residential_units_missing_or_invalid']
    if cls=='R0':return 'current_use_unresolved',['condominium_billing_lot_not_independent_site']
    if cls=='G0':reasons.append('residential_garage_shared_site_review')
    if cls in NONRES_CONDOS:reasons.append('nonresidential_condominium_class_shared_site_review')
    elif cls[:1] not in NONRES_PREFIXES and cls!='M2' and cls[:1]!='I' and cls[:1]!='M':
        return 'current_use_unresolved',['existing_use_class_not_resolved']
    if use not in ['5','6','7','8','9','10','11']:
        return 'current_use_unresolved',['existing_landuse_missing_or_unrecognized']
    if area is None:reasons.append('residential_area_missing_not_assumed_zero')
    return 'recorded_nonhousing',reasons+['zero_recorded_residential_units_and_nonhousing_use_signals']


def base_rule(zone,borough):
    if re.fullmatch(r'R(?:1[0-2]|[1-9])(?:-[1-9][0-9]?)?[A-Z]?',zone):
        return 'residential_use_allowed_in_principle',['residence']
    if re.fullmatch(r'C[1-6](?:-[1-9][0-9]?[A-Z]?)?[A-Z]?',zone):
        if re.fullmatch(r'C[12]-[1-5]',zone):return 'commercial_overlay_requires_underlying_district',['commercial']
        return 'residential_use_allowed_in_principle',['commercial','commercial_limits']
    if re.fullmatch(r'C[78](?:-[1-9][0-9]?)?',zone):
        return 'new_residential_use_not_allowed_by_general_rule',['commercial']
    if re.fullmatch(r'M[123]-[1-9][0-9]?',zone):
        if zone=='M1-1' and borough=='QN':return 'geographic_manufacturing_exception_review',['manufacturing','manufacturing_geography']
        return 'new_residential_use_not_allowed_by_general_rule',['manufacturing','manufacturing_geography']
    if zone.startswith('M') or '/' in zone:return 'manufacturing_exception_or_paired_district_review',['manufacturing','mixed_use']
    if zone=='PARK':return 'parkland_is_separate_review',['residence','commercial']
    return 'district_not_resolved',[]


def zoning(raw,borough,quality):
    zones=list(dict.fromkeys(str(raw[k]).strip().upper() for k in ['zonedist1','zonedist2','zonedist3','zonedist4'] if raw.get(k)))
    specials=[raw[k] for k in ['spdist1','spdist2','spdist3'] if raw.get(k)]
    rules=[base_rule(zone,borough) for zone in zones]
    reasons=[];refs=sorted(set(x for _,r in rules for x in r))
    if not zones:reasons.append('recorded_zoning_missing')
    if specials:reasons.append('special_district_provisions_require_review')
    if len(zones)>1 or raw.get('splitzone') in [True,'true','Y']:reasons.append('split_or_multiple_districts_require_review')
    if raw.get('ltdheight'):reasons.append('limited_height_district_requires_review')
    if quality:reasons.extend(quality)
    if any(rule not in ['residential_use_allowed_in_principle','new_residential_use_not_allowed_by_general_rule'] for rule,_ in rules):
        reasons.append('district_exception_or_unresolved_general_rule')
    if reasons:path='special_or_unresolved_review'
    elif rules[0][0]=='residential_use_allowed_in_principle':path='housing_permitted_by_general_use_rule'
    else:path='rezoning_path'
    return {'path':path,'recorded_districts':zones,'recorded_special_districts':specials,
            'recorded_overlays':[raw[k] for k in ['overlay1','overlay2'] if raw.get(k)],
            'base_use_rules':[{'district':z,'rule':r[0]} for z,r in zip(zones,rules)],
            'review_reasons':sorted(set(reasons)),'guidance_source_ids':refs,
            'residential_type_limits':'C3A permits only specified single/two-family types; low-density Residence District conditions and commercial additional conditions remain applicable. No apartment type or envelope is established.',
            'meaning':'General new-residential-use path from recorded district fields; official map, exceptions, conversions, nonconforming rights, bulk and approvals still need reconciliation. Not a parcel entitlement finding.'}


def evaluate(inv,supplement,request,pack,public_context=None):
    validate_request(request);guidance(pack)
    if inv['scope']!=request['scope'] or supplement['scope']!=request['scope']:raise ValueError('Geography differs from source evidence')
    if not inv['primary_complete']:raise ValueError('Incomplete primary inventory cannot define the discovery universe')
    links=defaultdict(list);uses=defaultdict(list)
    projects={x['row']['project_id']:x for x in inv['records']['zap_projects']}
    for item in inv['records']['zap_bbl']:links[bbl(item['row']['bbl'])].append(item)
    for item in inv['records']['colp']:uses[bbl(item['row']['bbl'])].append(item)
    rows=[]
    for item in inv['records']['pluto']:
        old=item['row'];identity=bbl(old['bbl']);extra=supplement['records'].get(identity)
        raw=extra['row'] if extra else old
        quality=[]
        if not extra:quality.append('zoning_supplement_missing_for_lot')
        if not supplement['metadata_stable']:quality.append('zoning_supplement_update_consistency_unresolved')
        if extra and extra['changed_since_inventory']:quality.append('fields_changed_between_inventory_and_supplement')
        category,use_reasons=current_use(raw)
        if extra and any(k in extra['changed_since_inventory'] for k in ['bldgclass','landuse','unitsres']):
            category='current_use_unresolved';use_reasons.append('existing_use_fields_changed_between_snapshots')
        cls=str(raw.get('bldgclass') or '');landuse=str(raw.get('landuse') or '').split('.')[0]
        zpath=zoning(raw,request['scope']['borough'],quality)
        flags=[]
        for field,name in [('edesignum','environmental_designation'),('histdist','historic_district'),('landmark','landmark'),('irrlotcode','irregular_lot')]:
            if old.get(field) not in [None,'',False,'false','N']:flags.append(name+'_review')
        if number(old.get('pfirm15_flag'))==1:flags.append('recorded_flood_flag_review')
        if any(z=='PARK' for z in zpath['recorded_districts']) or cls.startswith('Q'):
            lane='park_or_recreation_review'
        elif cls[:1] in ['T','U'] or landuse=='7' and not cls.startswith('G'):
            lane='infrastructure_review'
        elif uses[identity] or cls[:1] in ['W','I','M','N','P','Y'] or landuse=='8':
            lane='public_or_institutional_use_review'
        else:lane='other_nonhousing_review'
        if cls.startswith('G') and landuse=='7':flags.append('auto_use_in_broad_transportation_group')
        application=[]
        for link in links[identity]:
            pid=link['row'].get('project_id');project=projects.get(pid)
            status=project['row'].get('project_status') if project else None
            application.append({'link':link,'project':project})
            if status in ['Active','On-Hold']:flags.append('active_or_on_hold_zap_project_review')
            elif status not in ['Complete','Record Closed','Withdrawn-Other','Terminated','Terminated-Applicant Unresponsive']:
                flags.append('application_status_unresolved')
            if link['row'].get('validated') not in [True,'true','Y','Yes']:flags.append('zap_link_validation_review')
        for source,complete in inv['context_complete'].items():
            if not complete:flags.append(source+'_context_incomplete')
        place_context=annotate(raw,public_context)
        gft=place_context.get('green_fast_track')
        if gft is not None:
            mapped=set(x.strip() for x in str(gft['publisher_fields'].get('zoning_district') or '').split(',') if x.strip())
            if mapped and mapped!=set(zpath['recorded_districts']):
                zpath['path']='special_or_unresolved_review'
                zpath['review_reasons']=sorted(set(zpath['review_reasons']+['recorded_and_fast_tracker_districts_differ_across_vintages']))
                flags.append('cross_source_zoning_difference_review')
            if gft['positive_publisher_flags']:flags.append('fast_track_publisher_context_flags_require_review')
        if place_context['industrial_zone_point_relation'] in ['inside','boundary_review']:
            flags.append('industrial_business_zone_policy_review')
        row={'bbl':identity,'address':raw.get('address'),'current_use_category':category,
             'in_recorded_nonhousing_set':category=='recorded_nonhousing','current_use_reasons':use_reasons,
             'building_class':cls,'landuse':landuse,'recorded_unitsres':number(raw.get('unitsres')),
             'recorded_residential_area_sf':number(raw.get('resarea')),'recorded_lot_area_sf':number(raw.get('lotarea')),
             'recorded_building_area_sf':number(raw.get('bldgarea')),
             'recorded_residential_far':number(raw.get('residfar')),'recorded_affordable_residential_far':number(raw.get('affresfar')),
             'recorded_owner_label':raw.get('ownername'),'recorded_transit_zone':raw.get('transitzone'),
             'latitude':number(raw.get('latitude')),'longitude':number(raw.get('longitude')),
             'public_context':place_context,
             'zoning_path':zpath,'review_lane':lane,'flags':sorted(set(flags)),
             'zap_records':application,'colp_records':uses[identity],
             'inventory_reference':item['reference'],'supplement_reference':extra['reference'] if extra else None,
             'guidance_current_use_source_id':'building_classes',
             'unresolved':{'actual_occupancy':None,'leases_and_business_relocation':None,'site_control_and_owner_intent':None,
                           'parcel_assembly_and_shared_rights':None,'official_map_and_full_text_applicability':None,
                           'physical_housing_envelope':None,'pedestrian_and_job_access':None,
                           'industrial_policy_area_status':None,'environmental_satisfaction':None,'financing':None,
                           'net_new_homes':None},'review_order_in_group':None,'displayed_example':False}
        rows.append(row)
    groups=defaultdict(list)
    for row in rows:
        if row['in_recorded_nonhousing_set']:groups[(row['zoning_path']['path'],row['review_lane'])].append(row)
    for group in groups.values():
        group.sort(key=lambda r:(r['recorded_lot_area_sf'] is None,-(r['recorded_lot_area_sf'] or 0),r['bbl']))
        for i,row in enumerate(group,1):row['review_order_in_group']=i;row['displayed_example']=i<=request['display_per_group']
    nonhousing=[x for x in rows if x['in_recorded_nonhousing_set']]
    return {'version':'1.0.0','request_id':request['id'],'question':request['question'],'scope':request['scope'],
            'source_scope':inv['scope_definition'],'zoning_coverage':{k:v for k,v in supplement.items() if k!='records'},
            'public_context_coverage':({'stations':public_context['stations']['complete'],'industrial_zones':public_context['industrial_zones']['complete'],'fast_track_queries':public_context['fast_track']['query_coverage_complete']} if public_context is not None else {'stations':None,'industrial_zones':None}),
            'public_context_source_versions':public_context['fast_track']['source_versions'] if public_context is not None else None,
            'context_complete':inv['context_complete'],'counts':{'inventory':len(rows),'recorded_nonhousing':len(nonhousing),
            'by_current_use':dict(sorted(Counter(x['current_use_category'] for x in rows).items())),
            'nonhousing_by_zoning_path':dict(sorted(Counter(x['zoning_path']['path'] for x in nonhousing).items())),
            'nonhousing_by_review_lane':dict(sorted(Counter(x['review_lane'] for x in nonhousing).items()))},
            'order_method':'Group recorded nonhousing by zoning path and use-review lane; descending recorded lot sf, then BBL. This is a browsing order, not viability, availability or community benefit.',
            'admission_method':'Zero recorded residential units plus nonhousing use evidence; missing/conflicting housing signals remain in separate visible review queues. No auto-use, lot-size, FAR increment, pipeline or financing admission gate.',
            'limits':['Recorded nonhousing does not establish vacancy, absence of occupants, site availability or ease of relocation.',
                      'PLUTO district records are not a fresh spatial intersection or authoritative parcel entitlement opinion; small district pieces and intervening map amendments can be missed.',
                      'Special, split, paired, exceptional and missing districts are explicit review paths, not automatic rezoning candidates.',
                      'No housing yield, legal envelope, owner willingness, walking access, assemblage or funded feasibility is inferred.'],
            'lots':sorted(rows,key=lambda x:x['bbl'])}
