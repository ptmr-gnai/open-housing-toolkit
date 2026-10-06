"""Coverage and packet audits. Source presence is distinct from semantic compliance. MIT."""
import copy,json,pathlib,sys,zipfile
from scan import BASE,ROOT,discover,fp,norm
sys.path.insert(0,str(ROOT/'research/eligibility-gates'))
import engine as eligibility
MODES={'required','conditional','optional','not_required','deferred','review_instruction'}

def load():
    sources=json.loads((ROOT/'research/eligibility-gates/sources.json').read_text())
    for cid in ['west169','stanns']:
        eligibility.compile_case(json.loads((ROOT/'research/eligibility-gates/cases'/(cid+'.json')).read_text()),sources)
    return sources,json.loads((BASE/'registry.json').read_text())

def audit(registry,sources):
    units=discover(sources);byid={u['id']:u for u in units};reqs={r['id']:r for r in registry['requirements']};issues=[]
    declared=[u['anchor'] for u in registry['units']]
    if len(declared)!=len(set(declared)):issues.append({'code':'duplicate_anchor'})
    if len(reqs)!=len(registry['requirements']):issues.append({'code':'duplicate_requirement'})
    for missing in sorted(set(byid)-set(declared)):issues.append({'code':'unaccounted_source_unit','anchor':missing})
    for item in registry['units']:
        u=byid.get(item['anchor'])
        if not u or fp(u)!=item['source_fingerprint']:issues.append({'code':'stale_source_anchor','anchor':item['anchor']});continue
        for rid in item['requirements']:
            if rid not in reqs:issues.append({'code':'missing_requirement_definition','requirement':rid})
            elif item['anchor'] not in reqs[rid]['anchors']:issues.append({'code':'broken_mapping','requirement':rid})
        if item['expansion']=='authored_partial' and not item['requirements']:issues.append({'code':'empty_obligation_mapping','anchor':item['anchor']})
    for r in registry['requirements']:
        if r['mode'] not in MODES or type(r['excel'])!=bool:raise ValueError('Invalid obligation type')
        if r['mode']=='conditional' and not r['condition']:raise ValueError('Conditional requirement without predicate')
        if r['mode']=='deferred' and r['phase']=='submission':issues.append({'code':'phase_conflict','requirement':r['id']})
        for anchor in r['anchors']:
            if anchor not in byid or byid[anchor]['case']!=r['case']:issues.append({'code':'cross_case_or_unknown_anchor','requirement':r['id']})
            if not any(x['anchor']==anchor and r['id'] in x['requirements'] for x in registry['units']):issues.append({'code':'unmapped_requirement','requirement':r['id']})
        for citation in r.get('supporting_citations',[]):
            doc=next(d for d in sources['sources'] if d['id']==citation['source_id'])
            page=(ROOT/doc['text']).read_text().split('\f')[citation['pdf_page']-1]
            if norm(citation['quote']) not in norm(page):issues.append({'code':'bad_supporting_citation','requirement':r['id']})
    for change in registry['changes']:
        r=reqs.get(change['target'])
        if not r:issues.append({'code':'addendum_target_missing','change':change['id']});continue
        if change['anchor'] not in r['anchors']:issues.append({'code':'addendum_not_bound','change':change['id']})
        for key,value in change['required_effect'].items():
            if r.get(key)!=value:issues.append({'code':'addendum_effect_not_applied','change':change['id'],'field':key})
    review_queue=[{'anchor':u['anchor'],'expansion':u['expansion'],'review_status':u['review_status']} for u in registry['units'] if u['review_status']!='accepted' or u['expansion']!='fully_expanded']
    return {'source_units':len(units),'scoped_obligations':len(reqs),'addendum_operations':len(registry['changes']),'issues':issues,'structural_inventory_integrity':not issues,'review_queue':review_queue,'full_semantic_coverage':not issues and not review_queue,'limits':registry['limits']}

def pinned_audit(candidate=None):
    sources,baseline=load();pre=json.loads((BASE/'precommit.json').read_text())
    if fp(baseline)!=pre['registry_fingerprint']:raise ValueError('Baseline inventory changed without versioned review')
    if fp(sources)!=pre['sources_fingerprint']:raise ValueError('Source manifest changed')
    registry=baseline if candidate is None else candidate
    result=audit(registry,sources)
    # Proposed edits may be reviewed, but cannot silently change the declared baseline contract.
    old={r['id']:r for r in baseline['requirements']};new={r['id']:r for r in registry['requirements']}
    for rid,r in old.items():
        if rid not in new:result['issues'].append({'code':'baseline_requirement_omitted','requirement':rid})
        elif fp(r)!=fp(new[rid]):result['issues'].append({'code':'unreviewed_requirement_change','requirement':rid})
    old_changes={c['id']:c for c in baseline['changes']};new_changes={c['id']:c for c in registry['changes']}
    for cid,c in old_changes.items():
        if cid not in new_changes or fp(c)!=fp(new_changes[cid]):result['issues'].append({'code':'addendum_operation_omitted_or_changed','change':cid})
    result['structural_inventory_integrity']=not result['issues'];result['full_semantic_coverage']=not result['issues'] and not result['review_queue']
    return registry,result

