"""CLI backpressure at the claim boundary. MIT."""
import argparse,json,pathlib
from engine import BASE,compile_case,evaluate

def release(compiled,profile,purpose):
    if purpose not in {'evidence-pack','submission-readiness-claim'}:
        raise ValueError('Unsupported export purpose')
    # Recompute from versioned requirements/evidence; never trust a caller's readiness flag.
    result=evaluate(compiled,profile)
    allowed=purpose=='evidence-pack' or result['submission_readiness_claim_allowed']
    return {'purpose':purpose,'allowed':allowed,'blocking_gates':result['blocking_gates'] if not allowed else [],'required_label':'Eligibility and submission readiness unverified; gather/review evidence' if result['blocking_gates'] else 'Scoped rule review; no agency acceptance implied','result':result}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--case',choices=['west169','stanns'],required=True);parser.add_argument('--profile',type=pathlib.Path);parser.add_argument('--purpose',choices=['evidence-pack','submission-readiness-claim'],default='evidence-pack');args=parser.parse_args()
    case=json.loads((BASE/'cases'/(args.case+'.json')).read_text());sources=json.loads((BASE/'sources.json').read_text())
    profile=json.loads(args.profile.read_text()) if args.profile else {'id':'actual_team_credentials_not_supplied','kind':'actual','collections':{},'decisions':{}}
    output=release(compile_case(case,sources),profile,args.purpose);print(json.dumps(output,indent=2));raise SystemExit(0 if output['allowed'] else 2)
