"""Readable projections of discovery evidence, assumptions and all lot routes. MIT."""
import csv
import html
import io
from .common import dumps

FIELDS = ['bbl','address','recorded_owner','recorded_building_class','recorded_landuse','rank_in_screen_pool','recorded_zoning','recorded_lot_area_sf','recorded_residential_units','baseline_recorded_far_proxy','proposed_far_assumption','additional_zoning_area_proxy_sf','additional_home_equivalents','public_or_institutional_signal','shortlisted','hold_reasons','flags']


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |'] + ['| '+' | '.join(str(x).replace('|','/').replace('\n',' ') for x in row)+' |' for row in rows])


def project(ir,request):
    by_id = {x['bbl']:x for x in ir['lots']}
    chosen = [by_id[x] for x in ir['shortlist']]
    headers = ['BBL / address','Recorded zoning','Lot sf','Recorded homes','Baseline FAR proxy','Assumed FAR','Incremental area proxy sf','Additional home-equivalents']
    rows = [[x['bbl']+' '+str(x['address']),x['recorded_zoning'],x['recorded_lot_area_sf'],x['recorded_residential_units'],x['baseline_recorded_far_proxy'],x['proposed_far_assumption'],x['additional_zoning_area_proxy_sf'],x['additional_home_equivalents']] for x in chosen]
    c = ir['counts']
    intro = f"{c['inventory']} recorded lots in the point-defined bbox; {c['screen_pool']} in the declared screen pool, {c['shortlist']} shortlisted, {c['held']} held with reasons. These are conditional investigation candidates; legal and financial viability remain unknown."
    lines = ['# Housing discovery: '+ir['request_id'],'',ir['question'],'',intro,'',
             '**Scenario assumption:** '+request['scenario']['label']+'. '+request['scenario']['rationale'],'',
             '**Baseline:** max of recorded residential FAR and recorded affordable residential FAR. Applicability is not determined. Gross building area is not subtracted from zoning area.','',
             '**Evidence:** this screening reads a retained inventory. Source retrieval times and queries are in '+ir.get('evidence_prefix','evidence')+'/receipts.json. Retrieval dates do not make every field current.','',
             table(headers,rows) if rows else 'No lots entered the shortlist under these settings. Inspect all-lots.csv and hold counts.','',
             '## Why lots were held','','Reason counts overlap: one lot can have several holds.',table(['Reason','Count'],list(c['by_hold_reason'].items())),'','## Shortlist review questions','']
    if ir.get('focus'):
        lines[4:4]=['**Current-use focus:** '+ir['focus']['label']+'. '+ir['focus']['rationale'],'']
    for x in chosen:
        projects = [p['project_id']+': '+str(p['project']['row'].get('project_status') if p['project'] else 'unknown') for p in x['zap_projects']]
        lines += [f"### {x['bbl']} — {x['address']}",'',
                  'Flags: '+(', '.join(x['flags']) or 'No implemented flags found; this is not clearance.'),
                  'ZAP project links: '+('; '.join(projects) or 'No rows returned in the bounded join; historic identity and collection limits still apply.'),
                  f"COLP use records: {len(x['colp_use_records'])}. Owner label: {x['recorded_owner']}; site control remains unknown.",
                  x['next_review'],'']
    lines += ['## Scope and limits','',ir['coverage']['scope_definition'],'',ir['methods']['rank'],''] + ['- '+x for x in ir['limits']]
    md = '\n'.join(lines)+'\n'
    def cell(value):return html.escape(str(value))
    def ht(h,rs):return '<div class="table"><table><tr>'+''.join('<th>'+cell(x)+'</th>' for x in h)+'</tr>'+''.join('<tr>'+''.join('<td>'+cell(x)+'</td>' for x in r)+'</tr>' for r in rs)+'</table></div>'
    body = '<h1>'+cell('Housing discovery: '+ir['request_id'])+'</h1><p>'+cell(ir['question'])+'</p><p>'+cell(intro)+'</p><p><strong>Exploratory assumption:</strong> '+cell(request['scenario']['rationale'])+'</p>'+ht(headers,rows)
    if ir.get('focus'):
        body='<p><strong>Current-use focus:</strong> '+cell(ir['focus']['label']+'. '+ir['focus']['rationale'])+'</p>'+body
    for x in chosen:
        body += '<details><summary>'+cell(x['bbl']+' '+str(x['address']))+'</summary><p>'+cell(x['next_review'])+'</p><pre>'+cell(dumps(x))+'</pre></details>'
    body += '<h2>Hold reasons</h2>'+ht(['Reason','Count'],list(c['by_hold_reason'].items()))+'<h2>Coverage and limits</h2><p>'+cell(ir['coverage']['scope_definition'])+'</p><ul>'+''.join('<li>'+cell(x)+'</li>' for x in ir['limits'])+'</ul><p>See all-lots.csv, request.json and '+cell(ir.get('evidence_prefix','evidence'))+'/receipts.json for the complete local record.</p>'
    page = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Housing discovery</title><style>body{font:16px/1.5 system-ui;max-width:1200px;margin:30px auto;padding:0 20px;color:#17303a;background:#fafaf7}.table{overflow:auto}table{border-collapse:collapse;font-size:13px;width:100%}td,th{padding:9px;border:1px solid #cdd5d8;text-align:left}th{background:#e5eeed}details{background:white;padding:12px;border:1px solid #cdd5d8;margin:12px 0}summary{cursor:pointer}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}</style>'+body+'</html>'
    stream = io.StringIO(); writer = csv.DictWriter(stream,fieldnames=FIELDS,lineterminator='\n');writer.writeheader()
    for row in ir['lots']:
        writer.writerow({k:('; '.join(row[k]) if isinstance(row[k],list) else row[k]) for k in FIELDS})
    return {'packet.md':md,'packet.html':page,'all-lots.csv':stream.getvalue()}
