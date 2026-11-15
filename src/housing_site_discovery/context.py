"""Optional public station/industrial-policy context; source failures remain unknown. MIT."""
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import shutil
import ssl
import urllib.error
import urllib.parse
import urllib.request
from . import evidence
from .common import bbl, digest, fresh, load, number, save, seal, verify_files

STATION_FIELDS=['station_id','complex_id','gtfs_stop_id','stop_name','borough','daytime_routes',
                'gtfs_latitude','gtfs_longitude','ada','ada_notes']
GFT_BASE='https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/v_GFT_Green_Fast_Track_Lots/FeatureServer/0'
GFT_VERSIONS='https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/v_GFT_Source_Data_Versions/FeatureServer/0'
IBZ_BASE='https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/ArcGIS/rest/services/Industry_in_NYC_WFL/FeatureServer/0'


def query(base,params):return base+'?'+urllib.parse.urlencode(params)


def source_urls(ids):
    meta='https://data.ny.gov/api/views/39hk-dx4f.json';data='https://data.ny.gov/resource/39hk-dx4f.json'
    urls={
        'mta_metadata_before':meta,
        'mta_count_before':query(data,{'$select':'count(*) as n'}),
        'mta_stations':query(data,{'$select':','.join(STATION_FIELDS),'$order':'station_id','$limit':'1001'}),
        'mta_count_after':query(data,{'$select':'count(*) as n'}),
        'mta_metadata_after':meta,
        'ibz_portal':query('https://www.arcgis.com/sharing/rest/portals/GfwWNkhOj9bNBqoJ',{'f':'json'}),
        'ibz_item':query('https://www.arcgis.com/sharing/rest/content/items/f89585b18b88472fa563a68abd95b567',{'f':'json'}),
        'ibz_metadata_before':query(IBZ_BASE,{'f':'json'}),
        'ibz_count':query(IBZ_BASE+'/query',{'where':'1=1','returnCountOnly':'true','f':'json'}),
        'ibz_features':query(IBZ_BASE+'/query',{'where':'1=1','outFields':'FID,NAME,BORONAME','orderByFields':'FID',
                                             'returnGeometry':'true','outSR':'4326','resultRecordCount':'2001','f':'geojson'}),
        'ibz_metadata_after':query(IBZ_BASE,{'f':'json'}),
        'ibz_policy':'https://edc.nyc/industry/industrial-and-manufacturing',
        'gft_metadata_before':query(GFT_BASE,{'f':'json'}),
        'gft_versions_metadata':query(GFT_VERSIONS,{'f':'json'}),
        'gft_versions':query(GFT_VERSIONS+'/query',{'where':'1=1','outFields':'*','returnGeometry':'false','resultRecordCount':'1001','f':'json'}),
    }
    for i in range(0,len(ids),100):
        clause="bbl in ("+','.join("'"+x+"'" for x in ids[i:i+100])+")"
        urls['gft_lots_'+str(i//100)]=query(GFT_BASE+'/query',{'where':clause,'outFields':'*','orderByFields':'bbl','returnGeometry':'false','resultRecordCount':'101','f':'json'})
    urls['gft_metadata_after']=query(GFT_BASE,{'f':'json'})
    return urls


def collect(source,out,ca_file=None):
    source=Path(source);evidence.verify(source);out=fresh(out);(out/'sources').mkdir()
    ctx=ssl.create_default_context(cafile=ca_file);receipts=[]
    inv=load(source/'inventory/inventory.json')
    ids=[bbl(x['row']['bbl']) for x in inv['records']['pluto']]
    save(out/'universe.json',{'scope':inv['scope'],'bbls':ids,'evidence_manifest_sha256':digest((source/'manifest.json').read_bytes())})
    for name,url in source_urls(ids).items():
        row={'id':name,'url':url,'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'failed'}
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'OpenHousingToolkit-SiteDiscovery/1.0'})
            with urllib.request.urlopen(req,timeout=30,context=ctx) as response:
                body=response.read(16*1024*1024+1)
                if len(body)>16*1024*1024:raise ValueError('Context response exceeds 16 MiB')
                row['http_status']=response.status
            # Validate source shape later, preserving even malformed responses.
            row['status']='ok'
        except urllib.error.HTTPError as exc:
            body=exc.read(1024*1024);row.update(http_status=exc.code,error=str(exc))
        except (OSError,ValueError) as exc:
            body=None;row['error']=str(exc)
        if body is not None:
            suffix='html' if name=='ibz_policy' else 'json';path=f'sources/{name}.{suffix}';(out/path).write_bytes(body)
            row.update(body_path=path,sha256=digest(body),bytes=len(body))
        receipts.append(row);save(out/'receipts.json',receipts)
    save(out/'context.json',derive(out));seal(out,'context');return verify(out)


def derive(folder):
    folder=Path(folder);receipts=load(folder/'receipts.json')
    universe=load(folder/'universe.json');ids=universe['bbls']
    if not isinstance(ids,list) or not ids or len(ids)!=len(set(ids)) or any(bbl(x)!=x for x in ids):raise ValueError('Invalid context lot universe')
    urls=source_urls(ids)
    if [x['id'] for x in receipts]!=list(urls) or any(x['url']!=urls[x['id']] for x in receipts):
        raise ValueError('Context source/query inventory changed')
    data={};failures=[];refs={}
    for receipt in receipts:
        name=receipt['id']
        if receipt['status'] not in ['ok','failed']:raise ValueError('Invalid source status')
        if 'body_path' in receipt:
            suffix='html' if name=='ibz_policy' else 'json'
            if receipt['body_path']!=f'sources/{name}.{suffix}':raise ValueError('Context source path changed')
            body=(folder/receipt['body_path']).read_bytes()
            if digest(body)!=receipt['sha256'] or len(body)!=receipt['bytes']:raise ValueError('Context bytes differ from receipt')
        if receipt['status']!='ok':failures.append(name);continue
        refs[name]={'body_path':receipt['body_path'],'sha256':receipt['sha256'],'receipt_id':name,'url':receipt['url']}
        try:
            value=body.decode() if name=='ibz_policy' else json.loads(body)
            expected=str if name=='ibz_policy' else (list if name.startswith('mta_count') or name=='mta_stations' else dict)
            if not isinstance(value,expected):raise ValueError('Unexpected source shape')
            data[name]=value
        except (ValueError,UnicodeError):failures.append(name)
    station_errors=[];stations=[]
    required=['mta_metadata_before','mta_metadata_after','mta_count_before','mta_count_after','mta_stations']
    if any(name not in data for name in required):station_errors.append('station_source_missing_or_failed')
    else:
        before,after=data['mta_metadata_before'],data['mta_metadata_after'];raw=data['mta_stations']
        fields={c.get('fieldName'):c.get('dataTypeName') for c in before.get('columns',[])}
        if not set(STATION_FIELDS)<=set(fields) or any(fields.get(k)!='number' for k in ['station_id','gtfs_latitude','gtfs_longitude']):station_errors.append('station_schema_incomplete')
        if before.get('rowsUpdatedAt')!=after.get('rowsUpdatedAt'):station_errors.append('station_metadata_update_changed')
        try:
            count=int(data['mta_count_before'][0]['n'])
            if count!=int(data['mta_count_after'][0]['n']) or not isinstance(raw,list) or len(raw)!=count or count>=1001:
                station_errors.append('station_count_changed_or_truncated')
            identities=[]
            for index,row in enumerate(raw):
                if not isinstance(row,dict):station_errors.append('station_response_malformed');continue
                lat,lon=number(row.get('gtfs_latitude')),number(row.get('gtfs_longitude'))
                if not row.get('station_id') or lat is None or lon is None or not -90<=lat<=90 or not -180<=lon<=180:
                    station_errors.append('station_identity_or_coordinates_invalid');continue
                identities.append(str(row.get('gtfs_stop_id') or ''))
                if not row.get('gtfs_stop_id'):station_errors.append('station_identity_or_coordinates_invalid')
                stations.append({'row':row,'reference':{**refs['mta_stations'],'pointer':'/'+str(index)}})
            if len(identities)!=len(set(identities)):station_errors.append('duplicate_station_identity')
        except (KeyError,ValueError,TypeError,IndexError):station_errors.append('station_response_malformed')
    ibz_errors=[];features=[]
    required=['ibz_portal','ibz_item','ibz_metadata_before','ibz_metadata_after','ibz_count','ibz_features']
    if any(name not in data for name in required):ibz_errors.append('industrial_zone_source_missing_or_failed')
    else:
        portal,item=data['ibz_portal'],data['ibz_item'];before,after=data['ibz_metadata_before'],data['ibz_metadata_after']
        if portal.get('id')!='GfwWNkhOj9bNBqoJ' or portal.get('name')!='NYC DCP Mapping Portal' or item.get('orgId')!=portal['id']:
            ibz_errors.append('industrial_zone_publisher_not_verified')
        if before.get('name')!='IBZs' or before.get('serviceItemId')!=item.get('id'):
            ibz_errors.append('industrial_zone_layer_identity_changed')
        if before.get('editingInfo')!=after.get('editingInfo'):ibz_errors.append('industrial_zone_metadata_update_changed')
        try:
            result=data['ibz_features'];features=result['features']
            if result.get('type')!='FeatureCollection' or result.get('exceededTransferLimit') or len(features)!=data['ibz_count']['count'] or len(features)>=2001:
                ibz_errors.append('industrial_zone_count_mismatch_or_truncated')
            zone_ids=[]
            for feature in features:
                zone_ids.append(str(feature['properties']['FID']))
                if not feature['properties'].get('NAME') or not valid_geometry(feature['geometry']):
                    ibz_errors.append('industrial_zone_geometry_or_identity_invalid')
            if len(zone_ids)!=len(set(zone_ids)):ibz_errors.append('duplicate_industrial_zone_identity')
        except (KeyError,ValueError,TypeError):ibz_errors.append('industrial_zone_response_malformed')
    gft_errors=[];gft_rows={};versions=[]
    required=['gft_metadata_before','gft_metadata_after','gft_versions_metadata','gft_versions']
    if any(name not in data for name in required):gft_errors.append('fast_track_metadata_or_versions_missing')
    else:
        before,after=data['gft_metadata_before'],data['gft_metadata_after']
        if before.get('name')!='Green_Fast_Track_Lots' or before.get('serviceItemId')!='095fbe2e10b544a4974c5b4026d7f70a':
            gft_errors.append('fast_track_layer_identity_changed')
        fields={x.get('name'):x.get('type') for x in before.get('fields',[])}
        if fields.get('bbl')!='esriFieldTypeString' or not {'zoning_district','special_coastal_risk_flag','industrial_lots_flag'}<=set(fields):
            gft_errors.append('fast_track_schema_changed')
        if before.get('editingInfo')!=after.get('editingInfo'):gft_errors.append('fast_track_metadata_update_changed')
        version_result=data['gft_versions']
        if version_result.get('exceededTransferLimit') or not isinstance(version_result.get('features'),list) or len(version_result['features'])>=1001:
            gft_errors.append('fast_track_versions_truncated_or_malformed')
        else:
            versions=[x.get('attributes',{}) for x in version_result['features'] if isinstance(x,dict)]
            names=[x.get('schema_name') for x in versions]
            if 'dcp_mappluto_wi' not in names or len(names)!=len(set(names)) or any(not x.get('v') for x in versions):gft_errors.append('fast_track_source_versions_incomplete')
    missing_batches=[]
    for i in range(0,len(ids),100):
        name='gft_lots_'+str(i//100);requested=ids[i:i+100];result=data.get(name)
        if result is None:missing_batches.append(name);continue
        if result.get('exceededTransferLimit') or not isinstance(result.get('features'),list) or len(result['features'])>=101:
            missing_batches.append(name);continue
        for index,feature in enumerate(result['features']):
            if not isinstance(feature,dict) or not isinstance(feature.get('attributes'),dict):raise ValueError('Malformed Fast Tracker feature')
            row=feature['attributes']
            try:identity=bbl(row.get('bbl'))
            except ValueError:raise ValueError('Invalid Fast Tracker BBL')
            if identity not in requested or identity in gft_rows:raise ValueError('Unexpected or duplicate Fast Tracker lot')
            gft_rows[identity]={'row':row,'reference':{**refs[name],'pointer':'/features/'+str(index)+'/attributes'}}
    return {'version':'1.0','stations':{'complete':not station_errors,'errors':sorted(set(station_errors)),
                 'records':stations if not station_errors else [],'meaning':'Actual source station points and daytime-route labels; no entrance, walk routing, live service or journey/accessibility model.'},
            'industrial_zones':{'complete':not ibz_errors,'errors':sorted(set(ibz_errors)),
                 'features':features if not ibz_errors else [],'reference':refs.get('ibz_features'),
                 'policy_source_returned':'ibz_policy' in data,'policy_reference':refs.get('ibz_policy'),
                 'meaning':'DCP hosted IBZ polygons; recorded parcel-point overlap is a policy-review signal. Outside is not policy clearance. NYCEDC describes a City commitment not to support residential rezonings in IBZs; this is distinct from a zoning prohibition.'},
            'fast_track':{'query_coverage_complete':not gft_errors and not missing_batches,
                'schema_and_versions_valid':not gft_errors,'errors':gft_errors,'missing_batches':missing_batches,
                'missing_bbls':sorted(set(ids)-set(gft_rows)),'records':gft_rows if not gft_errors else {},
                'source_versions':versions,'versions_reference':refs.get('gft_versions'),
                'meaning':'Publisher precomputed Fast Tracker context, with separate source vintages. Missing BBLs/No flags do not prove absence of constraints or Green Fast Track eligibility; project actions and field review remain required.'},
            'failed_or_unparsed_sources':sorted(set(failures))}


def verify(folder):
    folder=Path(folder);verify_files(folder,'context')
    result=derive(folder)
    if result!=load(folder/'context.json'):raise ValueError('Public context differs from replay')
    return {'status':'passed','station_source_complete':result['stations']['complete'],
            'industrial_zone_source_complete':result['industrial_zones']['complete'],
            'fast_track_query_coverage_complete':result['fast_track']['query_coverage_complete'],
            'fast_track_returned_lots':len(result['fast_track']['records']),
            'failed_sources':result['failed_or_unparsed_sources']}


def valid_geometry(geometry):
    try:
        if geometry['type'] not in ['Polygon','MultiPolygon']:return False
        polygons=[geometry['coordinates']] if geometry['type']=='Polygon' else geometry['coordinates']
        if not polygons:return False
        for polygon in polygons:
            if not polygon:return False
            for ring in polygon:
                if len(ring)<4 or ring[0]!=ring[-1]:return False
                for pt in ring:
                    if len(pt)<2 or number(pt[0]) is None or number(pt[1]) is None or not -180<=pt[0]<=180 or not -90<=pt[1]<=90:return False
        return True
    except (KeyError,TypeError,IndexError):return False


def distance_m(lat1,lon1,lat2,lon2):
    a,b=math.radians(lat1),math.radians(lat2);dl=math.radians(lat2-lat1);do=math.radians(lon2-lon1)
    t=math.sin(dl/2)**2+math.cos(a)*math.cos(b)*math.sin(do/2)**2
    return 6371008.8*2*math.asin(min(1,math.sqrt(max(0,t))))


def in_ring(point,ring):
    """0 outside, 1 inside, 2 boundary. Longitude/latitude coordinates."""
    x,y=point;inside=False
    for a,b in zip(ring,ring[1:]+ring[:1]):
        ax,ay=a[:2];bx,by=b[:2]
        cross=(x-ax)*(by-ay)-(y-ay)*(bx-ax)
        if abs(cross)<=1e-12 and min(ax,bx)-1e-10<=x<=max(ax,bx)+1e-10 and min(ay,by)-1e-10<=y<=max(ay,by)+1e-10:
            return 2
        if (ay>y)!=(by>y) and x < (bx-ax)*(y-ay)/(by-ay)+ax:inside=not inside
    return int(inside)


def geometry_relation(point,geometry):
    polygons=[geometry['coordinates']] if geometry['type']=='Polygon' else geometry['coordinates']
    for rings in polygons:
        exterior=rings[0]
        xs=[p[0] for p in exterior];ys=[p[1] for p in exterior]
        if not min(xs)<=point[0]<=max(xs) or not min(ys)<=point[1]<=max(ys):continue
        outer=in_ring(point,exterior)
        holes=[in_ring(point,hole) for hole in rings[1:]]
        if outer==2 or 2 in holes:return 'boundary_review'
        if outer==1 and not any(holes):return 'inside'
    return 'outside'


def annotate(raw,pack):
    empty={'green_fast_track':None,'nearest_station':None,'industrial_zone_point_matches':None,
           'industrial_zone_point_relation':'unknown','limitations':['Point proximity is not walking access; policy overlap is not legal eligibility.']}
    if pack is None:return {**empty,'status':'not_collected'}
    lat,lon=number(raw.get('latitude')),number(raw.get('longitude'))
    if lat is None or lon is None:return {**empty,'status':'lot_coordinates_missing'}
    result={**empty,'status':'source_coverage_in_fields'}
    if pack['stations']['complete']:
        options=[]
        for item in pack['stations']['records']:
            row=item['row'];metres=distance_m(lat,lon,float(row['gtfs_latitude']),float(row['gtfs_longitude']))
            options.append((metres,str(row['gtfs_stop_id']),item))
        if options:
            metres,_,item=min(options);row=item['row']
            result['nearest_station']={'station_id':row['station_id'],'gtfs_stop_id':row['gtfs_stop_id'],'name':row.get('stop_name'),
                'straight_line_m':round(metres,1),'daytime_routes':row.get('daytime_routes'),
                'recorded_ada_code':row.get('ada'),'ada_notes':row.get('ada_notes'),
                'reference':item['reference'],'meaning':'Parcel point to station point; no walking route, entrance or live service inference.'}
    if pack.get('fast_track',{}).get('schema_and_versions_valid'):
        item=pack['fast_track']['records'].get(bbl(raw.get('bbl')))
        if item is not None:
            flags={k:v for k,v in item['row'].items() if k.endswith('_flag')}
            result['green_fast_track']={'publisher_fields':item['row'],'reference':item['reference'],
                'versions_reference':pack['fast_track']['versions_reference'],
                'positive_publisher_flags':sorted(k for k,v in flags.items() if v=='Yes'),
                'unresolved_publisher_flags':sorted(k for k,v in flags.items() if v not in ['Yes','No']),
                'meaning':pack['fast_track']['meaning']}
    if pack['industrial_zones']['complete']:
        matches=[]
        for index,feature in enumerate(pack['industrial_zones']['features']):
            relation=geometry_relation((lon,lat),feature['geometry'])
            if relation!='outside':matches.append({'name':feature['properties']['NAME'],'relation':relation,
                'reference':{**pack['industrial_zones']['reference'],'pointer':'/features/'+str(index)}})
        result['industrial_zone_point_matches']=matches
        result['industrial_zone_point_relation']='boundary_review' if any(x['relation']=='boundary_review' for x in matches) else ('inside' if matches else 'outside_returned_polygons')
    return result
