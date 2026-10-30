"""Deterministic schematic views, mesh, schedule and visual handoff. MIT."""
import csv
import html
import io
import math
from housing_workflow.contracts import digest, dumps


def obj(ir):
    lines=['# Open Housing Toolkit exploratory massing; international feet',
           '# Not a permitted envelope, architectural design, or existing conditions model',
           '# Local coordinate frame: '+dumps(ir['source_geometry']['coordinate_frame']).strip().replace('\n',' ')]
    for v in ir['mesh']['vertices']:lines.append('v '+' '.join(f'{n:.9f}' for n in v))
    for f in ir['mesh']['triangles']:lines.append('f '+' '.join(str(i+1) for i in f))
    return '\n'.join(lines)+'\n'


def svg(ir,mode):
    # Fixed schematic orthographic camera; explicitly not registered to a photo.
    def project(x,y,z=0):
        if mode=='plan':return x,-y
        a=math.radians(45);e=math.radians(35)
        return (x-y)*math.cos(a),(x+y)*math.sin(e)*math.sin(a)-z*math.cos(e)
    parcel=[project(x,y) for x,y in ir['source_geometry']['polygon_ft']]
    shapes=[]
    if mode=='plan':
        for index,f in enumerate(ir['floors']):
            shapes.append(([project(x,y) for x,y in f['footprint_ft']], '#c66c39' if index==0 else '#568cb3',f['id'],[]))
    else:
        from shapely.geometry import Polygon
        eye=[math.cos(math.radians(35))/math.sqrt(2),math.cos(math.radians(35))/math.sqrt(2),math.sin(math.radians(35))]
        surfaces=[]
        for index,f in enumerate(ir['floors']):
            poly=Polygon(f['footprint_ft']);pts=list(poly.exterior.coords)[:-1]
            if not poly.exterior.is_ccw:pts.reverse()
            color='#d89165' if index==0 else '#8db1cb'
            for i,(x,y) in enumerate(pts):
                xx,yy=pts[(i+1)%len(pts)]
                normal=[yy-y,x-xx,0]
                if sum(normal[j]*eye[j] for j in range(3))<=0:continue
                wall=[[x,y,f['base_z_ft']],[xx,yy,f['base_z_ft']],[xx,yy,f['top_z_ft']],[x,y,f['top_z_ft']]]
                surfaces.append((wall,[],color,f['id']))
            roof=poly if index==len(ir['floors'])-1 else poly.difference(Polygon(ir['floors'][index+1]['footprint_ft']))
            parts=list(roof.geoms) if roof.geom_type=='MultiPolygon' else [roof]
            for part in parts:
                if part.is_empty:continue
                outer=[[x,y,f['top_z_ft']] for x,y in part.exterior.coords]
                holes=[[[x,y,f['top_z_ft']] for x,y in ring.coords] for ring in part.interiors]
                surfaces.append((outer,holes,color,f['id']+' exposed roof'))
        def depth(surface):return sum(sum(p[j]*eye[j] for j in range(3)) for p in surface[0])/len(surface[0])
        for pts,holes,color,label in sorted(surfaces,key=depth):
            shapes.append(([project(*p) for p in pts],color,label,[[project(*p) for p in ring] for ring in holes]))
    allpts=parcel+[p for pts,_,_,_ in shapes for p in pts]
    xs=[p[0] for p in allpts];ys=[p[1] for p in allpts]
    xmin,xmax,ymin,ymax=min(xs),max(xs),min(ys),max(ys)
    scale=min(590/(xmax-xmin),620/(ymax-ymin))
    def points(pts):return ' '.join(f'{55+(x-xmin)*scale:.3f},{100+(y-ymin)*scale:.3f}' for x,y in pts)
    title='Site plan — north up' if mode=='plan' else 'Schematic axonometric — arbitrary camera'
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="700" height="820" viewBox="0 0 700 820">',
           '<rect width="700" height="820" fill="#f5f4ef"/>',
           '<text x="30" y="35" font-size="22" font-family="sans-serif">'+title+'</text>',
           '<text x="30" y="65" font-size="15" font-family="sans-serif">BBL '+ir['site_bbl']+' · assumed replacement massing</text>',
           '<polygon points="'+points(parcel)+'" fill="#e0e7da" stroke="#536448" stroke-width="2"/>']
    for pts,color,label,holes in shapes:
        path=' '.join('M '+' L '.join(points(ring).split())+' Z' for ring in [pts]+holes)
        parts.append('<path d="'+path+'" fill="'+color+'" fill-rule="evenodd" stroke="#32485a" stroke-width="0.7"><title>'+html.escape(label)+'</title></path>')
    if mode=='plan':
        bar=50*scale
        parts += [f'<path d="M 40 750 h {bar:.3f}" stroke="#233542" stroke-width="3"/>','<text x="40" y="775" font-size="14" font-family="sans-serif">50 international feet · mapped boundary, not a survey</text>']
    else:parts.append('<text x="30" y="775" font-size="14" font-family="sans-serif">Not photo-aligned · terrain and neighbors absent</text>')
    parts.append('<text x="30" y="804" font-size="14" font-family="sans-serif">Exploratory assumptions · zoning and building fit unverified</text></svg>')
    return '\n'.join(parts)+'\n'


