"""Standalone commands; no API collection or analysis package dependency. MIT."""
import argparse
from pathlib import Path
import json
import sys
from .contracts import load
from .engine import prepare,attach,verify

def main():
    p=argparse.ArgumentParser(description='Scene + explicit visual scenario → render brief → generated image receipt')
    sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('prepare');c.add_argument('--scene',type=Path,required=True);c.add_argument('--scenario',type=Path,required=True);c.add_argument('--analysis',type=Path);c.add_argument('--photo',type=Path);c.add_argument('--out',type=Path,required=True)
    c=sub.add_parser('attach');c.add_argument('--run',type=Path,required=True);c.add_argument('--image',type=Path,required=True);c.add_argument('--invocation',type=Path,required=True);c.add_argument('--review',type=Path,required=True)
    c=sub.add_parser('verify');c.add_argument('--run',type=Path,required=True)
    a=p.parse_args()
    try:
        if a.command=='prepare':
            prepare(load(a.scene),load(a.scenario),a.out,a.analysis,a.photo);r=verify(a.out)
        elif a.command=='attach':r=attach(a.run,a.image,load(a.invocation),load(a.review))
        else:r=verify(a.run)
        print(json.dumps(r,indent=2));return 0
    except (ValueError,OSError,KeyError,TypeError) as e:
        print(json.dumps({'status':'blocked','reason':str(e)},indent=2),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
