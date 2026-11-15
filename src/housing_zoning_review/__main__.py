"""Reconcile monthly zoning-tax-lot data with verified site discovery/reviews. MIT."""
import argparse,json
from .engine import collect,finalize,replay,verify


def main():
    parser=argparse.ArgumentParser(description=__doc__);s=parser.add_subparsers(dest='command',required=True)
    p=s.add_parser('collect');p.add_argument('--parent',required=True);p.add_argument('--out',required=True);p.add_argument('--ca-file')
    p=s.add_parser('replay');p.add_argument('--parent',required=True);p.add_argument('--capture',required=True);p.add_argument('--out',required=True)
    p=s.add_parser('finalize');p.add_argument('--run',required=True)
    p=s.add_parser('verify');p.add_argument('--run',required=True)
    a=parser.parse_args()
    if a.command=='collect':result=collect(a.parent,a.out,a.ca_file)
    elif a.command=='replay':result=replay(a.parent,a.capture,a.out)
    elif a.command=='finalize':result=finalize(a.run)
    else:result=verify(a.run)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,TypeError) as exc:print(json.dumps({'status':'blocked','reason':str(exc)}));raise SystemExit(2)
