"""Local rental underwriting CLI. MIT."""
import argparse
import json
from .engine import build,load,verify


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('build');p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--reference-source',action='append',default=[],metavar='ID=PATH')
    p=sub.add_parser('verify');p.add_argument('--run',required=True)
    args=parser.parse_args()
    if args.command=='build':
        files={}
        for value in args.reference_source:
            if '=' not in value:raise ValueError('Reference source must be ID=PATH')
            identity,path=value.split('=',1)
            if identity in files:raise ValueError('Duplicate reference source id')
            files[identity]=path
        result=build(load(args.input),args.out,files)
    else:result=verify(args.run)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as exc:print(json.dumps({'status':'blocked','reason':str(exc)}));raise SystemExit(2)
