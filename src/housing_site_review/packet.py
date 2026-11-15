"""Review summary and complete lot/signal exports. MIT."""
import csv
import html
import io
from housing_site_discovery.packet import table


def project(ir,review):
    count=review['reviewed_recorded_nonhousing_lots']
    text=['# Cross-source dwelling review','',f'{count} recorded nonhousing lots reviewed. Every base inventory lot and its original classification remains retained.','',
          table(['Returned-field review','Lots'],review['counts'].items()),'',
          '**Interpretation:** positive historical unit fields or HPD registration/program records require reconciliation. No positive returned signal does not establish no housing, no occupants, vacancy or a clean site.','',
          '## Source coverage','']
    rows=[[name,status,n] for name,source in review['source_coverage'].items() for status,n in source['lots_by_status'].items()]
    text+=[table(['Source','Per-lot query status','Lots'],rows),'','## Positive returned signals','']
    examples=[]
    for row in ir['lots']:
        r=row.get('dwelling_review')
        if r and r['positive_signals']:examples.append([row['bbl'],row.get('address'),len(r['positive_signals'])])
    text+=[table(['BBL','Address','Returned housing signals'],examples), '',
           'See signals.csv and review.json for every exact source pointer, filing date/status and query coverage. Original packet and complete context remain under discovery/.','']
    text+=['- '+x for x in review['limits']]
    md='\n'.join(text)+'\n'
    body='<h1>Cross-source dwelling review</h1><p>'+html.escape(f'{count} recorded nonhousing lots reviewed; every original inventory lot retained.')+'</p><p>Historical housing-unit, registration or program records require reconciliation. No positive returned signal is not proof of no housing or occupants.</p><pre>'+html.escape(table(['Status','Lots'],review['counts'].items()))+'</pre><p><a href="discovery/packet.html">Original broad discovery</a> · <a href="all-lots.csv">All lots and review status</a> · <a href="signals.csv">Every positive field observation</a> · <a href="receipts.json">Query receipts</a></p><h2>Source coverage</h2><pre>'+html.escape(table(['Source','Status','Lots'],rows))+'</pre><h2>Positive-field lots</h2><pre>'+html.escape(table(['BBL','Address','Observations'],examples))+'</pre><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in review['limits'])+'</ul>'
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dwelling field review</title><style>body{font:16px/1.5 system-ui;max-width:1100px;margin:24px auto;padding:0 18px;color:#17303a;background:#fafaf7}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}a{color:#075c70}</style>'+body+'</html>'
    out=io.StringIO();writer=csv.writer(out,lineterminator='\n');writer.writerow(['bbl','address','current_use_category','recorded_nonhousing','review_status','positive_field_count','flags'])
    signal_out=io.StringIO();sw=csv.writer(signal_out,lineterminator='\n');sw.writerow(['bbl','address','provider','field','value','job_id','filing_status','filing_date','body_path','json_pointer','sha256','query_url'])
    for row in ir['lots']:
        r=row.get('dwelling_review');writer.writerow([row['bbl'],row.get('address'),row['current_use_category'],row['in_recorded_nonhousing_set'],r['status'] if r else 'not_in_recorded_nonhousing_review_universe',len(r['positive_signals']) if r else None,'; '.join(row['flags'])])
        if r:
            for signal in r['positive_signals']:
                ref=signal['reference'];sw.writerow([row['bbl'],row.get('address'),signal['provider'],signal['field'],signal['value'],signal['job_id'],signal['status'],signal['filing_date'],ref['body_path'],ref['pointer'],ref['sha256'],ref['url']])
    return {'packet.md':md,'packet.html':page,'all-lots.csv':out.getvalue(),'signals.csv':signal_out.getvalue()}
