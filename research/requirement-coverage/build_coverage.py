"""Retain compact observed fault controls and explicit source review queue. MIT."""
import copy,json,pathlib
from scan import BASE,ROOT,discover,fp
from coverage_engine import load,pinned_audit,packet_check
from fixtures import packet
import engine as eligibility

def projection(r):
    return {'case':r['case'],'packet':r['packet'],'contract':r['contract'],'requirements':r['requirements'],'obsolete_requests':r['obsolete_requests'],'blockers':r['blockers'],'submission_completeness_claim_allowed':r['submission_completeness_claim_allowed'],'coverage_summary':{k:r['coverage'][k] for k in ['source_units','library_source_units','scoped_obligations','structural_inventory_integrity','full_semantic_coverage']}}

def build(output=BASE/'outputs'):
    output.mkdir(parents=True,exist_ok=True);sources,registry=load();_,audit=pinned_audit()
    units=discover(sources)
    (output/'source-units.json').write_text(json.dumps({'scope':'Checkbox units and paragraph blocks in detailed submission sections; addendum Q/A start anchors','units':units,'limits':registry['limits']},indent=2)+'\n')
    (output/'inventory-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    actual=[projection(packet_check(c,{'id':'actual_packet_not_supplied','kind':'actual','inventory_complete':False})) for c in ['west169','stanns']]
    (output/'actual-packets.json').write_text(json.dumps({'results':actual,'scope':'No actual packet supplied; absent artifacts are unknown, not presumed missing.'},indent=2)+'\n')
    faults=[]
    for case,key in [('west169','form_G'),('stanns','form_D1'),('stanns','gc_identified'),('stanns','sustainability_submission')]:
        p=packet(case);rid=case+'.'+key;p['artifacts'].pop(rid);r=packet_check(case,p)
        item=next(q for q in r['requirements'] if q['id']==rid)
        faults.append({'fixture':'remove_'+rid,'kind':'synthetic_packet_omission','observed':item,'readiness':r['submission_completeness_claim_allowed']})
    p=packet('west169');p['required_requests']=['west169.form_E4'];p['artifacts'].pop('west169.commercial_management');r=packet_check('west169',p)
    faults.append({'fixture':'obsolete_e4_and_missing_commercial_evidence','kind':'synthetic_packet_error','obsolete_requests':r['obsolete_requests'],'missing':next(q for q in r['requirements'] if q['id']=='west169.commercial_management')})
    p=packet('stanns');p['required_requests']=['stanns.multiple_site_submissions'];p['artifacts'].pop('stanns.green_certificate');r=packet_check('stanns',p)
    faults.append({'fixture':'obsolete_multisite_and_deferred_certificate','kind':'synthetic_packet_error','obsolete_requests':r['obsolete_requests'],'certificate':next(q for q in r['requirements'] if q['id']=='stanns.green_certificate')})
    for fault in ['remove_definition','remove_source_anchor','reclassify_required','remove_addendum','premature_review_acceptance']:
        proposed=copy.deepcopy(registry)
        if fault=='remove_definition':proposed['requirements']=[q for q in proposed['requirements'] if q['id']!='west169.form_G']
        if fault=='remove_source_anchor':proposed['units']=[u for u in proposed['units'] if 'west169.form_G' not in u['requirements']]
        if fault=='reclassify_required':next(q for q in proposed['requirements'] if q['id']=='west169.form_G')['mode']='optional'
        if fault=='remove_addendum':proposed['changes']=[c for c in proposed['changes'] if c['id']!='west169.replace_e4']
        if fault=='premature_review_acceptance':
            for u in proposed['units']:u['review_status']='accepted';u['expansion']='fully_expanded'
        _,observed=pinned_audit(proposed)
        faults.append({'fixture':fault,'kind':'inventory_mutation','issues':observed['issues'],'full_semantic_coverage':observed['full_semantic_coverage']})
    (output/'fault-injections.json').write_text(json.dumps({'scope':'Known deliberate defects test invariants; not an empirical analyst recall/precision benchmark. All packets are synthetic.','faults':faults},indent=2)+'\n')
    text=['# Coverage review queue','','All source units remain pending independent semantic review. Some have authored partial mappings; many contain unexpanded clauses.','A source unit is not an atomic requirement; do not turn these counts into a completeness percentage.','','| Case | Source review units | Scoped obligations | Current conclusion |','|---|---|---|---|']
    for case in ['west169','stanns']:text.append(f"| {case} | {sum(u['case']==case for u in units)} | {sum(r['case']==case for r in registry['requirements'])} | Full completeness unverified |")
    text+=['','## Mapped obligations','','| Obligation | Current mode and phase | Source |','|---|---|---|']
    byid={u['id']:u for u in units}
    for r in registry['requirements']:
        refs='; '.join(f"{byid[a]['source_id']} PDF p{byid[a]['pdf_page']}" for a in r['anchors'])
        text.append(f"| {r['case']}: {r['label']} | {r['mode']}, {r['phase']} | {refs} |")
    (output/'review-queue.md').write_text('\n'.join(text)+'\n')
    files=[p for p in BASE.glob('*.py')]+[BASE/'registry.json',BASE/'precommit.json']+list((BASE/'tests').glob('*.py'))+list((BASE/'fixtures').glob('*'))
    e=ROOT/'research/eligibility-gates';files+= [e/'engine.py',e/'check.py',e/'schemas/gates.schema.json',e/'sources.json',*sorted((e/'cases').glob('*.json'))]
    manifest={'files':{str(p.relative_to(ROOT)):eligibility.sha(p.read_bytes()) for p in sorted(files)},'outputs':{p.name:eligibility.sha(p.read_bytes()) for p in sorted(output.iterdir()) if p.name!='manifest.json'},'source_bytes_bound_by':'research/eligibility-gates/sources.json','scope':'Source anchor integrity and bounded authored obligations; no complete semantic inventory or expert acceptance.'}
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return {'source_units':len(units),'scoped_obligations':len(registry['requirements']),'addendum_operations':len(registry['changes']),'fault_controls':len(faults),'full_semantic_coverage':False}
if __name__=='__main__':print(json.dumps(build(),indent=2))
