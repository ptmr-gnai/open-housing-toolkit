"""Deterministic run, generated brief, trace and control evidence. MIT."""
import argparse, pathlib
from conclusion_engine import BASE, ROOT, check_pinned, build, render, write, sha
from controls import run_control, expected_response, metrics

def run(out=None):
    out=pathlib.Path(out or BASE/'outputs');out.mkdir(parents=True,exist_ok=True)
    spec=check_pinned();baseline=build();write(out/'baseline.json',baseline)
    (out/'conclusion.md').write_text(render(baseline))
    controls=[]
    for control in spec['controls']:
        observation,result=run_control(control,baseline)
        observation['expected_response_observed']=expected_response(observation,baseline)
        if not observation['expected_response_observed']: raise ValueError('Precommitted response not observed: '+control['id'])
        if result is not None:
            write(out/(control['id']+'.json'),result)
            (out/(control['id']+'.md')).write_text(render(result))
        controls.append(observation)
    write(out/'controls.json',controls)
    trace=['# Supporting facts and assumptions','','All rows belong to the conclusion dependency closure. Source strings are exact values, not interpretations.','',
           '| Claim | Kind | Value | Exact locator or dependency |','| --- | --- | --- | --- |']
    import json
    for key,c in baseline['claims'].items():
        value=json.dumps(c['value'],ensure_ascii=False).replace('|','\\|').replace('\n',' ')
        link=json.dumps(c.get('evidence',{}).get('locator',c.get('inputs',c.get('config_locator',c.get('policy_locator')))))
        trace.append(f"| {key} | {c['kind']} | {value} | {link} |")
    (out/'trace.md').write_text('\n'.join(trace)+'\n')
    summary={'source_families':len(baseline['sources']),'claims_in_one_conclusion':len(baseline['claims']),
             'controls_including_baseline':len(controls),'expected_responses_observed':sum(c['expected_response_observed'] for c in controls),
             'baseline_disposition':baseline['disposition'],'baseline_metrics':metrics(baseline),
             'professional_review':'pending','unfamiliar_human_reproduction_and_challenge':'pending','practitioner_utility':'not_tested',
             'selection_quality':'not_tested','current_site_facts':'not_verified'}
    write(out/'summary.json',summary)
    inputs=[ROOT/'pipeline.py',ROOT/'probe.json',BASE/'spec.json',BASE/'precommit.json',*BASE.glob('*.py'),*(BASE/'tests').glob('*.py')]
    manifest={'inputs':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in sorted(set(inputs))},
              'outputs':{p.name:sha(p.read_bytes()) for p in sorted(out.iterdir()) if p.is_file() and p.name!='manifest.json'},
              'source_inputs':'Every original cache file and receipt is bound by precommit.json'}
    write(out/'manifest.json',manifest)
    return summary

if __name__=='__main__':
    import json
    p=argparse.ArgumentParser();p.add_argument('--out');a=p.parse_args();print(json.dumps(run(a.out),indent=2))
