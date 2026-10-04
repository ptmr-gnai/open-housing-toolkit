"""Explicit bounded exception for linked agency PDFs exceeding the 12 MiB audit cap. MIT."""
import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request
P=pathlib.Path(__file__).resolve().parent
REQUESTS=[{'id':'powers_rfp_large','publisher':'NYC HPD','purpose':'Original August 2022 solicitation; raised size budget for known linked PDF','url':'https://www.nyc.gov/assets/hpd/downloads/pdfs/services/351-powers-avenue-rfp.pdf'}, {'id':'powers_cvr_large','publisher':'NYC HPD','purpose':'Pre-solicitation community vision report; raised size budget for known linked PDF','url':'https://www.nyc.gov/assets/hpd/downloads/pdfs/services/351-powers-community-visioning-report.pdf'}]
def fetch(r):
    f=P/'cache'/(r['id']+'.body')
    if f.exists():raise ValueError('Do not overwrite retained evidence')
    receipt={**r,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'max_bytes':64*1024*1024,'timeout_seconds':35}
    try:
        with urllib.request.urlopen(urllib.request.Request(r['url'],headers={'User-Agent':'OpenHousingBenchmark/0.1'}),timeout=35) as resp:
            data=resp.read(receipt['max_bytes']+1)
            if len(data)>receipt['max_bytes']:raise ValueError('Response exceeds explicit 64 MiB cap')
            if not data.startswith(b'%PDF'):raise ValueError('Linked document is not a PDF')
            receipt.update(status='ok',parsed='pdf',http_status=resp.status,content_type=resp.headers.get('Content-Type'),final_url=resp.url,last_modified=resp.headers.get('Last-Modified'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),cache_path='cache/'+f.name)
        f.write_bytes(data)
    except Exception as exc:receipt.update(status='failed',error=str(exc))
    (P/'cache'/(r['id']+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    return {k:receipt.get(k) for k in ['id','status','bytes','error']}
if __name__=='__main__':
    (P/'requests-large.json').write_text(json.dumps(REQUESTS,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for r in pool.map(fetch,REQUESTS):print(r,flush=True)
