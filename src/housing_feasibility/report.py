"""Project verified package contents into feasibility-report sections. MIT.

Every value is copied from a verified input or computed here with a stated formula.
Nothing is estimated: when an input is absent the section says so.
"""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import csv
import json

VERSION = '1.2.0'

BOROUGHS = {'1': 'Manhattan', '2': 'Bronx', '3': 'Brooklyn', '4': 'Queens', '5': 'Staten Island'}

SITE_FIELDS = [
    ('address', 'Address', None), ('zonedist1', 'Zoning district', None), ('zonedist2', 'Second zoning district', None),
    ('overlay1', 'Commercial overlay', None), ('overlay2', 'Second commercial overlay', None),
    ('spdist1', 'Special district', None), ('lotarea', 'Lot area', 'sf'), ('lotfront', 'Lot frontage', 'ft'),
    ('lotdepth', 'Lot depth', 'ft'), ('bldgarea', 'Existing building floor area', 'sf'),
    ('numfloors', 'Existing floors', 'floors'), ('bldgclass', 'Building class', None), ('landuse', 'Land use code', None),
    ('unitsres', 'Recorded residential units', 'units'), ('unitstotal', 'Recorded total units', 'units'),
    ('yearbuilt', 'Year built', None), ('builtfar', 'Built floor area ratio', 'FAR'),
    ('residfar', 'Recorded maximum residential FAR', 'FAR'), ('commfar', 'Recorded maximum commercial FAR', 'FAR'),
    ('facilfar', 'Recorded maximum community-facility FAR', 'FAR'), ('ownername', 'Tax-roll owner label', None),
    ('irrlotcode', 'Irregular lot', None), ('version', 'PLUTO release', None),
]

CAPITAL_LABELS = {
    'land': 'Land / acquisition price', 'acquisition_closing': 'Acquisition closing costs', 'demolition': 'Demolition',
    'remediation': 'Environmental remediation', 'hard_costs': 'Hard costs (construction)',
    'hard_contingency': 'Hard-cost contingency', 'soft_costs': 'Soft costs (design, legal, permits)',
    'soft_contingency': 'Soft-cost contingency', 'offsite_infrastructure': 'Off-site infrastructure',
    'construction_interest': 'Construction-period interest', 'taxes_and_carry': 'Taxes and carry during construction',
    'business_relocation': 'Business / tenant relocation', 'financing_fees': 'Financing fees',
    'developer_fee': 'Developer fee', 'initial_reserves': 'Initial reserves', 'other': 'Other',
}

UNKNOWN_ANSWERED_BY = {
    'finance': 'underwriting', 'title': 'ownership', 'physical_fit': 'massing',
}

NON_CLAIMS = [
    'This report assembles public records and explicitly approved test assumptions. It is not an appraisal, '
    'zoning determination, title opinion, design, cost estimate, lender quote or funding commitment.',
    'Recorded zoning fields (PLUTO) describe the tax lot; they are not a legal analysis of what may be built.',
    'Financial results are diagnostics of the stated inputs. A funding gap means the stated sources do not cover '
    'the stated costs; it is not a finding that a project is or is not feasible.',
    'Every figure links to the verified package it came from; professional review is pending.',
]


def D(value):
    return Decimal(str(value))


def money(value):
    return str(D(value).quantize(Decimal('0.01'), ROUND_HALF_UP))


def ratio(value, places='0.01'):
    return str(D(value).quantize(Decimal(places), ROUND_HALF_UP))


def load(path):
    return json.loads(Path(path).read_text())


def _packages(run, role):
    base = Path(run) / 'inputs' / role
    if not base.exists():
        return []
    if role in ('evidence', 'ownership', 'render', 'activity'):
        return [base]
    return sorted(p for p in base.iterdir() if p.is_dir())


def _rel(run, path):
    return str(Path(path).relative_to(run))


# ---------------------------------------------------------------- sections

def site_section(run, ir):
    claims = {c['id']: c for c in ir['claims']}
    bbl = ir['resolved_bbl']
    facts = []
    for field, label, unit in SITE_FIELDS:
        claim = claims.get('pluto.0.' + field)
        if not claim or claim.get('value') in (None, ''):
            continue
        ref = (claim.get('references') or [{}])[0]
        facts.append({'id': field, 'label': label, 'value': _clean(claim['value']), 'unit': unit,
                      'claim_id': claim['id'], 'source_id': ref.get('source_id')})
    by = {f['id']: f['value'] for f in facts}
    return {'bbl': bbl, 'address': by.get('address'), 'borough': BOROUGHS.get(bbl[0]),
            'block': str(int(bbl[1:6])), 'lot': str(int(bbl[6:])),
            'latitude': _clean(claims.get('pluto.0.latitude', {}).get('value')),
            'longitude': _clean(claims.get('pluto.0.longitude', {}).get('value')),
            'facts': facts, 'evidence_package': 'inputs/evidence',
            'evidence_scope': ir.get('scope')}


