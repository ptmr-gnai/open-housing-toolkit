"""Join eligibility and coverage checks at a concrete export boundary. MIT."""
import argparse,json,pathlib
from scan import BASE,ROOT
from coverage_engine import packet_check,load
import engine as eligibility

def combined(case,packet,profile=None,purpose='evidence-pack'):
    if purpose not in ['evidence-pack','submission-readiness-claim']:raise ValueError('Unsupported purpose')
    sources,_=load();rules=json.loads((ROOT/'research/eligibility-gates/cases'/(case+'.json')).read_text())
    profile=profile or {'id':'actual_credentials_not_supplied','kind':'actual'}
    eligibility_result=eligibility.evaluate(eligibility.compile_case(rules,sources),profile)
    coverage_result=packet_check(case,packet)
    eligibility_blockers=[x for x in eligibility_result['blocking_gates'] if x!='coverage.full_submission_inventory']
    allowed=purpose=='evidence-pack' or (not eligibility_blockers and coverage_result['submission_completeness_claim_allowed'])
    return {'purpose':purpose,'allowed':allowed,'eligibility':eligibility_result,'coverage':coverage_result,'eligibility_blockers':eligibility_blockers,'delegated_coverage_gate':'coverage.full_submission_inventory is evaluated by the source-coverage component','required_label':'Historical initial assessment; eligibility, substantive completeness and feasibility unverified.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--case',choices=['west169','stanns'],required=True);p.add_argument('--packet',type=pathlib.Path);p.add_argument('--profile',type=pathlib.Path);p.add_argument('--purpose',choices=['evidence-pack','submission-readiness-claim'],default='evidence-pack');a=p.parse_args()
    packet=json.loads(a.packet.read_text()) if a.packet else {'id':'actual_packet_not_supplied','kind':'actual','inventory_complete':False,'artifacts':{}}
    profile=json.loads(a.profile.read_text()) if a.profile else None
    result=combined(a.case,packet,profile,a.purpose);print(json.dumps(result,indent=2));raise SystemExit(0 if result['allowed'] else 2)
