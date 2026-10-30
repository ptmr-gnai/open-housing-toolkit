"""Technical integrity, scoped review intake and deterministic release gates. MIT."""
import argparse,hashlib,json,pathlib,sys
from build import P,bind,canonical,load,QUESTIONS,sha

class InvalidPacket(ValueError):pass

def require(condition,message):
    if not condition:raise InvalidPacket(message)

def validate_case(case):
    require(case['schema_version']=='0.1','Unsupported DSL version')
    require(case['case_id']=='jerome-1337','Different site needs a new evidence snapshot')
    claims={c['id']:c for c in case['claims']}
    require(len(claims)==len(case['claims']),'Duplicate claims')
    for c in case['claims']:
        require(c['kind'] in ['observed','assumption','unknown'],'Unsupported authored claim kind')
        require('value' in c and 'unit' in c,'Missing typed claim fields')
        if c['kind']=='unknown':require(c['value'] is None and bool(c.get('reason')),'Unknown cannot become zero/known without evidence')
        if c['kind']=='assumption':require(bool(c.get('reason')),'Unexplained assumption')
    required=set(['zoning','community','control','occupants','environment','finance','approvals','team','transit','buyers','rfp','design'])
    require({r['id'] for r in case['requirements']}==required,'Required professional gates removed or changed')
    for r in case['requirements']:
        require(r['status']=='unresolved','This snapshot supports unresolved gates only; new professional evidence needs a versioned packet')
        require(r['unknown_claim'] in claims and claims[r['unknown_claim']]['kind']=='unknown','Professional requirement must reference a typed unknown')
        require(bool(r['review_owner']) and bool(r['acceptance']),'Missing accountable requirement owner or evidence standard')
    return True

def review_errors(review,ir):
    if review.get('status')=='pending':return ['review pending']
    errors=[]
    if review.get('status')!='completed':errors.append('unsupported review status')
    if review.get('packet_sha256')!=ir['packet_sha256']:errors.append('stale packet fingerprint')
    for field in ['reviewer_name','expertise','reviewed_at']:
        if not isinstance(review.get(field),str) or not review[field].strip():errors.append('missing '+field)
    if review.get('independent_first_pass') is not True:errors.append('independent first pass not attested')
    if review.get('disposition') not in ['accept_for_second_site','revise','reject']:errors.append('missing/invalid disposition')
    for key,_ in QUESTIONS:
        answer=review.get('answers',{}).get(key)
        if not isinstance(answer,str) or not answer.strip():errors.append('missing answer '+key)
    if not isinstance(review.get('material_issues'),list):errors.append('material issue ledger required')
    else:
        for issue in review['material_issues']:
            if not all(isinstance(issue.get(k),str) and issue[k].strip() for k in ['target_id','description','consequence','correction','owner','disposition']):errors.append('incomplete material issue')
            if issue.get('target_id') not in {c['id'] for c in ir['claims']}|{r['id'] for r in ir['requirements']}:errors.append('unknown material issue target')
            # Closing an issue requires rebinding its correction/evidence in a new packet, not just editing a status field.
            if issue.get('disposition')!='open':errors.append('issue closure requires new reconciled packet evidence')
    return errors

def gates(ir,reviews):
    errors=[review_errors(r,ir) for r in reviews]
    names=[r.get('reviewer_name','') for r in reviews]
    same_identity=all(names) and names[0].strip().casefold()==names[1].strip().casefold()
    second=not any(errors) and not same_identity and all(r.get('disposition')=='accept_for_second_site' and not r.get('material_issues') for r in reviews)
    unresolved=[r['id'] for r in ir['requirements'] if r['status']!='resolved']
    return {'advisor_packet':{'allowed':True,'meaning':'Technical review readiness only; expert outcomes pending'},'second_site_workflow':{'allowed':second,'meaning':'Workflow feedback acceptance, not feasibility','review_errors':errors,'same_reviewer':bool(same_identity)},'agency_proposal':{'allowed':False,'meaning':'Snapshot has no issued Jerome RFP, completed professional evidence or approved project','unresolved_requirements':unresolved},'development_recommendation':{'allowed':False,'unresolved_requirements':unresolved},'reviewer_authentication':'Not performed; project owner must verify attribution and independence.'}

GENERATED=['ir.json','brief.md','page-body.md','claim-trace.md','review-protocol.md','finance-inputs.json','requirements.json']

def validate():
    case=load('case.json');validate_case(case);expected=bind(case);ir=load('ir.json')
    require(canonical(expected)==canonical(ir),'IR is stale or altered; rebuild from evidence')
    by={c['id']:c for c in ir['claims']};seen=set()
    for c in ir['claims']:
        for dep in c.get('inputs',[]):require(dep in seen,'Dangling/forward/cyclic dependency '+dep)
        seen.add(c['id'])
    # Independent identity cross-check: confidence score alone is insufficient.
    hits=[f for f in load('cache/geosearch.body')['features'] if f['properties'].get('name')=='1337 JEROME AVENUE']
    require(any(str(f['properties']['addendum']['pad']['bbl'])=='2028560051' and str(f['properties']['addendum']['pad']['bin'])=='2008295' for f in hits),'Parcel/building corroboration failed')
    require(by['income_2026_3person']['evidence']['source_id']=='ami','Income vintage source drift')
    require(by['housing_cost_share']['value']==0.33,'Wrong program affordability rule')
    require(by['e_screen']['value']==0 and by['environment']['kind']=='unknown','Empty environment query cannot clear site')
    finance=load('finance-inputs.json');require(all(v is None for v in finance['inputs'].values()),'This version has no sourced project financial inputs; new values require a versioned model')
    manifest=load('manifest.json');require(manifest['packet_sha256']==ir['packet_sha256'],'Stale artifact manifest')
    require(set(manifest['outputs'])==set(GENERATED),'Output manifest missing generated files')
    for name,digest in manifest['outputs'].items():require(sha((P/name).read_bytes())==digest,'Generated artifact altered: '+name)
    reviews=[load('reviews/A.json'),load('reviews/B.json')]
    require([r['review_slot'] for r in reviews]==['A','B'],'Review slots swapped or duplicated')
    require(all(r['packet_sha256']==ir['packet_sha256'] for r in reviews),'Stale review form; preserve old feedback and create new version-bound forms')
    gate=gates(ir,reviews)
    for r in reviews:
        if r['status']!='pending':require(not review_errors(r,ir),'Malformed completed review: '+str(review_errors(r,ir)))
    result={'technical_status':'pass','packet_sha256':ir['packet_sha256'],'source_receipts':len(ir['sources']),'bound_claims':len(ir['claims']),'professional_requirements':len(ir['requirements']),'gates':gate}
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--gate',choices=['advisor_packet','second_site_workflow','agency_proposal','development_recommendation']);args=parser.parse_args()
    try:result=validate()
    except (ValueError,KeyError,TypeError) as exc:print('FAIL: '+str(exc));sys.exit(1)
    print(json.dumps(result,indent=2))
    if args.gate and not result['gates'][args.gate]['allowed']:sys.exit(2)
