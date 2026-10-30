"""Collect, build and verify source-bound geometry. MIT."""
import argparse
import json
import sys
from pathlib import Path
from .engine import build, verify
from .sources import collect
from housing_workflow.contracts import load


def main():
    p=argparse.ArgumentParser(description='Mapped real parcel → assumed massing → area reconciliation; not a legal envelope.')
    sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('collect');c.add_argument('--bbl',required=True);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('build');c.add_argument('--analysis',type=Path,required=True);c.add_argument('--parcel-source',type=Path,required=True);c.add_argument('--scenario',type=Path,required=True);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('verify');c.add_argument('--run',type=Path,required=True)
    args=p.parse_args()
    try:
        if args.command=='collect':result=collect(args.bbl,args.out)
        elif args.command=='build':result=build(args.analysis,args.parcel_source,load(args.scenario),args.out)
        else:result=verify(args.run)
        print(json.dumps(result,indent=2));return 0
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},indent=2),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
