"""Guide-slot mapping without promoting diagnostic data into regulatory fields. MIT."""
from pathlib import Path
from .contracts import REQUIRED_IDS,Slot,Status as S,validate_request,read_json,fields
from housing_workflow.contracts import digest,dumps

ROOT=Path(__file__).resolve().parents[1]
ADAPTERS={'project_name','contact','preparer','date','application','missing','project_summary','interpret','res_zsf','total_homes','rent_mapping','income_mapping','reference_year','timing','conflict','nonres_zsf','jobs','construction_area','version_stage'}


def validate_catalog(catalog,guidance):
    fields(catalog,['version','inventory_scope','requirements'])
    fields(guidance,['version','extraction_tool_version','extraction_method','preparation_script_sha256','sources','scope'])
    if catalog['version']!='0.1.0' or guidance['version']!='0.1.0':raise ValueError('Unsupported guidance inventory version')
    items=catalog['requirements'];ids=[r['id'] for r in items]
    if len(ids)!=len(set(ids)) or set(ids)!=REQUIRED_IDS:raise ValueError('Required instruction inventory missing, duplicate or unexpected')
    docs={s['id']:s for s in guidance['sources']}
    if len(guidance['sources'])!=3 or set(docs)!={'guide','form','criteria'}:raise ValueError('Missing authoritative reference document')
    for r in items:
        fields(r,['id','section','label','adapter','citations','category'])
        if r['category'] not in {'instruction_slot','conditional_instruction','narrative_prompt'}:raise ValueError('Unknown instruction category')
        if r['id'].startswith('narrative.goal') and r['category']!='narrative_prompt':raise ValueError('Narrative prompt promoted to independent legal test')
        if r['adapter'] not in ADAPTERS or type(r['section'])!=int or r['section'] not in range(6) or not r['citations']:raise ValueError('Unmapped instruction slot')
        for c in r['citations']:
            fields(c,['document','pdf_page','subsection','url','document_sha256','page_sha256'])
            d=docs[c['document']];p=next((p for p in d['pages'] if p['pdf_page']==c['pdf_page']),None)
            if p is None or c['document_sha256']!=d['sha256'] or c['page_sha256']!=p['normalized_text_sha256'] or c['url']!=d['url']:raise ValueError('Guidance document/page binding changed; remap with review')
    # Cross-document divergence cannot be dropped or downgraded to one source.
    conflict=next(r for r in items if r['id']=='nonres.area_conflict')
    if {c['document'] for c in conflict['citations']}!={'guide','form'}:raise ValueError('Instruction divergence lost a source')


