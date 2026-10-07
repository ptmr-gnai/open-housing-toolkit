"""One bounded decision graph. Original snapshots remain immutable. MIT."""
import copy, csv, hashlib, io, json, math, pathlib, sys
BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[1]
sys.path.insert(0, str(ROOT))
import pipeline

def sha(data):
    return hashlib.sha256(data).hexdigest()

def fp(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())

def load(path):
    return json.loads(pathlib.Path(path).read_text())

def write(path, value):
    pathlib.Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False)+'\n')

def check_pinned():
    pin = load(BASE/'precommit.json')
    for name, digest in pin['files'].items():
        if sha((ROOT/name).read_bytes()) != digest:
            raise ValueError('Pinned input changed: '+name)
    return load(BASE/'spec.json')

def closure(claims, roots):
    seen, active = set(), set()
    def visit(key):
        if key not in claims: raise ValueError('Missing dependency: '+key)
        if key in active: raise ValueError('Dependency cycle: '+key)
        if key in seen: return
        active.add(key)
        for parent in claims[key].get('inputs', []): visit(parent)
        active.remove(key); seen.add(key)
    for key in roots: visit(key)
    return seen

def downstream(claims, seeds):
    affected = set(seeds)
    while True:
        added = {k for k, v in claims.items() if set(v.get('inputs', [])) & affected}
        if added <= affected: return sorted(affected)
        affected |= added

def numeric(value):
    if isinstance(value, bool): raise ValueError('Boolean is not a numeric fact')
    try: n = float(value)
    except (TypeError, ValueError): raise ValueError('Missing or nonnumeric material fact')
    if not math.isfinite(n): raise ValueError('Nonfinite material fact')
    return n

def check_snapshot(snapshot):
    pin = load(BASE/'precommit.json')['files']
    expected = {name for name in pin if name.startswith('cache/')}
    actual = {str(p.relative_to(snapshot)) for p in (snapshot/'cache').iterdir() if p.is_file()}
    if actual != expected: raise ValueError('Snapshot cache inventory differs')
    allowed = set()
    for source_id in ['pluto_universe','dob_bis_2028710002']:
        name = 'cache/'+source_id+'.source.json'
        original = load(ROOT/name); receipt = load(snapshot/name)
        if sha((snapshot/name).read_bytes()) != pin[name]:
            if receipt.get('kind') != 'synthetic' or receipt.get('parent_sha256') != original['sha256']:
                raise ValueError('Changed receipt lacks explicit synthetic lineage')
            if receipt['id'] != original['id'] or receipt['cache_path'] != original['cache_path']:
                raise ValueError('Synthetic receipt changes source identity')
            allowed |= {name,receipt['cache_path']}
    for name in expected-allowed:
        if sha((snapshot/name).read_bytes()) != pin[name]: raise ValueError('Source cache hash mismatch: '+name)
    for source_id in ['pluto_universe','mta_stations_official','dob_bis_2028710002','e_designation_2028710002']:
        receipt = load(snapshot/'cache'/(source_id+'.source.json'))
        if receipt.get('id')!=source_id or receipt.get('status')!='ok' or sha((snapshot/receipt['cache_path']).read_bytes())!=receipt['sha256']:
            raise ValueError('Source integrity or successful-status mismatch: '+source_id)

