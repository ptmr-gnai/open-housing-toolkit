"""Readable projections of report.json: a print-ready HTML memo and Markdown. MIT."""
from decimal import Decimal
from html import escape

STATUS_TEXT = {
    'within_recorded_residential_far': 'Within recorded residential FAR',
    'needs_affordable_housing_provisions': 'Above standard FAR; within the recorded affordable-housing FAR',
    'exceeds_recorded_far': 'Exceeds recorded FAR',
    'not_compared': 'Not compared',
    'matches_massing': 'Matches massing',
    'no_massing_with_same_gross_area': 'No massing with the same gross area',
    'no_massing_supplied': 'No massing supplied',
    'differs_from_massing': 'Differs from massing',
    'consistent_by_inspection': 'Consistent by inspection',
    'not_verified': 'Not verified',
}
DEBT_LABELS = {'dscr': 'Debt service coverage (income supports the payments)', 'loan_to_cost': 'Loan-to-cost limit',
               'loan_to_value': 'Loan-to-value limit', 'funding_need': 'Funding need (cost less other sources)', 'absolute': 'Absolute loan cap'}
PERSONA = {'housing_agency': 'Housing agency', 'developer': 'Developer', 'community': 'Community', 'other': 'General'}


def usd(value, cents=False):
    if value is None:
        return '—'
    d = Decimal(str(value))
    sign = '-' if d < 0 else ''
    d = abs(d)
    return sign + ('$' + format(d, ',.2f') if cents else '$' + format(d.quantize(Decimal('1')), ','))


def musd(value):
    if value is None:
        return '—'
    d = Decimal(str(value))
    return ('-' if d < 0 else '') + '$' + format(abs(d) / Decimal(1000000), '.1f') + 'M'


def num(value):
    if value in (None, ''):
        return '—'
    try:
        d = Decimal(str(value))
    except Exception:
        return str(value)
    return format(d, ',f') if d != d.to_integral_value() else format(d.to_integral_value(), ',')


def sqft(value):
    """Areas display to the nearest whole square foot; report.json keeps full precision."""
    if value in (None, ''):
        return '—'
    return format(Decimal(str(value)).quantize(Decimal('1')), ',')


def text(value):
    return STATUS_TEXT.get(value, value) if isinstance(value, str) else ('—' if value is None else str(value))


def summary_lines(r):
    h = r['headline']
    lo, hi = h['gap_range_usd']
    lines = ['Base case: %s homes in %s gross sf; total development cost %s; a modeled mortgage of %s.'
             % (h['homes'], num(h['gross_sf']), musd(h['total_development_cost_usd']), musd(h['modeled_loan_usd']))]
    lines.append('Year-1 yield on cost (net operating income ÷ total cost): %s in the base case, %s to %s across scenarios. '
                 'Developers usually compare this with prevailing capitalization rates; no benchmark is applied here.'
                 % (pct(h['base_yield_on_cost']), pct(h['yield_on_cost_range'][0]), pct(h['yield_on_cost_range'][1])))
    if Decimal(h['base_gap_usd']) > 0:
        lines.append('The rents support a mortgage covering %s of cost; after declared equity, %s remains to be filled by more equity, subsidy or lower cost.'
                     % (pct(h['base_loan_to_cost']), musd(h['base_gap_usd'])))
    else:
        lines.append('The declared sources cover the base-case cost under these assumptions.')
    lines.append('%s of %s tested scenarios leave a gap (range %s to %s).'
                 % (h['scenarios_with_gap'], h['scenarios'], musd(lo), musd(hi)))
    z = r['zoning']
    if z['massing_comparison']:
        parts = ['%s stories: %s' % (m['stories'], text(m['status']).lower()) for m in z['massing_comparison']]
        lines.append('Zoning check against recorded FAR: ' + '; '.join(parts) + '.')
    if r['ownership'] and r['ownership']['latest_recorded_deed']:
        d = r['ownership']['latest_recorded_deed']
        lines.append('Latest recorded deed: %s, recorded amount %s.' % (d['recorded_date'], usd(d['recorded_amount_usd'])))
    return lines


# ---------------------------------------------------------------- HTML

CSS = """
:root{--ink:#1d2327;--muted:#5b6670;--rule:#d8dde2;--band:#f3f5f7;--accent:#1f5f8b;--warn:#8a5a00;--bg:#fff}
@media (prefers-color-scheme: dark){:root{--ink:#e6e9ec;--muted:#a3adb6;--rule:#3a4148;--band:#22272c;--accent:#7fb6dd;--warn:#e0b25a;--bg:#15191c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,Segoe UI,Helvetica,Arial,sans-serif}
main{max-width:980px;margin:0 auto;padding:32px 20px 64px}
header{border-bottom:3px solid var(--accent);padding-bottom:14px;margin-bottom:22px}
h1{margin:4px 0 6px;font-size:28px;line-height:1.2}h2{font-size:19px;margin:34px 0 10px;padding-top:8px;border-top:1px solid var(--rule)}
h3{font-size:15px;margin:18px 0 6px}.meta{color:var(--muted);font-size:13px}
.summary{background:var(--band);border-left:4px solid var(--accent);padding:14px 18px;margin:12px 0}
.summary ul{margin:6px 0 0;padding-left:18px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0}
.kpi{border:1px solid var(--rule);padding:10px 12px}.kpi b{display:block;font-size:20px}.kpi span{color:var(--muted);font-size:12px}
table{width:100%;border-collapse:collapse;margin:8px 0 4px;font-size:13.5px}
th,td{padding:6px 8px;border-bottom:1px solid var(--rule);text-align:left;vertical-align:top}
th{background:var(--band);font-weight:600}td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
table.kv th{width:28%;background:none}tr.total td{font-weight:700;border-top:2px solid var(--ink)}tr.base td{background:var(--band);font-weight:600}
td.i1{padding-left:22px}.path{font-size:14px}.note{color:var(--muted);font-size:12.5px}.warn{color:var(--warn)}
.scroll{overflow-x:auto}figure{margin:12px 0}figure img{max-width:100%;border:1px solid var(--rule);background:#fff}
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}
figcaption{color:var(--muted);font-size:12.5px}code{font-size:12px;word-break:break-all}
@media print{@page{@bottom-center{content:"Open Housing Toolkit · github.com/ptmr-gnai/open-housing-toolkit";font-size:9px;color:#5b6670}}body{font-size:11.5px}main{max-width:none;padding:0}h2{break-after:avoid}table,figure{break-inside:avoid}.kpi b{font-size:16px}}
"""


