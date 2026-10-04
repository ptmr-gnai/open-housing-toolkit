"""Offline evidence binding, named arithmetic and review-packet generation. MIT."""
import copy,decimal,hashlib,json,pathlib,re
P=pathlib.Path(__file__).resolve().parent
D=decimal.Decimal

def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def sha(body):return hashlib.sha256(body).hexdigest()
def normalized(s):return re.sub(r'\s+',' ',s).strip()
def load(n):return json.loads((P/n).read_text())
def write(n,obj): (P/n).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

def bind(case):
    sources={}
    for f in sorted((P/'cache').glob('*.receipt.json')):
        r=json.loads(f.read_text());sources[r['id']]=r
        if r['status']=='ok':
            b=(P/r['cache_path']).read_bytes()
            if sha(b)!=r['sha256'] or len(b)!=r['bytes']:raise ValueError('Source hash/size mismatch: '+r['id'])
            if r.get('parsed')=='pdf':
                text_path=P/'cache'/(r['id']+'.text');text=text_path.read_text()
                r['text_transform']={'tool':'pdftotext -layout','output':'cache/'+r['id']+'.text','sha256':sha(text_path.read_bytes()),'page_count':len(text.split('\f'))-1}
    claims=copy.deepcopy(case['claims']);by={c['id']:c for c in claims}
    if len(by)!=len(claims):raise ValueError('Duplicate claim id')
    for c in claims:
        if c['kind']=='observed':
            e=c['evidence'];r=sources[e['source_id']]
            if r['status']!='ok':raise ValueError('Failed source supporting claim '+c['id'])
            if 'selector' in e:
                data=load(r['cache_path'])
                for key in e['selector']:
                    data=len(data) if key=='length' else data[int(key)] if isinstance(data,list) else data[key]
                if isinstance(c['value'],(int,float)) and not isinstance(c['value'],bool):
                    if D(str(data))!=D(str(c['value'])):raise ValueError('Numeric extraction mismatch '+c['id'])
                elif data!=c['value']:raise ValueError('Extraction mismatch '+c['id'])
            elif 'quote' in e:
                text=(P/'cache'/(r['id']+'.text')).read_text()
                if e['locator'].startswith('PDF page '):text=text.split('\f')[int(e['locator'].split()[2])-1]
                if normalized(e['quote']) not in normalized(text):raise ValueError('Quote not found '+c['id']+': '+e['quote'])
                if isinstance(c['value'],(int,float,list)) and not isinstance(c['value'],bool):
                    if 'extraction' not in e:raise ValueError('Numeric passage requires an extraction contract '+c['id'])
                    ex=e['extraction'];q=normalized(e['quote'])
                    if 'pattern' in ex:
                        match=re.search(ex['pattern'],q)
                        if not match:raise ValueError('Extraction regex does not match '+c['id'])
                        vals=[D(match.group(i).replace(',',''))*D(str(ex['scale'])) for i in ex['groups']]
                    else:
                        amounts=re.findall(r'\$([0-9,]+)',q);vals=[D(amounts[i].replace(',','')) for i in ex['all_currency_indices']]
                    want=c['value'] if isinstance(c['value'],list) else [c['value']]
                    if vals!=[D(str(v)) for v in want]:raise ValueError('Numeric passage extraction mismatch '+c['id'])
            else:raise ValueError('Observed claim lacks selector or quote')
            e['source_sha256']=r['sha256']
        elif c['kind']=='unknown':
            if c['value'] is not None or not c.get('reason'):raise ValueError('Unknown must remain null with reason')
        elif c['kind']=='assumption':
            if not c.get('reason'):raise ValueError('Assumption lacks rationale')
        else:raise ValueError('Unsupported authored claim kind')
    def number(id):return D(str(by[id]['value']))
    def derived(id,value,unit,inputs,formula,scope):
        c=dict(id=id,kind='derived',value=float(value),unit=unit,inputs=inputs,formula=formula,scope=scope);claims.append(c);by[id]=c
    derived('incremental_agency_units',number('agency_rezone_units')-number('agency_current_units'),'estimated homes',['agency_rezone_units','agency_current_units'],'rezone - current','Difference between two HPD planning estimates, not forecast completions or a causal effect')
    derived('unit_increase_pct',(number('agency_rezone_units')/number('agency_current_units')-1)*100,'percent',['agency_rezone_units','agency_current_units'],'100 * (rezone/current - 1)','Agency-estimate comparison')
    derived('far_increase_pct',(number('agency_rezone_far')/number('agency_current_far')-1)*100,'percent',['agency_rezone_far','agency_current_far'],'100 * (rezone/current - 1)','Arithmetic matches HPD example of <=30% increase, but is not full ELURP eligibility')
    for id,f in [('current_area_proxy','agency_current_far'),('rezone_area_proxy','agency_rezone_far')]:
        derived(id,number('lot_area')*number(f),'zoning square feet proxy',['lot_area',f],'tax_lot_area * agency_planning_far','Tax lot equals zoning lot only for this arithmetic illustration; no geometry/use/allocation verification. Not gross sf.')
    derived('incremental_area_proxy',number('rezone_area_proxy')-number('current_area_proxy'),'zoning square feet proxy',['rezone_area_proxy','current_area_proxy'],'rezone - current','Not physical buildability or gross construction area')
    budgets=[]
    for percent,income in zip([70,80,100,120],by['income_2026_3person']['value']):
        cost=(D(income)*number('housing_cost_share')/12).quantize(D('.01'),rounding=decimal.ROUND_HALF_UP)
        id='monthly_budget_'+str(percent);derived(id,cost,'USD monthly total housing cost',['income_2026_3person','housing_cost_share','budget_household_size'],'annual_income_for_selected_AMI * 0.33 / 12','Illustrative cap includes mortgage, maintenance and shareholder-paid utilities. Not rent, sales price, mortgage approval or local affordability finding.')
        budgets.append({'ami_pct':percent,'income':income,'monthly_cap':float(cost),'claim_id':id})
    payload={'schema_version':'0.1','case_id':case['case_id'],'as_of':case['as_of'],'purpose':case['purpose'],'sources':sources,'claims':claims,'requirements':case['requirements'],'budgets':budgets}
    # Review binds to evidence, assumptions, calculations, requirements and interpretation, excluding review status.
    payload['packet_sha256']=sha(canonical({'case':case,'sources':sources,'claims':claims,'builder_sha256':sha(pathlib.Path(__file__).read_bytes())}))
    return payload

