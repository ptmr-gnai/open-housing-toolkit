"""Stanyan known-case budget reconstruction and one-assumption diagnostics. MIT."""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import hashlib
import html
import io
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'src'))
import validate as evidence
from housing_common.local_outputs import destination

D = Decimal
ASSUMPTIONS = ('operating_expense_multiplier', 'losp_multiplier', 'hard_cost_multiplier')
MODEL_VERSION = 'stanyan-budget-0.1'


def canonical(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n'


def read(path):
    return json.loads(Path(path).read_text())


def money(value):
    return str(D(value).quantize(D('.01'), rounding=ROUND_HALF_UP))


def value_string(value, unit):
    return str(value.quantize(D('.000001'), rounding=ROUND_HALF_UP)) if unit == 'ratio' else money(value)


def change_contract(change):
    if change is None:
        return None
    if not isinstance(change, dict):
        raise ValueError('A change must be a JSON object')
    if set(change) != {'id', 'assumption', 'value', 'rationale'}:
        raise ValueError('A change needs exactly id, assumption, value and rationale')
    if not isinstance(change['id'], str) or not re.fullmatch(r'[a-z][a-z0-9-]{0,63}', change['id']):
        raise ValueError('Invalid change id')
    if change['id'] == 'baseline':
        raise ValueError('baseline is reserved')
    if change['assumption'] not in ASSUMPTIONS:
        raise ValueError('Unsupported assumption')
    if not isinstance(change['value'], str):
        raise ValueError('Assumption value must be a decimal string')
    try:
        number = D(change['value'])
        if not number.is_finite() or not 0 <= number <= 10:
            raise ValueError('Multiplier must be finite and between 0 and 10')
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal assumption') from exc
    if not isinstance(change['rationale'], str) or not change['rationale'].strip():
        raise ValueError('A change must explain its rationale')
    return change


class Graph:
    def __init__(self):
        self.nodes = {}
        self.values = {}

    def add(self, key, value, unit='USD', kind='calculation', deps=(), method='', source=None):
        if key in self.nodes or any(dep not in self.nodes for dep in deps):
            raise ValueError('Duplicate node or unresolved dependency: ' + key)
        value = D(value)
        if not value.is_finite():
            raise ValueError('Non-finite result')
        if unit != 'ratio':
            value = value.quantize(D('.01'), rounding=ROUND_HALF_UP)
        self.values[key] = value
        self.nodes[key] = {'value': value_string(value, unit), 'unit': unit, 'kind': kind,
                           'dependencies': sorted(deps), 'method': method, 'source': source}
        return value

    def total(self, key, deps, method='sum', unit='USD'):
        return self.add(key, sum((self.values[x] for x in deps), D(0)), unit, deps=deps, method=method)


def reference(source_id, page):
    return {'source_id': source_id, 'pdf_page': page}


def model(data, detail, change=None):
    change_contract(change)
    g = Graph()
    for key in ASSUMPTIONS:
        changed = change is not None and change['assumption'] == key
        g.add('assumptions.' + key, change['value'] if changed else '1', 'ratio',
              'assumption', method=change['rationale'] if changed else 'baseline multiplier of 1')
    for budget in data['finance']:
        prefix = 'capital.' + budget['id']
        source = reference(budget['source_id'], budget['pdf_page'])
        use_nodes, source_nodes = [], []
        for key, amount in budget['sources_usd'].items():
            node = prefix + '.source.' + key
            g.add(node, amount, kind='reported_budget', source=source)
            source_nodes.append(node)
        for key, amount in budget['uses_usd'].items():
            node = prefix + '.use.' + key
            raw = prefix + '.reported_use.' + key
            g.add(raw, amount, kind='reported_budget', source=source)
            deps = [raw]
            value = D(amount)
            if budget['id'] == '2023' and key == 'hard':
                deps.append('assumptions.hard_cost_multiplier')
                value *= g.values[deps[-1]]
            g.add(node, value, deps=deps, method='reported use * declared multiplier' if len(deps) > 1 else 'reported use unchanged')
            use_nodes.append(node)
        total_sources = g.total(prefix + '.total_sources', source_nodes)
        total_uses = g.total(prefix + '.total_uses', use_nodes)
        reported = g.add(prefix + '.reported_total', budget['reported_total_usd'], kind='reported_budget', source=source)
        g.add(prefix + '.source_residual', total_sources - reported,
              deps=[prefix + '.total_sources', prefix + '.reported_total'], method='source rows - reported total; preserve original discrepancy')
        g.add(prefix + '.unfunded_uses', total_uses - total_sources,
              deps=[prefix + '.total_uses', prefix + '.total_sources'], method='uses - source rows; no automatic funding')
        g.add(prefix + '.additional_unallocated_capital', total_uses - reported,
              deps=[prefix + '.total_uses', prefix + '.reported_total'], method='scenario uses - reported uses; excludes original source rounding residual')
        g.add(prefix + '.total_excluding_land', total_uses - g.values[prefix + '.use.acquisition'],
              deps=[prefix + '.total_uses', prefix + '.use.acquisition'], method='uses - acquisition in this budget')
        g.add(prefix + '.per_unit', total_uses / budget['units_including_manager'], 'USD/home',
              deps=[prefix + '.total_uses'], method=f'uses / {budget["units_including_manager"]} homes including manager')
    o = data['operations']
    src = reference(o['source_id'], 14)
    expenses = []
    for key, amount in detail['expense_categories_usd'].items():
        raw, node = 'operations.reported_expense.' + key, 'operations.expense.' + key
        g.add(raw, amount, kind='reported_budget', source=src)
        g.add(node, D(amount) * g.values['assumptions.operating_expense_multiplier'],
              deps=[raw, 'assumptions.operating_expense_multiplier'], method='expense category * multiplier; revenue response held fixed')
        expenses.append(node)
    base_expenses = g.total('operations.base_expenses', expenses)
    for key in ['tenant_rents_usd', 'pbv_assistance_usd', 'other_income_usd', 'vacancy_tenant_usd',
                'vacancy_pbv_usd', 'ground_rent_usd', 'bond_fees_usd', 'replacement_reserve_deposit_usd',
                'hard_debt_service_usd', 'below_line_fees_usd', 'separate_hsh_services_usd']:
        g.add('operations.' + key, o[key], kind='reported_budget',
              source=reference(o['source_id'], 10) if key == 'separate_hsh_services_usd' else src)
    g.add('operations.reported_losp', o['losp_usd'], kind='reported_budget', source=src)
    losp = g.add('operations.losp', D(o['losp_usd']) * g.values['assumptions.losp_multiplier'],
                 deps=['operations.reported_losp', 'assumptions.losp_multiplier'], method='full-year operating support * multiplier; capital sources unchanged')
    gross_deps = ['operations.tenant_rents_usd', 'operations.pbv_assistance_usd', 'operations.other_income_usd', 'operations.losp']
    gross = g.total('operations.gross_income', gross_deps)
    raw_egi = gross - o['vacancy_tenant_usd'] - o['vacancy_pbv_usd']
    g.add('operations.egi_before_bridge', raw_egi,
          deps=['operations.gross_income', 'operations.vacancy_tenant_usd', 'operations.vacancy_pbv_usd'], method='gross income - displayed vacancy deductions')
    historical_raw_egi = sum(o[k] for k in ['tenant_rents_usd', 'pbv_assistance_usd', 'losp_usd', 'other_income_usd']) - o['vacancy_tenant_usd'] - o['vacancy_pbv_usd']
    egi_bridge = g.add('operations.egi_rounding_bridge', o['reported_egi_usd'] - historical_raw_egi,
                       kind='reconciliation', method='fixed difference between source reported EGI and displayed revenue-row arithmetic', source=src)
    egi = g.add('operations.egi', raw_egi + egi_bridge, deps=['operations.egi_before_bridge', 'operations.egi_rounding_bridge'],
                method='row arithmetic + disclosed historical rounding bridge')
    fixed = g.total('operations.fixed_deductions', ['operations.ground_rent_usd', 'operations.bond_fees_usd', 'operations.replacement_reserve_deposit_usd'])
    deductions = g.total('operations.total_deductions', ['operations.base_expenses', 'operations.fixed_deductions'])
    historical_deductions = o['expenses_before_reserves_usd'] + o['ground_rent_usd'] + o['bond_fees_usd'] + o['replacement_reserve_deposit_usd']
    noi_bridge = g.add('operations.noi_rounding_bridge', o['reported_noi_usd'] - (o['reported_egi_usd'] - historical_deductions),
                       kind='reconciliation', method='fixed source reported NOI minus reported EGI less deductions', source=src)
    noi = g.add('operations.noi', egi - deductions + noi_bridge,
                deps=['operations.egi', 'operations.total_deductions', 'operations.noi_rounding_bridge'], method='EGI - expenses/reserves/ground rent/bond fees + disclosed bridge')
    debt = g.values['operations.hard_debt_service_usd']
    if debt <= 0:
        raise ValueError('Coverage ratio needs positive scheduled debt service')
    g.add('operations.dscr', noi / debt, 'ratio', deps=['operations.noi', 'operations.hard_debt_service_usd'], method='agency-defined NOI / scheduled hard debt service')
    cash = g.add('operations.cashflow', noi - debt, deps=['operations.noi', 'operations.hard_debt_service_usd'], method='NOI - hard debt service')
    g.add('operations.residual_receipts', cash - o['below_line_fees_usd'],
          deps=['operations.cashflow', 'operations.below_line_fees_usd'], method='cash flow - below-line fees; negative result is a shortfall, not a distributable receipt')
    screen = detail['coverage_screen']
    threshold = g.add('operations.minimum_dscr', screen['minimum_year_one_dscr'], 'ratio', 'historical_screen', source=reference(screen['source_id'], screen['pdf_page']))
    g.add('operations.coverage_headroom', noi - threshold * debt,
          deps=['operations.noi', 'operations.minimum_dscr', 'operations.hard_debt_service_usd'], method='NOI - selected minimum ratio * scheduled debt')
    g.add('operations.income_needed_for_coverage', max(D(0), threshold * debt - noi),
          deps=['operations.coverage_headroom'], method='max(0, -coverage headroom); required income is not an available subsidy')
    g.total('operations.building_plus_separate_services', ['operations.base_expenses', 'operations.separate_hsh_services_usd'], method='building expenses + separate PSH services; embedded services already inside building expenses')
    schedule = o['losp_schedule']
    ssrc = reference(o['source_id'], schedule['pdf_page'])
    g.add('schedule.reported_first_year', schedule['first_year_disbursement_usd'], kind='reported_budget', source=ssrc)
    g.add('schedule.pro_rata_first_year', D(o['losp_usd']) * schedule['first_year_months'] / 12,
          kind='calculation', method='historical full-year support * 5/12; historical schedule not revised by diagnostic', source=ssrc)
    rounded = g.values['schedule.pro_rata_first_year'].quantize(D(1), rounding=ROUND_HALF_UP)
    g.add('schedule.pro_rata_minus_reported', rounded - schedule['first_year_disbursement_usd'],
          deps=['schedule.pro_rata_first_year', 'schedule.reported_first_year'], method='whole-dollar pro rata - printed first-year amount; unresolved discrepancy')
    g.add('schedule.reported_sum', sum(schedule['disbursements_usd']), kind='calculation', method='sum historical calendar-year disbursements; not revised diagnostic subsidy contract', source=ssrc)
    return g


def evaluate_reference(graph, contract):
    checks = []
    for target in contract['expected']:
        actual = graph.values[target['node']]
        if 'round_places' in target:
            actual = actual.quantize(D(1).scaleb(-target['round_places']), rounding=ROUND_HALF_UP)
        checks.append({**target, 'actual': str(actual), 'matched': actual == D(target['value'])})
    return {'type': contract['evaluation_type'], 'checks': checks,
            'matched': sum(c['matched'] for c in checks), 'total': len(checks),
            'status': 'reproduced_with_disclosed_discrepancies' if all(c['matched'] for c in checks) else 'mismatch'}


def impact(baseline, changed, change):
    if change is None:
        return {'assumption': None, 'affected_nodes': [], 'changed_nodes': [], 'unchanged_affected_nodes': []}
    affected = {'assumptions.' + change['assumption']}
    for key, node in changed.nodes.items():
        if affected.intersection(node['dependencies']):
            affected.add(key)
    differences = []
    for key in sorted(changed.nodes):
        if baseline.values[key] != changed.values[key]:
            differences.append({'node': key, 'before': baseline.nodes[key]['value'],
                                'after': changed.nodes[key]['value'],
                                'delta': value_string(changed.values[key] - baseline.values[key], changed.nodes[key]['unit']),
                                'unit': changed.nodes[key]['unit']})
    if any(x['node'] not in affected for x in differences):
        raise ValueError('Unexplained change outside dependency graph')
    return {'assumption': change['assumption'], 'affected_nodes': sorted(affected),
            'changed_nodes': differences,
            'unchanged_affected_nodes': sorted(affected - {x['node'] for x in differences})}


def decision(graph, data):
    ratio = graph.values['operations.dscr']
    threshold = graph.values['operations.minimum_dscr']
    capital_delta = graph.values['capital.2023.additional_unallocated_capital']
    cash = graph.values['operations.cashflow']
    return {
        'kind': 'conditional analyst screening; not agency disposition',
        'operating_screen': 'meets_selected_year_one_screen' if ratio >= threshold else 'below_selected_year_one_screen',
        'operating_summary': f'Year 1 coverage {ratio:.3f} versus historical screen {threshold}; cash flow after hard debt ${cash:,.2f}.',
        'income_needed_to_meet_screen_usd': money(graph.values['operations.income_needed_for_coverage']),
        'capital_screen': 'additional_funding_or_cost_revision_needed' if capital_delta > 0 else 'no_increase_over_reported_uses',
        'capital_summary': f'2023 uses change ${capital_delta:,.2f} with sources held fixed; original source-table residual retained separately.',
        'next_review': ('Review expense scope and recurring support with the operator/funder; re-underwrite operations before advancing this diagnostic.' if ratio < threshold
                        else 'Selected Year 1 coverage screen holds; still review long-run operations, funding conditions and source conflicts.'),
        'capital_next_review': ('Identify funding or revise scope; no new commitment is inferred.' if capital_delta > 0 else 'Confirm source status, restrictions, timing and remaining conditions.'),
        'project_feasibility': 'not_determined', 'professional_review': 'pending',
        'unresolved': data['unresolved'] + ['First partial-year LOSP amount differs from rounded five-twelfths of displayed annual support.'],
        'scope': '2023 capital and 2025 operations are distinct dated snapshots. No cross-vintage debt sizing or full 20-year result is inferred.'}


def assemble(data, detail, contract, changes):
    if not isinstance(changes, list) or any(change is None for change in changes):
        raise ValueError('Changes must be a list of non-null change objects')
    baseline = model(data, detail)
    score = evaluate_reference(baseline, contract)
    if score['status'] == 'mismatch':
        raise ValueError('Baseline fails the frozen reference contract')
    variants = [{'id': 'baseline', 'change': None, 'graph': baseline.nodes, 'decision': decision(baseline, data),
                 'impact': impact(baseline, baseline, None)}]
    ids = {'baseline'}
    for change in changes:
        change_contract(change)
        if change['id'] in ids:
            raise ValueError('Duplicate scenario id')
        ids.add(change['id'])
        graph = model(data, detail, change)
        variants.append({'id': change['id'], 'change': change, 'graph': graph.nodes,
                         'decision': decision(graph, data), 'impact': impact(baseline, graph, change)})
    source_map = {s['id']: {k: s[k] for k in ['url', 'document_date', 'sha256']}
                  for s in evidence.load('sources.json')['sources']}
    return {'model_version': MODEL_VERSION, 'reference_policy': contract['reference_policy'],
            'sources': source_map,
            'reference_evaluation': score, 'variants': variants}


def rows(result):
    metrics = [('2023 capital uses', 'capital.2023.total_uses'),
               ('Additional unallocated capital', 'capital.2023.additional_unallocated_capital'),
               ('2025 base operating expenses', 'operations.base_expenses'),
               ('2025 annual LOSP support', 'operations.losp'), ('2025 NOI', 'operations.noi'),
               ('Year 1 debt coverage', 'operations.dscr'), ('Cash flow after hard debt', 'operations.cashflow'),
               ('Income needed for 1.15 coverage', 'operations.income_needed_for_coverage')]
    return [[title] + [v['graph'][node]['value'] for v in result['variants']] for title, node in metrics]


def md_table(headers, values):
    return '\n'.join(['| ' + ' | '.join(map(str, headers)) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |']
                     + ['| ' + ' | '.join(map(str, row)) + ' |' for row in values])


def budget_tables(variant):
    """Selected complete capital summaries and operating expense categories."""
    graph = variant['graph']
    tables = []
    for year, sid, page in [('2020', 'predevelopment-2020', 4),
                            ('2022', 'preliminary-gap-2022', 5),
                            ('2023', 'board-packet-2023', 13)]:
        prefix = 'capital.' + year
        budget_rows = []
        for group in ['source', 'use']:
            for key, node in sorted(graph.items()):
                if key.startswith(prefix + '.' + group + '.'):
                    budget_rows.append([group, key.rsplit('.', 1)[-1].replace('_', ' '), node['value']])
        for key in ['total_sources', 'total_uses', 'reported_total', 'source_residual', 'total_excluding_land', 'per_unit']:
            budget_rows.append(['reconciliation', key.replace('_', ' '), graph[prefix + '.' + key]['value']])
        tables.append((year + ' capital budget', sid, page, ['Scope', 'Line', 'Amount (USD; per-unit row USD/home)'], budget_rows))
    expense_rows = [[key.rsplit('.', 1)[-1].replace('_', ' '), node['value']]
                    for key, node in sorted(graph.items()) if key.startswith('operations.expense.')]
    expense_rows.append(['Total base expenses', graph['operations.base_expenses']['value']])
    tables.append(('2025 base operating expenses', 'operating-subsidy-2025', 14, ['Category', 'Annual USD'], expense_rows))
    return tables


def reports(result):
    ids = [v['id'] for v in result['variants']]
    headers = ['Metric (USD except coverage)'] + ids
    intro = ('Known-case reconstruction of selected public budgets. Capital is a 2023 snapshot; operations are a 2025 full-year budget. '
             'Each scenario changes one declared assumption. Monetary lines round to cents before totals are calculated. Other inputs and both historical rounding bridges stay fixed. '
             'Source discrepancies and funding conditions remain unresolved. No full 20-year model or feasibility approval is claimed.')
    score = result['reference_evaluation']
    markdown = ['# Stanyan budget benchmark', '', intro, '',
                f'Frozen reference targets: **{score["matched"]}/{score["total"]} matched**; {score["status"]}. This is reproduction, not blind prediction.', '',
                md_table(headers, rows(result)), '', '## Reconstructed source budgets', '']
    for title, sid, page, columns, table_rows in budget_tables(result['variants'][0]):
        markdown += ['### ' + title, '', f'Source: [{sid}, PDF page {page}]({result["sources"][sid]["url"]}#page={page}).', '',
                     md_table(columns, table_rows), '']
    markdown += ['## Decision implications', '']
    sections = []
    for variant in result['variants']:
        d = variant['decision']
        rationale = variant['change']['rationale'] if variant['change'] else 'Source-budget reconstruction with all multipliers equal to 1.'
        paragraphs = [rationale, d['operating_summary'], d['capital_summary'], d['next_review'], d['capital_next_review'],
                      'Feasibility: not determined. Professional review: pending.']
        markdown += ['### ' + variant['id'], '']
        markdown += [text + '\n' for text in paragraphs]
        changes = variant['impact']['changed_nodes']
        if changes:
            markdown += [md_table(['Changed node', 'Before', 'After', 'Delta', 'Unit'],
                                 [[x[k] for k in ['node', 'before', 'after', 'delta', 'unit']] for x in changes]), '']
        sections.append((variant, paragraphs))
    markdown += ['## Reconciliation and interpretation', '',
                 '- Capital source rows differ from reported totals by +$1 (2020), -$1 (2022), -$1 (2023).',
                 '- The operating calculation carries explicit -$1 EGI and +$1 NOI reconciliation bridges; neither is hidden funding.',
                 '- Historical opening-year LOSP is $236,794; displayed annual support prorated to five months rounds to $236,795. The $11,720,975 historical schedule stays unchanged.',
                 '- Separate PSH services are added once for the combined scope; embedded services are already inside operating expenses.',
                 '- Reported source-budget amounts are not proof of committed funds, paid costs or realized operations.',
                 '- Each result node includes its inputs, method, type, unit and source locator in results.json. impact.csv lists numerical changes.',
                 '', '## Remaining source issues', '']
    markdown += ['- ' + x for x in result['variants'][0]['decision']['unresolved']]
    markdown += ['', '## Reproduction targets', '', md_table(['Node', 'Expected', 'Actual', 'Match', 'Source / PDF page'],
                  [[x['node'], x['value'], x['actual'], x['matched'], f'{x["source_id"]} / {x["pdf_page"]}'] for x in score['checks']]), '']
    def table(h, rs):
        return '<table><thead><tr>' + ''.join('<th>' + html.escape(str(x)) + '</th>' for x in h) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + html.escape(str(x)) + '</td>' for x in row) + '</tr>' for row in rs) + '</tbody></table>'
    body = ['<h1>Stanyan budget benchmark</h1>', '<p>' + html.escape(intro) + '</p>',
            f'<p><strong>{score["matched"]}/{score["total"]} frozen reference targets reproduced.</strong> Known-case reconstruction.</p>', table(headers, rows(result))]
    body += ['<h2>Reconstructed source budgets</h2>']
    for title, sid, page, columns, table_rows in budget_tables(result['variants'][0]):
        url = result['sources'][sid]['url'] + '#page=' + str(page)
        body += ['<details><summary>' + html.escape(title) + '</summary>',
                 '<p>Source: <a href="' + html.escape(url, quote=True) + '">' + html.escape(sid) + f', PDF page {page}</a></p>',
                 table(columns, table_rows), '</details>']
    for variant, paragraphs in sections:
        body += ['<h2>' + html.escape(variant['id']) + '</h2>']
        body += ['<p>' + html.escape(p) + '</p>' for p in paragraphs]
        impacts = variant['impact']['changed_nodes']
        if impacts:
            body += ['<details><summary>Changed calculations and values</summary>', table(['Node', 'Before', 'After', 'Delta', 'Unit'], [[x[k] for k in ['node', 'before', 'after', 'delta', 'unit']] for x in impacts]), '</details>']
        graph_rows = [[key, n['value'], n['unit'], n['kind'], ', '.join(n['dependencies']), n['method'], json.dumps(n['source'], sort_keys=True) if n['source'] else ''] for key, n in sorted(variant['graph'].items())]
        body += ['<details><summary>Step through inputs, methods and dependencies</summary>', table(['Node', 'Value', 'Unit', 'Kind', 'Inputs', 'Method', 'Source / PDF page'], graph_rows), '</details>']
    body += ['<h2>Source discrepancies remain visible</h2><ul><li>Capital source-table residuals: +$1 / -$1 / -$1.</li><li>Operating reconciliation bridges: -$1 EGI, +$1 NOI.</li><li>First-year LOSP: $236,794 reported versus $236,795 rounded pro rata.</li></ul>',
             '<h2>Unresolved evidence</h2><ul>' + ''.join('<li>' + html.escape(x) + '</li>' for x in result['variants'][0]['decision']['unresolved']) + '</ul>',
             '<p>See results.json, inputs/, source-bindings.json and manifest.json for the full local record. Run verify with the matching repository checkout.</p>']
    html_doc = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stanyan budget benchmark</title><style>body{font:16px/1.55 system-ui,sans-serif;max-width:1200px;margin:32px auto;padding:0 20px;color:#172b3a;background:#fafaf7}h1,h2{line-height:1.2}table{border-collapse:collapse;font-size:13px;width:100%;display:block;overflow:auto;margin:16px 0}th,td{border:1px solid #cdd5d8;padding:9px;text-align:left;vertical-align:top}th{background:#e5eeed}details{margin:14px 0;padding:12px;background:white;border:1px solid #cdd5d8}summary{cursor:pointer;font-weight:600}td{overflow-wrap:anywhere;min-width:70px}p{max-width:90ch}</style>' + ''.join(body) + '</html>'
    return '\n'.join(markdown), html_doc


def rendered_files(result):
    md, html_doc = reports(result)
    stream = io.StringIO()
    fields = ['scenario', 'node', 'before', 'after', 'delta', 'unit']
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for variant in result['variants'][1:]:
        for item in variant['impact']['changed_nodes']:
            writer.writerow({'scenario': variant['id'], **item})
    return {'results.json': canonical(result), 'report.md': md, 'report.html': html_doc, 'impact.csv': stream.getvalue()}


def bound_files():
    files = ['benchmark.py', 'validate.py', 'case-data.json', 'operating-detail.json',
             'reference-contract.json', 'sources.json', 'checks.json', 'comparison-baseline.json']
    files += [s[k] for s in evidence.load('sources.json')['sources'] for k in ['pdf', 'pages']]
    return {name: evidence.sha(HERE / name) for name in files}


def validate_inputs(data, detail, contract):
    evidence.validate_boundaries(data, evidence.load('sources.json'))
    if (detail['source_id'], detail['pdf_page'], detail['document_date'], detail['cash_flow_domain']) != ('operating-subsidy-2025', 14, '2025-05-02', 'annual_building_operations'):
        raise ValueError('Wrong operating-detail source or domain')
    categories = detail['expense_categories_usd']
    if any(type(x) is not int or x < 0 for x in categories.values()) or sum(categories.values()) != data['operations']['expenses_before_reserves_usd']:
        raise ValueError('Expense categories do not reconcile with reported expense budget')
    if categories.get('embedded_supportive_services') != data['operations']['services_embedded_in_building_expenses_usd']:
        raise ValueError('Embedded services scope changed')
    if detail['coverage_screen']['minimum_year_one_dscr'] != '1.15':
        raise ValueError('Historical Year 1 screen changed; requires a separately versioned method')
    pages = read(HERE / 'sources/operating-subsidy-2025.pages.json')
    evidence.numeric_anchors(pages[13], categories.values(), 'expense categories')
    ids = set()
    for target in contract['expected']:
        if target['node'] in ids:
            raise ValueError('Duplicate reference target')
        ids.add(target['node'])
    if not contract['evaluation_type'].startswith('known-case'):
        raise ValueError('Outcome exposure must remain disclosed')


def build(out, changes):
    evidence.validate()
    data, detail, contract = [read(HERE / name) for name in ['case-data.json', 'operating-detail.json', 'reference-contract.json']]
    validate_inputs(data, detail, contract)
    result = assemble(data, detail, contract, changes)
    out = destination(out, ROOT)
    out.mkdir(parents=True, exist_ok=False)
    (out / 'inputs').mkdir()
    inputs = {'case-data.json': data, 'operating-detail.json': detail, 'reference-contract.json': contract, 'changes.json': changes}
    for name, value in inputs.items():
        (out / 'inputs' / name).write_text(canonical(value))
    (out / 'source-bindings.json').write_text(canonical(bound_files()))
    for name, content in rendered_files(result).items():
        (out / name).write_text(content)
    manifest = {str(p.relative_to(out)): evidence.sha(p) for p in sorted(out.rglob('*')) if p.is_file()}
    (out / 'manifest.json').write_text(canonical({'model_version': MODEL_VERSION, 'files': manifest}))
    verify(out)
    return out


def verify(out):
    out = Path(out).resolve()
    manifest = read(out / 'manifest.json')
    if set(manifest) != {'model_version', 'files'} or manifest['model_version'] != MODEL_VERSION:
        raise ValueError('Unsupported run manifest')
    expected_paths = {'inputs/case-data.json', 'inputs/operating-detail.json', 'inputs/reference-contract.json',
                      'inputs/changes.json', 'source-bindings.json', 'results.json', 'report.md', 'report.html', 'impact.csv'}
    if set(manifest['files']) != expected_paths:
        raise ValueError('Unexpected manifest paths')
    actual = {str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()}
    if actual != expected_paths | {'manifest.json'}:
        raise ValueError('Missing or extra run files')
    for name, digest in manifest['files'].items():
        p = out / name
        if not p.resolve().is_relative_to(out) or p.is_symlink() or evidence.sha(p) != digest:
            raise ValueError('Changed run file: ' + name)
    evidence.validate()
    if read(out / 'source-bindings.json') != bound_files():
        raise ValueError('Source or implementation binding changed')
    for name in ['case-data.json', 'operating-detail.json', 'reference-contract.json']:
        if read(out / 'inputs' / name) != read(HERE / name):
            raise ValueError('Run changed the frozen source or reference input: ' + name)
    data, detail, contract, changes = [read(out / 'inputs' / n) for n in ['case-data.json', 'operating-detail.json', 'reference-contract.json', 'changes.json']]
    validate_inputs(data, detail, contract)
    result = assemble(data, detail, contract, changes)
    for name, content in rendered_files(result).items():
        if (out / name).read_text() != content:
            raise ValueError('Run differs from recomputation: ' + name)
    return {'status': 'passed', 'reference_targets': result['reference_evaluation']['total'],
            'scenarios': len(changes), 'scope': 'bounded reconstruction and static diagnostics; professional review pending'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    run = sub.add_parser('run')
    run.add_argument('--out', type=Path, required=True)
    run.add_argument('--change', type=Path)
    suite = sub.add_parser('suite')
    suite.add_argument('--out', type=Path, required=True)
    check = sub.add_parser('verify')
    check.add_argument('--run', type=Path, required=True)
    sub.add_parser('check', help='Read-only source and frozen-reference checks')
    args = parser.parse_args()
    if args.command == 'check':
        evidence.validate()
        data, detail, contract = [read(HERE / n) for n in ['case-data.json', 'operating-detail.json', 'reference-contract.json']]
        validate_inputs(data, detail, contract)
        evaluation = assemble(data, detail, contract, [])['reference_evaluation']
        print(canonical({'status': evaluation['status'], 'matched': evaluation['matched'], 'total': evaluation['total']}), end='')
    elif args.command == 'verify':
        print(canonical(verify(args.run)), end='')
    else:
        changes = ([read(args.change)] if args.change else []) if args.command == 'run' else [read(HERE / 'scenarios' / name) for name in ['opex-plus-10.json', 'without-losp.json', 'hard-cost-plus-10.json']]
        out = build(args.out, changes)
        print(canonical({'status': 'built_and_verified', 'run': str(out), 'report': str(out / 'report.html')}), end='')


if __name__ == '__main__':
    main()