def build(snapshot=None, config=None, competing=None, prior_basis=None):
    spec = check_pinned()
    snapshot = pathlib.Path(snapshot or ROOT)
    check_snapshot(snapshot)
    c = copy.deepcopy(config or load(ROOT/'probe.json'))
    if c['required_gates'] != spec['required_gates']:
        raise ValueError('Required gate inventory differs from pinned policy')
    pipeline.validate_config(c)
    for name, assumption in c['assumptions'].items(): numeric(assumption['value'])
    for scenario in c['scenarios']:
        for name in ['far_share','coverage']: numeric(scenario[name])
    if c['assumptions']['soft_contingency_share']['value']<0 or c['assumptions']['gross_per_zoning_sf']['value']<=0 or c['assumptions']['monthly_rent_test']['value']<=0:
        raise ValueError('Invalid model assumption')
    original_root = pipeline.ROOT
    try:
        pipeline.ROOT = snapshot
        g = pipeline.Graph(c, snapshot/'probe.json')
    finally:
        pipeline.ROOT = original_root
    identity = spec['bbl']; p = 'lot.'+identity
    rows = load(snapshot/'cache/pluto_universe.body')
    matches = [(i,r) for i,r in enumerate(rows) if pipeline.bbl(r.get('bbl')) == identity]
    if len(matches) != 1: raise ValueError('Fixed site identity missing or ambiguous')
    index, row = matches[0]
    numbers = {'lotarea':'sf','residfar':'FAR','unitsres':'units','latitude':'degrees','longitude':'degrees','retailarea':'sf'}
    for field in [*numbers, 'address', 'bbl', 'version', 'ownername', 'bldgclass', 'zonedist1', 'edesignum']:
        value = row.get(field)
        if field in numbers: value = numeric(value)
        g.observed(p+'.'+field, value, 'pluto_universe', {'row':index,'field':field}, numbers.get(field))
    if g.val(p+'.lotarea') <= 0 or g.val(p+'.residfar') <= 0 or g.val(p+'.unitsres') < 0:
        raise ValueError('Invalid material parcel value')
    stations = list(csv.DictReader(io.StringIO((snapshot/'cache/mta_stations_official.body').read_text())))
    matches = [(i,r) for i,r in enumerate(stations) if r['Station ID'] == c['scope']['station_id']]
    if len(matches) != 1: raise ValueError('Station identity missing or ambiguous')
    si, station = matches[0]
    if station['Stop Name'] != c['scope']['station_name'] or c['scope']['route'] not in station['Daytime Routes'].split():
        raise ValueError('Station identity disagrees with declared scope')
    for field in ['GTFS Latitude','GTFS Longitude','Stop Name','Daytime Routes','Station ID']:
        value = numeric(station[field]) if field.startswith('GTFS') else station[field]
        g.observed('station.'+field, value, 'mta_stations_official', {'row':si,'column':field}, 'degrees' if field.startswith('GTFS') else None)
    g.derived(p+'.distance_m',pipeline.haversine(g.val(p+'.latitude'),g.val(p+'.longitude'),g.val('station.GTFS Latitude'),g.val('station.GTFS Longitude')),
              [p+'.latitude',p+'.longitude','station.GTFS Latitude','station.GTFS Longitude'],'haversine; earth_radius_m=6371000','metres straight line')
    historical = []
    dob = load(snapshot/'cache/dob_bis_2028710002.body')
    for i in spec['historical_rows']:
        if i >= len(dob) or pipeline.bbl(dob[i].get('bbl')) != identity: raise ValueError('Historical passage identity changed')
        for field in ['job_description','pre__filing_date','job__','doc__']:
            key = 'history.'+str(i)+'.'+field
            value = dob[i].get(field) or None
            g.observed(key,value,'dob_bis_2028710002',{'row':i,'field':field})
            historical.append(key)
    env = load(snapshot/'cache/e_designation_2028710002.body')
    if not env or any(pipeline.bbl(r.get('bbl')) != identity for r in env): raise ValueError('Environmental passage identity changed')
    environmental = []
    for i, record in enumerate(env):
        for field in ['hazmat_code','air_code','noise_code','description']:
            key = 'environment.'+str(i)+'.'+field
            g.observed(key,record.get(field),'e_designation_2028710002',{'row':i,'field':field})
            environmental.append(key)
    for name, a in c['assumptions'].items():
        g.assumption('assumption.'+name,a['value'],'/assumptions/'+name+'/value',a['unit'],a['rationale'])
    pipeline.scenario(c,g,identity,c['scenarios'][0])
    k = 'scenario.'+identity+'.A'
    g.derived('finance.model_gap',g.val(k+'.additional_non_debt_capital') > 0,
              [k+'.additional_non_debt_capital'],'additional_non_debt_capital > 0; conditional debt support, not total feasibility','boolean')
    gates = []
    for gate in spec['required_gates']:
        key = 'gate.'+gate
        g.unknown(key,'No current verification supplied; required by the pinned authored investigation policy.')
        g.claims[key]['policy_locator'] = '/required_gates/'+str(spec['required_gates'].index(gate))
        gates.append(key)
    g.add('judgment.investigation_priority',spec['decision_policy']['priority_rationale'],'judgment',actor=spec['decision_policy']['actor'],
          inputs=historical+[p+'.retailarea','gate.current_occupancy_and_leases'],professional_acceptance='pending')
    g.derived('resident.recorded_units', 'review_resident_impacts' if g.val(p+'.unitsres') > 0 else 'recorded_zero_does_not_establish_vacancy',
              [p+'.unitsres',p+'.version'],'recorded units > 0 changes the investigation lens; neither value establishes present occupancy')
    conflicts = []; reconciliation = []; assertions = []
    if competing is not None:
        receipt = competing['receipt']; file = snapshot/receipt['cache_path']
        if not file.resolve().is_relative_to(snapshot.resolve()) or sha(file.read_bytes()) != receipt['sha256']:
            raise ValueError('Competing evidence digest or path invalid')
        rival = load(file)
        if rival.get('subject_bbl') != identity or rival.get('field') not in ['unitsres','lotarea','residfar']:
            raise ValueError('Unsupported competing assertion scope')
        value = numeric(rival['value'])
        if value < 0 or (rival['field'] != 'unitsres' and value == 0): raise ValueError('Invalid competing fact')
        if receipt.get('kind') != 'synthetic' or rival.get('synthetic') is not True:
            raise ValueError('This probe only accepts explicitly synthetic competing controls')
        g.sources[receipt['id']] = {**receipt,'status':'ok','coverage_limits':'Synthetic assertion for a known contradiction test; not a real site observation.'}
        aid = 'competing.'+rival['field']; target = p+'.'+rival['field']
        g.observed(aid,value,receipt['id'],{'field':'value'},numbers[rival['field']])
        assertions.append(aid)
        if rival.get('version') != g.val(p+'.version'):
            reconciliation.append({'primary':target,'competing':aid,'reason':'Different or unknown observation vintage; no automatic supersession.'})
        elif value != g.val(target):
            conflicts.append({'primary':target,'competing':aid,'reason':'Same BBL, field and declared dataset version; incompatible values, no chosen winner.'})
    missing = [key for key in historical+environmental if g.claims[key]['kind'] == 'unknown']
    if conflicts: disposition = spec['decision_policy']['conflict']
    elif reconciliation: disposition = 'hold_for_temporal_reconciliation'
    elif missing: disposition = spec['decision_policy']['missing_material_basis']
    elif g.val(p+'.unitsres') > 0: disposition = spec['decision_policy']['positive_recorded_units']
    else: disposition = spec['decision_policy']['zero_recorded_units']
    inputs = ['judgment.investigation_priority','resident.recorded_units','finance.model_gap','station.Station ID','station.Stop Name','station.Daytime Routes',p+'.address',p+'.bbl',p+'.version',p+'.ownername',p+'.bldgclass',p+'.zonedist1',p+'.edesignum',p+'.distance_m',k+'.gross_sf',k+'.units',k+'.ex_land_cost',k+'.debt_support_rent_month']+environmental+gates+assertions
    g.add('conclusion.next_step',disposition,'judgment',inputs=inputs,actor='explicit authored policy evaluated by conclusion_engine.py',
          rule=spec['decision_policy'],professional_acceptance='pending',scope=spec['scope'])
    selected = closure(g.claims,['conclusion.next_step'])
    claims = {key:copy.deepcopy(g.claims[key]) for key in sorted(selected)}
    relevant_sources = {v['source_id'] for v in claims.values() if v.get('source_id')}
    sources = {key:copy.deepcopy(g.sources[key]) for key in sorted(relevant_sources)}
    for source in sources.values():
        meta = source.get('metadata_source_id')
        if meta:
            source['dataset_metadata_receipt'] = copy.deepcopy(g.sources[meta])
    for claim in claims.values():
        claim['state'] = 'unknown' if claim['kind'] == 'unknown' else 'unreviewed_judgment' if claim['kind'] == 'judgment' else 'supported_in_snapshot'
        if claim.get('source_id'):
            source = sources[claim['source_id']]
            data = list(csv.DictReader(io.StringIO((snapshot/source['cache_path']).read_text()))) if claim['source_id']=='mta_stations_official' else load(snapshot/source['cache_path'])
            loc = claim['locator']
            actual = data[loc['row']].get(loc.get('field',loc.get('column'))) if 'row' in loc else data.get(loc['field'])
            if claim['kind'] == 'observed':
                if isinstance(claim['value'], bool):
                    equal = isinstance(actual, bool) and actual == claim['value']
                elif isinstance(claim['value'], (int,float)):
                    equal = numeric(actual) == claim['value']
                else:
                    equal = actual == claim['value']
                if not equal: raise ValueError('Claim disagrees with exact source locator: '+claim['id'])
            claim['evidence'] = {'source_id':claim['source_id'],'sha256':source['sha256'],'locator':loc,'exact_value':actual,
                                 'retrieved_at':source.get('retrieved_at'),'dataset_version':row.get('version') if claim['source_id']=='pluto_universe' else None,
                                 'limitation':'Dataset version/retrieval date do not certify current field validity or current occupancy.'}
        if claim['kind'] == 'assumption':
            claim['config_path'] = 'embedded_config'
            claim['config_fingerprint'] = fp(c)
    affected = downstream(claims,[x['primary'] for x in conflicts+reconciliation]) if conflicts or reconciliation else []
    for key in affected: claims[key]['state'] = 'blocked_by_unreconciled_evidence'
    claims['conclusion.next_step']['state'] = 'withheld' if conflicts or reconciliation or missing else 'provisional_author_judgment'
    basis = fp({'claims':claims,'source_hashes':{k:v['sha256'] for k,v in sources.items()},'config':c,'spec':spec,'engine':sha(pathlib.Path(__file__).read_bytes()),'arithmetic':sha((ROOT/'pipeline.py').read_bytes())})
    result = {'version':'0.1','bbl':identity,'target':spec['target'],'snapshot_scope':spec['input_cutoff'],'config':c,'claims':claims,'sources':sources,
              'basis_fingerprint':basis,'prior_judgment_basis':'not_supplied' if prior_basis is None else 'matches' if prior_basis==basis else 'stale',
              'disposition':disposition,'conflicts':conflicts,'temporal_reconciliation':reconciliation,'affected_by_conflict':affected,'missing_material_passages':missing,
              'synthetic_input':any(s.get('kind')=='synthetic' for s in sources.values()),'required_gates':spec['required_gates'],
              'release':{'challenge_pack':True,'investigation_conclusion':not(conflicts or reconciliation or missing),'acquisition_or_design_clearance':False,
                         'professional_review':'pending','unfamiliar_human_reproduction_and_challenge':'pending'}}
    validate_graph(result)
    return result

