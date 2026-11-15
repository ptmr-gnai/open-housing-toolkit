"""Search declared housing targets over a verified nonhousing inventory. MIT."""
import argparse
import json
from pathlib import Path
from .engine import build,handoff,load,verify


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('build');p.add_argument('--discovery',required=True);p.add_argument('--underwriting',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True)
    p=sub.add_parser('compare');p.add_argument('--left',required=True);p.add_argument('--right',required=True);p.add_argument('--out',required=True)
    p=sub.add_parser('deepen');p.add_argument('--handoff',required=True);p.add_argument('--out',required=True)
    p=sub.add_parser('area-handoff');p.add_argument('--run',required=True);p.add_argument('--trial',required=True);p.add_argument('--parcel-evidence',required=True);p.add_argument('--out',required=True)
    p=sub.add_parser('verify');p.add_argument('--run',required=True)
    p=sub.add_parser('handoff');p.add_argument('--run',required=True);p.add_argument('--bbl',required=True,action='append');p.add_argument('--out',required=True)
    args=parser.parse_args()
    if args.command=='compare':
        from . import comparison
        result=comparison.build(args.left,args.right,args.out)
    elif args.command=='deepen':
        from . import pipeline_handoff
        result=pipeline_handoff.deepen(args.handoff,args.out)
    elif args.command=='area-handoff':
        from . import area_handoff
        result=area_handoff.build(args.run,args.trial,args.parcel_evidence,args.out)
    elif args.command=='build':result=build(args.discovery,args.underwriting,load(args.input),args.out)
    elif args.command=='handoff':result=handoff(args.run,args.bbl,args.out)
    else:
        if load(Path(args.run)/'manifest.json')['kind']=='search-area-handoff':
            from . import area_handoff
            result=area_handoff.verify(args.run)
        elif load(Path(args.run)/'manifest.json')['kind']=='site-search-comparison':
            from . import comparison
            result=comparison.verify(args.run)
        elif load(Path(args.run)/'manifest.json')['kind'] in ['search-handoff','search-investigation']:
            from . import pipeline_handoff
            result=pipeline_handoff.verify(args.run)
        else:result=verify(args.run)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as exc:print(json.dumps({'status':'blocked','reason':str(exc)}));raise SystemExit(2)
