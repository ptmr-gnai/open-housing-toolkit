"""CLI: explicit programs → typed comparisons → review packet. MIT."""
import argparse
import json
from pathlib import Path
import sys
from .engine import ROOT,build,verify,replay,impact


from .contracts import read_json as load


def main():
    p=argparse.ArgumentParser(description='Conditional housing-program comparison; no eligibility, ranking or causal benefit estimate.')
    sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('build');c.add_argument('--analysis',type=Path,required=True);c.add_argument('--references',type=Path,required=True);c.add_argument('--input',type=Path,required=True);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('verify');c.add_argument('--run',type=Path,required=True)
    c=sub.add_parser('demo');c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('replay');c.add_argument('--from-run',type=Path,required=True);c.add_argument('--input',type=Path);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('impact');c.add_argument('--run',type=Path,required=True);c.add_argument('--input',type=Path,required=True)
    args=p.parse_args()
    try:
        if args.command=='build':result=build(args.analysis,args.references,load(args.input),args.out)
        elif args.command=='verify':result=verify(args.run)
        elif args.command=='demo':result=replay(ROOT/'examples/affordability-comparison',args.out)
        elif args.command=='impact':result=impact(args.run,load(args.input))
        else:result=replay(args.from_run,args.out,load(args.input) if args.input else None)
        print(json.dumps(result,indent=2));return 0
    except (ValueError,KeyError,TypeError,OSError,ArithmeticError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},indent=2),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
