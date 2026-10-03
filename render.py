"""Human-readable exports from the evidence IR. MIT."""
import html, json, math, pathlib

def fmt(v, decimals=0):
    return 'unknown' if v is None else f'{v:,.{decimals}f}'

def render(ir, out):
    claims=ir['claims']
    value=lambda k:claims[k]['value']
    ref=lambda k:f'`{k}`'
    screen=ir['screen']
    av=lambda k:ir['config']['assumptions'][k]['value']
    settings=ir['config']['screen']
    radius=ir['config']['scope']['radius_m']['value']
    lead=ir['lead_decision']['bbl'] if ir['lead_decision'] else screen['investigated_bbls'][0]
    p='lot.'+lead
    lead_dossier=next(d for d in ir['dossiers'] if d['bbl']==lead)
    lines=[
        '# Bronx Housing Opportunity Probe One',
        f'**Disposition: investigate current uses and leases before commissioning design.** The lead is {value(p+".address")} (BBL {lead}). This is a conditional research concept, not an available or approved development site.',
        'The first probe demonstrates a reproducible screening and challenge process. Expert usefulness remains untested until the two advisors review it.',
        '## What the screen found',
        f'The cached PLUTO window contains {fmt(screen["bounding_window_count"])} lots; {fmt(screen["within_radius_count"])} have point coordinates within the assumed {fmt(radius)} metre straight line radius. {fmt(screen["eligible_count"])} pass the numeric screen. {len(screen["shortlist"])} were shortlisted and {len(ir["dossiers"])} investigated. Counts: '+', '.join(ref('screen.'+n) for n in ['bounding_window_count','within_radius_count','eligible_count'])+'.',
        f'Screen settings: lot area {fmt(settings["min_lotarea_sf"])} to {fmt(settings["max_lotarea_sf"])} square feet, positive recorded residential FAR, and at least {fmt(settings["min_capacity_gap_sf"])} square feet of the proxy lotarea × residfar − bldgarea. Prioritize no recorded residential units, then descending proxy. These are research choices. The proxy is not legal buildable area and the radius is not walking or job access.',
        '| Rank | Recorded address | BBL | Zoning | Lot area sf | Recorded homes | Distance m | Area gap proxy sf |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |'
    ]
    for row in screen['shortlist']:
        lines.append(f'| {row["rank"]} | {row["address"]} | {row["bbl"]} | {row["recorded_zoning"]} | {fmt(row["recorded_lotarea_sf"])} | {fmt(row["recorded_unitsres"])} | {fmt(row["distance_m"])} | {fmt(row["capacity_gap_sf"])} |')
    lines += ['Each row maps to `lot.<BBL>.<field>` in ir.json. The complete cached universe and exclusions are retained. No lot is inferred to be empty from its residential unit count.',
              '## Three candidate challenges']
    for d in ir['dossiers']:
        q='lot.'+d['bbl']
        lines += [f'### {value(q+".address")}',
                  f'Recorded owner: {value(q+".ownername")} ({ref(q+".ownername")}); building class {value(q+".bldgclass")} ({ref(q+".bldgclass")}).',
                  '**Research disposition:** '+(d['review']['disposition'] if d['review'] else 'Review outstanding')+'.',
                  d['review']['rationale'] if d['review'] else 'No researcher interpretation recorded.',
                  'Evidence: '+', '.join(ref(k) for k in d['review']['inputs'])+'.' if d['review'] else '',
                  '| Check | Returned rows | Meaning |','| --- | --- | --- |']
        for kind,check in d['checks'].items():
            lines.append(f'| {kind} | {check.get("record_count","unknown")} | Exact BBL query only; not a clearance or complete project count |')
        lines += ['Filings may have multiple documents or subsequent submissions. Row counts are not unique projects. A zero-row query is an observed query result, not evidence that there is no activity, no violation, or no occupant.']
    lines += ['## Lead site and first decision',
              f'The lead has recorded lot area {fmt(value(p+".lotarea"))} sf, building area {fmt(value(p+".bldgarea"))} sf, residential FAR {fmt(value(p+".residfar"),2)}, and affordable residential FAR {fmt(value(p+".affresfar"),2)}. Recorded zoning is {value(p+".zonedist1")}, overlay {value(p+".overlay1")}, special district code {value(p+".spdist1")}, and environmental designation {value(p+".edesignum")}. These fields are indicators for diligence, not a complete zoning or environmental opinion.',
              'The scenario uses the recorded ordinary residential FAR as a transparent reference. It does not apply the affordable FAR, MIH requirements, special district modifications, lot geometry constraints, or verified floor area exemptions. Recorded building area and zoning floor area are different measures.',
              '**First action:** establish what occupies the site today, which leases or community uses exist, and whether preservation, co-location, or redevelopment is even a relevant question. Historical owner names in filings differ from the current PLUTO label. This is time-varying evidence, not proof that a current owner or tenant has been identified.',
              '## Two conditional housing scenarios',
              'These model complete replacement housing concepts, not incremental additions to the existing building. Existing nonresidential services are not automatically preserved in the calculation. Neither scenario is a legal or architectural design.',
              '| Scenario | Gross sf | Illustrative homes | Concept floors | Modeled cost excluding land | Monthly rent for debt coverage |',
              '| --- | --- | --- | --- | --- | --- |']
    for sc in lead_dossier['scenarios']:
        k=sc['claim_prefix']
        lines.append(f'| {sc["id"]} | {fmt(value(k+".gross_sf"))} | {fmt(value(k+".units"))} | {fmt(value(k+".floors"))} | ${fmt(value(k+".ex_land_cost"))} | ${fmt(value(k+".debt_support_rent_month"))} |')
    specs=ir['config']['scenarios']
    lines += [f'Scenario A uses {fmt(specs[0]["far_share"]*100)} percent and B {fmt(specs[1]["far_share"]*100)} percent of recorded FAR; assumed lot coverage is {fmt(specs[0]["coverage"]*100)} percent for A and {fmt(specs[1]["coverage"]*100)} percent for B. Net efficiency is {fmt(av("net_efficiency")*100)} percent and average home size {fmt(av("avg_net_unit_sf"))} net sf. The assumed gross to zoning area conversion is {fmt(av("gross_per_zoning_sf"),2)}. Concept floors are area divided by an assumed footprint, rounded up; the last floor may be partial. Shape, setbacks, daylight, elevators, egress and height limits are unresolved.',
              f'Cost baseline: ${fmt(av("hard_cost_per_gsf"))} per gross sf hard cost plus a {fmt(av("soft_contingency_share")*100)} percent soft cost and contingency allowance. Debt baseline: {fmt(av("debt_ltc")*100)} percent of modeled cost, {fmt(av("annual_interest")*100,2)} percent interest, {fmt(av("amortization_years"))} year amortization and {fmt(av("dscr"),2)} debt service coverage. Operations assume {fmt(av("vacancy_share")*100)} percent vacancy and {fmt(av("opex_share_egi")*100)} percent operating expense share. All are editable hypothetical inputs, not sourced Bronx underwriting terms.',
              'The rent figure covers the modeled debt at the assumed coverage ratio. It is not a market rent, AMI rent, full project break even rent, or equity return. Cost excludes site acquisition, demolition, remediation, relocation, construction financing carry, verified fees and reserves. No subsidy amount or financing commitment is inferred.',
              f'At the hypothetical ${fmt(av("monthly_rent_test"))} monthly all-unit rent test:']
    for sc in lead_dossier['scenarios']:
        k=sc['claim_prefix']
        lines.append(f'- Scenario {sc["id"]}: baseline non-debt capital ${fmt(value(k+".baseline_non_debt_capital"))}; additional non-debt capital needed to reduce modeled debt ${fmt(value(k+".additional_non_debt_capital"))}. Additional capital is not synonymous with public subsidy. Inputs and formula: {ref(k+".additional_non_debt_capital")}.')
    lines += ['The 60 percent AMI objective remains a policy lens. No official rent schedule or utility allowance was verified, so the model does not call the hypothetical rent affordable at that income level.',
              '## Unresolved gates and next actions',
              '| Gate | Status | Next action |','| --- | --- | --- |']
    actions={
        'legal_entitlement':'Verify parcel geometry, zoning map, special Jerome rules, MIH applicability, permitted uses, bulk and affordability obligations.',
        'current_occupancy_and_leases':'Perform a site visit and establish current tenants, uses, leases and preservation needs.',
        'owner_willingness_and_title':'Check deed and mortgage history, parcel changes, title and willingness; no owner contact undertaken.',
        'environment_and_geotechnical':'Resolve the E designation and obtain professional environmental and site diligence.',
        'current_development_pipeline':'Cross-check block/lot, BIN and address aliases, permits and certificates; exact BBL filings alone are insufficient.',
        'full_cost_and_financing':'Obtain a quantity estimate, land and relocation assumptions, tax treatment, financing carry, reserves and actual program terms.',
        'official_affordability_schedule':'Specify household sizes, unit mix, official income and rent limits, utility allowance and duration.',
        'pedestrian_and_job_access':'Route from entrances to relevant jobs and services; assess travel schedules, reliability, fares and accessibility.'
    }
    for gate in ir['config']['required_gates']:
        lines.append(f'| {gate.replace("_"," ")} | Unknown | {actions[gate]} |')
    lines += ['## What changed in the playbook',
              'The naive numeric rank elevated a school and a police facility. The challenge stage corrected the decision without rewriting the original screen. Future missions should explicitly distinguish private redevelopment, public-service co-location, preservation and vacant-land development. A civic-use lens belongs before treating ranked capacity as an opportunity.',
              'The private lead illustrates a second rule: absence of recorded homes does not eliminate displacement or service-loss questions. Current uses and leases should precede expensive design or promotional imagery.',
              '## Advisor review',
              'Both reviews are outstanding. Ask each advisor to choose reject, investigate or advance; identify material errors and missing constraints; estimate work saved; trace three claims; and change one assumption. Use docs/advisor-review.md and keep their judgments separate.',
              '## Provenance and reproduction',
              'Data snapshot: PLUTO version 26v2. Dataset metadata reports an August 24, 2026 update; source snapshots were retrieved during this probe. Field-level effective dates remain incomplete. The generic downloaded PLUTO dictionary is from 2022 and is not accepted as current 26v2 entitlement guidance.',
              'Run `python pipeline.py` offline from the package. The resulting ir.json contains observed, derived, assumption, judgment and unknown claims; exact source queries and snapshot hashes; dependencies; and unresolved gates. The manifest hashes code, configuration, sources and outputs. See README.md for live collection, replay and validation.',
              'No adviser has endorsed this output. No proposal, media post, owner contact or image has been published or sent.'
    ]
    (out/'probe-report.md').write_text('\n\n'.join(lines).replace('|\n\n|','|\n|')+'\n')
    brief=[ '# Lead Site Brief for Independent Advisor Review',
            f'**{value(p+".address")} — BBL {lead}. Research disposition: investigate current uses and leases first.**',
            f'Why it surfaced: {fmt(value(p+".distance_m"))} m straight line from the published 170 St / 4 station coordinate, {fmt(value(p+".lotarea"))} sf recorded lot area, and a large recorded residential FAR proxy. No recorded homes does not mean vacant.',
            'Why it may fail: historical filings show community and commercial uses; current occupancy and leases are unverified. Environmental designation and special district review remain open. Availability, title, zoning entitlement and full economics are unresolved.',
            'Conditional concepts:']
    for sc in lead_dossier['scenarios']:
        brief.append(f'- {sc["id"]}: {fmt(sc["gross_sf"])} gross sf and {sc["units"]} illustrative homes. Not a buildable unit count.')
    brief += ['Next decision: is there a legitimate preservation, co-location or redevelopment question on this site? Verify occupants and uses before advancing architecture or acquisition.',
              'Reviewer questions: Is this lead worth investigating? Which fact or assumption changes your answer? What would you still need to collect yourself?',
              'This brief is for independent review. The full evidence graph and playbook are supplied separately; no legal or investment clearance is claimed.']
    (out/'advisor-brief.md').write_text('\n\n'.join(brief)+'\n')
    (out/'media-draft.md').write_text('Research process draft only — not published\n\nWe tested an open housing opportunity playbook around a Bronx subway station. A capacity screen elevated public facilities as well as a private commercial parcel. Checking uses and filings changed the next decision: verify current occupants and services before drawing buildings. The code, assumptions and source snapshots are available for review. No site is represented as available, approved or ready for construction.\n')
    render_html(ir,out,lead,lead_dossier)

