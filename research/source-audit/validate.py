"""Fail closed on evidence corruption, response errors and join drift. MIT."""
import datetime,hashlib,json,pathlib
P=pathlib.Path(__file__).resolve().parent

def api_data(obj):
    if not isinstance(obj,(dict,list)) or (isinstance(obj,dict) and 'error' in obj):raise ValueError('Not a successful structured API payload')
    return obj

def validate():
    registry=json.loads((P/'registry.json').read_text());ledger=json.loads((P/'access-ledger.json').read_text());by_id={r['id']:r for r in ledger}
    assert 1<=len(registry['sources'])<=10
    assert len(by_id)==len(ledger)
    assert len({s['id'] for s in registry['sources']})==len(registry['sources'])
    for r in ledger:
        if r.get('sha256'):
            body=(P/r['cache_path']).read_bytes();assert hashlib.sha256(body).hexdigest()==r['sha256'];assert len(body)==r['bytes']
        if r['semantic_status']=='structured_data':api_data(json.loads((P/r['cache_path']).read_text()))
    for s in registry['sources']:
        for key in ['probe_receipt','documentation_receipt']:assert s[key] in by_id and by_id[s[key]]['status']=='ok'
        for key in ['interface','join_keys','access','limitations','license']:assert s[key]
    def data(n):return api_data(json.loads((P/'cache'/(n+'.body')).read_text()))
    assert {r['document_id'] for r in data('acris_legals_lead')}=={r['document_id'] for r in data('acris_master_join')}
    parcel=data('jerome_pluto');assert len(parcel)==1 and int(float(parcel[0]['bbl']))==2028560051 and int(parcel[0]['lotarea'])==6516
    hits=[f for f in data('geosearch_jerome')['features'] if f['properties'].get('name')=='1337 JEROME AVENUE'];assert hits
    assert any(str(f['properties']['addendum']['pad']['bbl'])=='2028560051' for f in hits)
    probe=json.loads((P/'probe-results.json').read_text());feed=probe['gtfs']['feed_info'][0];date=registry['audit_date'].replace('-','')
    assert feed['feed_start_date']<=date<=feed['feed_end_date']
    assert probe['lodes_ny_2023']['rows']>100000
    assert by_id['census_sample']['semantic_status']=='credential_required_html'
    assert by_id['dec_layers']['semantic_status']=='api_error'
    for bad in ['<html>Missing Key</html>',{'error':{'code':400}}]:
        try:api_data(bad)
        except ValueError:pass
        else:raise AssertionError('Failed to reject invalid API payload')
    print(f"PASS: {len(registry['sources'])} sources, {len(ledger)} receipts; byte integrity, joins, feed dates, credential/error gates and rejection fixtures")
if __name__=='__main__':validate()
