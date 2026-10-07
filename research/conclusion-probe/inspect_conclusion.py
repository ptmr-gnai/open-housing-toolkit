"""Rebuild one conclusion from an editable assumption config. MIT."""
import argparse, json, pathlib
from conclusion_engine import BASE, build, load, render, write

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--config',help='Copy of probe.json with documented assumption changes')
    p.add_argument('--prior-basis',help='Old packet fingerprint to test staleness')
    p.add_argument('--out',type=pathlib.Path,help='Optional output directory for rebuilt graph and brief')
    p.add_argument('--purpose',choices=['challenge-pack','investigation-conclusion','acquisition-or-design'],default='challenge-pack')
    a=p.parse_args();r=build(config=load(a.config) if a.config else None,prior_basis=a.prior_basis)
    if a.out:
        a.out.mkdir(parents=True,exist_ok=True);write(a.out/'conclusion.json',r);(a.out/'conclusion.md').write_text(render(r))
    allowed={'challenge-pack':True,'investigation-conclusion':r['release']['investigation_conclusion'],'acquisition-or-design':False}[a.purpose]
    print(json.dumps({'disposition':r['disposition'],'basis_fingerprint':r['basis_fingerprint'],'prior_judgment_basis':r['prior_judgment_basis'],'allowed':allowed,'professional_review':'pending'},indent=2))
    raise SystemExit(0 if allowed else 2)