def render_html(ir,out,lead,dossier):
    claims=ir['claims'];v=lambda k:claims[k]['value'];esc=html.escape
    shortlist=ir['screen']['shortlist'];p='lot.'+lead
    lat0=float(ir['screen']['station']['GTFS Latitude']);lon0=float(ir['screen']['station']['GTFS Longitude'])
    points=[]
    for row in shortlist:
        q='lot.'+row['bbl']; x=300+(v(q+'.longitude')-lon0)*111320*math.cos(math.radians(lat0))/2.5;y=300-(v(q+'.latitude')-lat0)*111320/2.5
        points.append(f'<g><circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{"#ba4b32" if row["bbl"]==lead else "#286d68"}"><title>{esc(row["address"])}; BBL {row["bbl"]}; {row["distance_m"]:.0f} m straight line</title></circle><text x="{x+12:.1f}" y="{y+4:.1f}" font-size="13">{row["rank"]}</text></g>')
    map_svg='<svg viewBox="0 0 600 600" role="img" aria-label="Coordinate plot of ten shortlisted lots, numbered by screening rank"><rect width="600" height="600" fill="#f0f4ef"/><circle cx="300" cy="300" r="5" fill="#111"/><text x="310" y="293">170 St / 4</text>'+''.join(points)+'<path d="M35 545 v-35 l-6 10 m6-10 l6 10" stroke="#222" fill="none"/><text x="30" y="564">N</text><path d="M460 545 h100" stroke="#222"/><text x="465" y="565">≈250 m</text></svg>'
    table=''.join(f'<tr><td>{r["rank"]}</td><td>{esc(r["address"] or "Unknown")}</td><td>{esc(r["recorded_zoning"] or "Unknown")}</td><td>{r["distance_m"]:.0f}</td><td>{r["capacity_gap_sf"]:,.0f}</td></tr>' for r in shortlist)
    candidate_cards=[]
    for d in ir['dossiers']:
        q='lot.'+d['bbl'];rev=d['review']
        candidate_cards.append(f'<article class="card"><h3>{esc(v(q+".address"))}</h3><p>{esc(rev["disposition"])}</p><p>{esc(rev["rationale"])}</p><button data-claim="review.{d["bbl"]}">Trace this judgment</button></article>')
    keep={k for k in claims if k.startswith('assumption.') or k.startswith('scenario.'+lead) or k.startswith('station.') or k.startswith('scope.') or k.startswith('screen.') or k.startswith('decision.') or any(k.startswith('lot.'+b+'.') for b in ir['screen']['investigated_bbls']) or k.startswith('review.')}
    def add_parents(key):
        for parent in claims[key].get('inputs',[]):
            if parent not in keep: keep.add(parent);add_parents(parent)
    for key in list(keep):add_parents(key)
    compact_claims={k:claims[k] for k in sorted(keep)}
    # Count claims reference the entire universe; trim the display only, keep the full graph in ir.json.
    for key in ['screen.bounding_window_count','screen.within_radius_count','screen.eligible_count']:
        compact_claims[key]=dict(compact_claims[key],inputs=[x for x in compact_claims[key].get('inputs',[]) if not x.startswith('lot.')],full_dependency_graph='ir.json')
    compact_claims={k:val for k,val in compact_claims.items() if not k.startswith('lot.') or any(k.startswith('lot.'+b+'.') for b in ir['screen']['investigated_bbls'])}
    payload={'claims':compact_claims,'sources':ir['sources'],'config':ir['config'],'lead':lead}
    jsdata=json.dumps(payload,separators=(',',':')).replace('<','\\u003c')
    template='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bronx housing opportunity probe</title><style>
