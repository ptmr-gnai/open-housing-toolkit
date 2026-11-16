"""Massing-grounded concept render CLI. MIT.

python -m housing_concept prepare --massing runs/NAME/massing-7 --photo PHOTO.png --provider "Google Street View" \
    --capture-date "April 2026" --style brick --ground-use shops_and_supermarket --out runs/NAME/concept-7
python -m housing_concept review-template --out runs/NAME/concept-7-review.json
python -m housing_concept attach --run runs/NAME/concept-7 --image IMAGE.png --provider "Codex image_gen" --review REVIEW.json
python -m housing_concept verify --run runs/NAME/concept-7
"""
import argparse
import json

from .engine import CHECKS, GROUND_USES, STYLES, attach, prepare, review_template, verify


def main(argv=None):
    parser = argparse.ArgumentParser(prog='python -m housing_concept', description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare', help='Elevation drawing and fixed prompt from a verified massing and a site photo')
    p.add_argument('--massing', required=True)
    p.add_argument('--photo', required=True, help='Site photo or Street View screenshot (PNG or JPEG)')
    p.add_argument('--provider', required=True, help='Where the photo came from, e.g. "Google Street View" (max 40 characters)')
    p.add_argument('--capture-date', required=True, help='e.g. "April 2026" (max 20 characters)')
    p.add_argument('--style', required=True, choices=sorted(STYLES))
    p.add_argument('--ground-use', required=True, choices=sorted(GROUND_USES))
    p.add_argument('--frontage-edge', type=int, help='Parcel edge facing the street (default: longest; prepare lists them)')
    p.add_argument('--out', required=True)
    t = sub.add_parser('review-template', help='Write the review file to fill in after looking at the image')
    t.add_argument('--out', required=True)
    a = sub.add_parser('attach', help='Attach the generated image with its review')
    a.add_argument('--run', required=True)
    a.add_argument('--image', required=True)
    a.add_argument('--provider', required=True, help='Image tool used, e.g. "Codex image_gen"')
    a.add_argument('--review', required=True)
    v = sub.add_parser('verify')
    v.add_argument('--run', required=True)
    args = parser.parse_args(argv)
    if args.command == 'prepare':
        result = prepare(args.massing, args.photo, args.out, args.style, args.ground_use, args.provider, args.capture_date, args.frontage_edge)
    elif args.command == 'review-template':
        result = review_template(args.out)
    elif args.command == 'attach':
        result = attach(args.run, args.image, args.provider, args.review)
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
