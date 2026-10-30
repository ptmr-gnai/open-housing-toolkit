"""Validate explicit floor polygons and reconcile compatible area quantities. MIT."""
import math
from shapely.geometry import Polygon
from housing_workflow.contracts import digest, load
from .sources import SCALE, verify as verify_source

GATES=['zoning','survey','access_egress_layout','structural_geotechnical','finance','existing_context','photo_camera','professional_review']


def fields(obj,keys):
    if not isinstance(obj,dict) or set(obj)!=set(keys):raise ValueError('Expected exactly fields: '+', '.join(keys))


def text(v):
    if not isinstance(v,str) or not v.strip():raise ValueError('Nonempty explanation required')


def number(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):raise ValueError('Finite number required')
    return v


def assumption(v,lower,upper):
    fields(v,['value','rationale']);text(v['rationale']);n=number(v['value'])
    if not lower<=n<=upper:raise ValueError('Assumption outside supported numeric range')
    return n


def polygon(vertices):
    if not isinstance(vertices,list) or not 4<=len(vertices)<=2000:raise ValueError('Expected a closed polygon ring')
    for p in vertices:
        if not isinstance(p,list) or len(p)!=2:raise ValueError('Expected XY coordinate pairs')
        for v in p:number(v)
    if vertices[0]!=vertices[-1]:raise ValueError('Polygon ring must be explicitly closed')
    p=Polygon(vertices)
    if not p.is_valid or p.is_empty or p.area<=0:raise ValueError('Invalid/self-intersecting/empty polygon')
    return p


def parcel_geometry(folder):
    receipt=verify_source(folder);feature=load(folder/'parcel.json')['features'][0]
    rings=feature['geometry'].get('rings')
    if not isinstance(rings,list) or len(rings)!=1:raise ValueError('Only one simple parcel ring supported; holes/multipart require another adapter')
    polygon(rings[0])
    ox=min(p[0] for p in rings[0]);oy=min(p[1] for p in rings[0])
    local=[[(x-ox)*SCALE,(y-oy)*SCALE] for x,y in rings[0]]
    return polygon(local),{'origin_native_xy':[ox,oy],'native_crs':'EPSG:2263','native_unit':'US survey foot','native_to_international_ft':SCALE,'axes':'x east, y north, z up; local z=0 is an assumed flat datum, not surveyed elevation'},receipt,feature['attributes']


