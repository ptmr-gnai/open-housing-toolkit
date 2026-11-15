"""Counterexamples for broad nonhousing discovery and retained source composition. MIT."""
import copy
import json
from pathlib import Path
import runpy
import tempfile
import unittest
from housing_discovery import collection
from housing_site_discovery import context, engine, evidence, model
from housing_site_discovery.common import ROOT,bbl,digest,dumps,load,save,seal,validate_request

# Reuse the explicitly synthetic inventory fixture without changing its retained module.
base_fixture=runpy.run_path(str(ROOT/'tests/housing_discovery/test_discovery.py'))['fixture']

def fixture(folder,active=False):
    base_fixture(folder,active=active)
    receipts=load(folder/'receipts.json');row=receipts[2]
    raw=load(folder/row['body_path'])
    for item in raw:item['zonedist1']='R7-1'
    save(folder/row['body_path'],raw);body=(folder/row['body_path']).read_bytes()
    row.update(sha256=digest(body),bytes=len(body));save(folder/'receipts.json',receipts)
    save(folder/'inventory.json',collection.derive(folder))
    from housing_discovery.common import seal as old_seal
    old_seal(folder,'inventory')
    return folder


def request():return load(ROOT/'config/site-discovery/jerome.json')


def supplement(folder,inv):
    import shutil
    folder.mkdir();shutil.copytree(inv,folder/'inventory');(folder/'sources').mkdir()
    save(folder/'request.json',request())
    records=load(inv/'inventory.json')['records']['pluto'];rows=[]
    for item in records:
        row=copy.deepcopy(item['row']);row.update(resarea='0',zonedist1='R7-1')
        rows.append(row)
    ids=[bbl(x['bbl']) for x in rows];receipts=[]
    meta={'id':'64uk-42ks','rowsUpdatedAt':1,'columns':[{'fieldName':x,'dataTypeName':'number' if x=='bbl' else 'text'} for x in evidence.FIELDS]}
    for params,data in [(None,meta),(evidence.queries(ids)[0],rows),(None,meta)]:
        rid=str(len(receipts));path=f'sources/{rid}-pluto.json';body=dumps(data).encode();(folder/path).write_bytes(body)
        receipts.append({'id':rid,'provider':'pluto','url':collection.url('pluto',params),'params':params,'status':'ok','body_path':path,'sha256':digest(body),'bytes':len(body),'retrieved_at':'2026-11-09T00:00:00+00:00'})
    save(folder/'receipts.json',receipts);save(folder/'zoning-records.json',evidence.derive(folder));seal(folder,'evidence');return folder