def compile_drafts(req,parent,parent_sha,site_analysis,site_sha,catalog,guidance):
    validate_request(req);validate_catalog(catalog,guidance)
    claims={c['id']:c for c in parent['claims']};site={c['id']:(i,c) for i,c in enumerate(site_analysis['claims'])}
    docs={s['id']:s for s in guidance['sources']};year=int(req['prepared_on'][:4]);reports=[]
    def binding(cid):
        i=next(i for i,c in enumerate(parent['claims']) if c['id']==cid)
        return {'file':'comparison-run/ir.json','sha256':parent_sha,'pointer':'/claims/'+str(i)+'/value','claim_id':cid,'kind':claims[cid]['kind'],'value':claims[cid]['value']}
    for p in parent['programs']:
        slots=[];total=claims[p['total_claim']]['value']
        for r in catalog['requirements']:
            mode=r['adapter'];status=S.MISSING;value=None;bindings=[]
            reason='Required material is not supplied by the current comparison. No placeholder zero or unsupported narrative has been inserted.'
            if mode=='project_name':
                status=S.ILLUSTRATIVE;value=p['label'];reason='Comparison label only; not an application project name.'
                bindings=[{'file':'comparison-run/ir.json','sha256':parent_sha,'pointer':'/programs/'+str(parent['programs'].index(p))+'/label','kind':'comparison_metadata','value':value}]
            elif mode=='contact':reason=req['contact']['rationale']
            elif mode=='version_stage':status=S.INTERPRET;reason='Application certification/adoption stage is unknown. Our immutable reruns track changed inputs; that engineering policy is not a statement that the City requires post-certification report updates.'
            elif mode=='preparer':
                status=S.FILLED;value=req['prepared_by'];reason='Supplied draft authorship metadata, not applicant authority or professional endorsement.'
                bindings=[{'file':'request.json','sha256':digest(dumps(req).encode()),'pointer':'/prepared_by','kind':'supplied_metadata','value':value}]
            elif mode=='date':
                status=S.FILLED;value=req['prepared_on'];reason='Supplied preparation date; distinct from price/reference years.'
                bindings=[{'file':'request.json','sha256':digest(dumps(req).encode()),'pointer':'/prepared_on','kind':'supplied_metadata','value':value}]
            elif mode=='application':status=S.INTERPRET;reason=req['application']['rationale']+' Conditional scope or exceptions need an identified land-use action and professional interpretation.'
            elif mode=='project_summary':
                status=S.ILLUSTRATIVE;value=f'An illustrative rental offer of {total} homes for the linked site. Community context and fair-housing interpretation remain incomplete.';bindings=[binding(p['total_claim'])];reason='Uses an explicit assumption; not a verified development plan.'
            elif mode=='total_homes':status=S.ILLUSTRATIVE;value=total;bindings=[binding(p['total_claim'])];reason='Anticipated quantity in a constructed program, not a permitted or verified count.'
            elif mode=='interpret':
                status=S.INTERPRET;reason='Program rules, community evidence and/or an attributed professional interpretation are missing. Cost-test results and tool objectives cannot substitute for this field.'
            elif mode in {'res_zsf','nonres_zsf','construction_area'}:
                cid={'res_zsf':'scenario.residential_gross_sf','nonres_zsf':'scenario.nonresidential_gross_sf','construction_area':'scenario.gross_area_sf'}[mode]
                if cid in site:
                    i,c=site[cid];bindings=[{'file':'comparison-run/analysis-run/ir.json','sha256':site_sha,'pointer':'/claims/'+str(i)+'/value','claim_id':cid,'kind':c['kind'],'value':c['value'],'unit':c['unit'],'use':'candidate_only_not_populated'}]
                    status=S.INTERPRET
                    reason=(f'An upstream gross-area assumption is available, but it is not zoning square feet and is not reconciled to this {total}-home program. No conversion or construction-job estimate is made.' if mode!='construction_area' else 'An earlier gross-area assumption is available, but it is not established for this program. Do not manufacture construction employment from an unrelated scenario.')
            elif mode=='rent_mapping':
                status=S.INTERPRET;bindings=[binding(b['claims']['monthly_rent_usd']) for b in p['bins']]
                reason='Contract-rent assumptions are available. They are not verified AMI/program-based illustrative rent ranges. They appear as candidate inputs below, not as filled official rent cells.'
            elif mode=='income_mapping':
                status=S.INTERPRET;bindings=[binding(h['annual_income_claim']) for h in parent['profiles']]
                reason='Hypothetical household incomes are available. They are not program eligibility ranges; no inferred eligibility or AMI allocation is inserted.'
            elif mode=='reference_year':
                status=S.INTERPRET if parent['price_year']!=year else S.ILLUSTRATIVE
                value=None if status==S.INTERPRET else str(parent['price_year'])
                reason=f"The input comparison uses {parent['price_year']} references; this draft is prepared in {year}. Current reporting applicability and rounding conventions need review. No inflation or automatic year substitution."
            elif mode=='timing':
                status=S.FILLED;value='Final rents use construction-time limits; qualifying incomes use marketing-time limits.'
                reason='Reporting caveat from pinned guidance, not actual future limits or a certified schedule.'
            elif mode=='conflict':
                status=S.INTERPRET;reason='Pinned form (2023) says to skip the nonresidential section without a specific tenant; pinned guide (2025) still requests area information. Preserve both, keep area slots visible, suppress speculative job data, and request interpretation.'
            elif mode=='jobs':
                if req['nonresidential_tenants']['status']=='none_identified':
                    status=S.NA;reason='Conditional exclusion under the supplied none-identified assumption, attributed to '+req['nonresidential_tenants']['attribution']+'. '+req['nonresidential_tenants']['rationale']+' This is not a finding of no jobs or no existing businesses.'
                else:status=S.INTERPRET;reason='Tenant identification is unresolved. No job count, NAICS assignment, wage or workforce estimate is produced.'
            for b in bindings:b.setdefault('use','candidate_only_not_populated' if status==S.INTERPRET else 'input_for_slot')
            slots.append(Slot(r['id'],r['section'],r['label'],status,value,reason,tuple(bindings),tuple(r['citations'])).to_dict())
        counts={s.value:sum(row['status']==s.value for row in slots) for s in S}
        reports.append({'program_id':p['id'],'program_label':p['label'],'site_bbl':parent['site_bbl'],'report_status':'incomplete_illustrative_draft','official_submission_ready':False,
                        'applicability':'not_determined','professional_review':'pending','slots':slots,'status_counts':counts,
                        'interpretation':'A populated slot is not proof of compliance; status counts are not a completeness percentage or benefit score.'})
    return {'version':'0.1.0','module':'rer-preparation','prepared_on':req['prepared_on'],'prepared_by':req['prepared_by'],
            'request_sha256':digest(dumps(req).encode()),'comparison_sha256':parent_sha,'guide_inventory_sha256':digest(dumps(catalog).encode()),
            'scope':catalog['inventory_scope'],'source_documents':guidance['sources'],'source_verification_scope':guidance['scope'],
            'reports':reports,'comparison_programs':parent['programs'],'comparison_profiles':parent['profiles'],'comparison_claims':parent['claims'],'comparison_claims_base':'comparison-run/',
            'limitations':['This module prepares a draft and instruction map, not the official fillable PDF or an agency submission.','No EDDE export, displacement map or community geography has been validated/imported.','Applicant narrative and legal/program interpretation remain unresolved.','Parent household-cost diagnostics are supplemental and are not RER affordability classifications.','Manual scoped inventory; unrecognized omissions and professional correctness remain untested.']}
