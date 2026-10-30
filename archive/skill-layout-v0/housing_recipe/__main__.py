"""CLI for executing and inspecting analysis recipes. MIT."""
import argparse
import json
import sys
from pathlib import Path
from housing_workflow.contracts import load
from .engine import build, verify, preview


def main():
    p=argparse.ArgumentParser(description='Typed editable area-analysis recipe; no professional clearance.')
    sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('build');c.add_argument('--from-run',type=Path,required=True);c.add_argument('--recipe',type=Path,required=True);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('verify');c.add_argument('--run',type=Path,required=True)
    c=sub.add_parser('impact');c.add_argument('--run',type=Path,required=True);c.add_argument('--recipe',type=Path,required=True)
    args=p.parse_args()
    try:
        if args.command=='build':result=build(args.from_run,load(args.recipe),args.out)
        elif args.command=='verify':result=verify(args.run)
        else:result=preview(args.run,load(args.recipe))
        print(json.dumps(result,indent=2));return 0
    except (ValueError,KeyError,TypeError,OSError,RecursionError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},indent=2),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
