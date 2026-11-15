"""Readable discovery groups and every retained lot. MIT."""
import csv
import html
import io
from .common import dumps

FIELDS=['bbl','address','current_use_category','building_class','landuse','recorded_unitsres',
        'recorded_lot_area_sf','recorded_residential_far','recorded_affordable_residential_far',
        'zoning_path','review_lane','review_order_in_group','flags','recorded_owner_label',
        'nearest_station_name','nearest_station_straight_line_m','ibz_point_relation','fast_track_positive_flags']


def table(headers,rows):
    def cell(v):return str(v).replace('|','/').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])


def project(ir,request,pack):
    counts=ir['counts'];groups={}
    for row in ir['lots']:
        if row['displayed_example']:
            key=row['zoning_path']['path']+' / '+row['review_lane']
            groups.setdefault(key,[]).append(row)
    intro=f"{counts['inventory']} recorded lots; {counts['recorded_nonhousing']} in the recorded nonhousing set. All other lots remain in visible housing or uncertainty queues. These counts are not viable-site estimates."
    text=['# Nonhousing site discovery: '+request['id'],'',request['question'],'',intro,'',
          '**Admission:** '+ir['admission_method'],'','**Order:** '+ir['order_method'],'',
          '## Inventory disposition','',table(['Current-use category','Count'],counts['by_current_use'].items()),'',
          '## General zoning paths for recorded nonhousing','',table(['Path','Count'],counts['nonhousing_by_zoning_path'].items()),'',
          'Housing-permitted means a general use rule allows residential use in principle. It does not establish a lawful building program. Rezoning-path means the recorded general district does not permit new housing under the implemented general rule; alternatives and exceptions remain review items.','',
          '## Examples by path and review lane','',
          'Displayed examples are a browsing sample. There is no hard ten-site shortlist; every recorded nonhousing lot is available for explicit follow-up.','']
    def esc(x):return html.escape(str(x))
    def ht(headers,rows):
        return '<div class="scroll"><table><thead><tr>'+''.join('<th>'+esc(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
    body='<h1>'+esc('Nonhousing site discovery: '+request['id'])+'</h1><p>'+esc(request['question'])+'</p><p>'+esc(intro)+'</p><p><strong>Admission:</strong> '+esc(ir['admission_method'])+'</p><p><strong>Browsing order:</strong> '+esc(ir['order_method'])+'</p><h2>Inventory disposition</h2>'+ht(['Current use','Count'],counts['by_current_use'].items())+'<h2>General zoning paths</h2>'+ht(['Path','Count'],counts['nonhousing_by_zoning_path'].items())+'<p>General use permission is not a parcel entitlement or a finding of buildable housing. Special and unresolved conditions remain visible.</p>'
    headers=['BBL / address','Class / use','Districts','Lot sf','Recorded residential FAR','Nearest station (straight-line m)','IBZ point relation','Review flags']
    for key,items in sorted(groups.items()):
        items.sort(key=lambda x:x['review_order_in_group'])
        rows=[[x['bbl']+' '+str(x['address']),x['building_class']+' / '+x['landuse'],', '.join(x['zoning_path']['recorded_districts']),x['recorded_lot_area_sf'],x['recorded_residential_far'], ((str(x['public_context']['nearest_station']['name'])+' / '+str(x['public_context']['nearest_station']['straight_line_m'])) if x['public_context']['nearest_station'] else 'unknown'),x['public_context']['industrial_zone_point_relation'],'; '.join(x['flags'])] for x in items]
        text+=['### '+key,'',table(headers,rows),'']
        body+='<h3>'+esc(key)+'</h3>'+ht(headers,rows)
        for x in items:
            body+='<details><summary>'+esc(x['bbl']+' '+str(x['address']))+'</summary><pre>'+esc(dumps(x))+'</pre></details>'
    text+=['## Coverage and limits','',ir['source_scope'],'',ir['zoning_coverage']['map_coverage'],'']+['- '+x for x in ir['limits']]
    body+='<h2>Coverage and limits</h2><p>'+esc(ir['source_scope'])+'</p><p>'+esc(ir['zoning_coverage']['map_coverage'])+'</p><ul>'+''.join('<li>'+esc(x)+'</li>' for x in ir['limits'])+'</ul>'
    text+=['','## Sources and trace','',
           'All-lots.csv and ir.json retain every lot, including unresolved and housing records. Inventory references resolve under evidence/inventory; supplemental references under evidence/. Source receipts retain exact queries and retrieval times. Retrieval dates do not make all fields current.','']
    body+='<h2>Sources and trace</h2><p><a href="all-lots.csv">Every lot (CSV)</a> · <a href="ir.json">Complete classification and references</a> · <a href="evidence/receipts.json">Zoning supplement receipts</a> · <a href="evidence/inventory/receipts.json">Original inventory receipts</a></p>'
    for source in pack['sources']:
        line=f"- [{source['id']}]({source['url']}), retrieved {source['retrieved_at']}, SHA-256 {source['sha256']}"
        text.append(line)
        body+='<p><a href="'+esc(source['url'])+'">'+esc(source['id'])+'</a>: '+esc(source['retrieved_at'])+'</p>'
    text+=['','Official source bytes are retained in guidance.json. Implemented rules are an attributed general-use interpretation, not agency endorsement or complete zoning analysis.','']
    body+='<p>Official source bytes are retained in guidance.json. These rules are a general-use interpretation, not agency endorsement or complete zoning analysis.</p>'
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nonhousing site discovery</title><style>body{font:16px/1.5 system-ui;color:#17303a;background:#fafaf7;max-width:1200px;margin:24px auto;padding:0 18px}h1,h2,h3{overflow-wrap:anywhere}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}td,th{border:1px solid #cdd5d8;text-align:left;padding:9px}th{background:#e5eeed}details{padding:10px;background:white;border:1px solid #cdd5d8;margin:10px 0}summary{cursor:pointer;overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}</style>'+body+'</html>'
    stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=FIELDS,lineterminator='\n');writer.writeheader()
    for row in ir['lots']:
        item={key:row.get(key) for key in FIELDS}
        station=row['public_context']['nearest_station'];gft=row['public_context']['green_fast_track']
        item.update(nearest_station_name=station['name'] if station else None,nearest_station_straight_line_m=station['straight_line_m'] if station else None,ibz_point_relation=row['public_context']['industrial_zone_point_relation'],fast_track_positive_flags='; '.join(gft['positive_publisher_flags']) if gft else None)
        item['zoning_path']=row['zoning_path']['path'];item['flags']='; '.join(row['flags']);writer.writerow(item)
    return {'packet.md':'\n'.join(text),'packet.html':page,'all-lots.csv':stream.getvalue()}