def esc(value):
    return escape(text(value))


def table(head, rows, numeric=(), classes=None):
    if head is None:
        body = ''.join('<tr><th>%s</th>%s</tr>' % (row[0], ''.join('<td>%s</td>' % c for c in row[1:])) for row in rows)
        return '<div class="scroll"><table class="kv"><tbody>%s</tbody></table></div>' % body
    h = ''.join('<th class="n">%s</th>' % escape(c) if i in numeric else '<th>%s</th>' % escape(c) for i, c in enumerate(head))
    body = []
    for k, row in enumerate(rows):
        cls = (classes or [None] * len(rows))[k]
        cells = ''.join('<td class="n">%s</td>' % c if i in numeric else '<td>%s</td>' % c for i, c in enumerate(row))
        body.append('<tr%s>%s</tr>' % (' class="%s"' % cls if cls else '', cells))
    return '<div class="scroll"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, ''.join(body))


def embed(run, path):
    """Inline a figure so the report is one self-contained file (email, preview, PDF)."""
    import base64
    from pathlib import Path
    target = Path(run) / path
    if run is None or not target.exists():
        return escape(path)
    kind = {'.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}.get(target.suffix.lower())
    if not kind:
        return escape(path)
    return 'data:%s;base64,%s' % (kind, base64.b64encode(target.read_bytes()).decode('ascii'))


STEP_STATUS = {'ran': '✓', 'not_run': '—'}
ACTIVITY_TEXT = {'active_development': 'Active development recorded', 'site_preparation': 'Site preparation (fence)',
                 'none_found': 'None found', 'not_checked': 'Not checked'}
PATH_TEXT = {'housing_permitted_by_general_use_rule': 'housing allowed in principle', 'rezoning_path': 'rezoning path',
             'special_or_unresolved_review': 'special review'}


def _stories_for(r, gross_sf):
    for m in r['massing']:
        if abs(Decimal(str(m['totals_sf']['gross'])) - Decimal(str(gross_sf))) <= 1:
            return m['stories']
    return None


def _tested(r):
    v = r['sensitivity']
    heights = ', '.join('%s stories (%s homes)' % (_stories_for(r, g['gross_sf']) or '?', g['homes']) for g in v['by_program'])
    base = next(x for x in v['scenarios'] if x['is_base_case'])
    return ('%s; %s financing scenarios. Base case: %s stories, %s per sf hard cost, %s income per home per month (apartments and shops), %s%% mortgage.'
            % (heights or 'program as modeled', len(v['scenarios']), _stories_for(r, base['gross_sf']) or '?',
               usd(base['hard_cost_per_gross_sf_usd']), usd(base['scheduled_income_per_home_month_usd']), _pct(base['interest_rate'])))


def _packages_text(paths):
    if not paths:
        return ''
    if len(paths) == 1:
        return paths[0]
    parent = paths[0].rsplit('/', 1)[0]
    return '%s/ (%s packages)' % (parent, len(paths)) if all(p.startswith(parent + '/') for p in paths) else '%s +%d' % (paths[0], len(paths) - 1)


AGENT_NOTE = '''<!--
For AI agents: this file is a site feasibility report produced by the Open Housing Toolkit
({repository}, commit {commit}). The complete typed report is embedded at the end of this
file as JSON, in the script element whose id is report-data. Every figure traces to a public record or a
user-approved assumption; the user's goal and decisions are in report-data.brief.
Evidence fingerprint: {fingerprint}. To verify or continue the work, get the evidence bundle
(a zip whose README.md shows the same fingerprint), clone the toolkit at that commit, run
scripts/preflight.py, then python -m housing_feasibility verify --run BUNDLE/report --html THIS_FILE.
If you only have this file, read report-data and the "About this report" section.
-->'''


def embedded_report(page):
    """Read the typed report back out of a report.html."""
    import json
    import re as _re
    found = _re.findall(r'^<script type="application/json" id="report-data">(.*?)</script>$', page, _re.S | _re.M)
    if len(found) != 1:
        raise ValueError('No single embedded report-data block found in this HTML')
    return json.loads(found[0])


def _json_block(r):
    import json
    return json.dumps(r, sort_keys=True, ensure_ascii=False, allow_nan=False).replace('</', '<\\/')


def html(r, run=None):
    req, h, s, br = r['request'], r['headline'], r['site'], r['brief']
    tk = r['provenance']['toolkit']
    repo = tk.get('repository') or 'https://github.com/ptmr-gnai/open-housing-toolkit'
    n = [0]

    def section(title, anchor=None):
        n[0] += 1
        return '<h2%s>%s. %s</h2>' % (' id="%s"' % anchor if anchor else '', n[0], escape(title))

    out = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
           '<meta name="generator" content="Open Housing Toolkit %s (%s)">' % (escape(tk.get('package_version') or ''), escape(repo)),
           '<title>%s</title><style>%s</style></head><body>' % (escape(req['title']), CSS),
           AGENT_NOTE.format(repository=repo, commit=tk.get('git_commit') or 'unknown', fingerprint=r['provenance']['evidence_fingerprint']),
           '<main>']
    out.append('<header><h1>%s</h1>'
               '<div class="meta">%s · %s, Block %s, Lot %s · BBL %s<br>Prepared %s by %s using the <a href="%s">Open Housing Toolkit</a></div></header>'
               % (escape(req['title']), esc(s['address']), esc(s['borough']), esc(s['block']),
                  esc(s['lot']), esc(s['bbl']), esc(req['prepared_on']), esc(req['prepared_by']), escape(repo)))
    out.append('<section class="summary"><b>Goal.</b> “%s”<ul>%s</ul></section>'
               % (escape(br['goal']), ''.join('<li>%s</li>' % escape(x) for x in summary_lines(r))))
    lo, hi = h['gap_range_usd']
    kpis = [(num(h['homes']), 'homes (base case)'), (num(h['gross_sf']) + ' sf', 'gross area'),
            (musd(h['total_development_cost_usd']), 'total development cost'), (musd(h['modeled_loan_usd']), 'modeled mortgage'),
            (pct(h['base_yield_on_cost']), 'year-1 yield on cost'), (pct(h['base_loan_to_cost']), 'mortgage as share of cost'),
            (musd(h['base_gap_usd']), 'remaining gap (base case)'), ('%s – %s' % (musd(lo), musd(hi)), 'gap across %s scenarios' % h['scenarios'])]
    out.append('<div class="kpis">%s</div>' % ''.join('<div class="kpi"><b>%s</b><span>%s</span></div>' % (escape(a), escape(b)) for a, b in kpis))

    # Brief: what was asked
    out.append(section('Brief'))
    rows = [['Goal (user’s words)', '“%s”' % escape(br['goal'])], ['Prepared for', esc(PERSONA[br['persona']])]]
    rows += [[escape(p['label']), escape(p['value'])] for p in br['provided']]
    se = r['search']
    if se:
        sel = se['selected']
        why = ' '.join(sel['why_user_words'])
        rows.append(['Selected site', '%s (BBL %s)%s%s' % (esc(s['address']), esc(s['bbl']),
                     ', candidate #%s of %s' % (sel['rank'], se['candidates_count']) if sel['rank'] else
                     (', recorded as already in development' if sel['held_back_as_in_development'] else ''),
                     ' — “%s”' % escape(why) if why else '')])
    rows.append(['What was tested', escape(_tested(r))])
    out.append(table(None, rows))

    # Process: what was done
    out.append(section('How we got here'))
    out.append('<p class="path">%s</p>' % ' → '.join(
        ('<b>%s</b>' if st['status'] == 'ran' else '<span class="note">%s</span>') % escape(st['label']) for st in r['process']['steps']))
    out.append(table(['Step', 'Ran', 'Result', 'Decisions', 'Package'],
                     [[escape(st['label']), STEP_STATUS[st['status']], esc(st['result']), str(st['decisions']) if st['decisions'] else '',
                       '<code>%s</code>' % escape(_packages_text(st['packages'])) if st['packages'] else '']
                      for st in r['process']['steps']], numeric=(3,)))
    for e in r['provenance']['extends']:
        out.append('<p>Continues the report “%s” (%s, evidence fingerprint <code>%s</code>).</p>'
                   % (escape(e['title']), esc(e['prepared_on']), esc(e['evidence_fingerprint'][:16])))
    if br['decisions']:
        out.append('<p class="note">%s decisions recorded; the full log is in <a href="#appendix-decisions">Appendix: decisions</a>.</p>' % len(br['decisions']))

    # Search block (optional)
    if se:
        out.append(section('Area search'))
        paths = se['nonhousing_by_zoning_path'] or {}
        out.append('<p>Search request: “%s” — %s tax lots in the area; %s recorded as nonhousing (%s). %s ranked as conversion candidates.</p>'
                   % (escape(se['question'] or ''), esc(se['lots_in_area']), esc(se['recorded_nonhousing_in_area']),
                      escape(', '.join('%s %s' % (v, PATH_TEXT.get(k, k.replace('_', ' '))) for k, v in paths.items())),
                      esc(se['candidates_count'])))
        act = se.get('activity')
        if act:
            out.append('<p><b>Development activity check</b> (permits since %s): %s of the ranked lots show active development and are '
                       'listed separately below%s.</p>' % (esc(act['since']), len(se['in_development']),
                       '; site preparation (a construction fence) is flagged' if act['counts'].get('site_preparation') else ''))
            if act['coverage_gaps']:
                out.append('<p class="warn">⚠ Coverage gap: %s published no rows for this borough, so it could not contribute.</p>'
                           % escape('; '.join(act['coverage_gaps'])))
        head = ['#', 'Address', 'Class', 'Lot sf', 'Built FAR', 'Recorded res. FAR', 'Unused res. floor area', 'Station'] + (['Activity'] if act else [])
        out.append(table(head,
                         [['<b>%s</b>' % c['rank'] if c['bbl'] == s['bbl'] else str(c['rank']), ('<b>%s</b>' if c['bbl'] == s['bbl'] else '%s') % escape(c['address']),
                           esc(c['building_class']), num(c['lot_area_sf']), num(c['built_far']), num(c['recorded_residential_far']),
                           num(c['unused_residential_floor_area_sf']) + ' sf', '%s m, %s' % (c['station_m'], escape(c['nearest_station'] or ''))]
                          + ([escape(ACTIVITY_TEXT.get(c.get('development_activity'), ''))] if act else [])
                          for c in se['top_candidates']], numeric=(3, 4, 5, 6),
                         classes=['base' if c['bbl'] == s['bbl'] else None for c in se['top_candidates']]))
        if se['in_development']:
            out.append('<h3>Already in development (not ranked)</h3>')
            out.append(table(['Address', 'Lot sf', 'Recorded activity'],
                             [[('<b>%s</b>' if c['bbl'] == s['bbl'] else '%s') % escape(c['address']), num(c['lot_area_sf']), escape(c['development_latest'] or '')]
                              for c in se['in_development']], numeric=(1,),
                             classes=['base' if c['bbl'] == s['bbl'] else None for c in se['in_development']]))
        sel = se['selected']
        if sel['held_back_as_in_development']:
            out.append('<p class="warn">⚠ The selected site is recorded as already in development; it was chosen knowingly (see decisions).</p>')
        if sel['rank'] and sel['rank'] > len(se['top_candidates']):
            out.append('<p>Selected site is candidate #%s.</p>' % sel['rank'])
        if sel['why_user_words']:
            out.append('<p><b>Why this site:</b> “%s”</p>' % escape(' '.join(sel['why_user_words'])))
        out.append('<p class="note">%s <a href="#appendix-candidates">All %s candidates</a>.</p>' % (escape(se['candidate_method'] or ''), se['candidates_count']))
        if sel['flags']:
            out.append('<p class="note">Selected site review flags: %s</p>' % escape(', '.join(f.replace('_', ' ') for f in sel['flags'])))

    out.append(section('Site'))
    da = s.get('development_activity')
    if da:
        cls = 'warn' if da['status'] in ('active_development', 'site_preparation') else 'note'
        out.append('<p class="%s"><b>Development activity:</b> %s%s (permits and filings since %s).</p>'
                   % (cls, escape(ACTIVITY_TEXT[da['status']]), ' — ' + escape(da['latest']) if da['latest'] else '', esc(da['since'])))
        if da['signals']:
            out.append(table(['Date', 'Record', 'Description', 'Reference'],
                             [[esc(x['date']), escape(x['what']), escape(x['description'] or ''), '<code>%s</code>' % esc(x['reference'])] for x in da['signals'][:8]]))
    out.append(table(['Fact', 'Value', 'Source'], [[escape(f['label']), escape(num(f['value']) + (' ' + f['unit'] if f['unit'] and f['unit'] not in ('FAR',) else '')
                                                    if f['unit'] else str(f['value'])), '<code>%s</code>' % escape(f['claim_id'])] for f in s['facts']]))

    o = r['ownership']
    if o:
        out.append(section('Ownership and transactions'))
        rows = [['Tax-roll owner label', esc(o['tax_roll_owner_label'])]]
        deed = o['latest_recorded_deed']
        if deed:
            rows += [['Latest recorded deed', '%s (dated %s, recorded %s)' % (esc(deed['document_type']), esc(deed['document_date']), esc(deed['recorded_date']))],
                     ['Recorded amount', esc(usd(deed['recorded_amount_usd'])) + ' <span class="note">recorded instrument amount, not an appraisal</span>'],
                     ['Parties', escape('; '.join('%s (%s)' % (p['name'], p['role']) for p in deed['parties']))],
                     ['ACRIS document', '<code>%s</code>' % esc(deed['document_id'])]]
        if o['latest_dof_sale']:
            rows.append(['Latest DOF sale', '%s on %s' % (esc(usd(o['latest_dof_sale']['sale_price_usd'])), esc(o['latest_dof_sale']['sale_date']))])
        rows.append(['Recorded instruments', escape(', '.join('%s %s' % (v, k) for k, v in o['instrument_counts'].items()))])
        rows.append(['Current owner', esc(o['current_owner_status']) + ' <span class="note">title research not performed</span>'])
        out.append(table(['Item', 'Record'], rows))
        for c in o['conflicts']:
            out.append('<p class="warn">⚠ %s</p>' % escape(c))

    z = r['zoning']
    out.append(section('Zoning'))
    zrows = [['District', esc(z['district']) + (' / ' + esc(z['second_district']) if z['second_district'] else '')],
             ['Commercial overlay', esc(z['overlay'])], ['Special district', esc(z['special_district'])],
             ['Lot area', num(z['lot_area_sf']) + ' sf'], ['Existing floor area / built FAR', '%s sf / %s' % (num(z['existing_floor_area_sf']), esc(z['built_far']))],
             ['Recorded max residential FAR', esc(z['recorded_residential_far'])], ['Recorded max commercial FAR', esc(z['recorded_commercial_far'])],
             ['Recorded max community-facility FAR', esc(z['recorded_community_facility_far'])]]
    if z['recorded_affordable_residential_far']:
        zrows.append(['Recorded residential FAR with affordable-housing provisions', esc(z['recorded_affordable_residential_far'])])
    out.append(table(['Item', 'Value'], zrows))
    if z['capacity_calculations']:
        out.append(table(['Indicative capacity', 'Floor area', 'Formula'],
                         [[escape(c['label']), num(c['value_sf']) + ' sf', escape(c['formula'])] for c in z['capacity_calculations']], numeric=(1,)))
    if z['massing_comparison']:
        out.append(table(['Massing', 'Stories', 'Gross sf', 'Residential sf', 'Residential FAR (proxy)', 'Check'],
                         [[esc(m['massing_id']), esc(m['stories']), num(m['gross_sf']), num(m['residential_sf']), esc(m['residential_far_proxy']), esc(m['status'])]
                          for m in z['massing_comparison']], numeric=(1, 2, 3, 4)))
    out.append('<p class="note">%s</p>' % escape(' '.join(z['caveats'])))

    if r['massing']:
        out.append(section('Proposed program and massing'))
        for m in r['massing']:
            out.append('<h3>%s stories, %s ft — %s</h3>' % (esc(m['stories']), esc(m['total_height_ft']), esc(m['id'])))
            figs = ''.join('<figure><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>'
                           % (embed(run, p), escape(k), 'Schematic massing (assumed)' if k == 'massing.svg' else 'Plan (assumed footprint on mapped parcel)')
                           for k, p in m['figures'].items())
            if figs:
                out.append('<div class="figs">%s</div>' % figs)
            out.append(table(['Floor', 'Base ft', 'Top ft', 'Gross sf', 'Non-residential sf', 'Residential sf'],
                             [[esc(f['floor_id']), num(f['base_z_ft']), num(f['top_z_ft']), sqft(f['gross_floor_proxy_sf']), sqft(f['nonresidential_proxy_sf']), sqft(f['residential_proxy_sf'])]
                              for f in m['floors']] + [['<b>Total</b>', '', '', num(m['totals_sf']['gross']), num(m['totals_sf']['nonresidential']), num(m['totals_sf']['residential'])]],
                             numeric=(1, 2, 3, 4, 5)))
            out.append('<p class="note">%s · %s · area check: %s</p>' % (esc(m['design_status']), esc(m['mapped_containment']), escape(', '.join(m['area_reconciliation']))))
        bad = [x for x in r['program_reconciliation'] if x['status'] != 'matches_massing']
        if bad:
            out.append('<p class="warn">⚠ %s financial scenario(s) have no massing with the same gross area: %s</p>'
                       % (len(bad), escape(', '.join(x['underwriting_id'] for x in bad))))

    b = r['development_budget']
    out.append(section('Development budget (sources and uses)'))
    out.append('<p>Base case <code>%s</code>: %s homes, %s gross sf.</p>' % (esc(b['base_case_id']), esc(b['homes']), num(b['gross_sf'])))
    uses = [[escape(u['label']), usd(u['amount_usd']), escape(u['basis_kind'] or '')] for u in b['uses'] if Decimal(u['amount_usd']) != 0]
    uses.append(['Total uses', usd(b['total_uses_usd']), '%s per home · %s per gross sf' % (usd(b['cost_per_home_usd']), usd(b['cost_per_gross_sf_usd']))])
    out.append('<h3>Uses</h3>' + table(['Use', 'Amount', 'Basis'], uses, numeric=(1,), classes=[None] * (len(uses) - 1) + ['total']))
    src = [[escape(x['label']), escape(x['status']), usd(x['amount_usd'])] for x in b['sources']]
    src.append(['Total identified sources', '', usd(b['total_sources_usd'])])
    src.append(['<b>Remaining gap</b> (more equity, subsidy or lower cost)', '', '<b>%s</b>' % usd(b['gap_usd'])])
    out.append('<h3>Sources</h3>' + table(['Source', 'Status', 'Amount'], src, numeric=(2,), classes=[None] * (len(src) - 2) + ['total', None]))
    out.append(table(['Metric', 'Value', 'Formula'], [['Year-1 net operating income', usd(b['year1_noi_usd']), ''],
                                                      ['Yield on cost', pct(b['yield_on_cost']), escape(b['metric_formulas']['yield_on_cost'])],
                                                      ['Loan to cost', pct(b['loan_to_cost']), escape(b['metric_formulas']['loan_to_cost'])],
                                                      ['Gap to cost', pct(b['gap_to_cost']), escape(b['metric_formulas']['gap_to_cost'])]], numeric=(1,)))
    out.append('<p class="note">Gap = %s Typical private deals fill part of it with investor equity; affordable deals with public subsidy and tax credits. Neither is assumed here.</p>' % escape(b['gap_formula']))

    p = r['operating_pro_forma']
    out.append(section('Operating pro forma'))
    head = ['Line'] + ['Year %s (%s)' % (y, c) for y, c in zip(p['years'], p['calendar_years'])]
    rows, classes = [], []
    for row in p['rows']:
        vals = [('—' if v is None else (usd(v) if row['kind'] == 'money' else v)) for v in row['values']]
        rows.append([escape(row['label'])] + vals)
        classes.append('total' if row['indent'] == 0 and row['kind'] == 'money' and row['label'].startswith(('Net', 'Effective')) else None)
    out.append(table(head, rows, numeric=tuple(range(1, len(head))), classes=classes))
    out.append('<p class="note">%s Coverage shortfall years: %s.</p>' % (escape(p['price_basis'] or ''), escape(', '.join(map(str, p['coverage_breach_years'])) or 'none')))

    g = r['debt_sizing']
    out.append(section('Debt sizing'))
    out.append(table(['Constraint', 'Loan it allows'], [[escape(DEBT_LABELS.get(k, k.replace('_', ' '))) + (' <b>(binding)</b>' if k in g['binding_constraints'] else ''), usd(v)]
                                                     for k, v in g['constraints_usd'].items()], numeric=(1,)))
    out.append('<p>Modeled loan <b>%s</b> at %s%% interest, %s-year amortization, required coverage %s×. %s</p>'
               % (usd(g['loan_usd']), esc(_pct(g['interest_rate'])), esc(g['amortization_years']), esc(g['required_dscr']),
                  escape(' '.join(g['missing_checks']))))

    v = r['sensitivity']
    out.append(section('Sensitivity'))
    out.append(table(['Program', 'Homes', 'Scenarios', 'Yield on cost', 'Remaining gap'],
                     [['%s stories, %s gsf' % (_stories_for(r, x['gross_sf']) or '?', num(x['gross_sf'])) + (' (base case)' if x['includes_base_case'] else ''),
                       esc(x['homes']), esc(x['scenarios']), '%s – %s' % (pct(x['yield_on_cost_min']), pct(x['yield_on_cost_max'])),
                       '%s – %s' % (musd(x['gap_min_usd']), musd(x['gap_max_usd']))] for x in v['by_program']],
                     numeric=(1, 2, 3, 4), classes=['base' if x['includes_base_case'] else None for x in v['by_program']]))
    out.append('<p class="note">Ranges cover the tested hard costs, rents and interest rates. <a href="#appendix-scenarios">Every scenario</a>.</p>')

    rd = r['render']
    if rd:
        out.append(section('Visual concept'))
        if rd['image']:
            out.append('<figure><img src="%s" alt="Illustrative concept render"><figcaption>%s · %s · %s</figcaption></figure>'
                       % (embed(run, rd['image']), esc(rd['required_caption']), esc(rd['reference']['attribution']),
                          'Story count: ' + esc(rd['story_status'])))
            out.append(table(['Review check', 'Status', 'Note'], [[esc(c['id'].replace('_', ' ')), esc(c['status']), esc(c['note'])] for c in rd['review_checks']]))
        else:
            out.append('<p>Render brief prepared (<code>%s</code>); image not yet generated.</p>' % esc(rd['prompt']))

    out.append(section('Open items before a decision'))
    out.append(table(['Area', 'Item', 'Covered here'], [[esc(i['area']), esc(i['item']), esc(i['partly_addressed_by'] or '')] for i in r['open_items']]))
    out.append('<h2 id="about">About this report</h2>')
    out.append('<p>This report was produced with the <a href="%s">Open Housing Toolkit</a>, open-source tools an AI agent '
               '(Claude Code or Codex) uses to find New York City sites, research them from public records, sketch what could be built, '
               'test the finances and prepare renders. The agent runs the tools; the person makes every decision, and each one is '
               'recorded above in the user’s words.</p>' % escape(repo))
    out.append('<ul><li><b>Where the numbers come from.</b> Every figure is either copied from a public record (retrieved data is kept '
               'with a SHA-256 fingerprint, Appendix: sources) or an assumption the user approved (Appendix: decisions). Nothing is estimated '
               'by the report itself.</li>'
               '<li><b>Check it.</b> The evidence bundle (a zip sent with this report) holds every input. Its README shows the evidence '
               'fingerprint <code>%s</code>; if it matches, the bundle belongs to this report. Anyone can re-run the toolkit’s checks on it.</li>'
               '<li><b>Continue it.</b> Give the report and bundle to your own AI agent and ask it to verify the work or try a variation '
               '(other heights, rents, a render). It starts from <a href="%s">%s</a>.</li>'
               '<li><b>Machine-readable.</b> The full typed report is embedded in this file (<code>report-data</code>).</li></ul>'
               % (esc(r['provenance']['evidence_fingerprint']), escape(repo), escape(repo)))
    out.append('<p class="note">Toolkit %s, commit <code>%s</code>%s · report module %s.</p>'
               % (esc(tk.get('package_version')), esc((tk.get('git_commit') or 'unknown')[:12]),
                  ' (with uncommitted changes)' if tk.get('uncommitted_toolkit_changes') else '', esc(tk.get('report_module_version'))))
    out.append('<h2>Limits</h2><ul>%s</ul>' % ''.join('<li>%s</li>' % escape(x) for x in r['non_claims']))

    # Appendices
    letter = iter('ABCDEFG')
    if se:
        out.append('<h2 id="appendix-candidates">Appendix %s. All candidates from the area search</h2>' % next(letter))
        out.append('<p class="note">%s</p>' % escape(se['candidate_method'] or ''))
        out.append(table(['#', 'BBL', 'Address', 'Class', 'Lot sf', 'Built FAR', 'Res. FAR', 'Unused res. sf', 'Zoning path', 'Station', 'Owner label'],
                         [[str(c['rank']), esc(c['bbl']), escape(c['address']), esc(c['building_class']), num(c['lot_area_sf']), num(c['built_far']),
                           num(c['recorded_residential_far']), num(c['unused_residential_floor_area_sf']), escape(PATH_TEXT.get(c['zoning_path'], c['zoning_path'])),
                           '%s m' % c['station_m'], escape(c['owner_label'] or '')] for c in se['all_candidates']],
                         numeric=(4, 5, 6, 7), classes=['base' if c['bbl'] == s['bbl'] else None for c in se['all_candidates']]))
        if se['in_development']:
            out.append('<h3>Held back as already in development</h3>')
            out.append(table(['BBL', 'Address', 'Lot sf', 'Recorded activity'],
                             [[esc(c['bbl']), escape(c['address']), num(c['lot_area_sf']), escape(c['development_latest'] or '')] for c in se['in_development']], numeric=(2,)))
    out.append('<h2 id="appendix-scenarios">Appendix %s. Every financing scenario</h2>' % next(letter))
    out.append(table(['Scenario', 'Homes', 'Hard cost / gsf', 'Income / home / mo', 'Rate', 'Total cost', 'Yield on cost', 'Loan', 'Gap'],
                     [[esc(x['id']), esc(x['homes']), usd(x['hard_cost_per_gross_sf_usd']), usd(x['scheduled_income_per_home_month_usd']),
                       esc(_pct(x['interest_rate'])) + '%', musd(x['total_development_cost_usd']), pct(x['yield_on_cost']), musd(x['loan_usd']), musd(x['gap_usd'])]
                      for x in v['scenarios']], numeric=(1, 2, 3, 4, 5, 6, 7, 8),
                     classes=['base' if x['is_base_case'] else None for x in v['scenarios']]))
    out.append('<p class="note">%s</p>' % escape(v['note']))
    out.append('<h2 id="appendix-decisions">Appendix %s. Decisions</h2>' % next(letter))
    if br['decisions']:
        out.append(table(['Date', 'Step', 'Proposed', 'Answer (user’s words)'],
                         [[esc(d['decided_on']), esc(d['step']), escape(d['proposed']), '“%s”' % escape(d['answer'])] for d in br['decisions']]))
    else:
        out.append('<p class="note">No decisions were recorded in the brief.</p>')
    out.append('<h2 id="appendix-sources">Appendix %s. Sources and verification</h2>' % next(letter))
    out.append(table(['Source', 'Publisher / title', 'Retrieved', 'SHA-256'],
                     [['<a href="%s">%s</a>' % (escape(x['url'] or '#'), esc(x['id'])), esc(x['publisher']), esc((x['retrieved_at'] or '')[:19]),
                       '<code>%s</code>' % esc((x['sha256'] or '')[:16])] for x in r['sources']]))
    out.append(table(['Input package', 'Role', 'Manifest SHA-256'], [['<code>%s</code>' % esc(i['package']), esc(i['role']), '<code>%s</code>' % esc(i['manifest_sha256'][:16])] for i in r['inputs']]))
    out.append('<p class="note">Evidence fingerprint <code>%s</code> (%s). Each input was re-verified by its own module when this report was built '
               'and again by <code>python -m housing_feasibility verify</code>. The run brief is retained as <code>inputs/brief.json</code>.</p>'
               % (esc(r['provenance']['evidence_fingerprint']), escape(r['provenance']['fingerprint_method'])))
    out.append('</main>')
    out.append('<script type="application/json" id="report-data">%s</script>' % _json_block(r))
    out.append('</body></html>\n')
    return '\n'.join(out)


