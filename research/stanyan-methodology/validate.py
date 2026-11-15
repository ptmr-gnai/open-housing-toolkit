"""Read-only integrity and bounded arithmetic checks for a known case. MIT."""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(name):
    return json.loads((HERE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decimal(value, places=2):
    return str(Decimal(str(value)).quantize(
        Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))


def validate_boundaries(data, sources):
    require(data['case_id'] == '730-stanyan-methodology', 'wrong case')
    registry = {s['id']: s for s in sources['sources']}
    expected = {'2020': 'predevelopment-2020',
                '2022': 'preliminary-gap-2022',
                '2023': 'board-packet-2023'}
    require([f['id'] for f in data['finance']] == list(expected),
            'missing, duplicate or reordered budget versions')
    for f in data['finance']:
        require(f['source_id'] == expected[f['id']],
                'budget uses evidence from another decision stage')
        require(registry[f['source_id']]['document_date'][:4] == f['id'],
                'source date differs from budget version')
        require(f['cash_flow_domain'] == 'development_capital',
                'operating subsidy cannot become development capital')
        require(not any('losp' in key.lower() for key in f['sources_usd']),
                'LOSP operating subsidy is not permanent development capital')
        require(all(isinstance(v, int) and v >= 0
                    for v in [*f['sources_usd'].values(), *f['uses_usd'].values()]),
                'capital line requires nonnegative integer dollars')
        require(f['units_including_manager'] == (120 if f['id'] == '2020' else 160),
                'unit denominator changed from the selected design version')
        land = f['includes_city_land_acquisition']
        require(land == (f['id'] == '2023'), 'land accounting boundary changed')
        require(f['uses_usd']['acquisition'] == (15900000 if land else 0),
                'land duplicated or removed from selected budget')
        require(f['excluded_city_land_usd'] == (0 if land else 15900000),
                'off-budget land boundary changed')
    o = data['operations']
    require(o['source_id'] == 'operating-subsidy-2025', 'wrong operating vintage')
    require(o['cash_flow_domain'] == 'annual_building_operations',
            'building operations must remain a separate cash-flow domain')
    require(sum(o[k] for k in ['psh_losp_units', 'pbv_units', 'lottery_units',
                              'manager_units']) == o['units'],
            'household groups do not partition the building')
    require(0 <= o['nplh_subset_of_psh'] <= o['psh_losp_units'],
            'NPLH is a subset of PSH, not another additive group')
    require(o['losp_schedule']['first_year_months'] == 5,
            'opening-year funding must not become a full-year disbursement')
    require(len(o['losp_schedule']['disbursements_usd']) == 16,
            'calendar-year disbursement schedule incomplete')


def calculate(data):
    results = {'scope': 'selected reported-budget arithmetic; no feasibility clearance',
               'capital': {}, 'operations': {}, 'diagnostics': {}}
    for f in data['finance']:
        total = f['reported_total_usd']
        results['capital'][f['id']] = {
            'source_rows_usd': sum(f['sources_usd'].values()),
            'source_rows_minus_reported_total_usd': sum(f['sources_usd'].values()) - total,
            'use_rows_usd': sum(f['uses_usd'].values()),
            'use_rows_minus_reported_total_usd': sum(f['uses_usd'].values()) - total,
            'reported_total_per_unit_usd': decimal(Decimal(total) / f['units_including_manager']),
            'reported_total_plus_excluded_land_usd': total + f['excluded_city_land_usd'],
        }
    o = data['operations']
    egi = (o['tenant_rents_usd'] + o['pbv_assistance_usd'] + o['losp_usd']
           + o['other_income_usd'] - o['vacancy_tenant_usd'] - o['vacancy_pbv_usd'])
    deductions = (o['expenses_before_reserves_usd'] + o['ground_rent_usd']
                  + o['bond_fees_usd'] + o['replacement_reserve_deposit_usd'])
    debt = o['hard_debt_service_usd']
    tenant = o['estimated_psh_tenant_revenue_inputs']
    schedule = o['losp_schedule']
    results['operations'] = {
        'recomputed_egi_usd': egi,
        'egi_rows_minus_reported_egi_usd': egi - o['reported_egi_usd'],
        'total_operating_deductions_usd': deductions,
        'reported_egi_minus_deductions_usd': o['reported_egi_usd'] - deductions,
        'reported_noi_minus_recomputed_noi_usd': o['reported_noi_usd'] - (o['reported_egi_usd'] - deductions),
        'reported_noi_minus_hard_debt_usd': o['reported_noi_usd'] - debt,
        'reported_cashflow_minus_fees_usd': o['reported_cashflow_usd'] - o['below_line_fees_usd'],
        'reported_noi_based_dscr': decimal(Decimal(o['reported_noi_usd']) / debt, 6),
        'replacement_reserve_per_unit_usd': decimal(Decimal(o['replacement_reserve_deposit_usd']) / o['units']),
        'psh_estimated_annual_tenant_rent_usd': 12 * (
            tenant['family_units'] * tenant['family_monthly_rent_usd']
            + tenant['tay_units'] * tenant['tay_monthly_rent_usd']),
        'building_plus_separately_funded_psh_services_usd': o['expenses_before_reserves_usd'] + o['separate_hsh_services_usd'],
        'losp_first_calendar_year_rounded_usd': decimal(Decimal(o['losp_usd']) * schedule['first_year_months'] / 12, 0),
        'losp_schedule_sum_usd': sum(schedule['disbursements_usd']),
    }
    results['diagnostics'] = {
        'meaning': 'analyst static Year 1 perturbations; all other items held fixed; no subsidy adjustment or probabilities modeled',
        'without_losp_dscr': decimal(Decimal(o['reported_noi_usd'] - o['losp_usd']) / debt, 6),
        'without_losp_cashflow_usd': o['reported_cashflow_usd'] - o['losp_usd'],
        'ten_percent_base_opex_increase_dscr': decimal((Decimal(o['reported_noi_usd']) - Decimal('0.10') * o['expenses_before_reserves_usd']) / debt, 6),
        '2023_total_excluding_land_usd': data['finance'][2]['reported_total_usd'] - 15900000,
        '2022_to_2023_change_excluding_land_usd': data['finance'][2]['reported_total_usd'] - 15900000 - data['finance'][1]['reported_total_usd'],
        '2020_unallocated_area_sf': 184770 - 144770 - 20000,
        '2022_component_area_sf': sum([128289, 30770, 16000, 11180, 7500]),
        '2023_commercial_components_sf': sum([3685, 2324, 3126, 1852]),
        '2023_components_minus_stated_commercial_sf': sum([3685, 2324, 3126, 1852]) - 9135,
    }
    return results


def numeric_anchors(page, values, label):
    # This verifies transcription anchors, not semantic row interpretation.
    normalized = re.sub(r'[\s,$]', '', page)
    for value in values:
        require(str(value) in normalized, f'{label}: numeric anchor absent: {value}')


def validate():
    sources = load('sources.json')
    registry = {s['id']: s for s in sources['sources']}
    pages = {}
    for s in registry.values():
        require(sha(HERE / s['pdf']) == s['sha256'], f'changed source PDF: {s["id"]}')
        require(sha(HERE / s['pages']) == s['pages_sha256'], f'changed source text: {s["id"]}')
        pages[s['id']] = json.loads((HERE / s['pages']).read_text())
    for f in load('comparison-baseline.json')['files']:
        require(sha(ROOT / f['path']) == f['sha256'], f'Bronx/capability baseline changed: {f["path"]}')
    data = load('case-data.json')
    validate_boundaries(data, sources)
    for f in data['finance']:
        numeric_anchors(pages[f['source_id']][f['pdf_page'] - 1],
                        [f['reported_total_usd'], *f['sources_usd'].values(), *f['uses_usd'].values()], f['id'])
    o = data['operations']
    numeric_anchors(pages[o['source_id']][13], [o[k] for k in [
        'tenant_rents_usd', 'pbv_assistance_usd', 'losp_usd', 'other_income_usd',
        'reported_egi_usd', 'expenses_before_reserves_usd', 'reported_noi_usd',
        'hard_debt_service_usd', 'reported_cashflow_usd', 'reported_residual_receipts_usd']], '2025 worksheet')
    numeric_anchors(pages[o['source_id']][15], o['losp_schedule']['disbursements_usd']
                    + [o['losp_schedule']['reported_contract_usd']], 'LOSP schedule')
    calculated = calculate(data)
    require(calculated == load('checks.json'), 'saved reconciliation differs from recomputation')
    require(calculated['operations']['losp_schedule_sum_usd'] == o['losp_schedule']['reported_contract_usd'], 'LOSP schedule mismatch')
    return {'status': 'passed', 'source_pdfs': len(registry),
            'capital_source_residuals_usd': {k: v['source_rows_minus_reported_total_usd'] for k, v in calculated['capital'].items()},
            'meaning': 'Integrity and bounded arithmetic pass; reported source discrepancies remain unresolved.'}


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