*{box-sizing:border-box}.grid>*{min-width:0}select{width:100%;max-width:100%}#trace strong{overflow-wrap:anywhere}body{margin:0;background:#faf9f5;color:#213331;font:16px/1.55 system-ui,sans-serif}main{max-width:1080px;margin:auto;padding:32px 22px}h1{font-size:clamp(28px,5vw,46px);line-height:1.12}h2{margin-top:40px}h3{font-size:19px}p{max-width:78ch}.eyebrow{color:#286d68;font-weight:700}.notice{border-left:4px solid #ba4b32;padding:12px 18px;background:#fff1e8}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}.card{padding:20px;border:1px solid #c9d6cd;background:white;border-radius:8px}svg{width:100%;height:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:9px 7px;border-bottom:1px solid #dce2db;text-align:left}th{background:#edf2ed}.table{overflow:auto}label{display:block;margin:14px 0}input{width:100%}button,select{font:inherit;padding:8px 12px;border:1px solid #286d68;background:#f3f8f4;border-radius:5px;color:#213331;cursor:pointer}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #ba4b32}output{font-weight:700}.metric{font-size:24px;color:#286d68}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef3ed;padding:15px;font-size:13px}small{color:#4c615c}a{color:#22605c}.muted{color:#4c615c}footer{margin-top:40px;border-top:1px solid #c9d6cd;padding-top:18px}
</style></head><body><main><p class="eyebrow">OPEN HOUSING OPPORTUNITY PLAYBOOK · PROBE ONE</p><h1>Find a lead. Challenge it. Make the next decision.</h1><p class="notice">Research disposition: <strong>investigate current uses and leases first.</strong> No site is represented as available, approved, vacant or financially committed. The scenarios below are conditional calculations.</p><p>__ADDRESS__ is the private commercial lead. A school and a police facility also rose to the top of the numeric screen. The challenge stage changed their disposition; it preserved the original ranking for review.</p>
<h2>Ten lots near 170 St on the 4</h2><div class="grid"><div>__MAP__<small>Coordinate plot; no parcel boundaries or street network. Numbers match screening rank. This is proximity, not walked access.</small></div><div class="table"><table><thead><tr><th>Rank</th><th>Address</th><th>Zoning</th><th>m</th><th>Gap proxy sf</th></tr></thead><tbody>__ROWS__</tbody></table></div></div><p class="muted">The gap is lot area × recorded ordinary residential FAR minus recorded building area. It is a screening heuristic, not legal capacity. No recorded homes does not imply vacancy.</p>
<h2>Challenge the first three</h2><div class="grid">__CARDS__</div>
<h2>Conditional scenarios for the private lead</h2><p>The shapes below are area diagrams, not architectural renderings. They assume full replacement housing, 55% lot coverage and a partial top floor where needed. Current uses, actual footprint, setbacks, height limits, MIH and special district rules remain unresolved.</p><div class="grid"><div class="card"><label>Concept<select id="scenario"><option value="A">A · 65% of recorded FAR</option><option value="B">B · 90% of recorded FAR</option></select></label><label>Average net sf per home <output id="unitout"></output><input id="unitsize" type="range" min="650" max="1100" step="50"></label><label>Hard cost per gross sf <output id="costout"></output><input id="cost" type="range" min="275" max="450" step="25"></label><label>Annual debt interest <output id="rateout"></output><input id="rate" type="range" min="5" max="8" step="0.25"></label><label>Hypothetical monthly rent <output id="rentout"></output><input id="rent" type="range" min="1500" max="2500" step="100"></label><button id="reset">Reset to saved assumptions</button><p><small>Controls are local what-if assumptions. They do not alter the saved IR or establish official AMI rents. At changed settings, rerun the DSL to save a fully hashed evidence graph.</small></p></div><div class="card"><div id="massing"></div><div id="metrics" aria-live="polite"></div><button id="trace-cost">Trace saved cost calculation</button></div></div><p class="notice">Modeled cost excludes land, demolition, remediation, relocation and construction financing carry. Rent for debt coverage is not full economic break even or an equity return. Additional non-debt capital is not a public subsidy estimate. The 60% AMI lens has no verified rent schedule here.</p>
<h2>Inspect the evidence path</h2><label>Claim<select id="claim-select"></select></label><div id="trace"></div><p><small>The full graph, original source bodies and byte hashes are in the downloadable source package. The visual viewer exposes selected claims; complete universe dependencies are in ir.json.</small></p>
<h2>The next action</h2><p>Verify current occupants, uses and leases at the private lead before commissioning design. For the two public facilities, ordinary private redevelopment is the wrong mission; service replacement or co-location would require a separate agency-led case.</p><p>Then review zoning and MIH, E-designation obligations, title and parcel history, address and BIN aliases, complete development status, a full cost plan, official affordability schedules, and actual transit access.</p><footer>MIT licensed code · Original documentation CC BY 4.0 · Source data retain upstream terms. PLUTO 26v2 snapshot. Two independent advisor reviews are pending. No proposal or media draft has been sent or published.</footer></main><script id="probe-data" type="application/json">__DATA__</script><script>
const data=JSON.parse(document.getElementById('probe-data').textContent), el=id=>document.getElementById(id), a=data.config.assumptions, cv=k=>a[k].value, money=v=>Math.round(v).toLocaleString('en-US'), base='lot.'+data.lead, saved=k=>data.claims[base+'.'+k].value;
function model(spec,size,cost,rate,rent){const gross=saved('lotarea')*saved('residfar')*spec.far_share*cv('gross_per_zoning_sf'), units=Math.floor(gross*cv('net_efficiency')/size), floors=Math.ceil(gross/(saved('lotarea')*spec.coverage)), total=gross*cost*(1+cv('soft_contingency_share')), loan=total*cv('debt_ltc'), mr=rate/100/12,n=cv('amortization_years')*12,dc=12*mr/(1-Math.pow(1+mr,-n)),target=loan*dc*cv('dscr'),factor=units*12*(1-cv('vacancy_share'))*(1-cv('opex_share_egi')),need=target/factor,supported=factor*rent/(cv('dscr')*dc);return{gross,units,floors,total,need,extra:Math.max(0,loan-supported),baseline:total-loan};}
function update(){const spec=data.config.scenarios.find(s=>s.id===el('scenario').value), size=+el('unitsize').value,cost=+el('cost').value,rate=+el('rate').value,rent=+el('rent').value,m=model(spec,size,cost,rate,rent);el('unitout').textContent=size;el('costout').textContent='$'+cost;el('rateout').textContent=rate+'%';el('rentout').textContent='$'+rent;el('metrics').innerHTML='<p><span class="metric">'+m.units+'</span> illustrative homes · '+money(m.gross)+' gross sf</p><p>'+m.floors+' concept floors · modeled cost excluding land <strong>$'+money(m.total)+'</strong></p><p>Monthly rent for modeled debt coverage: <strong>$'+money(m.need)+'</strong></p><p>Baseline non-debt capital: $'+money(m.baseline)+'<br>Additional non-debt capital at tested rent: $'+money(m.extra)+'</p>';let blocks='';const h=180/m.floors;for(let i=0;i<m.floors;i++)blocks+='<rect x="60" y="'+(205-(i+1)*h)+'" width="'+(i===m.floors-1?130:180)+'" height="'+Math.max(1,h-2)+'" fill="'+(spec.id==='A'?'#286d68':'#ba4b32')+'"/>';el('massing').innerHTML='<svg viewBox="0 0 300 230" role="img" aria-label="Abstract stacked area diagram for scenario '+spec.id+'"><path d="M30 207 h240" stroke="#213331"/>'+blocks+'<text x="60" y="224">Concept '+spec.id+' · diagram only</text></svg>';}
function reset(){el('scenario').value='A';el('unitsize').value=cv('avg_net_unit_sf');el('cost').value=cv('hard_cost_per_gsf');el('rate').value=cv('annual_interest')*100;el('rent').value=cv('monthly_rent_test');update();}
function trace(key){el('claim-select').value=key;el('trace').replaceChildren();const seen=new Set();function visit(k,depth){if(seen.has(k)||depth>5)return;seen.add(k);const c=data.claims[k];if(!c){const p=document.createElement('p');p.textContent=k+' — complete dependency in ir.json';el('trace').append(p);return;}const box=document.createElement('div'),h=document.createElement('strong'),pre=document.createElement('pre');h.textContent=k;pre.textContent=JSON.stringify(c,null,2);box.append(h,pre);if(c.source_id){const s=data.sources[c.source_id],link=document.createElement('a');link.href=s.url;link.target='_blank';link.rel='noopener noreferrer';link.textContent='Open exact source query';box.append(link);}el('trace').append(box);(c.inputs||[]).forEach(parent=>visit(parent,depth+1));}visit(key,0);}
Object.keys(data.claims).filter(k=>k.startsWith('scenario.')||k.startsWith('review.')||k.startsWith('assumption.')||k.startsWith(base+'.')).forEach(k=>{const option=document.createElement('option');option.value=k;option.textContent=k;el('claim-select').append(option);});el('claim-select').addEventListener('change',e=>trace(e.target.value));document.querySelectorAll('[data-claim]').forEach(b=>b.addEventListener('click',()=>{trace(b.dataset.claim);el('trace').scrollIntoView({behavior:'smooth'});}));['scenario','unitsize','cost','rate','rent'].forEach(id=>el(id).addEventListener('input',update));el('reset').addEventListener('click',reset);el('trace-cost').addEventListener('click',()=>trace('scenario.'+data.lead+'.'+el('scenario').value+'.ex_land_cost'));reset();trace('scenario.'+data.lead+'.A.ex_land_cost');
</script></body></html>'''
    result=template.replace('__ADDRESS__',esc(v(p+'.address'))).replace('__MAP__',map_svg).replace('__ROWS__',table).replace('__CARDS__',''.join(candidate_cards)).replace('__DATA__',jsdata)
    (out/'advisor-explorer.html').write_text(result)
