"""Collect or replay bounded historical dwelling-field review. MIT."""
import argparse,json
from pathlib import Path
from . import engine


def main():
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='command',required=True)
    c=s.add_parser('collect');c.add_argument('--discovery',required=True,type=Path);c.add_argument('--out',required=True,type=Path);c.add_argument('--ca-file');c.add_argument('--max-requests',type=int,default=160)
    r=s.add_parser('recover');r.add_argument('--capture',required=True,type=Path);r.add_argument('--out',required=True,type=Path);r.add_argument('--ca-file');r.add_argument('--max-requests',type=int,default=160);r.add_argument('--offline',action='store_true')
    v=s.add_parser('verify');v.add_argument('--run',required=True,type=Path)
    a=p.parse_args()
    if a.command=='collect':result=engine.collect(a.discovery,a.out,a.ca_file,a.max_requests)
    elif a.command=='recover':result=engine.recover(a.capture,a.out,a.ca_file,a.max_requests,a.offline)
    else:result=engine.verify(a.run)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},indent=2));raise SystemExit(2)