def compile_model(scenario,source,analysis,analysis_sha):
    fields(scenario,['version','id','site_bbl','parcel_geometry_sha256','origin','purpose','floors','reconciliation'])
    if scenario['version']!='0.1.0' or scenario['origin']!='exploratory_assumptions':raise ValueError('Unsupported geometry scenario version/origin')
    for k in ['id','purpose']:text(scenario[k])
    p,frame,receipt,attrs=parcel_geometry(source)
    if scenario['site_bbl']!=receipt['bbl'] or analysis.get('resolved_bbl')!=receipt['bbl']:raise ValueError('Scenario/geometry/analysis parcel mismatch')
    if scenario['parcel_geometry_sha256']!=receipt['parcel_sha256']:raise ValueError('Scenario coordinate frame bound to different source geometry')
    fields(scenario['reconciliation'],['absolute_tolerance_sf','rationale'])
    tolerance=number(scenario['reconciliation']['absolute_tolerance_sf']);text(scenario['reconciliation']['rationale'])
    # Fixed maximum prevents a configuration from blessing a material mismatch.
    if not 0<=tolerance<=1:raise ValueError('Supported numerical tolerance is 0–1 sf, not a professional acceptance threshold')
    if not isinstance(scenario['floors'],list) or not 1<=len(scenario['floors'])<=30:raise ValueError('Provide 1–30 explicit floors')
    rows=[];previous=None;z=0;ids=set();vertices=[];faces=[]
    for f in scenario['floors']:
        fields(f,['id','footprint','height_ft','nonresidential_share'])
        text(f['id'])
        if f['id'] in ids:raise ValueError('Duplicate floor ID')
        ids.add(f['id'])
        fields(f['footprint'],['vertices_ft','rationale']);text(f['footprint']['rationale'])
        poly=polygon(f['footprint']['vertices_ft']);height=assumption(f['height_ft'],5,30)
        share=assumption(f['nonresidential_share'],0,1)
        if not p.covers(poly):raise ValueError('Footprint crosses mapped parcel boundary')
        if previous is not None and not previous.covers(poly):raise ValueError('Upper plate exceeds lower plate; cantilevers unsupported')
        # Mesh export deliberately restricts floors to convex plates, avoiding invalid fan triangulation.
        if abs(poly.convex_hull.area-poly.area)>1e-7:raise ValueError('Only convex floor plates supported by this mesh exporter')
        pts=f['footprint']['vertices_ft'][:-1]
        # Normalize counterclockwise orientation for reproducible outward face winding.
        if not poly.exterior.is_ccw:pts=list(reversed(pts))
        start=len(vertices);n=len(pts)
        vertices.extend([[x,y,z] for x,y in pts]+[[x,y,z+height] for x,y in pts])
        floorfaces=[]
        for i in range(1,n-1):
            floorfaces += [[start,start+i+1,start+i],[start+n,start+n+i,start+n+i+1]]
        for i in range(n):
            j=(i+1)%n;floorfaces += [[start+i,start+j,start+n+j],[start+i,start+n+j,start+n+i]]
        faces.extend(floorfaces)
        rows.append({'id':f['id'],'footprint_ft':f['footprint']['vertices_ft'],'base_z_ft':z,'top_z_ft':z+height,
                     'gross_floor_proxy_sf':poly.area,'nonresidential_proxy_sf':poly.area*share,
                     'residential_proxy_sf':poly.area*(1-share),'inputs':['scenario.floors.'+str(len(rows))+'.footprint','scenario.floors.'+str(len(rows))+'.height_ft','scenario.floors.'+str(len(rows))+'.nonresidential_share'],
                     'formula':'gross = polygon area; nonresidential = gross × share; residential = gross × (1 − share)',
                     'faces':floorfaces})
        z+=height;previous=poly
    claims={c['id']:c for c in analysis['claims']}
    if len(claims)!=len(analysis['claims']):raise ValueError('Duplicate analysis claims')
    targets={'gross':'scenario.gross_area_sf','nonresidential':'scenario.nonresidential_gross_sf','residential':'scenario.residential_gross_sf'}
    totals={k:sum(f[k+'_floor_proxy_sf' if k=='gross' else k+'_proxy_sf'] for f in rows) for k in targets}
    comparisons=[]
    for name,cid in targets.items():
        if cid not in claims:raise ValueError('Required compatible gross-area analysis claim missing: '+cid)
        c=claims[cid]
        if c['unit']!='gross sf' or c['kind'] not in {'assumption','calculation'}:raise ValueError('Analysis area definition/type incompatible')
        target=number(c['value'])
        if target<0:raise ValueError('Negative analysis target')
        diff=totals[name]-target
        comparisons.append({'quantity':name,'geometry_proxy_sf':totals[name],'analysis_target_sf':target,'difference_sf':diff,
                            'status':'consistent_within_tolerance' if abs(diff)<=tolerance else 'mismatch',
                            'basis':'Assumed complete plate area treated as gross-area proxy; not zoning floor area or architectural measurement.',
                            'analysis_claim':cid,'analysis_kind':c['kind'],'analysis_inputs':c['inputs'],'analysis_rationale':c['rationale'],
                            'analysis_sha256':analysis_sha,'floor_ids':[f['id'] for f in rows]})
    lot_source=claims.get('pluto.0.lotarea');version_source=claims.get('pluto.0.version')
    lot_area=float(attrs['LotArea'])
    return {'version':'0.1.0','module':'grounded-massing','site_bbl':receipt['bbl'],'scenario_id':scenario['id'],
            'source_geometry':{**receipt,'attributes':attrs,'coordinate_frame':frame,'polygon_ft':[list(x) for x in p.exterior.coords],
                               'mapped_polygon_area_sf':p.area,'recorded_lot_area_sf':lot_area,'mapped_minus_recorded_sf':p.area-lot_area,
                               'comparison_status':'unreconciled_source_observations','analysis_recorded_lotarea':lot_source['value'] if lot_source else None,
                               'analysis_pluto_version':version_source['value'] if version_source else None,'release_equivalence':'not certified by equal Version labels'},
            'floors':rows,'total_height_ft':z,'totals_sf':totals,'mesh':{'units':'international feet','vertices':vertices,'triangles':faces,'scope':'Overlapping floor-solid interfaces retained; schematic volume, not fabrication/BIM mesh.'},
            'analysis_sha256':analysis_sha,'comparisons':comparisons,'absolute_tolerance_sf':tolerance,
            'provenance':{
                'parcel_polygon':{'kind':'fact','file':'parcel-source/parcel.json','pointer':'/features/0/geometry/rings/0','sha256':receipt['parcel_sha256']},
                'source_attributes':{'kind':'fact','file':'parcel-source/parcel.json','pointer':'/features/0/attributes','sha256':receipt['parcel_sha256']},
                'coordinate_transform':{'kind':'calculation','method':'native-to-local-international-feet@1','formula':'(native_xy − componentwise ring minima) × (1200/3937)/0.3048','inputs':['parcel_polygon']},
                'design':{'kind':'assumption','file':'scenario.json','pointer':'/floors','role':'Explicit footprint, height and floor-use fractions, each with rationale; not observed dimensions.'},
                'areas':{'kind':'calculation','method':'floor-polygon-area-and-fractional-allocation@1','formula':'floor areas by shoelace/GEOS; sum gross, gross × share, gross × (1 − share)','inputs':['design','coordinate_transform']},
                'reconciliation_policy':{'kind':'assumption','file':'scenario.json','pointer':'/reconciliation','role':'Numerical tolerance and gross-floor proxy compatibility; unreviewed policy.'},
                'comparisons':{'kind':'calculation','inputs':['areas','analysis_sha256','reconciliation_policy'],'formula':'geometry proxy − bound analysis claim; absolute difference ≤ declared tolerance'},
                'review_gates':{'kind':'unknown','role':'No professional acceptance from numeric agreement.'}
            },
            'review_gates':{k:'unknown' for k in GATES},'mapped_containment':'contained_in_retained_polygon; not buildable envelope',
            'design_status':'exploratory_assumptions; not derived from zoning or a survey',
            'visual_handoff_status':'blocked_area_mismatch' if any(c['status']=='mismatch' for c in comparisons) else 'schematic_reference_only',
            'limits':['Gross plate area is a modeling proxy, not zoning floor area.','No existing context, legal envelope, layouts or physical/financial feasibility established.','No source photograph registered to this camera; no existing building retained in the scene.']}
