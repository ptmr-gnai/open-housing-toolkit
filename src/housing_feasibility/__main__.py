"""Feasibility report CLI. MIT.

python -m housing_feasibility brief start --goal "USER'S WORDS" --persona housing_agency --out runs/NAME/brief.json
python -m housing_feasibility brief provide --brief runs/NAME/brief.json --item "Station=Burnside Av (4)"
python -m housing_feasibility brief decide --brief runs/NAME/brief.json --step select --proposed "..." --answer "..."
python -m housing_feasibility build --request REQ.json --brief runs/NAME/brief.json --evidence DIR --underwriting DIR [--underwriting DIR ...]
    [--massing DIR ...] [--ownership DIR] [--render DIR] [--discovery DIR] --out runs/NAME/report
python -m housing_feasibility verify --run runs/NAME/report [--html EMAILED/report.html]
python -m housing_feasibility bundle --run runs/NAME/report --out runs/NAME/NAME-evidence.zip
python -m housing_feasibility continue --bundle UNZIPPED/report --out runs/NEW
python -m housing_feasibility template --out runs/NAME/report-request.json
"""
import argparse
import json
import sys
from pathlib import Path

from .engine import build, bundle, continue_from, load, save, verify, verify_html
from . import brief as briefs
from .brief import PERSONAS, STEPS


def main(argv=None):
    parser = argparse.ArgumentParser(prog='python -m housing_feasibility', description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    b = sub.add_parser('build', help='Assemble verified packages into a report')
    b.add_argument('--request', required=True, help='Report request JSON (see request.schema.json or the template command)')
    b.add_argument('--brief', required=True, help='Run brief (goal, inputs provided, decisions)')
    b.add_argument('--evidence', required=True, help='Verified parcel evidence package (housing_workflow)')
    b.add_argument('--underwriting', action='append', required=True, help='Verified underwriting package, or a folder of them; repeat for more')
    b.add_argument('--massing', action='append', default=[], help='Verified massing package (housing_geometry) or a folder of them; repeatable')
    b.add_argument('--ownership', help='Ownership run folder (housing_ownership)')
    b.add_argument('--render', help='Render package (housing_render), brief only or generated')
    b.add_argument('--discovery', help='Verified area discovery package the site came from')
    b.add_argument('--activity', help='Development-activity package (housing_activity) covering the site, and the candidates if a discovery is given')
    b.add_argument('--out', required=True)
    v = sub.add_parser('verify', help='Re-verify every input and recompute the report')
    v.add_argument('--run', required=True)
    v.add_argument('--html', help='Also confirm this report.html (e.g. one received by email) matches the bundle')
    z = sub.add_parser('bundle', help='Zip a verified report with its evidence and a README for people and agents')
    z.add_argument('--run', required=True)
    z.add_argument('--out', required=True, help='Path of the .zip to write')
    z.add_argument('--include-source-photo', action='store_true',
                   help='Include the render source photo (only if the user owns its rights)')
    w = sub.add_parser('show', help='Print the typed report embedded in a report.html (no bundle needed)')
    w.add_argument('--html', required=True)
    w.add_argument('--section', help='One section, e.g. headline, brief, process, search, zoning')
    c = sub.add_parser('continue', help='Start a new run from a verified report or unzipped bundle')
    c.add_argument('--bundle', required=True, help='The report folder (unzipped bundle: BUNDLE/report)')
    c.add_argument('--out', required=True)
    t = sub.add_parser('template', help='Write a report request to fill in')
    t.add_argument('--out', required=True)
    br = sub.add_parser('brief', help='Start or add to the run brief').add_subparsers(dest='action', required=True)
    x = br.add_parser('start', help='Record the goal before any work')
    x.add_argument('--goal', required=True, help="The user's goal, quoted in their words")
    x.add_argument('--persona', required=True, choices=sorted(PERSONAS))
    x.add_argument('--item', action='append', default=[], help='Something the user provided, "Label=value"; repeatable')
    x.add_argument('--out', required=True)
    x = br.add_parser('provide', help='Record something the user provided')
    x.add_argument('--brief', required=True)
    x.add_argument('--item', action='append', required=True, help='"Label=value"; repeatable')
    x = br.add_parser('decide', help='Record a decision: what you proposed and what the user answered')
    x.add_argument('--brief', required=True)
    x.add_argument('--step', required=True, choices=STEPS)
    x.add_argument('--proposed', required=True)
    x.add_argument('--answer', required=True, help="The user's answer, in their words")
    x.add_argument('--on', help='Date, default today')
    args = parser.parse_args(argv)
    if args.command == 'build':
        result = build(load(args.request), args.out, args.evidence, args.underwriting, args.massing,
                       args.ownership, args.render, args.discovery, args.brief, args.activity)
    elif args.command == 'brief':
        if args.action == 'start':
            result = briefs.start(args.out, args.goal, args.persona, args.item)
        elif args.action == 'provide':
            result = briefs.provide(args.brief, args.item)
        else:
            result = briefs.decide(args.brief, args.step, args.proposed, args.answer, args.on)
    elif args.command == 'verify':
        result = verify_html(args.html, args.run) if args.html else verify(args.run)
    elif args.command == 'bundle':
        result = bundle(args.run, args.out, args.include_source_photo)
    elif args.command == 'show':
        from .present import embedded_report
        data = embedded_report(Path(args.html).read_text())
        result = data[args.section] if args.section else {k: data[k] for k in ('request', 'brief', 'headline', 'provenance')}
    elif args.command == 'continue':
        result = continue_from(args.bundle, args.out)
    else:
        out = Path(args.out)
        if out.exists():
            raise ValueError('Refusing to overwrite ' + str(out))
        out.parent.mkdir(parents=True, exist_ok=True)
        save(out, {'version': '1.1', 'title': 'Site feasibility: ADDRESS', 'base_case': 'UNDERWRITING-REQUEST-ID',
                   'prepared_on': 'YYYY-MM-DD', 'prepared_by': 'AGENT NAME, assumptions approved by the user'})
        result = {'status': 'written', 'request': str(out)}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': str(exc)}))
        raise SystemExit(2)
