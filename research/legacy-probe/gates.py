"""Deterministic export eligibility. Technical validation is not professional approval. MIT."""
import argparse,json,pathlib
from pipeline import ROOT,read_json

def eligibility(ir,purpose,bbl):
    if purpose=='advisor-review':
        return {'allowed':True,'purpose':purpose,'conditions':['retain explicit unknowns and conditional scenario labels'],'professional_clearance':False}
    if purpose not in ['public-site-proposal','acquisition-recommendation']:
        raise ValueError('Unknown export purpose')
    dossier=next((d for d in ir['dossiers'] if d['bbl']==bbl),None)
    if dossier is None:raise ValueError('Site not investigated')
    unresolved=[key for key in ir['config']['required_gates'] if dossier['gates'].get(key,{}).get('status')!='verified']
    return {'allowed':not unresolved,'purpose':purpose,'bbl':bbl,'blocking_gates':unresolved,'professional_clearance':False,'note':'Verification workflow not implemented in v0.1; all site gates remain unknown.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('purpose');p.add_argument('--bbl',default='2028710002');p.add_argument('--run',type=pathlib.Path);args=p.parse_args()
    import pipeline
    ir=read_json(args.run/'ir.json') if args.run else pipeline.build(ROOT/'probe.json')
    result=eligibility(ir,args.purpose,args.bbl)
    print(json.dumps(result,indent=2));raise SystemExit(0 if result['allowed'] else 2)