def _clean(value):
    if isinstance(value, str):
        try:
            number = D(value)
        except Exception:
            return value.strip()
        if number == number.to_integral_value() and '.' in value:
            return str(number.to_integral_value())
        return str(number.normalize()) if '.' in value else value
    return value


def _fact(site, field):
    for f in site['facts']:
        if f['id'] == field:
            return f['value']
    return None


def search_section(run, bbl, decisions):
    path = Path(run) / 'inputs/discovery-extract.json'
    if not path.exists():
        return None
    extract = load(path)
    lot, row, summary = extract['lot'], extract.get('lot_csv_row') or {}, extract['summary']
    counts = summary.get('counts') or {}
    candidates = extract.get('candidates', [])
    held = extract.get('in_development', [])
    chosen = next((c for c in candidates if c['bbl'] == bbl), None)
    held_chosen = next((c for c in held if c['bbl'] == bbl), None)
    from .brief import decision_steps
    why = [d['answer'] for d in decisions if 'select' in decision_steps(d)]
    return {'question': summary.get('question'), 'scope': summary.get('scope'),
            'lots_in_area': counts.get('inventory'), 'recorded_nonhousing_in_area': counts.get('recorded_nonhousing'),
            'by_current_use': counts.get('by_current_use'),
            'nonhousing_by_zoning_path': counts.get('nonhousing_by_zoning_path'),
            'candidate_method': extract.get('candidate_method'), 'candidates_count': len(candidates),
            'top_candidates': candidates[:5], 'all_candidates': candidates,
            'in_development': held, 'activity': extract.get('activity'),
            'selected': {'bbl': bbl, 'rank': chosen['rank'] if chosen else None,
                         'in_ranked_candidates': chosen is not None,
                         'held_back_as_in_development': held_chosen is not None,
                         'development_activity': (chosen or held_chosen or {}).get('development_activity'),
                         'why_user_words': why,
                         'current_use_category': lot.get('current_use_category'),
                         'zoning_path': row.get('zoning_path') or None, 'review_lane': row.get('review_lane') or None,
                         'flags': lot.get('flags', []),
                         'nearest_station': row.get('nearest_station_name') or None,
                         'nearest_station_straight_line_m': row.get('nearest_station_straight_line_m') or None,
                         'recorded_affordable_residential_far': row.get('recorded_affordable_residential_far') or None},
            'order_method': summary.get('order_method'), 'limits': summary.get('limits'),
            'package': {'name': extract['package_name'], 'manifest_sha256': extract['package_manifest_sha256'],
                        'retention': extract['retention']}}


def activity_for_site(run, bbl):
    path = Path(run) / 'inputs/activity/activity.json'
    if not path.exists():
        return None
    result = load(path)
    lot = next((l for l in result['lots'] if l['bbl'] == bbl), None)
    if lot is None:
        raise ValueError('The activity package does not cover the selected lot %s' % bbl)
    return {'status': lot['status'], 'latest': lot['latest'], 'signals': lot['signals'], 'as_of': result['as_of'],
            'since': result['since'], 'coverage_gaps': result['coverage_gaps'], 'run_status': result['run_status'],
            'limits': result['limits'], 'package': 'inputs/activity'}


def brief_section(run):
    from .brief import validate
    brief = validate(load(Path(run) / 'inputs/brief.json'))
    return {'goal': brief['goal'], 'persona': brief['persona'], 'provided': brief['provided'],
            'decisions': brief['decisions'], 'extends': brief.get('extends', []), 'notes': brief.get('notes', []),
            'source': 'inputs/brief.json'}


STEP_LABELS = [('search', 'Search the area'), ('activity', 'Check development activity'), ('select', 'Choose a site'), ('research', 'Research the lot'),
               ('ownership', 'Ownership and sales'), ('massing', 'Sketch what could be built'),
               ('financing', 'Test the money'), ('render', 'Picture'), ('report', 'Report')]


