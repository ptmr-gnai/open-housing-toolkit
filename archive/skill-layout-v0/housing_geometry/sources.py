"""One reviewed DCP geometry adapter, exact bytes and query receipts. MIT."""
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from housing_workflow.contracts import bbl, digest, load, save
from housing_workflow.engine import fresh, safe

LAYER='https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/MAPPLUTO/FeatureServer/0'
ITEM='https://www.arcgis.com/sharing/rest/content/items/1564ace0b4f44318ac39920737f9bd07?f=json'
TERMS='https://www.nyc.gov/home/terms-of-use.page'
SCALE=(1200/3937)/0.3048  # EPSG:2263 US survey foot → international foot.


def urls(parcel):
    bbl(parcel)
    return {'parcel.json':LAYER+'/query?'+urlencode({'f':'json','where':'BBL = '+parcel,'outFields':'BBL,Address,LotArea,Version','returnGeometry':'true','outSR':2263}),
            'layer.json':LAYER+'?f=pjson','item.json':ITEM}


def collect(parcel,folder):
    fresh(folder);records={}
    for name,url in urls(parcel).items():
        with urlopen(Request(url,headers={'User-Agent':'open-housing-toolkit/geometry-probe'}),timeout=30) as response:
            raw=response.read(2_000_001)
            if response.status!=200 or len(raw)>2_000_000:raise ValueError('Invalid/oversized geometry source response')
            (folder/name).write_bytes(raw)
            records[name]={'url':url,'http_status':response.status,'retrieved_at':datetime.now(timezone.utc).isoformat(),'sha256':digest(raw),'bytes':len(raw)}
    save(folder/'receipt.json',{'version':'0.1.0','bbl':parcel,'publisher':'NYC Department of City Planning / DCP_GIS','terms_url':TERMS,'files':records,'limits':'Mapped tax lot, not survey/legal boundary; retrieval date is not observation date.'})
    return verify(folder)


def verify(folder):
    r=load(folder/'receipt.json');parcel=bbl(r['bbl']);expected=urls(parcel)
    if r.get('version')!='0.1.0' or set(r['files'])!=set(expected) or r.get('terms_url')!=TERMS or r.get('publisher')!='NYC Department of City Planning / DCP_GIS':raise ValueError('Unsupported geometry receipt')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!=set(expected)|{'receipt.json'}:raise ValueError('Geometry source inventory changed')
    for name,url in expected.items():
        rec=r['files'][name];raw=safe(folder,name).read_bytes()
        if rec['url']!=url or rec['http_status']!=200 or not rec.get('retrieved_at') or rec['sha256']!=digest(raw) or rec['bytes']!=len(raw):
            raise ValueError('Geometry source query/bytes binding changed')
        data=load(folder/name)
        if not isinstance(data,dict) or 'error' in data:raise ValueError('Geometry service returned an error')
    item=load(folder/'item.json');layer=load(folder/'layer.json');data=load(folder/'parcel.json')
    if item.get('owner')!='DCP_GIS' or item.get('id')!='1564ace0b4f44318ac39920737f9bd07':raise ValueError('Unexpected service ownership metadata')
    if layer.get('geometryType')!='esriGeometryPolygon':raise ValueError('Unexpected layer geometry type')
    sr=data.get('spatialReference',{})
    if sr.get('wkid') not in {2263,102718} or sr.get('latestWkid',2263)!=2263:raise ValueError('Geometry must use EPSG:2263; degrees are not feet')
    if data.get('exceededTransferLimit') or len(data.get('features',[]))!=1:raise ValueError('Missing, ambiguous or truncated parcel geometry')
    feature=data['features'][0]
    if str(feature['attributes'].get('BBL')) not in {parcel,parcel+'.0'}:raise ValueError('Geometry parcel mismatch')
    if not feature['attributes'].get('Version'):raise ValueError('Missing parcel source version')
    return {'status':'passed','bbl':parcel,'source_version':feature['attributes']['Version'],'parcel_sha256':r['files']['parcel.json']['sha256']}
