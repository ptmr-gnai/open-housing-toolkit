"""Authored bounded obligation map; unmapped text remains an explicit review queue. MIT."""
import json
from scan import BASE,ROOT,discover,fp
S=json.loads((ROOT/'research/eligibility-gates/sources.json').read_text());units=discover(S)
reqs=[];changes=[]
def unit(case,needle,source=None):
    matches=[u for u in units if u['case']==case and needle in u['quote'] and (source is None or u['source_id']==source)]
    if len(matches)!=1:raise ValueError((case,needle,len(matches)))
    return matches[0]
def add(case,key,label,needle,mode='required',condition=None,excel=False,source=None):
    u=unit(case,needle,source)
    r={'id':case+'.'+key,'case':case,'label':label,'mode':mode,'condition':condition,'excel':excel,'anchors':[u['id']],'content_review_required':True,'owner':'Proposal coordinator and responsible specialist','phase':'submission','authority':'authored source interpretation, pending independent review'}
    reqs.append(r);return r
for case in ['west169','stanns']:
    for key,needle in [('A1','Form A-1'),('A2','Form A-2')]:
        add(case,'form_'+key,'Form '+key,needle,source=case+'_rfp')
    add(case,'form_B','Proposal summary Form B','Form B',source=case+'_rfp')
if True:
    c='west169'
    for key in ['D1','E1','E2','E3']:
        add(c,'form_'+key,'Form '+key,key[0]+'-'+key[1],excel=key in ['E1','E2'],source=c+'_rfp')
    add(c,'form_D2','Nonprofit team member form D-2','Form D-2','conditional','nonprofit_team',source=c+'_rfp')
    add(c,'form_G','Financing scenario Form G','Form G:','required',excel=True,source=c+'_rfp')
    add(c,'organization_chart','Ownership and organization chart','Organizational Structure.',source=c+'_rfp')
    add(c,'project_narrative','Project narrative','Project Narrative must introduce',source=c+'_rfp')
    add(c,'project_budgets','Hard and soft cost budgets','Project Budgets.',source=c+'_rfp')
    add(c,'zoning_analysis','Detailed zoning analysis','Zoning Analysis: Zoning map',source=c+'_rfp')
    add(c,'staffing_plan','Optional staffing and governance plan','Project Staffing and Governance Plan','optional',source=c+'_rfp')
    r=add(c,'commercial_management','Commercial management evidence in permitted format','Form E-4.','conditional','nonresidential_space',source=c+'_rfp')
    r['anchors'].append(unit(c,'There is no Form e-4',c+'_add3')['id'])
    changes.append({'id':'west169.replace_e4','case':c,'anchor':r['anchors'][-1],'operation':'replace_artifact','target':r['id'],'obsolete_artifact':'form_E4','required_effect':{'mode':'conditional','condition':'nonresidential_space','excel':False,'phase':'submission'},'reason':'No E-4 blank form exists; commercial experience may use chosen format. Do not drop the evidence obligation.'})
    r=add(c,'condominium_requirement','Condominium component','The proposed project may include a condominium','optional',source=c+'_add3')
    changes.append({'id':'west169.condo_optional','case':c,'anchor':r['anchors'][0],'operation':'not_mandatory','target':r['id'],'obsolete_artifact':None,'required_effect':{'mode':'optional','condition':None,'excel':False,'phase':'submission'},'reason':'Condominium is permitted, not required; counsel experience follows proposed elements.'})
    r=add(c,'rail_overbuild','Rail-overbuild experience','Q12: The RFP notes','not_required',source=c+'_add1')
    changes.append({'id':'west169.rail_removed','case':c,'anchor':r['anchors'][0],'operation':'not_required','target':r['id'],'obsolete_artifact':'rail_overbuild','required_effect':{'mode':'not_required','condition':None,'excel':False,'phase':'submission'},'reason':'This copied experience criterion does not apply.'})