def process_section(run, brief, search, ownership, massing, sensitivity, render):
    decided = {}
    for d in brief['decisions']:
        from .brief import decision_steps
        for step in decision_steps(d):
            decided.setdefault(step, []).append(d)
    act = (Path(run) / 'inputs/activity/activity.json')
    act = load(act) if act.exists() else None
    ran = {'activity': act is not None, 'search': search is not None, 'select': search is not None or bool(decided.get('select')),
           'research': True, 'ownership': ownership is not None, 'massing': bool(massing),
           'financing': True, 'render': render is not None, 'report': True}
    results = {
        'search': search and '%s lots, %s recorded nonhousing, %s ranked candidates' % (
            search['lots_in_area'], search['recorded_nonhousing_in_area'], search['candidates_count']),
        'activity': act and '%s of %s lots show active development' % (act['counts']['active_development'], act['lots_checked']),
        'select': search and (('Chosen although recorded as already in development' if search['selected']['held_back_as_in_development'] else None)
                              or (search['selected']['rank'] and 'Candidate #%s of %s' % (search['selected']['rank'], search['candidates_count']))),
        'research': 'Public records collected and verified',
        'ownership': ownership and ('Latest deed %s' % ownership['latest_recorded_deed']['recorded_date']
                                    if ownership['latest_recorded_deed'] else 'No deed found'),
        'massing': massing and ', '.join('%s stories' % m['stories'] for m in massing),
        'financing': '%s scenarios' % len(sensitivity['scenarios']),
        'render': render and ('Image generated and reviewed' if render['image'] else 'Brief prepared'),
        'report': 'This document'}
    packages = {'search': ['inputs/discovery-extract.json'] if search else [], 'research': ['inputs/evidence'],
                'ownership': ['inputs/ownership'] if ownership else [], 'massing': [m['package'] for m in massing],
                'financing': [x['package'] for x in sensitivity['scenarios']],
                'render': [render['package']] if render else [], 'select': [], 'report': [],
                'activity': ['inputs/activity'] if act else []}
    steps = []
    for key, label in STEP_LABELS:
        steps.append({'step': key, 'label': label, 'status': 'ran' if ran[key] else 'not_run',
                      'result': results[key] or None, 'packages': packages[key],
                      'decisions': len(decided.get(key, []))})
    return {'steps': steps, 'decisions_total': len(brief['decisions'])}


def ownership_section(run):
    packages = _packages(run, 'ownership')
    if not packages:
        return None
    return summarize_ownership(load(packages[0] / 'package.json'))


def summarize_ownership(package):
    records = package['records']
    instruments = [r for r in records if r['kind'] == 'recorded_instrument']
    deeds = [r for r in instruments if r.get('instrument_family') == 'deed']
    deeds.sort(key=lambda r: ((r.get('dates') or {}).get('recorded_datetime') or '', r['raw']['master']['document_id']
                              if r.get('raw', {}).get('master') else ''), reverse=True)
    latest = None
    if deeds:
        d = deeds[0]
        latest = {'document_type': d.get('doc_type_description') or d.get('doc_type_raw'),
                  'document_date': _day((d.get('dates') or {}).get('document_date')),
                  'recorded_date': _day((d.get('dates') or {}).get('recorded_datetime')),
                  'recorded_amount_usd': money(d['instrument_amount']) if d.get('instrument_amount') not in (None, '') else None,
                  'amount_note': d.get('instrument_amount_note'),
                  'parties': [{'name': p.get('name'), 'role': p.get('role') or ('party ' + str(p.get('party_type')))}
                              for p in d.get('parties', [])],
                  'document_id': (d.get('raw', {}).get('master') or {}).get('document_id')}
    sales = sorted((r for r in records if r['kind'] == 'sale'),
                   key=lambda r: r['fields'].get('sale_date') or '', reverse=True)
    last_sale = None
    if sales:
        f = sales[0]['fields']
        last_sale = {'sale_date': _day(f.get('sale_date')), 'sale_price_usd': money(f['sale_price']) if f.get('sale_price') else None,
                     'source': 'NYC DOF rolling/annualized sales'}
    identity = next((r['fields'] for r in records if r['kind'] == 'parcel_identity'), {})
    families = {}
    for r in instruments:
        families[r.get('instrument_family') or 'other'] = families.get(r.get('instrument_family') or 'other', 0) + 1
    current = (package.get('ownership_evidence') or {}).get('current_owner') or {'status': 'unknown'}
    return {'run_status': package['run_status'], 'tax_roll_owner_label': identity.get('ownername') or identity.get('owner1'),
            'latest_recorded_deed': latest, 'latest_dof_sale': last_sale,
            'instrument_counts': dict(sorted(families.items())),
            'conflicts': [c['description'] for c in package.get('conflicts', [])],
            'current_owner_status': current.get('status'),
            'limitations': package.get('limitations', [])[:4], 'package': 'inputs/ownership/package.json'}


def _day(value):
    return value[:10] if isinstance(value, str) else value


def massing_section(run):
    result = []
    for folder in _packages(run, 'massing'):
        g = load(folder / 'geometry.json')
        floors = []
        with (folder / 'floor-schedule.csv').open(newline='') as handle:
            for row in csv.DictReader(handle):
                floors.append({k: (_clean(v) if k != 'floor_id' else v) for k, v in row.items()})
        totals = {k: ratio(v, '1') for k, v in g['totals_sf'].items()}
        result.append({'id': g['scenario_id'], 'package': _rel(run, folder), 'stories': len(g['floors']),
                       'total_height_ft': _clean(str(g['total_height_ft'])), 'totals_sf': totals, 'floors': floors,
                       'mapped_containment': g.get('mapped_containment'), 'design_status': g.get('design_status'),
                       'area_reconciliation': sorted({c['status'] for c in g.get('comparisons', [])}),
                       'unresolved_review_gates': sorted(k for k, v in (g.get('review_gates') or {}).items() if v == 'unknown'),
                       'figures': {name: _rel(run, folder / name) for name in ('massing.svg', 'plan.svg') if (folder / name).exists()}})
    return result