class Discovery(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name)
        self.inv=fixture(self.base/'inventory');self.source=supplement(self.base/'supplement',self.inv)
        self.inventory=load(self.inv/'inventory.json');self.supp=load(self.source/'zoning-records.json')
        self.req=request();self.guidance=load(ROOT/'src/housing_site_discovery/guidance.json')

    def tearDown(self):self.temp.cleanup()

    def evaluate(self):return model.evaluate(self.inventory,self.supp,self.req,self.guidance)

    def test_nonhousing_does_not_require_auto_use_extra_far_size_or_private_mission(self):
        ir=self.evaluate();rows={r['bbl']:r for r in ir['lots']}
        self.assertEqual(ir['counts']['recorded_nonhousing'],4)
        self.assertTrue(rows['2020000001']['in_recorded_nonhousing_set']) # school retained in review lane
        self.assertTrue(rows['2020000002']['in_recorded_nonhousing_set']) # already FAR 6, no extra FAR
        self.assertTrue(rows['2020000005']['in_recorded_nonhousing_set']) # missing area doesn't exclude land
        self.assertEqual(rows['2020000002']['zoning_path']['path'],'housing_permitted_by_general_use_rule')
        self.assertEqual(len(ir['lots']),5)
        self.assertTrue(all(r['unresolved']['net_new_homes'] is None for r in ir['lots']))

    def test_large_sites_and_zero_residential_far_are_preserved(self):
        row=self.supp['records']['2020000003']['row'];row.update(lotarea='500000',residfar='0',affresfar='0',zonedist1='C8-3',landuse='7')
        target=next(r for r in self.evaluate()['lots'] if r['bbl']=='2020000003')
        self.assertTrue(target['in_recorded_nonhousing_set']);self.assertEqual(target['review_lane'],'other_nonhousing_review')
        self.assertEqual(target['zoning_path']['path'],'rezoning_path')

    def test_accommodation_and_residential_evidence_dont_become_empty_nonhousing(self):
        for row in [{'unitsres':'0','bldgclass':'O8','landuse':'5'},{'unitsres':'0','bldgclass':'RH','landuse':'5'},{'unitsres':'0','bldgclass':'H4','landuse':'5'},{'unitsres':'0','bldgclass':'R2','landuse':'5'},
                    {'unitsres':'0','bldgclass':'I1','landuse':'8'},{'unitsres':None,'bldgclass':'G2','landuse':'7'},
                    {'unitsres':'0','resarea':'600','bldgclass':'G2','landuse':'7'}]:
            category,_=model.current_use(row);self.assertNotEqual(category,'recorded_nonhousing')

    def test_nonresidential_condos_and_land_remain_visible_with_shared_site_review(self):
        category,reasons=model.current_use({'unitsres':'0','resarea':'0','bldgclass':'R5','landuse':'5'})
        self.assertEqual(category,'recorded_nonhousing');self.assertIn('nonresidential_condominium_class_shared_site_review',reasons)
        self.assertEqual(model.current_use({'unitsres':'0','bldgclass':'V0','landuse':'11'})[0],'recorded_nonhousing')

    def test_special_split_paired_overlay_and_geographic_exceptions_get_review(self):
        for raw,borough in [({'zonedist1':'R7-1','spdist2':'J'},'BX'),({'zonedist1':'R7-1','zonedist3':'M1-2'},'BX'),
                            ({'zonedist1':'M1-2/R6A'},'BX'),({'zonedist1':'M1-1D'},'BX'),({'zonedist1':'M1-1'},'QN'),
                            ({'zonedist1':'C1-2'},'BX'),({'zonedist1':'PARK'},'BX'),({},'BX')]:
            with self.subTest(raw=raw):self.assertEqual(model.zoning(raw,borough,[])['path'],'special_or_unresolved_review')
        self.assertEqual(model.zoning({'zonedist1':'M1-2'},'BX',[])['path'],'rezoning_path')
        self.assertEqual(model.zoning({'zonedist1':'R7-1','overlay1':'C2-4'},'BX',[])['path'],'housing_permitted_by_general_use_rule')

    def test_missing_supplement_or_snapshot_changes_are_unknown_not_clean_paths(self):
        self.supp['records'].pop('2020000003')
        target=next(r for r in self.evaluate()['lots'] if r['bbl']=='2020000003')
        self.assertEqual(target['zoning_path']['path'],'special_or_unresolved_review')
        self.supp['records']['2020000002']['changed_since_inventory']=['unitsres']
        target=next(r for r in self.evaluate()['lots'] if r['bbl']=='2020000002')
        self.assertEqual(target['current_use_category'],'current_use_unresolved')

    def test_active_and_missing_context_are_review_flags_not_admission_gates(self):
        inv=fixture(self.base/'active',active=True)
        self.inventory=load(inv/'inventory.json');self.inventory['context_complete']['colp']=False
        target=next(r for r in self.evaluate()['lots'] if r['bbl']=='2020000003')
        self.assertTrue(target['in_recorded_nonhousing_set'])
        self.assertIn('active_or_on_hold_zap_project_review',target['flags']);self.assertIn('colp_context_incomplete',target['flags'])

    def test_supplement_query_identity_and_coverage_cannot_be_rehashed_away(self):
        receipts=load(self.source/'receipts.json');receipts[1]['params']['$where']='bbl in (2020000003)'
        receipts[1]['url']=collection.url('pluto',receipts[1]['params']);save(self.source/'receipts.json',receipts)
        with self.assertRaisesRegex(ValueError,'exact inventory'):evidence.derive(self.source)

    def test_verify_recomputes_ir_and_packets(self):
        out=self.base/'result';engine.build(self.source,self.req,out)
        self.assertEqual(engine.verify(out)['recorded_nonhousing'],4)
        ir=load(out/'ir.json');ir['lots'][0]['in_recorded_nonhousing_set']=False;save(out/'ir.json',ir);seal(out,'discovery')
        with self.assertRaisesRegex(ValueError,'recomputation'):engine.verify(out)

    def test_explicit_handoff_is_not_limited_to_display_examples_and_invents_no_program(self):
        req=copy.deepcopy(self.req);req['display_per_group']=1
        out=self.base/'result';engine.build(self.source,req,out)
        engine.handoff(out,['2020000002'],self.base/'handoff')
        self.assertIsNone(load(self.base/'handoff/requests.json')[0]['scenario'])
        with self.assertRaisesRegex(ValueError,'nonhousing'):engine.handoff(out,['2020000004'],self.base/'bad')

    def test_unknown_fields_geography_and_shipped_destinations_block(self):
        req=copy.deepcopy(self.req);req['scenario']={'far':6}
        with self.assertRaises(ValueError):validate_request(req)
        with self.assertRaisesRegex(ValueError,'read-only'):engine.build(self.source,self.req,ROOT/'examples/no')
        req=copy.deepcopy(self.req);req['scope']['bbox'][0]-=.001
        with self.assertRaisesRegex(ValueError,'Geography'):model.evaluate(self.inventory,self.supp,req,self.guidance)

    def test_optional_public_context_does_not_change_admission_and_null_is_unknown(self):
        ir=self.evaluate();self.assertTrue(all(r['public_context']['nearest_station'] is None for r in ir['lots']))
        raw={'latitude':'40','longitude':'-74'}
        pack={'stations':{'complete':False},'industrial_zones':{'complete':False}}
        result=context.annotate(raw,pack)
        self.assertIsNone(result['industrial_zone_point_matches']);self.assertIsNone(result['nearest_station'])

    def test_distance_and_polygon_holes_boundaries_and_multipolygons(self):
        self.assertAlmostEqual(context.distance_m(40,-74,40,-74),0)
        self.assertGreater(context.distance_m(40,-74,40.01,-74),1100)
        shape={'type':'Polygon','coordinates':[[[0,0],[10,0],[10,10],[0,10],[0,0]],[[3,3],[7,3],[7,7],[3,7],[3,3]]]}
        for pt,want in [((1,1),'inside'),((5,5),'outside'),((3,5),'boundary_review'),((0,5),'boundary_review'),((-1,5),'outside')]:
            self.assertEqual(context.geometry_relation(pt,shape),want)
        multi={'type':'MultiPolygon','coordinates':[shape['coordinates'],[[[20,20],[21,20],[21,21],[20,21],[20,20]]]]}
        self.assertEqual(context.geometry_relation((20.5,20.5),multi),'inside')