QUESTIONS=[
('next_decision','What concrete next decision does this packet let you make, and which role would make it?'),
('usefulness','Would you use it in your workflow? Name the artifact it would replace or improve and the most useful section.'),
('fatal_errors','Identify each material error or unsupported claim by claim ID; write none if none found. State consequence and correction.'),
('zoning','Which rule branches explain the 175/185-foot concepts given PLUTO MIH flags and §§141-23/141-25? What evidence resolves applicability?'),
('approval','Is the ELURP concept eligible? Which criteria, public-land disposition and environmental steps must be checked?'),
('units','Are the ~48/~60 estimates reasonable with the actual core, setbacks, amenity area and unit mix? What makes them fail?'),
('buyers','Which household sizes/incomes can buy and remain given savings, mortgage access, maintenance, reserves and resale restrictions?'),
('finance','What would an actual Open Door sources/uses and sales/maintenance model require? Which missing input changes the recommendation most?'),
('environment','What environmental investigation/pathway is needed for the former pest-control facility and elevated-rail frontage?'),
('community','Which published local priorities are needed? Is the packet keeping uncollected community views separate from agency goals?'),
('control','What current title, occupancy, site-control or sponsor evidence is required before treating this as executable?'),
('provenance','Can you follow a consequential claim to the original source passage and identify assumptions? Name a broken or unclear trace.'),
('workflow','Using your usual approach as baseline, which work remains manual and which checks would you automate? Give measured time if available; otherwise label estimate.'),
('acceptance','What exact correction or additional evidence would make you accept this playbook for a second site?'),
('signoff','Which conclusions would you refuse to sign, and which parts lie outside your expertise?')]


def review_template(slot,ir):
    return {'schema_version':'0.1','review_slot':slot,'packet_sha256':ir['packet_sha256'],'status':'pending','reviewer_name':None,'expertise':None,'reviewed_at':None,'independent_first_pass':None,'disposition':None,'answers':{k:None for k,q in QUESTIONS},'material_issues':[],'time_minutes':None,'time_measurement':'not_measured','identity_verification':'Not performed by this pipeline; reviewer attribution must be checked by project owner.'}