def zoning_section(site, massing, discovery):
    lot_area = _fact(site, 'lotarea')
    residfar, commfar, facilfar = _fact(site, 'residfar'), _fact(site, 'commfar'), _fact(site, 'facilfar')
    calcs = []

    def capacity(far, label):
        if lot_area in (None, '0') or far in (None, ''):
            return None
        value = ratio(D(lot_area) * D(far), '1')
        calcs.append({'label': label, 'value_sf': value, 'formula': 'recorded lot area %s sf x recorded FAR %s' % (lot_area, far)})
        return value

    max_res = capacity(residfar, 'Indicative maximum residential floor area')
    capacity(commfar, 'Indicative maximum commercial floor area')
    capacity(facilfar, 'Indicative maximum community-facility floor area')
    affordable_far = (discovery or {}).get('selected', {}).get('recorded_affordable_residential_far')
    max_aff = None
    if affordable_far:
        max_aff = capacity(affordable_far, 'Indicative maximum residential floor area with affordable-housing provisions')
    options = []
    for m in massing:
        gross, res = D(m['totals_sf']['gross']), D(m['totals_sf']['residential'])
        res_far = res / D(lot_area) if lot_area else None
        status = 'not_compared'
        if max_res is not None:
            if res <= D(max_res):
                status = 'within_recorded_residential_far'
            elif max_aff is not None and res <= D(max_aff):
                status = 'needs_affordable_housing_provisions'
            else:
                status = 'exceeds_recorded_far'
        options.append({'massing_id': m['id'], 'stories': m['stories'], 'gross_sf': m['totals_sf']['gross'],
                        'residential_sf': m['totals_sf']['residential'],
                        'gross_far_proxy': ratio(gross / D(lot_area)) if lot_area else None,
                        'residential_far_proxy': ratio(res_far) if res_far is not None else None,
                        'status': status})
    existing = _fact(site, 'bldgarea')
    return {'district': _fact(site, 'zonedist1'), 'second_district': _fact(site, 'zonedist2'),
            'overlay': _fact(site, 'overlay1'), 'special_district': _fact(site, 'spdist1'),
            'lot_area_sf': lot_area, 'recorded_residential_far': residfar, 'recorded_commercial_far': commfar,
            'recorded_community_facility_far': facilfar, 'recorded_affordable_residential_far': affordable_far,
            'existing_floor_area_sf': existing, 'built_far': _fact(site, 'builtfar'),
            'capacity_calculations': calcs, 'massing_comparison': options,
            'caveats': ['Uses recorded PLUTO zoning descriptors, not the Zoning Resolution text, maps or approvals.',
                        'Massing area is gross plate area, a proxy; zoning floor area excludes some spaces and was not computed.',
                        'Height and setback rules, yards, street width and zoning-lot mergers were not checked.']}


def _capital(result):
    return [{'category': l['category'], 'label': CAPITAL_LABELS.get(l['category'], l['category'].replace('_', ' ')),
             'amount_usd': money(l['amount_usd']), 'basis_kind': (l.get('basis') or {}).get('kind'),
             'rationale': (l.get('basis') or {}).get('rationale')} for l in result['capital_lines']]


def _year(result, year):
    return next((a for a in result['annual'] if a['year'] == year), None)