def exports(ir):
    mesh=obj(ir);geometry_hash=digest(dumps(ir).encode())
    eligible=ir['visual_handoff_status']=='schematic_reference_only'
    handoff={'version':'0.1.0','module':'geometry-visual-handoff','site_bbl':ir['site_bbl'],
             'geometry_ir_sha256':geometry_hash,'mesh_sha256':digest(mesh.encode()),'analysis_sha256':ir['analysis_sha256'],
             'geometry_file':'geometry.json','mesh_file':'massing.obj','reference_views':['plan.svg','massing.svg'],
             'status':ir['visual_handoff_status'],'eligible_as_schematic_reference':eligible,
             'generation_executed':False,'existing_photo_renderer_compatible':False,
             'camera':'Fixed schematic axonometric; no photo registration',
             'blockers':[c['quantity']+' area mismatch' for c in ir['comparisons'] if c['status']=='mismatch'],
             'unverified':list(ir['review_gates']),
             'prompt':('Illustrate the attached explicit massing geometry. Preserve its silhouette, floor count and footprint changes. Use a neutral schematic setting: no existing neighbors or street/photo alignment has been established. Label exploratory assumed massing; zoning and building fit unverified. Any visual deviation requires review.' if eligible else None),
             'required_review':'Inspect generated silhouette, floor count, footprint changes and viewpoint against the mesh; no fidelity acceptance exists yet.'}
    output=io.StringIO();w=csv.writer(output,lineterminator='\n')
    w.writerow(['floor_id','base_z_ft','top_z_ft','gross_floor_proxy_sf','nonresidential_proxy_sf','residential_proxy_sf'])
    for f in ir['floors']:w.writerow([f[k] for k in ['id','base_z_ft','top_z_ft','gross_floor_proxy_sf','nonresidential_proxy_sf','residential_proxy_sf']])
    rows=['# Grounded exploratory massing: '+ir['site_bbl'],'',
          '**'+ir['visual_handoff_status']+'**. Design assumptions, not a zoning envelope or professionally validated design.','',
          '## Geometry and analysis agreement','','| Quantity | Geometry proxy sf | Analysis sf | Difference sf | Status |','| --- | --- | --- | --- | --- |']
    for c in ir['comparisons']:rows.append('| '+c['quantity']+' | '+f"{c['geometry_proxy_sf']:.2f}"+' | '+f"{c['analysis_target_sf']:.2f}"+' | '+f"{c['difference_sf']:.2f}"+' | '+c['status']+' |')
    s=ir['source_geometry']
    rows += ['', '## Source and assumptions','',
             'Mapped source: NYC DCP MapPLUTO '+str(s['source_version'])+'. BBL matches the verified analysis. Original bytes, exact query, metadata and retrieval receipts are in parcel-source/.',
             '',f"Mapped polygon area: {s['mapped_polygon_area_sf']:.2f} sf. Source recorded lot area: {s['recorded_lot_area_sf']:.2f} sf. Difference: {s['mapped_minus_recorded_sf']:.2f} sf; unreconciled observations, not a correction.",'',
             'Assumed floor count: '+str(len(ir['floors']))+'. Assumed total height: '+str(ir['total_height_ft'])+' international feet. Coordinates and rationales are in scenario.json. No height or footprint was inferred from the source photo.',
             '', 'The 40,000-sf example dimensions were selected to match the area budget algebraically. A match is a consistency test, not independent validation. Gross polygon area and fractional use allocation are simplified proxies, not code-compliant measured areas or architectural layouts.',
             '', 'All review gates remain unknown: '+', '.join(ir['review_gates'])+'.',
             '', '## Inspect the outputs','',
             '![Mapped parcel and assumed plates](plan.svg)','', '![Schematic massing](massing.svg)','',
             '[Floor schedule](floor-schedule.csv) · [Geometry IR](geometry.json) · [Mesh](massing.obj) · [Visual handoff](visual-handoff.json)','',
             'analysis-run/ retains the complete original verified analysis. This geometry module has not changed its assumptions, calculated homes or review gates. No photorealistic image was generated.']
    md='\n'.join(rows)+'\n'
    comparisons=''.join('<tr>'+''.join('<td>'+html.escape(str(c[k]))+'</td>' for k in ['quantity','geometry_proxy_sf','analysis_target_sf','difference_sf','status'])+'</tr>' for c in ir['comparisons'])
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Grounded exploratory massing</title><style>body{font:17px/1.5 system-ui;max-width:1150px;margin:32px auto;padding:20px;color:#223542}img{width:49%;vertical-align:top}table{border-collapse:collapse;display:block;overflow:auto}td,th{border:1px solid #ccd3d8;padding:8px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.5 system-ui}@media(max-width:700px){img{width:100%}}</style><h1>Grounded exploratory massing: '+ir['site_bbl']+'</h1><p><strong>'+ir['visual_handoff_status']+'</strong> · assumed design; all professional review gates unknown.</p><table><tr><th>Quantity</th><th>Geometry proxy sf</th><th>Analysis sf</th><th>Difference sf</th><th>Status</th></tr>'+comparisons+'</table><img src="plan.svg" alt="Mapped parcel with assumed floor plates"><img src="massing.svg" alt="Schematic assumed building massing"><h2>Evidence, assumptions and limits</h2><pre>'+html.escape(md)+'</pre><p><a href="geometry.json">Geometry IR</a> · <a href="massing.obj">OBJ mesh</a> · <a href="floor-schedule.csv">Floor schedule</a> · <a href="visual-handoff.json">Visual handoff</a> · <a href="scenario.json">Scenario assumptions</a></p></html>\n'
    return {'geometry.json':dumps(ir),'massing.obj':mesh,'plan.svg':svg(ir,'plan'),'massing.svg':svg(ir,'axonometric'),
            'floor-schedule.csv':output.getvalue(),'packet.md':md,'packet.html':page,'visual-handoff.json':dumps(handoff)}
