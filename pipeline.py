#!/usr/bin/env python3
"""An inspectable housing screening and scenario pipeline. MIT; Python stdlib."""
import argparse, csv, hashlib, io, json, math, pathlib, urllib.parse

from local_outputs import destination,new_run

ROOT = pathlib.Path(__file__).resolve().parent

def read_json(path):
    return json.loads(pathlib.Path(path).read_text())

def write_json(path, obj):
    pathlib.Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def number(value):
    if value is None or value == '':
        return None
    try:
        v = float(value)
        return v if math.isfinite(v) else None
    except (TypeError, ValueError):
        return None

def bbl(value):
    n = number(value)
    return str(int(n)) if n is not None else None

def haversine(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dlat, dlon = p2-p1, math.radians(lon2-lon1)
    a = math.sin(dlat/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlon/2)**2
    return 6371000 * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def validate_config(c):
    if c['dsl_version'] != '0.1':
        raise ValueError('Unsupported DSL version')
    s = c['screen']
    if s['ranking'] != 'no_recorded_residential_first_then_capacity_gap_desc_bbl_asc':
        raise ValueError('Unsupported ranking')
    if s['capacity_formula'] != 'max(0, lotarea * residfar - bldgarea)':
        raise ValueError('Unsupported capacity formula')
    if s['missing_policy'] != 'exclude_from_numeric_rank_and_record_unknown':
        raise ValueError('Unsupported missing policy')
    if [x['id'] for x in c['scenarios']]!=['A','B']:
        raise ValueError('DSL v0.1 requires ordered scenarios A and B')
    if c['exports']!={'public_site_claims':'blocked_until_required_gates_reviewed','expert_pack':'allowed_with_unknowns','media_draft':'research_process_only'}:
        raise ValueError('Unsupported export gates')
    for name, item in c['assumptions'].items():
        if 'value' not in item or not item.get('unit') or not item.get('rationale'):
            raise ValueError('Undocumented assumption: ' + name)
    av = lambda k: c['assumptions'][k]['value']
    for k in ['net_efficiency','vacancy_share','opex_share_egi','debt_ltc']:
        if not 0 < av(k) < 1:
            raise ValueError('Invalid fraction: ' + k)
    for k in ['avg_net_unit_sf','hard_cost_per_gsf','floor_height_ft','annual_interest','amortization_years','dscr']:
        if av(k) <= 0:
            raise ValueError('Nonpositive assumption: ' + k)
    for scenario in c['scenarios']:
        if not 0 < scenario['coverage'] <= 1 or not 0 < scenario['far_share'] <= 1:
            raise ValueError('Invalid scenario geometry')

class Graph:
    def __init__(self, config, config_path):
        self.claims = {}
        self.sources = {}
        self.config = config
        self.config_path = str(pathlib.Path(config_path).resolve().relative_to(ROOT)) if pathlib.Path(config_path).resolve().is_relative_to(ROOT) else str(config_path)
        for f in sorted((ROOT/'cache').glob('*.source.json')):
            source = read_json(f)
            if source['status'] == 'ok':
                if digest(ROOT/source['cache_path']) != source['sha256']:
                    raise ValueError('Source cache hash mismatch: ' + source['id'])
            self.sources[source['id']] = source
        for source_id,source in self.sources.items():
            parent = ('pluto_metadata' if source_id=='pluto_universe' else
                      'dob_jobs_metadata' if source_id.startswith('dob_bis_') else
                      'dob_now_metadata' if source_id.startswith('dob_now_') else
                      'hpd_violations_metadata' if source_id.startswith('hpd_violations_') else
                      'e_designation_metadata' if source_id.startswith('e_designation_20') else None)
            if parent and parent in self.sources:
                source['metadata_source_id']=parent
                source['dataset_update_timestamp']=self.sources[parent].get('source_updated_at')
                source['update_timestamp_limitation']='Dataset update timestamp; not validity date of this parcel field.'

    def add(self, claim_id, value, kind, unit=None, **kwargs):
        if claim_id in self.claims:
            raise ValueError('Duplicate claim ' + claim_id)
        self.claims[claim_id] = dict(id=claim_id, value=value, kind=kind, unit=unit, **kwargs)
        return claim_id

    def observed(self, claim_id, value, source_id, locator, unit=None):
        return self.add(claim_id, value, 'observed' if value is not None else 'unknown', unit,
                        source_id=source_id, locator=locator,
                        limitation=self.sources[source_id]['coverage_limits'])

    def assumption(self, claim_id, value, locator, unit, rationale):
        return self.add(claim_id, value, 'assumption', unit, config_locator=locator,
                        rationale=rationale, config_path=self.config_path)

    def derived(self, claim_id, value, inputs, formula, unit=None):
        return self.add(claim_id, value, 'derived', unit, inputs=inputs, formula=formula,
                        code='pipeline.py')

    def val(self, claim_id):
        return self.claims[claim_id]['value']

    def unknown(self, claim_id, reason):
        return self.add(claim_id, None, 'unknown', reason=reason)

    def validate(self):
        allowed = {'observed','derived','assumption','judgment','unknown'}
        for key, claim in self.claims.items():
            if claim['kind'] not in allowed:
                raise ValueError('Unknown evidence kind')
            if claim['kind'] == 'derived':
                if not claim.get('inputs') or not claim.get('formula'):
                    raise ValueError('Untraceable derived claim: ' + key)
                for parent in claim['inputs']:
                    if parent not in self.claims:
                        raise ValueError('Dangling dependency: ' + parent)
            if claim['kind'] == 'observed' and self.sources[claim['source_id']]['status'] != 'ok':
                raise ValueError('Observed claim from failed source')
        visited, active = set(), set()
        def visit(key):
            if key in active:
                raise ValueError('Cycle at ' + key)
            if key in visited:
                return
            active.add(key)
            for parent in self.claims[key].get('inputs',[]):
                visit(parent)
            active.remove(key)
            visited.add(key)
        for key in self.claims:
            visit(key)

def screen(c, graph):
    station_rows = list(csv.DictReader(io.StringIO((ROOT/'cache/mta_stations_official.body').read_text())))
    matches = [(i,r) for i,r in enumerate(station_rows) if r['Station ID']==c['scope']['station_id']]
    if len(matches) != 1:
        raise ValueError('Station identity not unique')
    i, station = matches[0]
    if station['Stop Name']!=c['scope']['station_name'] or c['scope']['route'] not in station['Daytime Routes'].split():
        raise ValueError('Declared station name or route does not match source')
    for field in ['GTFS Latitude','GTFS Longitude','Stop Name','Daytime Routes','Station ID','ADA']:
        v = number(station[field]) if field in ['GTFS Latitude','GTFS Longitude'] else station[field]
        graph.observed('station.'+field,v,'mta_stations_official',{'row':i,'column':field})
    for key in ['min_lotarea_sf','max_lotarea_sf','min_capacity_gap_sf','shortlist_count','investigate_count']:
        graph.assumption('screen.'+key,c['screen'][key],'/screen/'+key,'sf' if key.endswith('_sf') else 'count','Bounded research screen parameter; not an entitlement.')
    r = c['scope']['radius_m']
    graph.assumption('scope.radius_m',r['value'],'/scope/radius_m/value',r['unit'],r['rationale'])
    raw = json.loads((ROOT/'cache/pluto_universe.body').read_bytes())
    if not isinstance(raw,list) or len(raw) >= 10000:
        raise ValueError('Invalid or potentially truncated PLUTO universe')
    lat0,lon0 = number(station['GTFS Latitude']),number(station['GTFS Longitude'])
    query=urllib.parse.parse_qs(urllib.parse.urlparse(graph.sources['pluto_universe']['url']).query).get('$where',[''])[0]
    padlat,padlon=c['scope']['bbox_padding_lat'],c['scope']['bbox_padding_lon']
    expected_lat=f'latitude between {lat0-padlat:.6f} and {lat0+padlat:.6f}'
    expected_lon=f'longitude between {lon0-padlon:.6f} and {lon0+padlon:.6f}'
    if expected_lat not in query or expected_lon not in query:
        raise ValueError('Cached universe does not match declared station and bounding window; recollect sources')
    if r['value']>min(haversine(lat0,lon0,lat0+padlat,lon0),haversine(lat0,lon0,lat0,lon0+padlon)):
        raise ValueError('Radius exceeds cached bounding window; recollect a larger universe')
    inside, eligible, excluded = [],[],[]
    for i,row in enumerate(raw):
        identity = bbl(row.get('bbl'))
        if not identity:
            raise ValueError('Missing BBL in bounded universe')
        prefix = 'lot.'+identity
        vals = {}
        numeric_fields = ['lotarea','bldgarea','residfar','affresfar','unitsres','numfloors','latitude','longitude','lotfront','lotdepth','retailarea','comarea','builtfar']
        text_fields = ['address','ownername','ownertype','bldgclass','landuse','zonedist1','zonedist2','overlay1','spdist1','splitzone','edesignum','version','zoningdate','rpaddate','bbl']
        for field in numeric_fields+text_fields:
            v = number(row.get(field)) if field in numeric_fields else row.get(field)
            vals[field]=v
            graph.observed(prefix+'.'+field,v,'pluto_universe',{'row':i,'field':field},'sf' if field in ['lotarea','bldgarea','retailarea','comarea'] else None)
        dist = haversine(lat0,lon0,vals['latitude'],vals['longitude']) if vals['latitude'] is not None and vals['longitude'] is not None else None
        graph.derived(prefix+'.distance_m',dist,['station.GTFS Latitude','station.GTFS Longitude',prefix+'.latitude',prefix+'.longitude'],'haversine; earth_radius_m=6371000','metres straight line')
        reason = []
        if dist is None: reason.append('missing_coordinates')
        elif dist > r['value']: reason.append('outside_radius')
        else: inside.append(identity)
        for field in ['lotarea','bldgarea','residfar','unitsres']:
            if vals[field] is None: reason.append('missing_'+field)
        if all(vals[f] is not None for f in ['lotarea','bldgarea','residfar']):
            gap=max(0,vals['lotarea']*vals['residfar']-vals['bldgarea'])
            graph.derived(prefix+'.capacity_gap_sf',gap,[prefix+'.lotarea',prefix+'.residfar',prefix+'.bldgarea'],'max(0, lotarea * residfar - bldgarea); mixed-use heuristic, not legal capacity','sf')
            if vals['lotarea'] < c['screen']['min_lotarea_sf']: reason.append('lot_too_small')
            if vals['lotarea'] > c['screen']['max_lotarea_sf']: reason.append('lot_too_large')
            if gap < c['screen']['min_capacity_gap_sf']: reason.append('capacity_gap_below_threshold')
            if vals['residfar'] <= 0: reason.append('no_positive_recorded_residential_far')
        else:
            gap=None
            graph.unknown(prefix+'.capacity_gap_sf','Required numeric inputs missing')
        record={'bbl':identity,'address':vals['address'],'recorded_unitsres':vals['unitsres'],'distance_m':dist,'capacity_gap_sf':gap,'recorded_zoning':vals['zonedist1'],'recorded_lotarea_sf':vals['lotarea'],'recorded_bldgarea_sf':vals['bldgarea'],'claim_prefix':prefix,'exclusion_reasons':reason}
        (excluded if reason else eligible).append(record)
    if len({bbl(row['bbl']) for row in raw}) != len(raw):
        raise ValueError('Duplicate BBLs; resolve before ranking')
    eligible.sort(key=lambda row:(0 if row['recorded_unitsres']==0 else 1,-row['capacity_gap_sf'],row['bbl']))
    shortlist=eligible[:c['screen']['shortlist_count']]
    for i,row in enumerate(shortlist):
        row['rank']=i+1
        row['selected_reason']='No recorded residential units first; descending capacity proxy; BBL tie-break. No finding of vacancy or availability.'
    investigated=[r['bbl'] for r in shortlist[:c['screen']['investigate_count']]]
    return {'station':station,'bounding_window_count':len(raw),'within_radius_count':len(inside),'eligible_count':len(eligible),'shortlist':shortlist,'eligible':eligible,'excluded':excluded,'investigated_bbls':investigated}

def scenario(c, g, identity, spec):
    p='lot.'+identity
    k='scenario.'+identity+'.'+spec['id']
    for field in ['far_share','coverage']:
        g.assumption(k+'.'+field,spec[field],'/scenarios/'+str(c['scenarios'].index(spec))+'/'+field,'fraction','Illustrative geometry; not certified zoning or architectural capacity.')
    def derive(name,value,inputs,formula,unit):
        g.derived(k+'.'+name,value,inputs,formula,unit)
        return value
    av=lambda key:g.val('assumption.'+key)
    lotarea,far = g.val(p+'.lotarea'),g.val(p+'.residfar')
    zoned=derive('zoning_area_proxy_sf',lotarea*far*spec['far_share'],[p+'.lotarea',p+'.residfar',k+'.far_share'],'lotarea * recorded residfar * far_share; reference area only','sf')
    gross=derive('gross_sf',zoned*av('gross_per_zoning_sf'),[k+'.zoning_area_proxy_sf','assumption.gross_per_zoning_sf'],'zoning_area_proxy_sf * gross_per_zoning_sf; simplified conversion, no verified zoning exclusions','sf')
    net=derive('net_sf',gross*av('net_efficiency'),[k+'.gross_sf','assumption.net_efficiency'],'gross_sf * net_efficiency','sf')
    units=derive('units',math.floor(net/av('avg_net_unit_sf')),[k+'.net_sf','assumption.avg_net_unit_sf'],'floor(net_sf / average_net_unit_sf)','units')
    footprint=derive('footprint_sf',lotarea*spec['coverage'],[p+'.lotarea',k+'.coverage'],'lotarea * coverage','sf')
    floors=derive('floors',math.ceil(gross/footprint),[k+'.gross_sf',k+'.footprint_sf'],'ceil(gross_sf / footprint_sf); last floor partial','floors')
    derive('height_ft',floors*av('floor_height_ft'),[k+'.floors','assumption.floor_height_ft'],'floors * floor_height_ft; conceptual only','ft')
    cost=derive('ex_land_cost',gross*av('hard_cost_per_gsf')*(1+av('soft_contingency_share')),[k+'.gross_sf','assumption.hard_cost_per_gsf','assumption.soft_contingency_share'],'gross_sf * hard_cost_per_gsf * (1 + soft_contingency_share); excludes land, relocation, remediation, demolition, financing carry','USD')
    loan=derive('illustrative_loan',cost*av('debt_ltc'),[k+'.ex_land_cost','assumption.debt_ltc'],'ex_land_cost * debt_ltc','USD')
    rate,n=av('annual_interest')/12,av('amortization_years')*12
    constant=derive('annual_debt_constant',12*rate/(1-(1+rate)**(-n)),['assumption.annual_interest','assumption.amortization_years'],'12 * monthly_rate / (1 - (1 + monthly_rate)^(-months))','annual fraction')
    debt=derive('annual_debt_service',loan*constant,[k+'.illustrative_loan',k+'.annual_debt_constant'],'illustrative_loan * annual_debt_constant','USD/year')
    needed=derive('target_noi',debt*av('dscr'),[k+'.annual_debt_service','assumption.dscr'],'annual_debt_service * dscr','USD/year')
    rent=derive('debt_support_rent_month',needed/(units*12*(1-av('vacancy_share'))*(1-av('opex_share_egi'))) if units else None,[k+'.target_noi',k+'.units','assumption.vacancy_share','assumption.opex_share_egi'],'target_noi / (units * 12 * (1-vacancy) * (1-opex)); debt coverage only, excludes equity return','USD/unit/month')
    noi=derive('rent_test_noi',units*12*av('monthly_rent_test')*(1-av('vacancy_share'))*(1-av('opex_share_egi')),[k+'.units','assumption.monthly_rent_test','assumption.vacancy_share','assumption.opex_share_egi'],'units * 12 * monthly_rent_test * (1-vacancy) * (1-opex)','USD/year')
    supported=derive('rent_supported_debt',noi/(av('dscr')*constant),[k+'.rent_test_noi','assumption.dscr',k+'.annual_debt_constant'],'rent_test_noi / (dscr * annual_debt_constant)','USD')
    derive('additional_non_debt_capital',max(0,loan-supported),[k+'.illustrative_loan',k+'.rent_supported_debt'],'max(0, illustrative_loan - rent_supported_debt); additional to baseline non-debt capital, not a public subsidy estimate','USD')
    derive('baseline_non_debt_capital',cost-loan,[k+'.ex_land_cost',k+'.illustrative_loan'],'ex_land_cost - illustrative_loan','USD')
    return {'id':spec['id'],'label':spec['label'],'bbl':identity,'claim_prefix':k,
            'gross_sf':gross,'units':units,'floors':floors,'ex_land_cost':cost,'debt_support_rent_month':rent}

def enrich(c,g,screen_result):
    dossiers=[]
    for identity in screen_result['investigated_bbls']:
        checks={}
        for source_key in ['dob_bis','dob_now','hpd_violations','e_designation']:
            source_id=source_key+'_'+identity
            record=g.sources.get(source_id)
            key='check.'+identity+'.'+source_key
            if record and record['status']=='ok':
                data=json.loads((ROOT/record['cache_path']).read_bytes())
                if not isinstance(data,list) or len(data)>=10000:
                    raise ValueError('Invalid or truncated challenge query: '+source_id)
                g.observed(key+'.records',len(data),source_id,{'operation':'length of returned array'},'filing rows' if source_key.startswith('dob') else 'violation rows')
                for index,row in enumerate(data):
                    for field,value in row.items():
                        g.observed(key+'.row.'+str(index)+'.'+field,value,source_id,{'row':index,'field':field})
                checks[source_key]={'status':'observed','source_id':source_id,'record_count':len(data),'rows':data}
            else:
                g.unknown(key+'.records','Challenge source unavailable or not collected; no inference of zero')
                checks[source_key]={'status':'unknown','source_id':source_id}
        gates={gate:{'status':'unknown','claim_id':g.unknown('gate.'+identity+'.'+gate,'Requires additional evidence or professional verification.')} for gate in c['required_gates']}
        review=c.get('candidate_reviews',{}).get(identity)
        if review:
            g.add('review.'+identity,review['disposition'],'judgment',rationale=review['rationale'],inputs=review['inputs'],actor='researcher review of cached public records')
            for parent in review['inputs']:
                if parent not in g.claims:
                    raise ValueError('Unknown review input '+parent)
        dossiers.append({'bbl':identity,'checks':checks,'gates':gates,'review':review,'scenarios':[scenario(c,g,identity,spec) for spec in c['scenarios']]})
    return dossiers

def build(config_path):
    c=read_json(config_path)
    validate_config(c)
    g=Graph(c,config_path)
    for name,record in c['assumptions'].items():
        g.assumption('assumption.'+name,record['value'],'/assumptions/'+name+'/value',record['unit'],record['rationale'])
    result=screen(c,g)
    dossiers=enrich(c,g,result)
    g.observed('screen.bounding_window_count',result['bounding_window_count'],'pluto_universe',{'operation':'length of returned array'},'lots')
    g.derived('screen.within_radius_count',result['within_radius_count'],['scope.radius_m']+[k for k in g.claims if k.startswith('lot.') and k.endswith('.distance_m')],'count nonmissing distances <= scope radius','lots')
    g.derived('screen.eligible_count',result['eligible_count'],['scope.radius_m','screen.min_lotarea_sf','screen.max_lotarea_sf','screen.min_capacity_gap_sf']+[k for k in g.claims if k.startswith('lot.') and any(k.endswith('.'+field) for field in ['distance_m','capacity_gap_sf','lotarea','unitsres','bldgarea','residfar'])],'count records satisfying all pipeline.screen conditions; inspect universe and exclusions','lots')
    g.add('decision.screening',c['screen']['selection_rationale'],'judgment',rule=c['screen']['ranking'],inputs=['screen.eligible_count'],actor='declared researcher preference')
    lead=c.get('lead_decision',{})
    if lead:
        if lead['bbl'] not in result['investigated_bbls']:
            raise ValueError('Lead must be one of the investigated candidates')
        g.add('decision.lead',lead['bbl'],'judgment',rationale=lead['rationale'],actor='researcher',inputs=lead['inputs'])
        for parent in lead['inputs']:
            if parent not in g.claims:
                raise ValueError('Unknown lead decision input '+parent)
    g.validate()
    return {'ir_version':'0.1','config':c,'sources':g.sources,'claims':g.claims,'screen':result,'dossiers':dossiers,'lead_decision':lead or None,'limitations':['No legal zoning clearance','No verified current occupancy or availability','No verified AMI rent schedule','No actual pedestrian or job-access routing','No expert advisor review yet']}

def export(ir,outdir,config_path):
    outdir=destination(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    write_json(outdir/'ir.json',ir)
    fields=['rank','bbl','address','recorded_zoning','recorded_lotarea_sf','recorded_bldgarea_sf','recorded_unitsres','distance_m','capacity_gap_sf','selected_reason']
    with (outdir/'shortlist.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(ir['screen']['shortlist'])
    write_json(outdir/'exclusions.json',ir['screen']['excluded'])
    write_json(outdir/'dossiers.json',ir['dossiers'])
    from render import render
    render(ir,outdir)
    input_files=list(ROOT.glob('*.py'))+list((ROOT/'schemas').glob('*.json'))+[p for p in (ROOT/'tests').glob('*') if p.is_file()]
    inputs={str(p.relative_to(ROOT)):digest(p) for p in sorted(input_files)}
    inputs[str(pathlib.Path(config_path).resolve().relative_to(ROOT)) if pathlib.Path(config_path).resolve().is_relative_to(ROOT) else str(config_path)]=digest(config_path)
    outputs={str(p.relative_to(outdir)):digest(p) for p in sorted(outdir.rglob('*')) if p.is_file() and p.name not in ['manifest.json','validation.json']}
    write_json(outdir/'manifest.json',{'schema_version':'0.1','code_and_config_sha256':inputs,'source_sha256':{k:v.get('sha256') for k,v in ir['sources'].items()},'output_sha256':outputs,'replay_mode':'offline cached snapshots','verification':'See tests and validation.json; no professional clearance'})

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--config',default=str(ROOT/'probe.json'))
    parser.add_argument('--out',help='Fresh local output directory; default is a new ignored runs/core-* directory')
    args=parser.parse_args()
    ir=build(args.config)
    out=destination(args.out) if args.out else new_run('core')
    if args.out and out.exists() and any(out.iterdir()):raise ValueError('Use a fresh local output directory')
    export(ir,out,args.config)
    print('Local outputs: '+str(out))
    print(json.dumps({'window_lots':ir['screen']['bounding_window_count'],'radius_lots':ir['screen']['within_radius_count'],'eligible':ir['screen']['eligible_count'],'investigated':ir['screen']['investigated_bbls'],'lead':ir['lead_decision']}))