def contract(registry,sources):
    return fp({'registry':registry,'sources':sources,'scanner_sha':eligibility.sha((BASE/'scan.py').read_bytes()),'checker_sha':eligibility.sha(pathlib.Path(__file__).read_bytes())})

def review_ok(payload,review,fingerprint):
    if review.get('status')!='accepted':return False
    if review.get('contract')!=fingerprint or review.get('payload_fingerprint')!=fp(payload):raise ValueError('Stale packet or applicability review')
    if not review.get('reviewer'):raise ValueError('Review attribution missing')
    return True

def packet_check(case,packet,candidate=None):
    registry,coverage=pinned_audit(candidate);sources,_=load();fingerprint=contract(registry,sources)
    if packet['kind'] not in ['actual','synthetic']:raise ValueError('Unknown packet kind')
    facts=packet.get('facts',{});fact_known=review_ok(facts,packet.get('facts_review',{}),fingerprint)
    artifacts=packet.get('artifacts',{});results=[]
    for r in registry['requirements']:
        if r['case']!=case:continue
        mode=r['mode'];status='unknown';reason='Packet not supplied or applicability/content not reviewed'
        if mode in ['optional','not_required','deferred']:status='not_a_submission_blocker';reason=mode
        elif mode=='conditional' and (not fact_known or facts.get(r['condition']) is None):status='unknown';reason='Applicability unknown; no unsupported waiver'
        elif mode=='conditional' and type(facts[r['condition']]) is not bool:raise ValueError('Applicability fact must be Boolean')
        elif mode=='conditional' and facts[r['condition']] is False:status='not_applicable';reason='Scoped reviewed applicability'
        else:
            artifact=artifacts.get(r['id'])
            if not artifact:
                status='missing' if packet.get('inventory_complete') is True else 'unknown'
                reason='Absent from declared complete packet' if status=='missing' else 'Packet inventory incomplete'
            else:
                path=(ROOT/artifact['file']).resolve()
                if not path.is_relative_to(ROOT):raise ValueError('Artifact path escapes repository')
                data=path.read_bytes()
                if eligibility.sha(data)!=artifact['sha256']:raise ValueError('Artifact bytes changed')
                if ('fixtures' in path.parts or artifact.get('synthetic') is True) and packet['kind']=='actual':raise ValueError('Synthetic artifact cannot support actual packet')
                if r['excel']:
                    valid=False
                    if path.suffix.lower()=='.xlsx' and zipfile.is_zipfile(path):
                        with zipfile.ZipFile(path) as z:valid={'[Content_Types].xml','xl/workbook.xml'}.issubset(z.namelist())
                    elif path.suffix.lower()=='.xls':valid=data.startswith(bytes.fromhex('D0CF11E0A1B11AE1'))
                    if not valid:status='wrong_format';reason='Required Excel container not established'
                if status!='wrong_format':
                    payload={k:v for k,v in artifact.items() if k!='review'}
                    status='scoped_review_pass' if review_ok(payload,artifact.get('review',{}),fingerprint) else 'present_unreviewed'
                    reason='Content review is separate from file presence and workbook container checks'
        results.append({'id':r['id'],'label':r['label'],'status':status,'reason':reason,'anchors':r['anchors']})
    obsolete=[]
    for change in registry['changes']:
        key=case+'.'+str(change['obsolete_artifact'])
        if change['case']==case and change['obsolete_artifact'] and key in packet.get('required_requests',[]):obsolete.append({'change':change['id'],'obsolete_request':key})
    blockers=[x['id'] for x in results if x['status'] not in ['scoped_review_pass','not_a_submission_blocker','not_applicable']]
    if not coverage['full_semantic_coverage']:blockers.append('coverage.semantic_expansion_and_review')
    if coverage['issues']:blockers.append('coverage.structural_inventory')
    if obsolete:blockers.append('obsolete_submission_requests')
    if packet['kind']=='synthetic':blockers.append('synthetic_packet_not_actual_evidence')
    return {'case':case,'packet':packet['id'],'contract':fingerprint,'coverage':coverage,'requirements':results,'obsolete_requests':obsolete,'submission_completeness_claim_allowed':not blockers,'blockers':blockers,'limits':['Presence/container checks do not establish valid signatures, template correctness, complete actor coverage, sound budgets or architectural acceptance.','Reviewer identities are attested, not authenticated.','All required experience/eligibility and professional feasibility gates remain separate.']}
