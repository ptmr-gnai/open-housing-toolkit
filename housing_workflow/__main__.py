"""Agent- and human-callable CLI. Standard library only. MIT."""
import argparse
import json
from pathlib import Path
import sys
from .contracts import load, save, validate_request
from .engine import ROOT, build, collect, replay, run, verify

def main():
    p=argparse.ArgumentParser(description='One Bronx parcel → public evidence → typed model → information packet. Partial playbook, not feasibility clearance.')
    commands=p.add_subparsers(dest='command',required=True)
    init=commands.add_parser('init',help='Interactive intake, or use an agent to write the same request JSON')
    init.add_argument('--out',type=Path,required=True)
    for command in ['run','collect']:
        c=commands.add_parser(command);c.add_argument('--input',type=Path,required=True);c.add_argument('--out',type=Path,required=True)
    for command in ['build','verify']:
        c=commands.add_parser(command);c.add_argument('--run',type=Path,required=True)
    c=commands.add_parser('demo',help='Offline, real-source worked example; no API key or network required')
    c.add_argument('--out',type=Path,required=True)
    c=commands.add_parser('replay',help='Rebuild from retained evidence; optional changed assumptions/question, same site')
    c.add_argument('--from-run',type=Path,required=True);c.add_argument('--input',type=Path);c.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    try:
        if args.command=='init':
            from local_outputs import destination
            destination(args.out)
            if args.out.exists():raise ValueError('Request file already exists; use a new path.')
            site=input('Bronx BBL (10 digits), or exact street address: ').strip()
            question=input('What decision/question should this packet support? ').strip()
            req={'version':'0.2.0','bbl' if site.isdigit() else 'address':site,'question':question,'scenario':None}
            validate_request(req);args.out.parent.mkdir(parents=True,exist_ok=True);save(args.out,req)
            result={'request':str(args.out),'next':'Run collect or run with this input. Scenario is optional; agent may add explicitly explained assumptions.'}
        elif args.command=='run':result=run(load(args.input),args.out)
        elif args.command=='collect':result={'resolved_bbl':collect(load(args.input),args.out),'next':'build --run '+str(args.out)}
        elif args.command=='build':build(args.run);result=verify(args.run)
        elif args.command=='verify':result=verify(args.run)
        elif args.command=='demo':result=replay(ROOT/'examples/parcel-investigation',args.out)
        else:result=replay(args.from_run,args.out,load(args.input) if args.input else None)
        print(json.dumps(result,indent=2));return 0
    except (ValueError,KeyError,OSError,TypeError,ZeroDivisionError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc),'action':'Correct the input or inspect retained collection receipts. No feasibility claim is released.'},indent=2),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
