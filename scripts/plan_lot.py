#!/usr/bin/env python3
"""Turn plain building and money assumptions into consistent toolkit inputs. MIT.

Agents should use this instead of hand-writing floor polygons, area requests or
underwriting JSON. Every value it writes carries the rationale the user approved.

  shortlist  an area search -> the lots most worth discussing first
  massing    parcel geometry + "N stories, retail on the ground floor" ->
             geometry scenario, matching area request and program.json
  lot-request  a confirmed BBL -> the evidence request for that lot
  ownership  an ownership run -> latest deed, sale and conflicts in plain fields
  results    a folder of underwriting packages -> cost, loan, gap, yield on cost per scenario
  scenarios  program.json + an underwriting template + approved assumptions ->
             one underwriting request per combination, plus assumptions.md for approval

Examples (from the repository root, after preflight):

  .venv/bin/python scripts/plan_lot.py massing --evidence runs/P/evidence \
      --parcel-source runs/P/parcel --stories 7 --ground-nonresidential-sf 8000 \
      --out runs/P/plan-7

  .venv/bin/python scripts/plan_lot.py scenarios --program runs/P/plan-7/program.json \
      --land-usd 15000000 --land-note "Recorded deed amount, Feb 2025 (ACRIS)" \
      --hard-cost-psf 450,525,600 --rent-per-home-month 1800,2400,3000 \
      --out runs/P/scenarios-7
"""
import argparse
import copy
import itertools
import json
import math
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
TEMPLATE = ROOT / 'config/underwriting/rental-60-base.json'
SCALE_WITH_SIZE = {'construction_interest', 'financing_fees', 'developer_fee', 'taxes_and_carry'}


