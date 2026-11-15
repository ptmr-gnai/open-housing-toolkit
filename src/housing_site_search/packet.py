"""Reviewable scenario search, including every failed/unknown trial. MIT."""
import csv
import html
import io
import json


def project(req,result):
    by={x['id']:x for x in result['trials']};chosen=[by[x] for x in result['detailed_trial_ids']]
    headers=['BBL / address','Proposed homes','Assumed land $/lot sf','Required zoning FAR proxy','Unallocated capital/home','Station point distance m','Zoning path']
    rows=[[x['bbl']+' '+str(x['address']),x['proposed_homes'],x['assumed_land_usd_per_lot_sf'],x['required_zoning_far'],x['unallocated_capital_per_home_usd'],x['station_straight_line_m'],x['zoning_path']] for x in chosen]
    def mdtable(h,rs):return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('|','/').replace('\n',' ') for x in r)+' |' for r in rs])
    c=result['counts'];intro=f"{c['inventory_lots']} inventory lots retained; {c['recorded_nonhousing_lots']} recorded nonhousing lots; {c['trials']} explicit program/price trials. Matches are conditional search results, not viable-site estimates."
    lines=['# Housing site search: '+req['id'],'',req['question'],'',intro,'',result['meaning'],'','## Target outcomes','',mdtable(['Trial status','Count'],list(c['trials_by_status'].items())),'',mdtable(['Lot status','Count'],list(c['lots_by_status'].items())),'','## Selected scenarios for inspection','',mdtable(headers,rows) if rows else 'No scenarios met all declared targets with sufficient target evidence. All failed/unknown trials remain in trials.csv.','',result['pareto_method']]
    for x in chosen:lines+=['',f"- [{x['id']} detailed model](models/{x['id']}/packet.md)"]
    lines+=['','## Exact targets and scaling','', '```json',json.dumps(req,indent=2,sort_keys=True),'```','','## Scope and unresolved work','']+['- '+x for x in result['limits']]
    lines+=['','[Broad discovery](discovery/packet.md) retains source records, all use queues and zoning paths. [Financial template](underwriting-template/packet.md) retains input bases and references. Every inventory lot remains in all-lots.csv; every modeled scenario remains in trials.csv/results.json.','', 'Select explicit BBLs with the search handoff command. It verifies this package and uses the existing evidence-only parcel workflow; the model is not silently promoted to a lawful building program.']
    esc=lambda x:html.escape(str(x))
    def table(h,rs):return '<div class="scroll"><table><thead><tr>'+''.join('<th>'+esc(x)+'</th>' for x in h)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in r)+'</tr>' for r in rs)+'</tbody></table></div>'
    body='<h1>'+esc(req['id'])+'</h1><p>'+esc(req['question'])+'</p><p>'+esc(intro)+'</p><p>'+esc(result['meaning'])+'</p><h2>Scenario outcomes</h2>'+table(['Status','Count'],list(c['trials_by_status'].items()))+'<h2>Scenarios selected for inspection</h2>'+table(headers,rows)+'<p>'+esc(result['pareto_method'])+'</p>'
    for x in chosen:body+='<p><a href="models/'+esc(x['id'])+'/packet.html">'+esc(x['id'])+' detailed financial model</a></p>'
    body+='<h2>Limits</h2><ul>'+''.join('<li>'+esc(x)+'</li>' for x in result['limits'])+'</ul><p><a href="discovery/packet.html">Broad discovery and sources</a> · <a href="underwriting-template/packet.html">Financial template</a></p><details><summary>Exact targets and scaling assumptions</summary><pre>'+esc(json.dumps(req,sort_keys=True,indent=2))+'</pre></details>'
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Housing site search</title><style>body{font:16px/1.5 system-ui;max-width:1200px;margin:30px auto;padding:0 20px;background:#fafaf7;color:#17303a}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid #cdd5d8;padding:9px;text-align:left}th{background:#e5eeed}pre{white-space:pre-wrap;overflow-wrap:anywhere}details{padding:14px;background:white}</style>'+body+'</html>'
    output={'packet.md':'\n'.join(lines)+'\n','packet.html':page}
    for filename,items in [('all-lots.csv',result['lots']),('trials.csv',result['trials'])]:
        stream=io.StringIO();fields=list(dict.fromkeys(k for x in items for k in x)) if items else ['id','status'];writer=csv.DictWriter(stream,fieldnames=fields,lineterminator='\n');writer.writeheader()
        for row in items:writer.writerow({k:('; '.join(map(str,v)) if isinstance(v,list) else v) for k,v in row.items()})
        output[filename]=stream.getvalue()
    return output