def context_fixture(folder,source):
    folder.mkdir();(folder/'sources').mkdir()
    inv=load(source/'inventory/inventory.json');ids=[bbl(x['row']['bbl']) for x in inv['records']['pluto']]
    save(folder/'universe.json',{'scope':inv['scope'],'bbls':ids,'evidence_manifest_sha256':digest((source/'manifest.json').read_bytes())})
    station_meta={'rowsUpdatedAt':1,'columns':[{'fieldName':k,'dataTypeName':'number' if k in ['station_id','gtfs_latitude','gtfs_longitude'] else 'text'} for k in context.STATION_FIELDS]}
    stations=[{'station_id':'1','gtfs_stop_id':stop,'stop_name':'TEST PLATFORM '+stop,'gtfs_latitude':'40.84','gtfs_longitude':'-73.92','daytime_routes':'TEST','ada':'0'} for stop in ['A1','B1']]
    ibz_meta={'name':'IBZs','serviceItemId':'f89585b18b88472fa563a68abd95b567','editingInfo':{'lastEditDate':1}}
    gft_meta={'name':'Green_Fast_Track_Lots','serviceItemId':'095fbe2e10b544a4974c5b4026d7f70a','editingInfo':{'lastEditDate':1},'fields':[{'name':k,'type':'esriFieldTypeString'} for k in ['bbl','zoning_district','special_coastal_risk_flag','industrial_lots_flag']]}
    data={'mta_metadata_before':station_meta,'mta_metadata_after':station_meta,
          'mta_count_before':[{'n':'2'}],'mta_count_after':[{'n':'2'}],'mta_stations':stations,
          'ibz_portal':{'id':'GfwWNkhOj9bNBqoJ','name':'NYC DCP Mapping Portal'},
          'ibz_item':{'id':'f89585b18b88472fa563a68abd95b567','orgId':'GfwWNkhOj9bNBqoJ'},
          'ibz_metadata_before':ibz_meta,'ibz_metadata_after':ibz_meta,'ibz_count':{'count':1},
          'ibz_features':{'type':'FeatureCollection','features':[{'type':'Feature','properties':{'FID':0,'NAME':'TEST IBZ'},'geometry':{'type':'Polygon','coordinates':[[[-74,40],[-73,40],[-73,41],[-74,41],[-74,40]]]}}]},
          'ibz_policy':'TEST SOURCE ONLY',
          'gft_metadata_before':gft_meta,'gft_metadata_after':gft_meta,'gft_versions_metadata':{},
          'gft_versions':{'features':[{'attributes':{'schema_name':'dcp_mappluto_wi','v':'TEST VINTAGE'}}]},
          'gft_lots_0':{'features':[{'attributes':{'bbl':identity,'zoning_district':'R8','industrial_lots_flag':'Yes','special_coastal_risk_flag':'No'}} for identity in ids]}}
    receipts=[]
    for name,url in context.source_urls(ids).items():
        body=data[name].encode() if isinstance(data[name],str) else dumps(data[name]).encode()
        path='sources/'+name+('.html' if name=='ibz_policy' else '.json');(folder/path).write_bytes(body)
        receipts.append({'id':name,'url':url,'status':'ok','body_path':path,'sha256':digest(body),'bytes':len(body),'retrieved_at':'2026-11-09T00:00:00+00:00'})
    save(folder/'receipts.json',receipts);save(folder/'context.json',context.derive(folder));seal(folder,'context');return folder