def render(case,ir):
    by={c['id']:c for c in ir['claims']};v=lambda k:by[k]['value']
    def cite(key,label=None):
        c=by[key];e=c.get('evidence')
        if e:return f"[{label or key}]({ir['sources'][e['source_id']]['url']}) ({e['locator']})"
        return f'`{key}`'
    t=f'''# 1337 Jerome Avenue opportunity brief for expert review

Prepared 4 October 2026 for the project owner and two independent housing advisors. **The next decision is whether the additional approximately {v('incremental_agency_units'):.0f} homes in HPD’s rezoning concept justify further zoning, design and economic review.** This packet reconstructs an existing public project; it does not identify an available private development site, nominate a bidder or respond to an issued RFP.

The brief is ready for an initial expert critique. Legal capacity, approval eligibility, project finances and actual buyer access remain unresolved. Both advisor reviews are pending.

## What we know

HPD plans affordable cooperative homeownership and community amenities at 1337 Jerome Avenue in Mount Eden, Bronx Community District 4, through Open Door. Its site page describes a vacant one-story building formerly used as a City pest-control facility until 2013 and slated for demolition. These are agency descriptions; we have not verified present occupancy or title. {cite('program','HPD project page')}; {cite('past_use')}.

GeoSearch’s exact-address candidate and PLUTO agree on BBL {v('parcel_bbl')}, with BIN {v('building_bin'):.0f} in the address response. PLUTO records a {v('lot_area'):,.0f} sf tax lot, {v('existing_bldg_area'):,.0f} sf building, zero residential units, R8A/C2-4/J and an HPD owner label. It flags an irregular lot and MIH options 1 and 3. These are recorded screening attributes, not a survey or legal conclusion. {cite('lot_area','PLUTO snapshot')}.

HPD’s September 14, 2026 Community Board briefing supplies the two planning concepts below. We retain their attribution rather than presenting them as independently computed entitlements.

## Existing condition and conditional scenarios

| Condition or scenario | Homes | FAR | Height | Meaning |
|---|---:|---:|---:|---|
| Recorded existing condition | 0 residential units | Built FAR recorded {v('existing_built_far'):.2f} | One recorded floor | Existing public-agency property; zero homes does not establish zero occupants |
| Illustrative No-Action | No residential redevelopment assumed | Existing condition retained | Existing condition retained | Analyst comparison assumption, not an accepted CEQR forecast |
| HPD current-zoning concept | Approximately {v('agency_current_units'):.0f} | {v('agency_current_far'):.2f} | {v('agency_current_height'):.0f} ft | HPD describes R8A/C2-4/Special Jerome; envelope review pending |
| HPD potential rezoning concept | Approximately {v('agency_rezone_units'):.0f} | {v('agency_rezone_far'):.2f} | {v('agency_rezone_height'):.0f} ft | HPD describes R9A/C2-4/Special Jerome with ELURP; change not approved |

Source: {cite('agency_current_units','HPD briefing')}. The difference is approximately {v('incremental_agency_units'):.0f} homes ({v('unit_increase_pct'):.0f}%); FAR rises {v('far_increase_pct'):.2f}%. This comparison estimates neither completed homes nor a causal rezoning effect.

Multiplying the recorded tax-lot area by HPD’s planning FAR yields {v('current_area_proxy'):,.2f} and {v('rezone_area_proxy'):,.2f} zoning-sf proxies, a difference of {v('incremental_area_proxy'):,.2f}. This arithmetic assumes the tax lot is the relevant zoning lot. It does not allocate commercial/community space, prove setbacks or core fit, or convert zoning area into gross construction area.

**Zoning reconciliation is the first professional task.** Section 141-25’s special R8A height branch refers to sites outside MIH areas and within 100 feet of a wide street. PLUTO’s MIH flags make that applicability unresolved. Section 141-23 has a separate elevated-rail branch outside Subdistrict A; general rules, affordable-housing qualifications and other modifications also matter. The flag is not proof that HPD’s concept is wrong. Ask an architect/zoning specialist to identify the controlling branch, mapped boundaries and assumptions. {cite('zoning_141_25_condition','§141-25')}; {cite('zoning_141_23_condition','§141-23')}.

HPD’s current expedited-housing page describes modest density increases of no more than 30% as one ELURP-CPC example. The {v('far_increase_pct'):.2f}% arithmetic fits that example numerically. It does not establish the full statutory eligibility test or resolve disposition of public land, environmental review or approvals. {cite('expedited_density_description','HPD approval pathways')}.

## Open Door requirements that change the analysis

The linked Open Door term sheet is dated June 30, 2025. It describes homeownership, not a rental debt-coverage model. The property must be HDFC-owned during construction. Cooperative projects have a minimum {v('coop_regulatory_years'):.0f}-year regulatory agreement, owner-occupancy and resale restrictions, operating/replacement reserves, a minimum 10% resale flip tax to the co-op, an approved monitor/property manager and minimum {v('maintenance_escalation')*100:.0f}% annual maintenance increases. {cite('hdfc_ownership')}; {cite('coop_regulatory_years')}.

| Underwritten AMI tier | Published maximum subsidy per home |
|---|---:|
| Up to 80% | $445,000 |
| 81–90% | $430,000 |
| 91–100% | $365,000 |
| 101–120% | $355,000 |

These are contingent maxima, not commitments or a project budget. The sheet conditions them on AHOP/AHC availability, market conditions and HPD’s determination. We have not verified funding availability or the eventual Jerome unit mix. {cite('subsidy_caps','Open Door table')}; {cite('subsidy_contingency')}.

Prices are set jointly with HPD at levels affordable to households earning 70–120% AMI or as dictated by market, with at least a 10% discount to market. The sheet caps total housing costs at 33% of annual income and uses maintenance, shareholder-paid utilities and projected mortgage payments, with a 30-year mortgage, 5% down payment and current fixed rates. This is a rule to apply, not a verified price. {cite('housing_cost_share','Sales price rules')}.

## Who could afford the homes

For an illustrative three-person household, applying the 33% rule to HPD’s **2026 regional income table** gives the following total monthly housing-cost ceilings. These are not rents, sale prices or evidence that local residents can obtain mortgages.

| AMI benchmark | Annual household income | Total monthly housing-cost ceiling |
|---|---:|---:|
'''
    for b in ir['budgets']:t+=f"| {b['ami_pct']}% | ${b['income']:,.0f} | ${b['monthly_cap']:,.2f} |\n"
    t+=f'''
Source: {cite('income_2026_3person','2026 HPD income table')}, combined with Open Door’s cost share. The same HPD webpage has a 2025 rent table; we have not used it. Annual maintenance increases and reserve needs must be tested over time. Down payment, closing costs, buyer assets/credit, household/unit-size matching and assistance remain missing. Regional AMI is not neighborhood median income, and this program alone does not establish access for households below the stated sale-price targeting range.

## Community input and timing

The captured project page is in community visioning, with a questionnaire deadline stated as October 16, and says the RFP is planned for Fall 2026. The September slide deck gives RFP release before year-end, submissions in early spring 2027 and designation in late spring/early summer 2027. These are agency planning statements, not final procurement deadlines; preserve both rather than inventing a single precise schedule. {cite('rfp_status','Project status')}; {cite('agency_timeline','Briefing schedule')}.

A completed Jerome Community Visioning Report and site-specific issued RFP were not located in the captured project links. Community amenities are an agency goal; the actual community’s preferred spaces, services and tradeoffs remain uncollected here. Do not substitute the New Utrecht library project’s requirements or citywide policy for Jerome feedback. The next community input is the published report and final RFP, when available.

## What would make the concepts fail

- The actual surveyed geometry, MIH/subdistrict applicability, setbacks, elevated-rail rules, core/elevators or ground-floor uses support fewer units or a different envelope.
- The extra homes require costs or funding that cannot be supported by restricted sales, subsidy availability, reserves and maintenance.
- Prospective buyers meet income limits but cannot fund down payment/closing costs, obtain a mortgage or sustain escalating maintenance.
- Community needs require a different amenity or housing mix, or the final RFP/qualified-developer conditions differ from this reconstruction.
- Site control, occupancy, contamination, rail noise/air or infrastructure obligations change the design, costs or schedule.

These are analyst risk hypotheses, not findings about this property.

## Environmental and design evidence

The exact-BBL E-designation query returned zero rows. That does not clear contamination, lot-history instruments or environmental obligations. Former pest-control use and elevated-rail frontage justify asking for the applicable investigation and noise/air work; they do not prove contamination.

HPD’s 2026 design process applies to Design Consultation submissions on or after October 1, 2026. Its environmental note requires Phase I **unless** the site follows Brownfield Cleanup or hazardous-material E-designation pathways, and requires noise screening. The exceptions must remain in the rule. No environmental pathway, investigation or agency acceptance is established here. {cite('environmental_review_rule','HPD process guide')}.

## Requirement and evidence checklist

All twelve requirements below remain unresolved for an executable project. Technical checks establish a traceable review packet; they cannot resolve these professional decisions.

| Requirement | Evidence needed | Review owner |
|---|---|---|
'''
    for r in ir['requirements']:t+=f"| {r['title']} | {r['acceptance']} | {r['review_owner']} |\n"
    t+='''
## Financial model contract

The machine-readable `finance-inputs.json` is a completeness contract, with missing inputs represented as null rather than zero. It asks for acquisition/disposition/land debt, gross and zoning areas, hard/soft/demolition/remediation costs, contingency, financing/interest/carry, fees, construction reserves, tax exemption and timing, public/private sources, unit/income mix, restricted sale proceeds, maintenance/utility/reserve costs and buyer financing/access. There is no invented cost estimate, funding gap or projected sales price.

Keep project sources/uses separate from buyer financing and ongoing co-op operations. A project can balance financially while excluding its intended buyers. A nominal $1 public-land disposition does not erase land debt, restrictions or transaction costs.

## Advisor review and acceptance

Each advisor should review this version independently before seeing the other’s answers. Start with the scenario comparison and zoning flag, then the buyer/finance analysis, then the requirement checklist. Use the attached review protocol and independent A/B forms; mark conclusions outside your expertise. Readiness for a second site means each advisor identifies a useful next decision and supplies actionable corrections, material issues are reconciled and every accepted change retains provenance. Two agreeing advisors do not establish legal or financial approval.

Both forms are currently pending. No messages have been sent to advisors and no external review is claimed. The technical gates allow an initial advisor packet while blocking an agency proposal or development recommendation until unresolved requirements and review dispositions are addressed.

## Reproduction and evidence

The companion packet contains `case.json` (authored facts/assumptions/unknowns), `ir.json` (bound claims, arithmetic, sources and requirements), `claim-trace.md` (exact passages/fields), `finance-inputs.json`, `review-protocol.md`, two independent review forms, validation results and retained evidence. Original response bytes have URL/timestamp/SHA-256 receipts. PDF passages use page locators and retained `pdftotext -layout` output. Zoning text is a retrieved snapshot; effective dates and site applicability need professional review.

Run `python research/jerome-brief/build.py`, `python research/jerome-brief/validate.py` and `python -m unittest discover -s research/jerome-brief/tests -v`. Offline replay must reproduce generated artifacts. For fresh evidence, create a new versioned snapshot and reset reviews; the collector refuses to overwrite this one.
'''
    return t