def validate_graph(result):
    claims = result['claims']; reachable = closure(claims,['conclusion.next_step'])
    if reachable != set(claims): raise ValueError('Unexpected unconnected claims')
    required = set(check_pinned()['required_gates'])
    if set(result['required_gates']) != required or any('gate.'+gate not in reachable for gate in required):
        raise ValueError('Missing decisive requirement from conclusion graph')
    for key, claim in claims.items():
        if claim['kind'] not in ['observed','derived','assumption','judgment','unknown']: raise ValueError('Untyped claim')
        if claim['kind']=='observed' and not claim.get('evidence'): raise ValueError('Observed fact lacks source locator')
        if claim['kind']=='derived' and (not claim.get('inputs') or not claim.get('formula')): raise ValueError('Calculation lacks inputs or formula')
        if claim['kind']=='assumption' and (not claim.get('rationale') or not claim.get('config_locator')): raise ValueError('Undocumented assumption')
        if claim['kind']=='judgment' and (not claim.get('inputs') or not claim.get('actor')): raise ValueError('Judgment lacks basis or attribution')
        if claim['kind']=='unknown' and claim['value'] is not None: raise ValueError('Unknown promoted to value')
    if result['release']['acquisition_or_design_clearance']: raise ValueError('Professional clearance unsupported')
    for gate in required:
        if claims['gate.'+gate]['kind']!='unknown' or claims['gate.'+gate]['value'] is not None:
            raise ValueError('Unverified site requirement promoted')
    unresolved=bool(result['conflicts'] or result['temporal_reconciliation'] or result['missing_material_passages'])
    if result['release']['investigation_conclusion'] == unresolved:
        raise ValueError('Investigation release disagrees with unresolved evidence')
    return True

