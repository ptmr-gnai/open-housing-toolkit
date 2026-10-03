#!/usr/bin/env python3
"""Bounded public-source audit. Retain bytes, links, text and request receipts. MIT."""
import argparse,concurrent.futures,datetime,hashlib,json,pathlib,urllib.error,urllib.parse,urllib.request
from html.parser import HTMLParser

ROOT=pathlib.Path(__file__).resolve().parent

class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.text=[];self.links=[];self.ignore=0;self.href=None;self.label=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag in ['script','style']:self.ignore+=1
        if tag=='a':self.href=attrs.get('href');self.label=[]
        if tag in ['p','br','h1','h2','h3','li','tr']:self.text.append('\n')
    def handle_endtag(self,tag):
        if tag in ['script','style']:self.ignore=max(0,self.ignore-1)
        if tag=='a' and self.href is not None:
            self.links.append({'href':self.href,'label':' '.join(self.label).strip()});self.href=None
    def handle_data(self,data):
        if not self.ignore:
            self.text.append(data)
            if self.href is not None:self.label.append(data.strip())

def collect(req):
    key=req['id'];cache=ROOT/'cache';cache.mkdir(exist_ok=True)
    receipt={**req,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request=urllib.request.Request(req['url'],headers={'User-Agent':'OpenHousingSourceAudit/0.1'})
        with urllib.request.urlopen(request,timeout=35) as response:
            body=response.read(12*1024*1024+1)
            if len(body)>12*1024*1024:raise ValueError('Response exceeds audit size budget')
            receipt.update(status='ok',http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),last_modified=response.headers.get('Last-Modified'))
        (cache/(key+'.body')).write_bytes(body)
        receipt.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),cache_path='cache/'+key+'.body')
        content_type=receipt['content_type'] or ''
        if 'json' in content_type or body.lstrip().startswith((b'{',b'[')):
            obj=json.loads(body);receipt['parsed']='json'
            if isinstance(obj,list):receipt['row_count']=len(obj)
            else:receipt['top_level_keys']=list(obj)[:30]
        elif 'html' in content_type or b'<html' in body[:1000].lower():
            doc=Document();doc.feed(body.decode('utf8',errors='replace'))
            (cache/(key+'.text')).write_text(''.join(doc.text))
            links=[dict(label=x['label'],url=urllib.parse.urljoin(receipt['final_url'],x['href'])) for x in doc.links if x['href']]
            (cache/(key+'.links.json')).write_text(json.dumps(links,indent=2)+'\n')
            receipt.update(parsed='html',text_chars=len(''.join(doc.text)),link_count=len(links))
        elif body.startswith(b'%PDF'):receipt['parsed']='pdf'
        else:receipt['parsed']='other'
    except urllib.error.HTTPError as exc:
        receipt.update(status='failed',http_status=exc.code,error=str(exc))
        (cache/(key+'.error')).write_bytes(exc.read(20000))
    except Exception as exc:receipt.update(status='failed',error=type(exc).__name__+': '+str(exc))
    (cache/(key+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    return {k:receipt.get(k) for k in ['id','status','http_status','parsed','bytes','row_count','text_chars','error']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('requests');args=p.parse_args()
    requests=json.loads(pathlib.Path(args.requests).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(collect,requests):print(json.dumps(result),flush=True)
