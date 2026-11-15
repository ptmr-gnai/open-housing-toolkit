"""Public CLI for bounded source inventory and conditional discovery. MIT."""
import argparse
from pathlib import Path
import sys
from . import collection, engine
from .common import dumps, load


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    collect=sub.add_parser('collect');collect.add_argument('--input',type=Path,required=True);collect.add_argument('--out',type=Path,required=True);collect.add_argument('--ca-file',type=Path)
    screen=sub.add_parser('screen');screen.add_argument('--inventory',type=Path,required=True);screen.add_argument('--input',type=Path,required=True);screen.add_argument('--out',type=Path,required=True)
    compare=sub.add_parser('compare');compare.add_argument('--left',type=Path,required=True);compare.add_argument('--right',type=Path,required=True);compare.add_argument('--out',type=Path,required=True)
    focus=sub.add_parser('focus');focus.add_argument('--screen',type=Path,required=True);focus.add_argument('--input',type=Path,required=True);focus.add_argument('--out',type=Path,required=True)
    handoff=sub.add_parser('handoff');handoff.add_argument('--screen',type=Path,required=True);handoff.add_argument('--out',type=Path,required=True);handoff.add_argument('--top',type=int,default=3)
    deepen=sub.add_parser('deepen');deepen.add_argument('--handoff',type=Path,required=True);deepen.add_argument('--out',type=Path,required=True)
    verify=sub.add_parser('verify');verify.add_argument('--run',type=Path,required=True)
    finish=sub.add_parser('finalize');finish.add_argument('--run',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.command=='collect':result=collection.collect(load(args.input),args.out,args.ca_file)
        elif args.command=='screen':result=engine.build(args.inventory,load(args.input),args.out)
        elif args.command=='compare':result=engine.compare(args.left,args.right,args.out)
        elif args.command=='focus':result=engine.focus(args.screen,load(args.input),args.out)
        elif args.command=='handoff':result=engine.handoff(args.screen,args.out,args.top)
        elif args.command=='deepen':result=engine.deepen(args.handoff,args.out)
        elif args.command=='finalize':result=collection.finalize(args.run)
        else:result=engine.verify(args.run)
        print(dumps(result),end='');return 0
    except (ValueError,KeyError,OSError,TypeError) as exc:
        print(dumps({'status':'blocked','reason':str(exc),'action':'Preserve receipts and completed runs; correct inputs and use a fresh destination.'}),file=sys.stderr);return 2


if __name__=='__main__':raise SystemExit(main())