def compare(before, after):
    changed = [key for key in before['claims'] if key not in after['claims'] or
               (before['claims'][key]['value'],before['claims'][key]['state']) != (after['claims'][key]['value'],after['claims'][key]['state'])]
    return {'changed_values_or_states':sorted(changed),'dependent_claims_requiring_recheck':downstream(after['claims'],changed),
            'prior_judgment_basis':after['prior_judgment_basis'],'before_disposition':before['disposition'],'after_disposition':after['disposition']}

def render(result):
    c = result['claims']; v = lambda key:c[key]['value']; k = 'scenario.'+result['bbl']+'.A'; p='lot.'+result['bbl']
    text = ['# One site conclusion and its evidence','',
            ('SYNTHETIC CONTROL INPUTS — values are not new site findings.\n\n' if result['synthetic_input'] else '')+
            f"{v(p+'.address')} — fixed-site analysis of the October 3 cached snapshot. Disposition: **{result['disposition']}**.",'',
            'Professional interpretation and an unfamiliar human’s reproduction/challenge remain pending. Acquisition and design clearance are blocked.','',
            f"Recorded residential units: {v(p+'.unitsres'):g}; lot area: {v(p+'.lotarea'):,.0f} sf; dataset version: {v(p+'.version')}. Recorded zero does not establish vacancy.",'',
            f"Station proximity is {v(p+'.distance_m'):,.0f} metres straight line. It does not establish pedestrian access, reliability or jobs reachable.",'',
            'Historical filing passages support an occupancy investigation; they do not establish current occupants or leases.','']
    for key in sorted(c):
        if key.startswith('history.') and key.endswith('.job_description'):
            e = c[key]['evidence']; text += [f"- {json.dumps(e['exact_value'])} — {e['source_id']}, row {e['locator']['row']}, field job_description. Related filing dates remain in the graph."]
    text += ['',f"Conditional concept A: {v(k+'.gross_sf'):,.0f} gross sf and {v(k+'.units'):g} illustrative homes. Legal and physical capacity are unverified.",'',
             f"At the assumed ${v('assumption.hard_cost_per_gsf'):,.0f}/gross sf and ${v('assumption.monthly_rent_test'):,.0f}/unit/month rent, the simplified model needs ${v(k+'.debt_support_rent_month'):,.0f}/unit/month to support its illustrative loan. Additional non-debt capital beyond the modeled baseline is ${v(k+'.additional_non_debt_capital'):,.0f}.",'',
             'These are conditional debt-support calculations. They exclude land, relocation, remediation, demolition, financing carry and equity return; the rent is hypothetical. They are not a subsidy estimate or a feasibility finding.','',
             'Required unresolved checks: '+', '.join(result['required_gates'])+'.','']
    if result['conflicts'] or result['temporal_reconciliation']:
        text += ['The conclusion is withheld. Displayed numbers retain their primary-source basis; affected claims are marked blocked in the graph. Neither competing assertion is promoted to a reconciled site fact.','']
    if result['missing_material_passages']: text += ['The conclusion is withheld because material source passages are missing. Missing evidence does not clear occupancy.','']
    text += ['The priority of occupancy investigation is an authored judgment. Its relevance and interpretation require independent challenge. Every displayed fact/calculation resolves to the accompanying graph and source receipts.','']
    return '\n'.join(text)