def underwriting_sections(run, base_id):
    packages = []
    for folder in _packages(run, 'underwriting'):
        packages.append((folder, load(folder / 'request.json'), load(folder / 'results.json')))
    ids = [r['request_id'] for _, _, r in packages]
    if len(set(ids)) != len(ids):
        raise ValueError('Two underwriting packages share a request id')
    if base_id not in ids:
        raise ValueError('Base case %r is not among the underwriting packages: %s' % (base_id, ', '.join(ids)))
    folder, req, res = next(p for p in packages if p[2]['request_id'] == base_id)
    homes, gross = res['program']['homes'], D(res['program']['gross_area_sf'])
    tdc = D(res['total_development_cost_usd'])
    loan = D(res['modeled_primary_loan_usd'])
    sources = [{'label': 'Permanent mortgage (modeled, not committed)', 'kind': 'primary_debt', 'status': 'modeled',
                'amount_usd': money(loan)}]
    for s in req.get('sources', []):
        sources.append({'label': s['id'].replace('-', ' ').capitalize(), 'kind': s['kind'], 'status': s['status'],
                        'amount_usd': money(s['amount_usd'])})
    gap = D(res['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd'])
    budget = {'base_case_id': base_id, 'package': _rel(run, folder), 'homes': homes, 'gross_sf': ratio(gross, '1'),
              'uses': _capital(res), 'total_uses_usd': money(tdc),
              'cost_per_home_usd': money(tdc / homes), 'cost_per_gross_sf_usd': money(tdc / gross),
              'sources': sources, 'total_sources_usd': money(sum(D(s['amount_usd']) for s in sources)),
              'gap_usd': money(gap), 'surplus_usd': money(res['surplus_after_modeled_loan_and_all_declared_sources_usd']),
              'year1_noi_usd': money(_year(res, 1)['noi_before_replacement_reserve_usd']),
              'yield_on_cost': ratio(D(_year(res, 1)['noi_before_replacement_reserve_usd']) / tdc, '0.0001'),
              'loan_to_cost': ratio(loan / tdc, '0.0001'),
              'gap_to_cost': ratio(gap / tdc, '0.0001'),
              'metric_formulas': {'yield_on_cost': 'year-1 net operating income (before reserve) / total development cost',
                                  'loan_to_cost': 'modeled permanent loan / total development cost',
                                  'gap_to_cost': 'funding gap / total development cost'},
              'gap_formula': res['methods']['gap']}
    years = [y for y in (1, 5, 10, 15, 20) if _year(res, y)]
    rows = []

    def add(label, key=None, kind='money', fn=None, indent=0):
        values = []
        for y in years:
            a = _year(res, y)
            v = fn(a) if fn else a.get(key)
            values.append(None if v is None else (money(v) if kind == 'money' else ratio(v)))
        rows.append({'label': label, 'kind': kind, 'indent': indent, 'values': values})

    first = _year(res, 1)
    for line in first['income_lines']:
        lid = line['id']
        add(_title(lid) + ' (scheduled)', fn=lambda a, lid=lid: _line(a, 'income_lines', lid, 'scheduled_usd'), indent=1)
        add(_title(lid) + ' vacancy and loss', fn=lambda a, lid=lid: -D(_line(a, 'income_lines', lid, 'vacancy_loss_usd') or 0), indent=1)
    add('Effective gross income', 'effective_gross_income_usd')
    for line in first['expense_lines']:
        lid = line['id']
        add(_title(lid), fn=lambda a, lid=lid: _line(a, 'expense_lines', lid, 'amount_usd'), indent=1)
    add('Total operating expenses', 'operating_expenses_usd')
    add('Net operating income (before reserve)', 'noi_before_replacement_reserve_usd')
    add('Replacement reserve', 'replacement_reserve_usd', indent=1)
    add('Mortgage payments (debt service)', 'primary_debt_service_usd')
    add('Debt service coverage ratio', 'dscr', kind='ratio')
    add('Cash flow after debt service and reserves', 'cash_after_reserves_debt_and_below_line_usd')
    pro_forma = {'base_case_id': base_id, 'years': years, 'calendar_years': [_year(res, y)['calendar_year'] for y in years],
                 'rows': rows, 'price_basis': req.get('price_basis'),
                 'coverage_breach_years': res['coverage_breach_years'], 'cashflow_shortfall_years': res['cashflow_shortfall_years']}
    debt = req['debt']
    sizing = {'loan_usd': money(loan), 'binding_constraints': res['binding_debt_caps'],
              'constraints_usd': {k: money(v) for k, v in res['debt_caps_usd'].items()},
              'interest_rate': debt.get('annual_interest_rate'), 'amortization_years': debt.get('amortization_years'),
              'required_dscr': first.get('required_dscr'), 'missing_checks': res.get('missing_financing_checks', []),
              'method': res['methods']['debt']}
    sensitivity = []
    for folder, req_i, r in packages:
        g = D(r['program']['gross_area_sf'])
        hard = sum(D(l['amount_usd']) for l in r['capital_lines'] if l['category'] == 'hard_costs')
        y1 = _year(r, 1)
        scheduled = sum(D(l['scheduled_usd']) for l in y1['income_lines'])
        sensitivity.append({'id': r['request_id'], 'package': _rel(run, folder), 'homes': r['program']['homes'],
                            'gross_sf': ratio(g, '1'), 'hard_cost_per_gross_sf_usd': money(hard / g),
                            'scheduled_income_per_home_month_usd': money(scheduled / r['program']['homes'] / 12),
                            'interest_rate': req_i['debt'].get('annual_interest_rate'),
                            'total_development_cost_usd': money(r['total_development_cost_usd']),
                            'year1_noi_usd': money(y1['noi_before_replacement_reserve_usd']),
                            'loan_usd': money(r['modeled_primary_loan_usd']),
                            'gap_usd': money(r['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd']),
                            'yield_on_cost': ratio(D(y1['noi_before_replacement_reserve_usd']) / D(r['total_development_cost_usd']), '0.0001'),
                            'is_base_case': r['request_id'] == base_id})
    gaps = [D(s['gap_usd']) for s in sensitivity]
    unresolved = list(res.get('unresolved', [])) + list(res.get('missing_financing_checks', []))
    groups = {}
    for x in sensitivity:
        groups.setdefault((x['gross_sf'], x['homes']), []).append(x)
    by_program = []
    for (gross_sf, homes), rows in sorted(groups.items(), key=lambda kv: D(kv[0][0])):
        by_program.append({'gross_sf': gross_sf, 'homes': homes, 'scenarios': len(rows),
                           'yield_on_cost_min': min((r['yield_on_cost'] for r in rows), key=D),
                           'yield_on_cost_max': max((r['yield_on_cost'] for r in rows), key=D),
                           'gap_min_usd': min((r['gap_usd'] for r in rows), key=D),
                           'gap_max_usd': max((r['gap_usd'] for r in rows), key=D),
                           'includes_base_case': any(r['is_base_case'] for r in rows)})
    return budget, pro_forma, sizing, {'scenarios': sensitivity, 'by_program': by_program, 'gap_min_usd': money(min(gaps)),
                                        'gap_max_usd': money(max(gaps)), 'scenarios_with_gap': sum(1 for g in gaps if g > 0),
                                        'note': 'Each row is a separately verified underwriting package; '
                                                'scheduled income includes all income lines (residential and commercial).'}, unresolved


