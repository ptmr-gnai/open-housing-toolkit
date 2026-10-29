"""Deterministic packet and CSV projections of the same typed records. MIT."""
import csv
import html
import io
import re
from housing_workflow.contracts import dumps


def project(ir,reference):
    c={x['id']:x for x in ir['claims']}
    def val(cid):return c[cid]['value']
    lines=['# Conditional housing-program comparison: '+ir['site_bbl'],'',ir['question'],'',
           '**Illustrative programs; professional review pending. No overall ranking.**','',
           'Prices and reference schedules: **'+str(ir['price_year'])+'**, historical. No current-year or future-rent forecast.','',
           'The profiles are hypothetical households at published rounded income reference values. Counts below mean only that the stated cost threshold and exact bedroom category match. They are **not** counts of eligible households, available homes or achieved benefits.','',
           '## Stated objective','',ir['objective']['text']+' — supplied by '+ir['objective']['author'], '',
           '## Explicit offers and profile comparisons','',
           '| Program | Total proposed homes | '+ ' | '.join(p['label'] for p in ir['profiles'])+' | Delivery |',
           '| --- | --- | '+' | '.join('---' for _ in ir['profiles'])+' | --- |']
    for p in ir['programs']:
        lines.append('| '+p['label'].replace('|','/')+' | '+str(val(p['total_claim']))+' | '+' | '.join(str(val(x['homes_claim'])) for x in p['profile_counts'])+' | unknown |')
    lines += ['', 'These counts describe supplied offers. No known no-action baseline establishes net additions or an effect caused by intervention.', '', '## The visible tradeoff', '']
    a,b=ir['programs'];diff=val(ir['comparisons'][0]['claim'])
    lines.append(b['label']+' minus '+a['label']+': **'+str(diff)+' total proposed homes**.')
    lines.append('')
    for item in ir['comparisons'][1:]:
        p=next(p for p in ir['profiles'] if p['id']==item['profile_id'])
        lines.append('- '+p['label']+': '+str(val(item['claim']))+' homes meeting the diagnostic conditions.')
    lines += ['', 'These are separate dimensions. The module does not choose a winner or infer community preferences.', '', '## Household profiles','',
              '| Profile | Hypothetical annual income USD | Household size | Exact bedrooms | Monthly budget USD |','| --- | --- | --- | --- | --- |']
    for p in ir['profiles']:lines.append('| '+p['label'].replace('|','/')+' | '+val(p['annual_income_claim'])+' | '+str(p['household_size'])+' | '+str(p['bedrooms'])+' | '+val(p['monthly_budget_claim'])+' |')
    lines += ['', 'Budget = annual income × stated threshold / 100 / 12. Threshold: '+str(val('policy.cost_threshold_percent'))+'%. Burden percentages are displayed to six decimal places. Tests use the exact inequality before rounding.', '', '## Offer assumptions, restrictions and cost tests','',
              '| Program / bin | Homes | Bedrooms | Rent USD/month | Utilities USD/month | Gross USD/month | Proposed restriction years | Commitment |','| --- | --- | --- | --- | --- | --- | --- | --- |']
    for p in ir['programs']:
        for b in p['bins']:
            r=b['claims'];lines.append('| '+p['label'].replace('|','/')+' / '+b['id']+' | '+' | '.join(str(val(r[k])) for k in ['homes','bedrooms','monthly_rent_usd','tenant_utilities_usd','gross_monthly','restriction_years'])+' | proposed |')
    lines += ['', 'Restriction duration is a proposed input, not a promise of fixed rents over that period, a legal certification, or a forecast of household-years served. The exact-bedroom rule is a scoped comparison convention, not a suitability or eligibility determination.', '',
              '| Program / bin | Profile | Housing cost burden % | Cost test | Bedroom test | Both |','| --- | --- | --- | --- | --- | --- |']
    for p in ir['programs']:
        for b in p['bins']:
            for a in b['assessments']:
                lines.append('| '+p['id']+' / '+b['id']+' | '+a['profile_id']+' | '+' | '.join(str(val(a[k])) for k in ['burden_claim','cost_test_claim','bedroom_test_claim','combined_test_claim'])+' |')
    lines += ['', '## Unknowns and limits','']
    for x in ir['claims']:
        if x['kind']=='unknown':lines.append('- **'+x['label']+'**: '+x['rationale'])
    lines += ['']+['- '+x for x in ir['limitations']]
    m=reference['receipt']
    lines += ['', '## Reference and implementation scope','',
              'Foundation: [NYC Racial Equity Report submission guide]('+m['url']+'), Table 3, printed page 6; document stamp '+m['document_stamp']+'. The table contains rounded illustrative references. Rents shown there are context, not calculated regulatory rent ceilings or utility-adjusted program limits.', '',
              'Original PDF SHA256: `'+m['source_pdf_sha256']+'`. It is externally available and not bundled. The selected excerpt was checked against that PDF at preparation; ordinary offline replay parses the retained passages and receipt without re-extracting the external PDF. Source interpretation and current applicability still need review.', '',
              'Rent and income table vintages must match each other and the request price year. No compatibility override or inflation adapter is implemented.', '',
              '## Complete claim register','',
              'Each source fact has a passage/field reference; assumptions have rationales; derived claims have versioned methods and input IDs. All source excerpt, request and analysis bytes are bound in the manifest. Citations and byte checks do not establish complete coverage or professional acceptance.','']
    for x in ir['claims']:
        lines += ['### '+x['id'], '', '['+x['kind']+'] '+x['label']+': '+str(x['value'])+' '+x['unit'], '']
        if x['inputs']:lines += ['Inputs: '+', '.join(x['inputs'])+'.','']
        if x['method']:lines += ['Method: `'+x['method']+'`.','']
        if x['rationale']:lines += [x['rationale'],'']
        for ref in x['references']:lines += ['Reference: `'+dumps(ref).strip()+'`','']
    md='\n'.join(lines).rstrip()+'\n'
    # Escape every user/source string; HTML does not evaluate Markdown or request URLs.
    parts=[];table=False
    for line in lines:
        if line.startswith('|'):
            if not table:parts.append('<table>');table=True
            if set(line.replace('|','').replace(' ',''))=={'-'}:continue
            parts.append('<tr>'+''.join('<td>'+html.escape(x.strip())+'</td>' for x in line.strip('|').split('|'))+'</tr>');continue
        if table:parts.append('</table>');table=False
        if line.startswith('### '):parts.append('<h3>'+html.escape(line[4:])+'</h3>')
        elif line.startswith('## '):parts.append('<h2>'+html.escape(line[3:])+'</h2>')
        elif line.startswith('# '):parts.append('<h1>'+html.escape(line[2:])+'</h1>')
        elif line:parts.append('<p>'+re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',html.escape(line))+'</p>')
    if table:parts.append('</table>')
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Conditional housing-program comparison</title><style>body{font:17px/1.5 system-ui;max-width:1100px;margin:35px auto;padding:20px;color:#223542}table{border-collapse:collapse;display:block;overflow:auto}td{border:1px solid #cbd4dc;padding:8px}tr:first-child{background:#edf2f6}p{overflow-wrap:anywhere}h2{margin-top:2em}</style><main>'+''.join(parts)+'</main></html>\n'
    out=io.StringIO();w=csv.writer(out,lineterminator='\n');w.writerow(['claim_id','kind','value','unit','method','inputs','rationale','references'])
    def spreadsheet_safe(value):
        return "'"+value if isinstance(value,str) and value.lstrip().startswith(('=','+','-','@')) else value
    for x in ir['claims']:
        cells=[x['id'],x['kind'],x['value'],x['unit'],x['method'] or '',','.join(x['inputs']),x['rationale'] or '',dumps(x['references']).strip()]
        w.writerow([spreadsheet_safe(v) for v in cells])
    return {'packet.md':md,'packet.html':page,'claim-register.csv':out.getvalue()}
