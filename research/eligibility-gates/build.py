"""Build deterministic actual-unknown evidence requests and labeled synthetic checks. MIT."""
import copy,json,pathlib
from engine import BASE,ROOT,compile_case,evaluate,fingerprint,sha
FIXTURE=BASE/'fixtures/credential-examples.json'
DATA=json.loads(FIXTURE.read_text())

def attested(payload,compiled):
    item=copy.deepcopy(payload)
    item['evidence']={'file':str(FIXTURE.relative_to(ROOT)),'sha256':sha(FIXTURE.read_bytes()),'synthetic':True}
    item['review']={'status':'accepted','reviewer':'synthetic-test-reviewer','requirements_fingerprint':compiled['fingerprint'],'payload_fingerprint':fingerprint(item)}
    return item

def profile_for(compiled,scenario):
    cutoff=compiled['case']['cutoff'];year=int(cutoff[:4])+scenario.get('year_offset',DATA['default_year_offset'])
    date=f'{year:04d}'+cutoff[4:]
    facts=copy.deepcopy(DATA['default_facts']);facts['completion_date']=facts['management_date']=date
    facts['residential_units']=scenario.get('units',facts['residential_units'])
    for key in ['work_type','nyc']:
        if key in scenario:facts[key]=scenario[key]
    for key in scenario.get('omit_fields',[]):facts.pop(key,None)
    development=[]
    for i,units in enumerate(scenario.get('development_unit_counts',[facts['residential_units']])):
        value=copy.deepcopy(facts);value['residential_units']=units
        development.append(attested({'id':f'dev{i}','facts':value},compiled))
    managed=copy.deepcopy(facts);managed['residential_units']=scenario.get('management_units',facts['residential_units'])
    collections={}
    for name,records in [('development',development),('management',[attested({'id':'management-reviewed-unique-portfolio','facts':managed},compiled)])]:
        scope=attested({'facts':{'complete':True,'record_set_fingerprint':fingerprint(records)}},compiled)
        collections[name]={'records':records,'scope_complete':scenario.get('scope_complete',True),'scope_review':scope}
    decisions={}
    if scenario.get('manual_reviews'):
        decisions={g['id']:attested({'verdict':'pass','facts':{'fixture_only':True}},compiled) for g in compiled['case']['gates'] if g['kind']=='review'}
    if scenario.get('reviewed') is False:
        for collection in collections.values():
            for record in collection['records']:record['review']['status']='pending'
            collection['scope_review']['review']['status']='pending'
    return {'id':scenario['id'],'kind':'synthetic','collections':collections,'decisions':decisions,'limits':['Synthetic evidence and test-review attribution; cannot support actual submission readiness.']}

def build(output=BASE/'outputs'):
    output.mkdir(parents=True,exist_ok=True)
    sources=json.loads((BASE/'sources.json').read_text());results=[];compilations=[]
    for file in sorted((BASE/'cases').glob('*.json')):
        compiled=compile_case(json.loads(file.read_text()),sources);compilations.append(compiled)
        actual={'id':'actual_team_credentials_not_supplied','kind':'actual','collections':{},'decisions':{}}
        result=evaluate(compiled,actual)
        (output/(file.stem+'-actual-unknown.json')).write_text(json.dumps(result,indent=2)+'\n')
        for scenario in DATA['scenarios']:
            result=evaluate(compiled,profile_for(compiled,scenario));results.append(result)
    (output/'synthetic-transfer.json').write_text(json.dumps({'scope':'Source-driven cross-case regression, not independent held-out analyst assessment or actual eligibility','results':results},indent=2)+'\n')
    selected=[r for r in results if r['profile_id'] in {'sixty_units','seventy_units','rehabilitation','outside_nyc','split_projects','all_scoped_reviews_match'}]
    table=['# Applicant requirements evidence requests','','No actual applicant credentials were supplied. Every actual applicant/proposal gate remains unknown.','Request reviewed project history and management portfolio evidence before claiming readiness to submit.','These are historical solicitations, not current opportunities.','','## Synthetic transfer checks','','Synthetic fixtures below exercise code; they are not evidence about actual applicants.','','| Fixture | Solicitation | Development | NYC management | Submission readiness claim |','|---|---|---|---|---|']
    for r in selected:
        statuses={g['id']:g for g in r['gates']}
        dev=statuses['team.development'];label=dev['status']+(' (agency review route)' if dev['base_status']=='fail' and dev['status']=='unknown' else '')
        table.append(f"| {r['profile_id']} | {r['case_id']} | {label} | {statuses['team.management']['status']} | Blocked |")
    table+=['','## Actual unknown team next actions','']
    for c in compilations:
        table+=['### '+c['case']['title'],'','| Requirement | Responsible role | Evidence to gather | Source |','|---|---|---|---|']
        for gate in c['case']['gates']:
            action=gate['next_action']
            if gate['kind']=='experience':
                action=f"Document at least {c['bindings'][gate['id']]['min_units']} qualifying residential units within {c['bindings'][gate['id']]['lookback']} years. "+action
            refs='; '.join(f"{q['source_id']} PDF p{q['pdf_page']}" for q in gate['citations'])
            table.append(f"| {gate['label']} | {gate['owner']} | {action} | {refs} |")
        table+=['']
    (output/'evidence-requests.md').write_text('\n'.join(table)+'\n')
    inputs=[BASE/'engine.py',BASE/'build.py',BASE/'check.py',BASE/'validate.py',BASE/'author_cases.py',BASE/'sources.json',BASE/'schemas/gates.schema.json',FIXTURE,*sorted((BASE/'cases').glob('*.json')),*sorted((BASE/'tests').glob('test_*.py'))]
    manifest={'scope':'Reproducible code behavior; no professional or agency acceptance','files':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in inputs},'outputs':{p.name:sha(p.read_bytes()) for p in sorted(output.iterdir()) if p.name!='manifest.json'},'case_fingerprints':{c['case']['id']:c['fingerprint'] for c in compilations}}
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return {'cases':len(compilations),'gates':sum(len(c['case']['gates']) for c in compilations),'synthetic_scenarios':len(results),'actual_submission_ready':False}
if __name__=='__main__':print(json.dumps(build(),indent=2))