class PublicContext(unittest.TestCase):
    setUp=Discovery.setUp
    tearDown=Discovery.tearDown
    def test_paired_mta_records_remain_and_tie_breaks_on_gtfs_stop_id(self):
        folder=context_fixture(self.base/'context',self.source)
        result=load(folder/'context.json');self.assertTrue(result['stations']['complete'])
        self.assertEqual(len(result['stations']['records']),2)
        row=context.annotate({'bbl':'2020000003','latitude':'40.84','longitude':'-73.92'},result)
        self.assertEqual(row['nearest_station']['gtfs_stop_id'],'A1');self.assertEqual(row['nearest_station']['straight_line_m'],0)
        self.assertEqual(row['industrial_zone_point_relation'],'inside')
        self.assertEqual(row['green_fast_track']['positive_publisher_flags'],['industrial_lots_flag'])

    def test_cross_vintage_district_disagreement_becomes_review_without_exclusion(self):
        folder=context_fixture(self.base/'context',self.source)
        ir=model.evaluate(self.inventory,self.supp,self.req,self.guidance,load(folder/'context.json'))
        row=next(r for r in ir['lots'] if r['bbl']=='2020000003')
        self.assertTrue(row['in_recorded_nonhousing_set']);self.assertEqual(row['zoning_path']['path'],'special_or_unresolved_review')
        self.assertIn('cross_source_zoning_difference_review',row['flags'])

    def test_truncated_context_is_unknown_and_missing_fast_track_record_is_not_clear(self):
        folder=context_fixture(self.base/'context',self.source)
        receipts=load(folder/'receipts.json')
        def change(name,data):
            receipt=next(r for r in receipts if r['id']==name);save(folder/receipt['body_path'],data);body=(folder/receipt['body_path']).read_bytes();receipt.update(sha256=digest(body),bytes=len(body))
        change('ibz_features',{'type':'FeatureCollection','exceededTransferLimit':True,'features':[]})
        change('gft_lots_0',{'features':[]});save(folder/'receipts.json',receipts)
        result=context.derive(folder);self.assertFalse(result['industrial_zones']['complete'])
        self.assertTrue(result['fast_track']['query_coverage_complete']);self.assertEqual(len(result['fast_track']['missing_bbls']),5)
        row=context.annotate({'bbl':'2020000003','latitude':'40.84','longitude':'-73.92'},result)
        self.assertIsNone(row['industrial_zone_point_matches']);self.assertIsNone(row['green_fast_track'])

    def test_context_from_different_evidence_cannot_be_composed(self):
        folder=context_fixture(self.base/'context',self.source)
        origin=load(folder/'universe.json');origin['evidence_manifest_sha256']='0'*64;save(folder/'universe.json',origin);seal(folder,'context')
        with self.assertRaisesRegex(ValueError,'evidence differ'):engine.build(self.source,self.req,self.base/'bad',folder)

    def test_context_projection_recomputation_and_tamper_detection(self):
        folder=context_fixture(self.base/'context',self.source)
        out=self.base/'complete';engine.build(self.source,self.req,out,folder)
        self.assertEqual(engine.verify(out)['recorded_nonhousing'],4)
        path=out/'public-context/context.json';data=load(path);data['stations']['complete']=False;save(path,data);seal(out/'public-context','context');seal(out,'discovery')
        with self.assertRaisesRegex(ValueError,'replay'):engine.verify(out)

    def test_unknown_request_properties_are_rejected_by_schema(self):
        import jsonschema
        schema=load(ROOT/'src/housing_site_discovery/request.schema.json');jsonschema.validate(self.req,schema)
        req=copy.deepcopy(self.req);req['scenario']={'far':6}
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(req,schema)

if __name__=='__main__':unittest.main()