def pct(value):
    return '—' if value is None else format((Decimal(str(value)) * 100).quantize(Decimal('0.1')), 'f') + '%'


def _pct(rate):
    if rate is None:
        return '—'
    return format((Decimal(str(rate)) * 100).normalize(), 'f')


# ---------------------------------------------------------------- Markdown

def markdown(r):
    req, h, s, b, br = r['request'], r['headline'], r['site'], r['development_budget'], r['brief']
    n = [0]

    def section(title):
        n[0] += 1
        return ['', '## %s. %s' % (n[0], title), '']

    lines = ['# ' + req['title'], '',
             '%s · %s, Block %s, Lot %s · BBL %s  ' % (s['address'], s['borough'], s['block'], s['lot'], s['bbl']),
             'Prepared %s by %s using the [Open Housing Toolkit](%s)' % (req['prepared_on'], req['prepared_by'],
                                                                         r['provenance']['toolkit'].get('repository') or 'https://github.com/ptmr-gnai/open-housing-toolkit'), '',
             '**Goal.** “%s”' % br['goal'], '']
    lines += ['- ' + x for x in summary_lines(r)]
    lines += section('Brief') + ['- Prepared for: %s' % PERSONA[br['persona']]]
    lines += ['- %s: %s' % (p['label'], p['value']) for p in br['provided']]
    se = r['search']
    if se:
        sel = se['selected']
        lines += ['- Selected site: %s (BBL %s)%s%s' % (s['address'], s['bbl'],
                  ', candidate #%s of %s' % (sel['rank'], se['candidates_count']) if sel['rank'] else '',
                  ' — “%s”' % ' '.join(sel['why_user_words']) if sel['why_user_words'] else '')]
    lines += ['- What was tested: ' + _tested(r)]
    lines += section('How we got here')
    lines += [' → '.join(('**%s**' if st['status'] == 'ran' else '%s') % st['label'] for st in r['process']['steps']), '',
              '| Step | Ran | Result | Package |', '|---|---|---|---|']
    lines += ['| %s | %s | %s | %s |' % (st['label'], STEP_STATUS[st['status']], text(st['result']),
                                         '`%s`' % _packages_text(st['packages']) if st['packages'] else '') for st in r['process']['steps']]
    if se:
        lines += section('Area search')
        lines += ['“%s” — %s lots; %s recorded nonhousing; %s ranked candidates.' % (se['question'], se['lots_in_area'],
                  se['recorded_nonhousing_in_area'], se['candidates_count']), '',
                  '| # | Address | Class | Lot sf | Unused res. sf | Station |', '|---:|---|---|---:|---:|---|']
        lines += ['| %s | %s%s | %s | %s | %s | %s m |' % (c['rank'], c['address'], ' (selected)' if c['bbl'] == s['bbl'] else '',
                                                        c['building_class'], num(c['lot_area_sf']), num(c['unused_residential_floor_area_sf']), c['station_m'])
                  for c in se['top_candidates']]
        if se['in_development']:
            lines += ['', 'Already in development (not ranked): ' + '; '.join('%s (%s)' % (c['address'], c['development_latest']) for c in se['in_development'])]
        if se['selected']['why_user_words']:
            lines += ['', 'Why this site: “%s”' % ' '.join(se['selected']['why_user_words'])]
        lines += ['', se['candidate_method'] or '']
    lines += section('Site')
    if s.get('development_activity'):
        da = s['development_activity']
        lines += ['**Development activity:** %s%s (since %s).' % (ACTIVITY_TEXT[da['status']], ' — ' + da['latest'] if da['latest'] else '', da['since']), '']
    lines += ['| Fact | Value | Source |', '|---|---|---|']
    lines += ['| %s | %s | `%s` |' % (f['label'], f['value'], f['claim_id']) for f in s['facts']]
    o = r['ownership']
    if o:
        lines += section('Ownership and transactions')
        deed = o['latest_recorded_deed']
        lines += ['- Tax-roll owner label: %s' % text(o['tax_roll_owner_label'])]
        if deed:
            lines += ['- Latest recorded deed: %s, dated %s, recorded %s, recorded amount %s (not an appraisal)'
                      % (deed['document_type'], deed['document_date'], deed['recorded_date'], usd(deed['recorded_amount_usd'])),
                      '- Parties: ' + '; '.join('%s (%s)' % (p['name'], p['role']) for p in deed['parties'])]
        if o['latest_dof_sale']:
            lines += ['- Latest DOF sale: %s on %s' % (usd(o['latest_dof_sale']['sale_price_usd']), o['latest_dof_sale']['sale_date'])]
        lines += ['- Current owner: %s (title research not performed)' % o['current_owner_status']]
        lines += ['- Conflict: ' + c for c in o['conflicts']]
    z = r['zoning']
    lines += section('Zoning') + ['| Item | Value |', '|---|---|',
              '| District | %s |' % text(z['district']), '| Overlay | %s |' % text(z['overlay']),
              '| Lot area | %s sf |' % num(z['lot_area_sf']), '| Recorded residential FAR | %s |' % text(z['recorded_residential_far'])]
    lines += ['| %s | %s sf (%s) |' % (c['label'], num(c['value_sf']), c['formula']) for c in z['capacity_calculations']]
    lines += ['| Massing %s (%s stories) | %s |' % (m['massing_id'], m['stories'], text(m['status'])) for m in z['massing_comparison']]
    lines += ['', ' '.join(z['caveats'])]
    if r['massing']:
        lines += section('Proposed program and massing')
        for m in r['massing']:
            lines += ['- %s stories, %s ft (%s): %s gross sf, %s residential, %s non-residential; %s'
                      % (m['stories'], m['total_height_ft'], m['id'], num(m['totals_sf']['gross']), num(m['totals_sf']['residential']),
                         num(m['totals_sf']['nonresidential']), ', '.join(m['area_reconciliation']))]
            lines += ['  ![%s](%s)' % (k, p) for k, p in m['figures'].items()]
    lines += section('Development budget (base case `%s`)' % b['base_case_id']) + ['| Use | Amount |', '|---|---:|']
    lines += ['| %s | %s |' % (u['label'], usd(u['amount_usd'])) for u in b['uses'] if Decimal(u['amount_usd']) != 0]
    lines += ['| **Total uses** | **%s** |' % usd(b['total_uses_usd']), '', '| Source | Status | Amount |', '|---|---|---:|']
    lines += ['| %s | %s | %s |' % (x['label'], x['status'], usd(x['amount_usd'])) for x in b['sources']]
    lines += ['| **Remaining gap** | | **%s** |' % usd(b['gap_usd'])]
    lines += ['', 'Yield on cost %s · loan to cost %s · gap to cost %s' % (pct(b['yield_on_cost']), pct(b['loan_to_cost']), pct(b['gap_to_cost']))]
    p = r['operating_pro_forma']
    lines += section('Operating pro forma') + ['| Line | ' + ' | '.join('Year %s' % y for y in p['years']) + ' |',
                                               '|---|' + '---:|' * len(p['years'])]
    for row in p['rows']:
        lines.append('| %s | %s |' % (row['label'], ' | '.join('—' if v is None else (usd(v) if row['kind'] == 'money' else v) for v in row['values'])))
    g = r['debt_sizing']
    lines += section('Debt sizing')
    lines += ['- %s: %s%s' % (DEBT_LABELS.get(k, k), usd(val), ' (binding)' if k in g['binding_constraints'] else '') for k, val in g['constraints_usd'].items()]
    lines += ['- Modeled loan %s at %s%% interest, %s-year amortization, required coverage %sx. %s'
              % (usd(g['loan_usd']), _pct(g['interest_rate']), g['amortization_years'], g['required_dscr'], ' '.join(g['missing_checks']))]
    v = r['sensitivity']
    lines += section('Sensitivity') + ['| Program | Homes | Scenarios | Yield on cost | Remaining gap |', '|---|---:|---:|---:|---:|']
    lines += ['| %s stories, %s gsf%s | %s | %s | %s – %s | %s – %s |' % (_stories_for(r, x['gross_sf']) or '?', num(x['gross_sf']),
              ' (base case)' if x['includes_base_case'] else '', x['homes'], x['scenarios'], pct(x['yield_on_cost_min']),
              pct(x['yield_on_cost_max']), musd(x['gap_min_usd']), musd(x['gap_max_usd'])) for x in v['by_program']]
    rd = r['render']
    if rd:
        lines += section('Visual concept')
        if rd['image']:
            lines += ['![%s](%s)' % (rd['required_caption'], rd['image']), '', '%s · story count: %s' % (rd['reference']['attribution'], text(rd['story_status']))]
        else:
            lines += ['Render brief prepared (`%s`); image not yet generated.' % rd['prompt']]
    lines += section('Open items') + ['- **%s**: %s' % (i['area'], i['item']) for i in r['open_items']]
    lines += ['', '## About this report', '',
              'Produced with the [Open Housing Toolkit](%s), toolkit commit %s. Every figure is copied from a public record or an '
              'approved assumption. Evidence fingerprint: `%s` (matches the evidence bundle README). The typed report is report.json.'
              % (r['provenance']['toolkit'].get('repository'), r['provenance']['toolkit'].get('git_commit') or 'unknown',
                 r['provenance']['evidence_fingerprint'])]
    lines += ['', '## Limits', ''] + ['- ' + x for x in r['non_claims']]
    letter = iter('ABCDEFG')
    if se:
        lines += ['', '## Appendix %s. All candidates from the area search' % next(letter), '', se['candidate_method'] or '', '',
                  '| # | BBL | Address | Class | Lot sf | Unused res. sf | Station m | Owner label |', '|---:|---|---|---|---:|---:|---:|---|']
        lines += ['| %s | %s | %s | %s | %s | %s | %s | %s |' % (c['rank'], c['bbl'], c['address'], c['building_class'], num(c['lot_area_sf']),
                                                              num(c['unused_residential_floor_area_sf']), c['station_m'], c['owner_label'] or '')
                  for c in se['all_candidates']]
    lines += ['', '## Appendix %s. Every financing scenario' % next(letter), '',
              '| Scenario | Homes | Total cost | Yield on cost | Loan | Gap |', '|---|---:|---:|---:|---:|---:|']
    lines += ['| %s%s | %s | %s | %s | %s | %s |' % (x['id'], ' (base)' if x['is_base_case'] else '', x['homes'], musd(x['total_development_cost_usd']),
                                                    pct(x['yield_on_cost']), musd(x['loan_usd']), musd(x['gap_usd'])) for x in v['scenarios']]
    lines += ['', '## Appendix %s. Decisions' % next(letter), '']
    lines += ['| Date | Step | Proposed | Answer |', '|---|---|---|---|'] + ['| %s | %s | %s | “%s” |' % (d['decided_on'], d['step'], d['proposed'], d['answer'])
                                                                           for d in br['decisions']] if br['decisions'] else ['No decisions were recorded.']
    lines += ['', '## Appendix %s. Sources and verification' % next(letter), '', '| Source | Publisher / title | Retrieved | SHA-256 |', '|---|---|---|---|']
    lines += ['| [%s](%s) | %s | %s | `%s` |' % (x['id'], x['url'] or '#', text(x['publisher']), (x['retrieved_at'] or '')[:19], (x['sha256'] or '')[:16]) for x in r['sources']]
    lines += ['', 'Input packages: ' + ', '.join('`%s`' % i['package'] for i in r['inputs']) + '. Each was re-verified by its own module.', '']
    return '\n'.join(lines)