def _line(annual, key, lid, field):
    return next((l.get(field) for l in annual[key] if l['id'] == lid), None)


def _title(identifier):
    return identifier.replace('-', ' ').replace('_', ' ').capitalize()


def reconciliation(budget_rows, massing):
    out = []
    for row in budget_rows:
        match = [m['id'] for m in massing if abs(D(m['totals_sf']['gross']) - D(row['gross_sf'])) <= 1]
        out.append({'underwriting_id': row['id'], 'gross_sf': row['gross_sf'],
                    'matching_massing': match, 'status': 'matches_massing' if match else
                    ('no_massing_supplied' if not massing else 'no_massing_with_same_gross_area')})
    return out


def concept_section(run, folder, massing):
    """A massing-grounded concept (housing_concept): prompt compiled from the massing, elevation drawn from it."""
    concept = load(folder / 'concept.json')
    gen = load(folder / 'generation.json') if (folder / 'generation.json').exists() else None
    review = load(folder / 'review.json') if gen else None
    matches = [m['id'] for m in massing if m['id'] == concept['massing_id']]
    return {'stage': 'generated_and_reviewed' if gen else 'prompt_prepared', 'kind': 'massing_grounded',
            'package': _rel(run, folder), 'image': _rel(run, folder / gen['image']) if gen else None,
            'elevation': _rel(run, folder / 'elevation.png'), 'elevation_svg': _rel(run, folder / 'elevation.svg'),
            'massing_view': _rel(run, folder / 'massing-3d.png'), 'site_plan': _rel(run, folder / 'site-plan.png'),
            'prompt': _rel(run, folder / 'prompt.txt'), 'required_caption': concept['caption'],
            'stories': concept['stories'], 'matching_massing': matches,
            'story_status': 'matches_massing' if matches else ('no_massing_supplied' if not massing else 'differs_from_massing'),
            'grounding': {k: concept[k] for k in ('massing_id', 'height_ft', 'ground_floor_height_ft', 'ground_floor_width_ft',
                                                  'upper_floor_height_ft', 'upper_floor_width_ft', 'upper_setback_ft', 'style', 'ground_use')},
            'reference': {'provider': concept['photo']['provider'], 'attribution': concept['credit'],
                          'capture_date': concept['photo']['capture_date'], 'source_image_byte_bound': True},
            'provider': gen['provider'] if gen else None,
            'review_checks': [{'id': k, 'status': v['status'], 'note': v['note']} for k, v in (review or {}).get('checks', {}).items()],
            'unverified': ['surveyed footprint', 'camera alignment', 'zoning envelope', 'design'], 'site_bbl': concept['site_bbl']}


