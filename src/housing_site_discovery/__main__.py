"""Local command line for nonhousing discovery. MIT."""
import argparse
import json
from pathlib import Path
from . import context,engine,evidence
from .common import load


def main():
    p=argparse.ArgumentParser(description='Discover nonhousing lots and general zoning paths without capacity gates')
    commands=p.add_subparsers(dest='command',required=True)
    for name in ['collect','enrich','context','discover','handoff','deepen','compare-legacy','verify']:
        sub=commands.add_parser(name)
        if name in ['collect','enrich','discover']:sub.add_argument('--input',required=True,type=Path)
        if name=='enrich':sub.add_argument('--inventory',required=True,type=Path)
        if name in ['collect','enrich','context']:sub.add_argument('--ca-file')
        if name in ['discover','context']:sub.add_argument('--evidence',required=True,type=Path)
        if name=='discover':sub.add_argument('--context',type=Path)
        if name in ['handoff','compare-legacy']:sub.add_argument('--discovery',required=True,type=Path)
        if name=='handoff':sub.add_argument('--bbl',required=True,action='append')
        if name=='deepen':sub.add_argument('--handoff',required=True,type=Path)
        if name=='compare-legacy':sub.add_argument('--legacy',required=True,type=Path)
        if name=='verify':sub.add_argument('--run',required=True,type=Path)
        else:sub.add_argument('--out',required=True,type=Path)
    a=p.parse_args()
    if a.command=='collect':result=evidence.collect(load(a.input),a.out,a.ca_file)
    elif a.command=='enrich':result=evidence.enrich(a.inventory,load(a.input),a.out,a.ca_file)
    elif a.command=='context':result=context.collect(a.evidence,a.out,a.ca_file)
    elif a.command=='discover':result=engine.build(a.evidence,load(a.input),a.out,a.context)
    elif a.command=='handoff':result=engine.handoff(a.discovery,a.bbl,a.out)
    elif a.command=='deepen':result=engine.deepen(a.handoff,a.out)
    elif a.command=='compare-legacy':result=engine.compare_legacy(a.discovery,a.legacy,a.out)
    else:result=engine.verify(a.run)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},indent=2));raise SystemExit(2)
