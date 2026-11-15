"""Bounded public-JSON capture for explicit provider registries. MIT.

Registry URLs come from module code, never from source-returned instructions.
Every failed attempt is retained. Missing/failed capture is never an empty list.
"""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request


def same_query(actual,expected):
    a,b=urllib.parse.urlsplit(actual),urllib.parse.urlsplit(expected)
    return (a.scheme,a.netloc,a.path,a.fragment)==(b.scheme,b.netloc,b.path,b.fragment) and sorted(urllib.parse.parse_qsl(a.query,keep_blank_values=True))==sorted(urllib.parse.parse_qsl(b.query,keep_blank_values=True))


class PublicJSON:
    def __init__(self,folder,providers,ca_file=None,max_attempts=120,minimum_interval=1):
        self.folder=Path(folder);(self.folder/'sources').mkdir(exist_ok=False)
        self.providers=providers;self.context=ssl.create_default_context(cafile=ca_file)
        self.receipts=[];self.attempts=0;self.max_attempts=max_attempts;self.minimum_interval=minimum_interval;self.last={}

    def url(self,provider,params):
        config=self.providers[provider]
        base=config['metadata_url'] if params is None else config['records_url']
        return base if params is None else base+'?'+urllib.parse.urlencode(params)

    def save(self):
        (self.folder/'receipts.json').write_text(json.dumps(self.receipts,sort_keys=True,indent=2,allow_nan=False)+'\n')

    def fetch(self,provider,params=None):
        if provider not in self.providers:raise ValueError('Unknown public provider')
        url=self.url(provider,params)
        r={'id':str(len(self.receipts)),'provider':provider,'url':url,'params':params,'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'failed','attempts':[]}
        self.receipts.append(r);body=None;parsed=None
        for retry in range(2):
            if self.attempts>=self.max_attempts:r['error']='Session attempt budget reached';break
            host=urllib.parse.urlsplit(url).netloc
            time.sleep(max(0,self.minimum_interval-(time.monotonic()-self.last.get(host,0))))
            self.attempts+=1;self.last[host]=time.monotonic()
            try:
                req=urllib.request.Request(url,headers={'User-Agent':'OpenHousingToolkit-PublicData/1.0','Accept':'application/json'})
                with urllib.request.urlopen(req,context=self.context,timeout=30) as response:
                    body=response.read(8*1024*1024+1);r['attempts'].append({'http_status':response.status});r['http_status']=response.status
                if len(body)>8*1024*1024:raise ValueError('Public response exceeds 8 MiB cap')
                parsed=json.loads(body)
                shape=self.providers[provider]['metadata_shape' if params is None else 'records_shape']
                if not isinstance(parsed,dict if shape=='object' else list):raise ValueError('Unexpected public JSON shape')
                r['status']='ok';r.pop('error',None);break
            except urllib.error.HTTPError as exc:
                body=exc.read(1024*1024);r['attempts'].append({'http_status':exc.code});r['error']='HTTP '+str(exc.code)
                wait=exc.headers.get('Retry-After','1')
                if retry==0 and exc.code in [429,500,502,503,504] and wait.isdigit() and int(wait)<=5:
                    time.sleep(max(1,int(wait)));continue
                break
            except (ValueError,OSError) as exc:r['error']=str(exc);break
        if body is not None:
            name='sources/'+r['id']+'-'+provider+'.json';(self.folder/name).write_bytes(body)
            r.update(body_path=name,sha256=hashlib.sha256(body).hexdigest(),bytes=len(body))
        self.save()
        return parsed if r['status']=='ok' else None