def load(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    path = Path(path)
    if path.exists():
        raise ValueError('Refusing to overwrite ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def money(value, places='1'):
    return str(Decimal(str(value)).quantize(Decimal(places), ROUND_HALF_UP))


def slug(text):
    return re.sub(r'[^a-z0-9-]+', '-', str(text).lower()).strip('-')


# ---------------------------------------------------------------- massing

def best_rectangle(poly):
    """Largest rectangle inside a polygon, aligned with its longest edge (vertex-coordinate search)."""
    from shapely import affinity
    from shapely.geometry import box
    coords = list(poly.exterior.coords)
    angles = sorted({round(math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 180, 3)
                     for a, b in zip(coords, coords[1:]) if math.dist(a, b) > 5})
    found = [r for r in (_rectangle_at(poly, angle) for angle in angles) if r is not None]
    if not found:
        raise ValueError('Could not fit a rectangular plate inside the parcel; supply a scenario by hand')
    return max(found, key=lambda r: r.area)


def _rectangle_at(poly, angle):
    from shapely import affinity
    from shapely.geometry import box
    origin = poly.centroid
    rotated = affinity.rotate(poly, -angle, origin=origin)
    xs = sorted({round(x, 3) for x, _ in rotated.exterior.coords})
    ys = sorted({round(y, 3) for _, y in rotated.exterior.coords})
    shrunk = rotated.buffer(1e-6)
    best = None
    for x0, x1 in itertools.combinations(xs, 2):
        for y0, y1 in itertools.combinations(ys, 2):
            area = (x1 - x0) * (y1 - y0)
            if best and area <= best[0]:
                continue
            candidate = box(x0, y0, x1, y1)
            if shrunk.covers(candidate):
                best = (area, candidate)
    return affinity.rotate(best[1], angle, origin=origin) if best else None


def ring(poly):
    pts = [[round(x, 4), round(y, 4)] for x, y in poly.exterior.coords]
    pts[-1] = pts[0]
    return pts


def plan_massing(args):
    from shapely.geometry import Polygon
    from housing_geometry.model import parcel_geometry
    from housing_geometry.sources import verify as verify_source
    out = Path(args.out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty')
    evidence = load(Path(args.evidence) / 'request.json')
    receipt = verify_source(Path(args.parcel_source))
    if receipt['bbl'] != evidence['bbl']:
        raise ValueError('Parcel geometry and evidence are for different tax lots')
    parcel, _, _, attrs = parcel_geometry(Path(args.parcel_source))
    site = parcel.buffer(-args.setback_ft, join_style=2) if args.setback_ft else parcel
    if site.geom_type != 'Polygon' or site.is_empty:
        raise ValueError('Setback leaves no single buildable polygon')
    convex = site.convex_hull.area - site.area <= max(1.0, site.area * 0.001)
    if convex:
        # Hull of a near-convex outline, pulled in slightly so it stays inside the mapped line.
        ground = site.convex_hull.buffer(-0.05, join_style=2)
        ground = ground.buffer(-(site.convex_hull.area - site.area) / max(ground.length, 1) - 0.05, join_style=2) \
            if not parcel.covers(ground) else ground
    else:
        ground = best_rectangle(site)
    ground = Polygon(ring(ground))
    if not parcel.covers(ground) or abs(ground.convex_hull.area - ground.area) > 1e-7:
        ground = Polygon(ring(best_rectangle(site)))
    how = ('the mapped parcel outline' + (' inset %s ft' % args.setback_ft if args.setback_ft else '')) if convex else \
        'the largest rectangle that fits inside the mapped parcel' + (' after a %s ft inset' % args.setback_ft if args.setback_ft else '') + \
        ', aligned with its longest edge'
    nonres = args.ground_nonresidential_sf
    if nonres > ground.area + 1e-6:
        raise ValueError('Ground-floor non-residential area %.0f sf exceeds the ground plate of %.0f sf. This lot (%.0f sf mapped) is %s, '
                         'so the plate is %s. Use --ground-nonresidential-sf %d or less.'
                         % (nonres, ground.area, parcel.area, 'roughly convex' if convex else 'irregular',
                            'its outline' if convex else 'the largest rectangle that fits inside it', int(ground.area)))
    from shapely import affinity
    upper = Polygon(ring(affinity.scale(ground, math.sqrt(args.upper_coverage), math.sqrt(args.upper_coverage), origin=ground.centroid))) \
        if args.upper_coverage < 1 else ground
    floors, gross = [], 0.0
    for n in range(1, args.stories + 1):
        plate = ground if n == 1 else upper
        share = (nonres / plate.area) if n == 1 else 0.0
        floors.append({'id': 'floor-%d' % n,
                       'footprint': {'vertices_ft': ring(plate),
                                     'rationale': ('Ground plate: ' + how + '.' if n == 1 else
                                                   'Upper plate: ground plate scaled to %s%% of its area about its centroid.' % round(args.upper_coverage * 100)
                                                   if args.upper_coverage < 1 else 'Upper plate repeats the ground plate.') +
                                     ' Generated by scripts/plan_lot.py; not a legal envelope, yard or setback analysis.'},
                       'height_ft': {'value': args.ground_height_ft if n == 1 else args.upper_height_ft,
                                     'rationale': 'Schematic floor-to-floor height used in this plan (%s); not a code or survey finding.' % args.approval_note},
                       'nonresidential_share': {'value': round(share, 12),
                                                'rationale': ('%s sf of ground-floor non-residential space, as a share of the plate (%s).' % (money(nonres), args.approval_note)) if n == 1
                                                else 'Upper floors assumed residential.'}})
        gross += plate.area
    nonres_total = sum(Polygon(f['footprint']['vertices_ft']).area * f['nonresidential_share']['value'] for f in floors)
    scenario_id = args.id or '%s-%d-story' % (evidence['bbl'], args.stories)
    geometry = {'version': '0.1.0', 'id': scenario_id, 'site_bbl': evidence['bbl'],
                'parcel_geometry_sha256': receipt['parcel_sha256'], 'origin': 'exploratory_assumptions',
                'purpose': '%d-story schematic massing with ground-floor non-residential space, generated from approved plain-language inputs.' % args.stories,
                'floors': floors,
                'reconciliation': {'absolute_tolerance_sf': 1, 'rationale': 'Numerical tolerance for comparing plate area with the matching area request; not a professional threshold.'}}
    gross_r, nonres_r = round(gross, 2), round(nonres_total, 2)
    residential = gross_r - nonres_r
    homes = math.floor(residential * args.net_efficiency / args.average_home_sf)
    area = {'version': evidence['version'], 'bbl': evidence['bbl'], 'question': evidence['question'],
            'scenario': {'name': '%d stories, ground-floor non-residential, matched to the schematic massing' % args.stories,
                         'gross_area_sf': {'value': gross_r, 'rationale': 'Sum of the schematic massing floor plates (scripts/plan_lot.py); a gross-area proxy, not zoning floor area.'},
                         'nonresidential_gross_sf': {'value': nonres_r, 'rationale': 'Ground-floor non-residential area used in this plan (%s).' % args.approval_note},
                         'residential_net_efficiency': {'value': args.net_efficiency, 'rationale': 'Share of residential gross area inside apartments (%s).' % args.approval_note},
                         'average_net_home_sf': {'value': args.average_home_sf, 'rationale': 'Average apartment size; no unit mix established (%s).' % args.approval_note}}}
    lot_area = float(attrs.get('LotArea') or 0)
    program = {'version': '1.0', 'bbl': evidence['bbl'], 'scenario_id': scenario_id, 'stories': args.stories,
               'gross_sf': money(gross_r, '0.01'), 'nonresidential_sf': money(nonres_r, '0.01'),
               'residential_sf': money(residential, '0.01'), 'homes': homes,
               'ground_plate_sf': round(ground.area, 1), 'upper_plate_sf': round(upper.area, 1),
               'total_height_ft': args.ground_height_ft + args.upper_height_ft * (args.stories - 1),
               'gross_to_lot_area': round(gross_r / lot_area, 2) if lot_area else None,
               'residential_to_lot_area': round(residential / lot_area, 2) if lot_area else None,
               'net_efficiency': args.net_efficiency, 'average_home_sf': args.average_home_sf,
               'assumptions': {'ground_height_ft': args.ground_height_ft, 'upper_height_ft': args.upper_height_ft,
                               'upper_coverage': args.upper_coverage, 'setback_ft': args.setback_ft,
                               'ground_nonresidential_sf': args.ground_nonresidential_sf, 'approval': args.approval_note},
               'files': {'geometry_scenario': 'geometry-scenario.json', 'area_request': 'area-request.json',
                         'render_scenario': 'render-scenario.json'}}
    render = {'version': '0.1.0', 'id': scenario_id + '-render', 'site_bbl': evidence['bbl'],
              'label': 'Illustrative %d-story concept matching the schematic massing' % args.stories,
              'parameters': {
                  'total_stories': {'value': args.stories, 'kind': 'assumption',
                                    'rationale': 'Same story count as the schematic massing %s; not a zoning limit.' % scenario_id},
                  'ground_floor_use': {'value': args.ground_use, 'kind': 'assumption',
                                       'rationale': 'Matches the %s sf of ground-floor non-residential space in the massing.' % money(nonres)},
                  'upper_floor_use': {'value': 'apartments', 'kind': 'assumption',
                                      'rationale': 'Upper floors are residential in the massing; unit mix and affordability not established.'},
                  'architectural_treatment': {'value': args.architecture, 'kind': 'design_preference',
                                              'rationale': 'Confirm or replace with the user before preparing the render brief.'}},
              'geometry_status': 'unverified', 'analysis_reconciliation': 'not_reconciled_to_area_budget'}
    out.mkdir(parents=True, exist_ok=True)
    save(out / 'render-scenario.json', render)
    save(out / 'geometry-scenario.json', geometry)
    save(out / 'area-request.json', area)
    save(out / 'program.json', program)
    return {'status': 'planned', **{k: program[k] for k in ('stories', 'gross_sf', 'nonresidential_sf', 'residential_sf', 'homes',
                                                           'gross_to_lot_area', 'residential_to_lot_area', 'total_height_ft')},
            'next': ['housing_workflow replay --from-run EVIDENCE --input %s/area-request.json --out AREA' % out,
                     'housing_geometry build --analysis AREA --parcel-source PARCEL --scenario %s/geometry-scenario.json --out MASSING' % out]}


# ---------------------------------------------------------------- financing scenarios

def pct(value):
    return format((Decimal(str(value)) * 100).normalize(), 'f')


def numbers(text):
    return [Decimal(x.strip()) for x in str(text).split(',') if x.strip()]


def basis(rationale, refs=()):
    return {'kind': 'analyst_assumption', 'rationale': rationale, 'reference_ids': list(refs)}


def plan_scenarios(args):
    program = load(args.program)
    template = load(args.template)
    out = Path(args.out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty')
    approval = args.approval_note
    homes, gross = program['homes'], Decimal(program['gross_sf'])
    nonres = Decimal(program['nonresidential_sf'])
    grid = list(itertools.product(numbers(args.hard_cost_psf), numbers(args.rent_per_home_month), numbers(args.interest_rate)))
    if len(grid) > 60:
        raise ValueError('More than 60 combinations; narrow the ranges')
    refs = []
    if args.land_reference_url:
        refs.append({'id': 'land-basis', 'title': args.land_note or 'Land cost reference', 'url': args.land_reference_url,
                     'locator': args.land_note or 'Land cost basis'})
    written = []
    rows = []
    base_hard, base_rent, base_rate = (numbers(args.hard_cost_psf)[len(numbers(args.hard_cost_psf)) // 2],
                                       numbers(args.rent_per_home_month)[len(numbers(args.rent_per_home_month)) // 2],
                                       numbers(args.interest_rate)[len(numbers(args.interest_rate)) // 2])
    size = gross / Decimal(template['program']['gross_area_sf'])
    for hard, rent, rate in grid:
        req = copy.deepcopy(template)
        rid = slug('%s-%dst-rent%s-cost%s-rate%s' % (program['bbl'], program['stories'], rent, hard, pct(rate)))[:80]
        req['id'] = rid
        req['question'] = 'Funding gap for %s stories / %s homes at %s; approved test assumptions, not a market estimate.' % (program['stories'], homes, args.site_label)
        req['program'] = {'homes': homes, 'gross_area_sf': str(gross), 'basis': basis('Homes and gross area from the schematic massing (%s). %s' % (program['scenario_id'], approval))}
        req['references'] = refs
        tmpl_note = 'Template default from %s, kept unchanged; review before relying on it. ' % Path(args.template).name
        for line in req['capital']['lines']:
            cat = line['category']
            if cat == 'land':
                line['usd'] = str(Decimal(args.land_usd))
                line['basis'] = basis((args.land_note or 'User-approved land cost.') + ' ' + approval, ['land-basis'] if refs else [])
            elif cat == 'hard_costs':
                line['usd'] = str(hard)
                line['basis'] = basis('Hard cost of $%s per gross sf, one value in the approved sensitivity range. %s' % (hard, approval))
            elif cat == 'hard_contingency':
                line['usd'] = str((hard * Decimal(args.hard_contingency)).quantize(Decimal('0.01')))
                line['basis'] = basis('%s%% of hard cost. %s' % (pct(args.hard_contingency), approval))
            elif cat == 'soft_costs':
                line['usd'] = str((hard * Decimal(args.soft_cost_share)).quantize(Decimal('0.01')))
                line['basis'] = basis('%s%% of hard cost per gross sf. %s' % (pct(args.soft_cost_share), approval))
            elif cat == 'soft_contingency':
                line['usd'] = str((hard * Decimal(args.soft_cost_share) * Decimal('0.1')).quantize(Decimal('0.01')))
                line['basis'] = basis('10% of soft cost. ' + approval)
            elif cat in SCALE_WITH_SIZE and line['measure'] == 'fixed':
                line['usd'] = str((Decimal(line['usd']) * size).quantize(Decimal('1')))
                line['basis'] = basis('Template amount scaled by gross area (%s x template); review. %s' % (size.quantize(Decimal('0.01')), approval))
            else:
                line['basis'] = basis(tmpl_note + line['basis']['rationale'])
        ops = req['operations']
        income = [{'id': 'apartment-rent', 'annual_usd': str(rent * homes * 12), 'annual_growth': args.rent_growth,
                   'vacancy_rate': args.vacancy, 'start_year': 1, 'end_year': ops['horizon_years'],
                   'basis': basis('Average $%s per apartment per month x %s homes x 12. %s' % (rent, homes, approval))}]
        if nonres > 0 and Decimal(args.retail_rent_psf_year) > 0:
            income.append({'id': 'retail-rent', 'annual_usd': str((nonres * Decimal(args.retail_rent_psf_year)).quantize(Decimal('1'))),
                           'annual_growth': args.rent_growth, 'vacancy_rate': args.retail_vacancy, 'start_year': 1,
                           'end_year': ops['horizon_years'],
                           'basis': basis('$%s per sf per year on %s sf of ground-floor space. %s' % (args.retail_rent_psf_year, nonres, approval))})
        ops['income'] = income
        scale = Decimal(homes) / Decimal(template['program']['homes'])
        for line in ops['expenses'] + ops['below_line']:
            line['annual_usd'] = str((Decimal(line['annual_usd']) * scale).quantize(Decimal('1')))
            line['basis'] = basis('Template per-home amount scaled to %s homes (%s); review before relying on it.' % (homes, Path(args.template).name))
        reserve = ops['replacement_reserve']
        reserve['annual_usd'] = str((Decimal(reserve['annual_usd']) * scale).quantize(Decimal('1')))
        reserve['basis'] = basis('Template per-home reserve scaled to %s homes; review.' % homes)
        req['debt']['annual_interest_rate'] = str(rate)
        req['debt']['basis'] = basis('%s%% interest, other terms from template (%s). Not a lender quote. %s'
                                     % (pct(rate), Path(args.template).name, approval))
        req['sources'] = [{'id': 'sponsor-equity', 'kind': 'equity', 'amount_usd': str(Decimal(args.equity_usd)), 'status': 'proposed',
                           'basis': basis('Hypothetical sponsor equity; not committed. ' + approval)}]
        req['basis'] = basis('Generated by scripts/plan_lot.py from approved assumptions. ' + approval)
        save(out / (rid + '.json'), req)
        written.append(rid)
        rows.append((rid, hard, rent, rate, hard == base_hard and rent == base_rent and rate == base_rate))
    base = next(r[0] for r in rows if r[4])
    lines = ['# Assumptions for approval', '',
             'Site: %s · %s stories · %s homes · %s gross sf (%s sf non-residential)' % (args.site_label, program['stories'], homes, gross, nonres), '',
             '| Input | Value | Basis |', '|---|---|---|',
             '| Land | $%s | %s |' % (format(Decimal(args.land_usd), ','), args.land_note or 'user-approved'),
             '| Hard cost per gross sf | $%s | sensitivity range |' % ', $'.join(map(str, numbers(args.hard_cost_psf))),
             '| Hard-cost contingency | %s%% of hard cost | |' % pct(args.hard_contingency),
             '| Soft costs | %s%% of hard cost | |' % pct(args.soft_cost_share),
             '| Average rent per apartment per month | $%s | sensitivity range |' % ', $'.join(map(str, numbers(args.rent_per_home_month))),
             '| Retail rent | $%s per sf per year | |' % args.retail_rent_psf_year,
             '| Vacancy (apartments / retail) | %s / %s | |' % (args.vacancy, args.retail_vacancy),
             '| Mortgage interest | %s | other terms from template |' % ', '.join('%s%%' % pct(r) for r in numbers(args.interest_rate)),
             '| Sponsor equity | $%s | proposed, not committed |' % format(Decimal(args.equity_usd), ','),
             '| Construction interest, financing fees, developer fee, carry | template amounts scaled by gross area | review |',
             '| Everything else | template `%s`, expenses scaled per home | review |' % Path(args.template).name, '',
             'Base case (middle values): `%s`. %d scenarios.' % (base, len(written))]
    (out / 'assumptions.md').write_text('\n'.join(lines) + '\n')
    save(out / 'scenarios.json', {'version': '1.0', 'program': str(Path(args.program)), 'base_case': base,
                                  'scenarios': [{'id': r[0], 'hard_cost_psf': str(r[1]), 'rent_per_home_month': str(r[2]), 'interest_rate': str(r[3])} for r in rows]})
    return {'status': 'planned', 'scenarios': len(written), 'base_case': base, 'approval_sheet': str(out / 'assumptions.md'),
            'next': 'for each request: housing_underwriting build --input %s/ID.json --out UNDERWRITING/ID' % out}


def shortlist(args):
    """Rank likely conversion candidates (same ranking the feasibility report shows)."""
    from housing_feasibility.candidates import rank
    method, rows = rank(args.discovery, args.min_lot_sf, args.include_public)
    return {'status': 'ok', 'discovery': str(args.discovery), 'candidates_considered': len(rows),
            'method': method, 'top': rows[:args.top]}


def lot_request(args):
    """Write the one-lot evidence request (housing_workflow) for a confirmed BBL."""
    if not re.fullmatch(r'2[0-9]{9}', args.bbl):
        raise ValueError('The full lot workflow supports Bronx BBLs (ten digits starting with 2)')
    save(args.out, {'version': '0.2.0', 'bbl': args.bbl, 'question': args.question})
    return {'status': 'written', 'request': str(args.out),
            'next': 'housing_workflow run --input %s --out runs/NAME/evidence' % args.out}


def ownership(args):
    """Plain summary of an ownership run (the same reading the report uses)."""
    from housing_feasibility.report import summarize_ownership
    summary = summarize_ownership(load(Path(args.run) / 'package.json'))
    summary.pop('package', None)
    return {'status': 'ok', **summary}


def results(args):
    """One row per verified underwriting package: cost, loan, gap, yield on cost."""
    from housing_feasibility.engine import expand
    from housing_underwriting.engine import verify
    rows = []
    for folder in expand([args.underwriting]):
        verify(folder)
        r = load(folder / 'results.json')
        y1 = r['annual'][0]
        tdc = Decimal(r['total_development_cost_usd'])
        rows.append({'id': r['request_id'], 'homes': r['program']['homes'],
                     'total_cost_usd': money(tdc), 'loan_usd': money(r['modeled_primary_loan_usd']),
                     'gap_usd': money(r['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd']),
                     'yield_on_cost': str((Decimal(y1['noi_before_replacement_reserve_usd']) / tdc * 100).quantize(Decimal('0.1'))) + '%'})
    return {'status': 'ok', 'packages_verified': len(rows), 'scenarios': rows,
            'note': 'Gap = cost minus modeled loan and declared sources. Yield on cost = year-1 net operating income / total cost.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    m = sub.add_parser('massing', help='Plan a schematic massing and matching area request')
    m.add_argument('--evidence', required=True, help='Verified evidence package for the lot')
    m.add_argument('--parcel-source', required=True, help='Collected parcel geometry (housing_geometry collect)')
    m.add_argument('--stories', type=int, required=True)
    m.add_argument('--ground-height-ft', type=float, default=15)
    m.add_argument('--upper-height-ft', type=float, default=10)
    m.add_argument('--ground-nonresidential-sf', type=float, default=0)
    m.add_argument('--upper-coverage', type=float, default=1.0, help='Upper plate area as a share of the ground plate (e.g. 0.75)')
    m.add_argument('--setback-ft', type=float, default=0, help='Uniform inset from the mapped parcel line')
    m.add_argument('--net-efficiency', type=float, default=0.8)
    m.add_argument('--average-home-sf', type=float, default=750)
    m.add_argument('--approval-note', default='proposed for user approval; not yet approved',
                   help='Who approved these inputs and when, e.g. "approved by the user on 2026-11-16"')
    m.add_argument('--ground-use', default='shops and community space')
    m.add_argument('--architecture', default='Contemporary masonry apartment building in keeping with the street: brick base with large shopfront windows, regular punched windows above, a clear residential entrance.')
    m.add_argument('--id')
    m.add_argument('--out', required=True)
    s = sub.add_parser('scenarios', help='Write one underwriting request per assumption combination')
    s.add_argument('--program', required=True, help='program.json from the massing step')
    s.add_argument('--template', default=str(TEMPLATE))
    s.add_argument('--site-label', default='the site')
    s.add_argument('--land-usd', required=True)
    s.add_argument('--land-note')
    s.add_argument('--land-reference-url')
    s.add_argument('--hard-cost-psf', required=True, help='Comma list, e.g. 450,525,600')
    s.add_argument('--hard-contingency', default='0.10')
    s.add_argument('--soft-cost-share', default='0.20')
    s.add_argument('--rent-per-home-month', required=True, help='Comma list, e.g. 1800,2400,3000')
    s.add_argument('--retail-rent-psf-year', default='35')
    s.add_argument('--rent-growth', default='0.02')
    s.add_argument('--vacancy', default='0.05')
    s.add_argument('--retail-vacancy', default='0.10')
    s.add_argument('--interest-rate', default='0.065', help='Comma list allowed')
    s.add_argument('--equity-usd', default='3000000')
    s.add_argument('--approval-note', default='Proposed for user approval; not yet approved.',
                   help='Record who approved and when, e.g. "Approved by the user on 2026-11-16."')
    s.add_argument('--out', required=True)
    k = sub.add_parser('shortlist', help='Rank likely conversion candidates from an area search')
    k.add_argument('--discovery', required=True, help='Discovery package folder (housing_site_discovery discover)')
    k.add_argument('--top', type=int, default=8)
    k.add_argument('--min-lot-sf', type=float, default=5000)
    k.add_argument('--include-public', action='store_true', help='Also list parks, public and institutional lots')
    q = sub.add_parser('lot-request', help='Write the evidence request for one confirmed lot')
    q.add_argument('--bbl', required=True)
    q.add_argument('--question', required=True, help="Why this lot is being researched, in the user's terms")
    q.add_argument('--out', required=True)
    o = sub.add_parser('ownership', help='Summarise an ownership run: latest deed, sale, conflicts')
    o.add_argument('--run', required=True, help='Ownership run folder containing package.json')
    r = sub.add_parser('results', help='Summarise verified underwriting packages in a folder')
    r.add_argument('--underwriting', required=True, help='A package or a folder of packages')
    args = parser.parse_args(argv)
    result = {'massing': plan_massing, 'scenarios': plan_scenarios, 'shortlist': shortlist, 'lot-request': lot_request,
              'ownership': ownership, 'results': results}[args.command](args)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': str(exc)}))
        raise SystemExit(2)