def render_section(run, massing):
    packages = _packages(run, 'render')
    if not packages:
        return None
    folder = packages[0]
    if (folder / 'concept.json').exists():
        return concept_section(run, folder, massing)
    brief = load(folder / 'render-brief.json')
    scenario_path = folder / 'inputs/scenario.json'
    stories = None
    if scenario_path.exists():
        stories = ((load(scenario_path).get('parameters') or {}).get('total_stories') or {}).get('value')
    receipt = load(folder / 'render-receipt.json') if (folder / 'render-receipt.json').exists() else None
    review = load(folder / 'review.json') if (folder / 'review.json').exists() else None
    matches = [m['id'] for m in massing if m['stories'] == stories]
    ref = brief['reference']
    return {'stage': 'generated_and_reviewed' if receipt else 'brief_prepared', 'kind': 'photo_brief', 'package': _rel(run, folder),
            'image': _rel(run, folder / receipt['image_path']) if receipt else None,
            'prompt': _rel(run, folder / 'prompt.txt'), 'required_caption': brief.get('required_caption'),
            'stories': stories, 'matching_massing': matches,
            'story_status': 'matches_massing' if matches else ('no_massing_supplied' if not massing else 'differs_from_massing'),
            'reference': {'provider': ref.get('provider'), 'attribution': ref.get('attribution'),
                          'capture_date': ref.get('capture_date'), 'source_image_byte_bound': ref.get('sha256') is not None},
            'provider': receipt.get('provider') if receipt else None,
            'review_checks': [{'id': c['id'], 'status': c['status'], 'note': c.get('note')} for c in (review or {}).get('checks', [])],
            'unverified': brief.get('unverified', [])}


def open_items(ir, ownership, massing, unresolved, render, present, activity=None):
    items = []
    if activity and activity['status'] in ('active_development', 'site_preparation'):
        items.append({'area': 'current activity', 'item': 'Recorded permits show this lot is %s: %s. Any scenario here competes with, '
                      'or describes, a project already underway; confirm with the owner and DOB before relying on it.'
                      % ('already being developed' if activity['status'] == 'active_development' else 'being prepared for work',
                         activity['latest']), 'partly_addressed_by': None, 'source': 'activity'})
    for c in ir['claims']:
        if c['kind'] == 'unknown' and c['id'].startswith('unknown.'):
            key = c['id'].split('.', 1)[1]
            covered = UNKNOWN_ANSWERED_BY.get(key)
            note = None
            if covered and covered in present:
                note = {'underwriting': 'Explored with test scenarios in this report; inputs are assumptions, not commitments.',
                        'ownership': 'Recorded deeds and parties are summarised in this report; title is still not established.',
                        'massing': 'A schematic massing is included; it does not establish survey, envelope or layout fit.'}[covered]
            items.append({'area': key.replace('_', ' '), 'item': c['rationale'], 'partly_addressed_by': note, 'source': 'evidence'})
    if ownership:
        for text in ownership['conflicts']:
            items.append({'area': 'ownership', 'item': text, 'partly_addressed_by': None, 'source': 'ownership'})
    gates = sorted({g for m in massing for g in m['unresolved_review_gates']})
    if gates:
        items.append({'area': 'design', 'item': 'Massing review gates still unknown: ' + ', '.join(g.replace('_', ' ') for g in gates) + '.',
                      'partly_addressed_by': None, 'source': 'massing'})
    for text in unresolved:
        items.append({'area': 'finance', 'item': text, 'partly_addressed_by': None, 'source': 'underwriting'})
    if render:
        bad = [c['id'].replace('_', ' ') for c in render['review_checks'] if c['status'] != 'consistent_by_inspection']
        if bad:
            items.append({'area': 'render', 'item': 'Render review checks not confirmed: ' + ', '.join(bad) + '.',
                          'partly_addressed_by': None, 'source': 'render'})
        if render['story_status'] == 'differs_from_massing':
            items.append({'area': 'render', 'item': 'Render story count differs from every massing in this report.',
                          'partly_addressed_by': None, 'source': 'render'})
    return items


def sources_section(run, ownership_present):
    rows = []
    for r in load(Path(run) / 'inputs/evidence/receipts.json'):
        rows.append({'id': r['id'], 'publisher': r.get('publisher'), 'url': r.get('url'), 'catalog_url': r.get('catalog_url'),
                     'retrieved_at': r.get('retrieved_at'), 'sha256': r.get('sha256'), 'status': r.get('status'), 'package': 'evidence'})
    if ownership_present:
        for s in load(Path(run) / 'inputs/ownership/package.json')['sources']:
            rows.append({'id': s['id'], 'publisher': s.get('publisher'), 'url': s.get('url'), 'catalog_url': None,
                         'retrieved_at': s.get('retrieved_at'), 'sha256': s.get('sha256'), 'status': s.get('status') or
                         ('ok' if s.get('http_status') == 200 else None), 'package': 'ownership'})
    seen = set()
    for folder in _packages(run, 'underwriting'):
        for ref in load(folder / 'references.json'):
            if ref['id'] in seen:
                continue
            seen.add(ref['id'])
            rows.append({'id': ref['id'], 'publisher': ref.get('title'), 'url': ref.get('url'), 'catalog_url': None,
                         'retrieved_at': None, 'sha256': ref.get('sha256'), 'status': ref.get('retention'), 'package': 'underwriting'})
    return rows


