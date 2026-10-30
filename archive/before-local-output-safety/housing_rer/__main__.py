"""Guide-mapped draft preparation CLI. Standard library. MIT."""
import argparse,json,sys
from pathlib import Path
from housing_benefit.contracts import read_json as load
from .engine import ROOT,build,verify,replay


def main():
    p=argparse.ArgumentParser(description='Prepare incomplete five-section RER drafts and instruction coverage; no official submission.')
    sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('build');c.add_argument('--comparison',type=Path,required=True);c.add_argument('--input',type=Path,required=True);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('verify');c.add_argument('--run',type=Path,required=True)
    c=sub.add_parser('demo');c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('replay');c.add_argument('--from-run',type=Path,required=True);c.add_argument('--input',type=Path);c.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    try:
        if a.command=='build':result=build(a.comparison,load(a.input),a.out)
        elif a.command=='verify':result=verify(a.run)
        elif a.command=='demo':result=replay(ROOT/'examples/rer-preparation',a.out)
        else:result=replay(a.from_run,a.out,load(a.input) if a.input else None)
        print(json.dumps(result,indent=2));return 0
    except (ValueError,KeyError,TypeError,OSError) as e:
        print(json.dumps({'status':'blocked','reason':str(e)},indent=2),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