def build():
    case=load('case.json');ir=bind(case);write('ir.json',ir)
    (P/'brief.md').write_text(render(case,ir))
    (P/'page-body.md').write_text(render(case,ir).split('\n\n',1)[1])
    trace='# Claim trace for 1337 Jerome Avenue\n\nEvery observed claim below binds to retained source bytes. Quote matching verifies extraction, not legal interpretation. Derived claims list dependencies; unknowns remain null.\n\n'
    for c in ir['claims']:
        trace+=f"## {c['id']}\n\nKind: {c['kind']}. Value: `{json.dumps(c['value'],ensure_ascii=False)}`. Units: {c['unit'] or 'not applicable'}.\n\n"
        if 'evidence' in c:
            e=c['evidence'];r=ir['sources'][e['source_id']];trace+=f"[Original source]({r['url']}); {e['locator']}; retrieved {r['retrieved_at']}; SHA-256 `{r['sha256']}`.\n\n"
            trace+='Exact normalized passage: '+e['quote']+'\n\n' if 'quote' in e else 'JSON selector: `'+json.dumps(e['selector'])+'`.\n\n'
        if 'inputs' in c:trace+=f"Formula: `{c['formula']}`. Dependencies: {', '.join(c['inputs'])}.\n\n"
        trace+=c.get('scope',c.get('reason',''))+'\n\n'
    (P/'claim-trace.md').write_text(trace)
    protocol='''# Independent advisor review protocol

Please review the 1337 Jerome Avenue brief independently before reading the other advisor’s response. This tests whether an open housing playbook produces useful, traceable work. It does not ask you to approve a development, endorse a bidder or act for HPD.

Suggested first pass: 30–45 minutes. Record actual time if measured; otherwise leave null. Read the summary/scenarios and zoning issue, affordability/program discussion and requirements, then inspect at least three consequential claims in claim-trace.md against their original sources. Follow with a short conversation focused on the largest decision-changing gap.

Use one A/B form per advisor. Enter name, expertise, date, version fingerprint and whether this was an independent first pass. Answer every question, including “outside my expertise” where appropriate. Disposition choices: accept_for_second_site, revise or reject. Acceptance is about this research workflow, not legal feasibility.

'''
    for i,(key,q) in enumerate(QUESTIONS,1):protocol+=f'{i}. **{key}** — {q}\n\n'
    protocol+='''## Reconcile after the independent reviews

Record each material issue by claim/requirement ID, evidence, consequence, proposed correction, owner and disposition. Preserve disagreements rather than averaging them into a score. Ask a relevant professional to decide disagreements outside either advisor’s expertise. Changes to evidence, assumptions or interpretation create a new packet fingerprint and reset review validity.

For a second-site pilot, require both reviewers to identify a useful next decision, complete their scoped review, and accept the corrected workflow with no unresolved material issues. Compare against a redacted customary memo if they can supply one. Measure completeness, material-error count, trace success, work/time saved and remaining manual work; do not claim speed gains without a baseline.

The validator checks form completeness and fingerprint binding. It does not authenticate reviewer identity or enforce that they did not communicate. The project owner must confirm attribution and independence. Receiving a form is not a substitute for professional scope-specific signoff.
'''
    (P/'review-protocol.md').write_text(protocol)
    reviews=P/'reviews';reviews.mkdir(exist_ok=True)
    for slot in ['A','B']:
        f=reviews/(slot+'.json')
        existing=json.loads(f.read_text()) if f.exists() else None
        untouched=existing and existing.get('status')=='pending' and not existing.get('reviewer_name') and not existing.get('material_issues') and all(v is None for v in existing.get('answers',{}).values())
        if not existing or untouched:f.write_text(json.dumps(review_template(slot,ir),indent=2)+'\n')
    fields=['zoning_area_sf','gross_area_sf','unit_and_ami_mix','community_amenity_program','land_disposition_and_land_debt','demolition','remediation','hard_costs','soft_costs','contingencies','interest_and_financing_fees','taxes_and_carry','developer_fee','capitalized_reserves','tax_exemption_and_timing','subsidy_commitment_by_program','private_construction_sources','sponsor_equity','restricted_sales_proceeds','sales_and_absorption_schedule','maintenance_and_operating_costs','replacement_reserves','shareholder_utilities','buyer_mortgage_rates_and_fees','buyer_down_payment_and_closing_costs','buyer_assets_credit_and_assistance','market_discount_comparables','long_term_maintenance_escalation_and_stress']
    existing_finance=load('finance-inputs.json') if (P/'finance-inputs.json').exists() else None
    if existing_finance and any(v is not None for v in existing_finance.get('inputs',{}).values()):raise ValueError('Preserve supplied finance inputs; bind them to new versioned evidence before rebuilding')
    write('finance-inputs.json',{'schema_version':'0.1','status':'incomplete','packet_sha256':ir['packet_sha256'],'meaning':'Input checklist, not executable underwriting. Null is missing, never zero. Each supplied value needs units, source/assumption, vintage and review attribution.','inputs':{f:None for f in fields}})
    write('requirements.json',{'packet_sha256':ir['packet_sha256'],'requirements':ir['requirements']})
    files=['ir.json','brief.md','page-body.md','claim-trace.md','review-protocol.md','finance-inputs.json','requirements.json']
    write('manifest.json',{'packet_sha256':ir['packet_sha256'],'outputs':{name:sha((P/name).read_bytes()) for name in files}})
    print(f"Built {len(ir['claims'])} claims; packet {ir['packet_sha256']}")
if __name__=='__main__':build()