def _manifest_sha(folder):
    import hashlib
    return hashlib.sha256((folder / 'manifest.json').read_bytes()).hexdigest() if (folder / 'manifest.json').exists() else \
        hashlib.sha256((folder / 'package.json').read_bytes()).hexdigest()


def evidence_fingerprint(run, fallback_hashes=None):
    """One hash over the request and every retained input file (the report's receipts)."""
    import hashlib
    run = Path(run)
    lines = {}
    for path in sorted([run / 'request.json'] + [p for p in (run / 'inputs').rglob('*') if p.is_file()]):
        if '__pycache__' in path.parts:
            continue
        lines[str(path.relative_to(run))] = hashlib.sha256(path.read_bytes()).hexdigest()
    for name, sha in (fallback_hashes or {}).items():
        lines.setdefault(name, sha)
    text = ''.join('%s  %s\n' % (sha, name) for name, sha in sorted(lines.items()))
    return hashlib.sha256(text.encode()).hexdigest()


def provenance_section(run, brief, fallback_hashes=None):
    path = Path(run) / 'inputs/toolkit.json'
    toolkit = load(path) if path.exists() else {'name': 'Open Housing Toolkit', 'repository': None}
    return {'toolkit': toolkit, 'evidence_fingerprint': evidence_fingerprint(run, fallback_hashes),
            'fingerprint_method': 'sha256 of the sorted list of "sha256  path" lines for request.json and every file under inputs/',
            'extends': brief.get('extends', []),
            'machine_readable': 'report.json; the same JSON is embedded in report.html in the script element with id report-data'}


def assemble(run, fallback_hashes=None):
    run = Path(run)
    request = load(run / 'request.json')
    ir = load(run / 'inputs/evidence/ir.json')
    brief = brief_section(run)
    site = site_section(run, ir)
    site['development_activity'] = activity_for_site(run, site['bbl'])
    search = search_section(run, site['bbl'], brief['decisions'])
    ownership = ownership_section(run)
    massing = massing_section(run)
    zoning = zoning_section(site, massing, search)
    budget, pro_forma, sizing, sensitivity, unresolved = underwriting_sections(run, request['base_case'])
    render = render_section(run, massing)
    present = {'underwriting'} | ({'ownership'} if ownership else set()) | ({'massing'} if massing else set())
    if ownership and load(run / 'inputs/ownership/package.json')['parcel']['bbl'] != site['bbl']:
        raise ValueError('Ownership package is for a different tax lot')
    for m in massing:
        if load(run / m['package'] / 'geometry.json')['site_bbl'] != site['bbl']:
            raise ValueError('Massing package is for a different tax lot')
    if render and (render.get('site_bbl') or load(run / render['package'] / 'render-brief.json')['site_bbl']) != site['bbl']:
        raise ValueError('Render package is for a different tax lot')
    gaps = sensitivity
    headline = {'bbl': site['bbl'], 'address': site['address'], 'base_case_id': budget['base_case_id'],
                'homes': budget['homes'], 'gross_sf': budget['gross_sf'],
                'total_development_cost_usd': budget['total_uses_usd'], 'modeled_loan_usd': sizing['loan_usd'],
                'base_gap_usd': budget['gap_usd'], 'gap_range_usd': [gaps['gap_min_usd'], gaps['gap_max_usd']],
                'base_yield_on_cost': budget['yield_on_cost'], 'base_loan_to_cost': budget['loan_to_cost'],
                'yield_on_cost_range': [min(x['yield_on_cost'] for x in gaps['scenarios']), max(x['yield_on_cost'] for x in gaps['scenarios'])],
                'scenarios': len(gaps['scenarios']), 'scenarios_with_gap': gaps['scenarios_with_gap']}
    inputs = [{'role': role, 'package': _rel(run, f), 'manifest_sha256': _manifest_sha(f)}
              for role in ('evidence', 'ownership', 'activity', 'massing', 'underwriting', 'render') for f in _packages(run, role)]
    return {'version': VERSION, 'module': 'feasibility-report', 'request': request, 'brief': brief,
            'provenance': provenance_section(run, brief, fallback_hashes),
            'process': process_section(run, brief, search, ownership, massing, sensitivity, render),
            'headline': headline, 'site': site, 'search': search, 'ownership': ownership, 'zoning': zoning,
            'massing': massing, 'development_budget': budget, 'operating_pro_forma': pro_forma, 'debt_sizing': sizing,
            'sensitivity': sensitivity, 'program_reconciliation': reconciliation(sensitivity['scenarios'], massing),
            'render': render, 'open_items': open_items(ir, ownership, massing, unresolved, render, present, site['development_activity']),
            'sources': sources_section(run, bool(ownership)), 'inputs': inputs, 'non_claims': NON_CLAIMS}
