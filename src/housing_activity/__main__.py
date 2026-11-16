"""Development-activity CLI. MIT.

python -m housing_activity collect --discovery runs/NAME/discovery --out runs/NAME/activity
python -m housing_activity collect --bbl 2031780001 --out runs/NAME/activity-lot
python -m housing_activity verify --run runs/NAME/activity
"""
import argparse
import json

from .engine import collect, verify


def main(argv=None):
    parser = argparse.ArgumentParser(prog='python -m housing_activity', description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    c = sub.add_parser('collect', help='Check lots for recent demolition, foundation, new-building and similar activity')
    c.add_argument('--discovery', help='Area search package; checks its ranked candidates')
    c.add_argument('--all-nonhousing', action='store_true', help='Check every recorded-nonhousing lot, not just ranked candidates')
    c.add_argument('--bbl', action='append', default=[], help='A lot to check; repeatable')
    c.add_argument('--since-years', type=float, default=3)
    c.add_argument('--as-of', help='Date the window ends (default today)')
    c.add_argument('--out', required=True)
    v = sub.add_parser('verify')
    v.add_argument('--run', required=True)
    args = parser.parse_args(argv)
    if args.command == 'collect':
        result = collect(args.out, args.bbl, args.discovery, args.since_years, args.as_of, args.all_nonhousing)
    else:
        result = verify(args.run)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': str(exc)}))
        raise SystemExit(2)