if True:
    c='stanns'
    for key in ['C1','C2']:
        add(c,'form_'+key,'Form '+key,'Forms C-1' if key=='C1' else 'Form C-2','required' if key=='C1' else 'conditional',None if key=='C1' else 'nonprofit_team',source=c+'_rfp')
    for key in ['D1','D2','D3']:
        add(c,'form_'+key,'Per-principal Form '+key+' including None when applicable','Forms D-1 through D-3',excel=key in ['D1','D2'],source=c+'_rfp')
    add(c,'form_K','Financing proposal Form K','completed Financing Proposal (Form K)',excel=True,source=c+'_rfp')
    add(c,'project_narrative','Project narrative','In addition, Applicants must include',source=c+'_rfp')
    add(c,'market_comparables','Residential income comparables','detailed rental listings of at least three properties',source=c+'_rfp')
    add(c,'marketing_plan','Fair housing marketing plan','Applicants must provide a marketing plan',source=c+'_rfp')
    r=add(c,'gc_identified','General contractor identified at proposal','Q12: The RFP states','required',source=c+'_add2')
    changes.append({'id':'stanns.gc_at_submission','case':c,'anchor':r['anchors'][0],'operation':'add','target':r['id'],'obsolete_artifact':None,'required_effect':{'mode':'required','condition':None,'excel':False,'phase':'submission'},'reason':'GC identification is necessary for proposal, not only after designation.'})
    r=add(c,'green_certificate','Enterprise Green Communities certification','Q14: Will Enterprise','deferred',source=c+'_add2');r['phase']='post_selection'
    changes.append({'id':'stanns.cert_deferred','case':c,'anchor':r['anchors'][0],'operation':'defer','target':r['id'],'obsolete_artifact':'green_certificate_at_submission','required_effect':{'mode':'deferred','condition':None,'excel':False,'phase':'post_selection'},'reason':'Certification follows selection. Submission sustainability material remains a separate instruction.'})
    add(c,'sustainability_submission','Sustainability narrative and certification overlay instructions','TAB I– Sustainability','review_instruction',source=c+'_rfp')
    r=add(c,'multiple_site_submissions','Obsolete multiple-site separate submission instruction','Q18: On page 21','not_required',source=c+'_add1')
    changes.append({'id':'stanns.multisite_removed','case':c,'anchor':r['anchors'][0],'operation':'not_required','target':r['id'],'obsolete_artifact':'multiple_site_submissions','required_effect':{'mode':'not_required','condition':None,'excel':False,'phase':'submission'},'reason':'Agency says disregard former multi-site language.'})
registry={'version':'0.1','requirements':reqs,'changes':changes,'units':[],'limits':['Initial authored mapping, not complete semantic expansion.','Nested clauses, per-principal cardinality, signatures, formula correctness, dates and referenced appendices require substantive review.','All addendum Q/A text anchors enumerated, but cross-page continuation and graphics are not fully expanded.','Not a blind analyst benchmark, real submitted proposal or expert accepted inventory.']}
for u in units:
    linked=[r['id'] for r in reqs if u['id'] in r['anchors']]
    registry['units'].append({'anchor':u['id'],'source_fingerprint':fp(u),'requirements':linked,'expansion':'authored_partial' if linked else 'needs_review','review_status':'pending','reason':'Scoped artifacts mapped; nested obligations remain to review.' if linked else 'Unexpanded source unit retained in review queue.'})
for r in reqs:
    if r['id'] in {'west169.form_E1','west169.form_E2'}:
        text=(ROOT/'research/benchmark-case-search/inputs/97-west-169th-st-rfp.text').read_text().split('\f')[15]
        q=' '.join(text.split());start=q.index('Forms E1-3');end=q.index('format.',start)+len('format.')
        r['supporting_citations']=[{'source_id':'west169_rfp','pdf_page':16,'quote':q[start:end]}]
(BASE/'registry.json').write_text(json.dumps(registry,indent=2)+'\n')
print(len(reqs),'scoped obligations;',len(changes),'addendum operations;',len(units),'independent source anchors')
