"""Behavioral counterexamples for discovery coverage, screening and handoff. MIT."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from housing_discovery import collection, engine, screen
from housing_discovery.common import ROOT, bbl, digest, dumps, load, save, seal, validate_request


def request():
    return load(ROOT/'config/discovery/jerome-far6.json')


def fixture(folder, active=False, failed_context=False):
    folder.mkdir();(folder/'sources').mkdir();req=request();save(folder/'request.json',req)
    rows=[]
    for i,area,res,aff,homes,cls,use in [(1,20000,3,3,0,'W1','8'),(2,10000,3,6,0,'K1','5'),(3,15000,0,0,0,'G2','10'),(4,12000,3,6,12,'C1','2'),(5,None,3,3,0,'K1','5')]:
        row={'bbl':str(2020000000+i),'borough':'BX','lotarea':str(area) if area is not None else None,'residfar':str(res),'affresfar':str(aff),'unitsres':str(homes),'bldgclass':cls,'landuse':use,'address':'TEST '+str(i),'ownername':'TEST OWNER','latitude':'40.84','longitude':'-73.92','version':'TEST-FIXTURE'}
        rows.append(row)
    receipts=[]
    def record(provider,params,data,failed=False):
        rid=str(len(receipts));path=f'sources/{rid}-{provider}.json';body=dumps(data).encode();(folder/path).write_bytes(body)
        receipts.append({'id':rid,'provider':provider,'url':collection.url(provider,params),'params':params,'status':'failed' if failed else 'ok','body_path':path,'sha256':digest(body),'bytes':len(body),'retrieved_at':'2026-11-09T00:00:00+00:00'})
    def meta(provider):
        fields=collection.REGISTRY[provider]['fields'];key='project_id' if provider=='zap_projects' else 'bbl'
        return {'id':collection.REGISTRY[provider]['dataset'],'rowsUpdatedAt':1,'columns':[{'fieldName':x,'dataTypeName':'number' if x==key and key=='bbl' else 'text'} for x in fields]}
    pred=collection.predicate(req['scope'])
    record('pluto',None,meta('pluto'));record('pluto',{'$select':'count(*) as n','$where':pred},[{'n':'5'}])
    record('pluto',{'$select':','.join(collection.REGISTRY['pluto']['fields']),'$where':pred,'$order':'bbl','$limit':'1000'},rows)
    record('pluto',{'$select':'count(*) as n','$where':pred},[{'n':'5'}]);record('pluto',None,meta('pluto'))
    for p in ['zap_bbl','zap_projects','colp']:record(p,None,meta(p))
    clause='bbl in ('+','.join(x['bbl'] for x in rows)+')'
    record('zap_bbl',{'$select':','.join(collection.REGISTRY['zap_bbl']['fields']),'$where':clause,'$order':'bbl,project_id','$limit':'2001'},[{'bbl':rows[2]['bbl'],'project_id':'P1','validated':'Y'}] if active else [],failed_context)
    record('colp',{'$select':','.join(collection.REGISTRY['colp']['fields']),'$where':clause,'$order':'bbl','$limit':'2001'},[{'bbl':rows[0]['bbl'],'agency':'DOE','use_type':'SCHOOL'}])
    if active and not failed_context:
        record('zap_projects',{'$select':','.join(collection.REGISTRY['zap_projects']['fields']),'$where':"project_id in ('P1')",'$order':'project_id','$limit':'2001'},[{'project_id':'P1','project_status':'Active','project_name':'TEST ONLY'}])
    save(folder/'receipts.json',receipts);save(folder/'inventory.json',collection.derive(folder));seal(folder,'inventory')
    return folder


class Discovery(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name)
        self.inventory=fixture(self.base/'inventory')
        self.req=request()

    def tearDown(self):self.temp.cleanup()

    def test_zero_residential_far_is_included_and_affordable_far_not_ignored(self):
        result=screen.evaluate(load(self.inventory/'inventory.json'),self.req)
        by={x['bbl']:x for x in result['lots']}
        self.assertEqual(result['shortlist'],['2020000003'])
        self.assertEqual(by['2020000003']['additional_zoning_area_proxy_sf'],90000)
        self.assertEqual(by['2020000002']['baseline_recorded_far_proxy'],6)
        self.assertEqual(by['2020000002']['additional_zoning_area_proxy_sf'],0)
        self.assertIsNone(by['2020000005']['additional_home_equivalents'])
        self.assertTrue(all(x['net_new_homes'] is None for x in result['lots']))

    def test_public_facility_gets_different_mission_without_claiming_vacancy(self):
        req=copy.deepcopy(self.req);req['selection']['mission']='public_or_institutional_review'
        result=screen.evaluate(load(self.inventory/'inventory.json'),req)
        self.assertEqual(result['shortlist'],['2020000001'])
        row=next(x for x in result['lots'] if x['bbl']=='2020000001')
        self.assertIsNone(row['current_occupancy']);self.assertTrue(row['colp_use_records'])

    def test_active_application_and_failed_context_do_not_become_zero(self):
        for active,failed in [(True,False),(False,True)]:
            with self.subTest(active=active,failed=failed):
                inv=fixture(self.base/f'inv-{active}-{failed}',active,failed)
                result=screen.evaluate(load(inv/'inventory.json'),self.req)
                self.assertEqual(result['shortlist'],[])
                self.assertGreater(result['counts']['held'],0)

    def test_incomplete_primary_and_changed_scope_block_ranking(self):
        inv=load(self.inventory/'inventory.json');inv['primary_complete']=False
        with self.assertRaisesRegex(ValueError,'Incomplete inventory'):screen.evaluate(inv,self.req)
        inv=load(self.inventory/'inventory.json');req=copy.deepcopy(self.req);req['scope']['bbox'][0]-=.001
        with self.assertRaisesRegex(ValueError,'geography'):screen.evaluate(inv,req)

    def test_hotel_parks_and_infrastructure_are_not_silently_treated_as_empty_sites(self):
        for cls,use,zoning,hold in [('H4','5','C8-1','occupancy_review'),('Q1','9','PARK','parkland_review'),('U7','7','M1-2','different_mission')]:
            inv=load(self.inventory/'inventory.json')
            row=next(x['row'] for x in inv['records']['pluto'] if bbl(x['row']['bbl'])=='2020000003')
            row.update(bldgclass=cls,landuse=use,zonedist1=zoning)
            result=screen.evaluate(inv,self.req)
            target=next(x for x in result['lots'] if x['bbl']=='2020000003')
            self.assertTrue(any(hold in x for x in target['hold_reasons']))
            self.assertIsNone(target['current_occupancy'])

    def test_auto_business_in_transportation_group_remains_a_private_candidate(self):
        inv=load(self.inventory/'inventory.json')
        row=next(x['row'] for x in inv['records']['pluto'] if bbl(x['row']['bbl'])=='2020000003')
        row.update(bldgclass='G2',landuse='7')
        result=screen.evaluate(inv,self.req)
        target=next(x for x in result['lots'] if x['bbl']=='2020000003')
        self.assertIn(target['bbl'],result['shortlist'])
        self.assertFalse(target['public_or_institutional_signal'])
        self.assertIn('auto_use_in_transportation_landuse_group_requires_current_use_review',target['flags'])

    def test_changed_count_and_missing_context_batch_are_detected(self):
        receipts=load(self.inventory/'receipts.json')
        count=receipts[3];save(self.inventory/count['body_path'],[{'n':'6'}]);body=(self.inventory/count['body_path']).read_bytes();count['sha256']=digest(body);count['bytes']=len(body);save(self.inventory/'receipts.json',receipts)
        self.assertFalse(collection.derive(self.inventory)['primary_complete'])
        receipts=load(self.inventory/'receipts.json');receipts[-1]['params']['$where']='bbl in (2020000001)';receipts[-1]['url']=collection.url('colp',receipts[-1]['params']);save(self.inventory/'receipts.json',receipts)
        with self.assertRaisesRegex(ValueError,'does not cover'):collection.derive(self.inventory)

    def test_unknown_nan_boolean_and_reversed_inputs_are_rejected(self):
        for mutate in [lambda r:r['scenario'].update(proposed_residential_far=True),lambda r:r['scenario'].update(proposed_residential_far=float('nan')),lambda r:r['selection'].update(top_n=0),lambda r:r.update(unknown='x'),lambda r:r['scope'].update(bbox=[-73.9,40.8,-73.92,40.9])]:
            r=copy.deepcopy(self.req);mutate(r)
            with self.assertRaises(ValueError):validate_request(r)

    def test_same_inventory_comparison_retains_all_lots_and_changed_reasons(self):
        left,right=self.base/'left',self.base/'right'
        engine.build(self.inventory,self.req,left)
        other=copy.deepcopy(self.req);other['scenario']['proposed_residential_far']=8;other['id']='TEST-FAR8'
        engine.build(self.inventory,other,right)
        out=self.base/'comparison';engine.compare(left,right,out)
        self.assertIn('2020000002',load(out/'comparison.json')['entered_shortlist'])
        self.assertEqual(len(load(right/'ir.json')['lots']),5)
        self.assertEqual(engine.verify(out)['status'],'passed')

    def test_edited_rank_or_prose_cannot_pass_by_rehashing(self):
        out=self.base/'screen';engine.build(self.inventory,self.req,out)
        ir=load(out/'ir.json');ir['shortlist']=['2020000001'];save(out/'ir.json',ir);seal(out,'screen')
        with self.assertRaisesRegex(ValueError,'recomputation'):engine.verify(out)

    def test_auto_focus_keeps_zero_home_lots_and_preserves_the_full_inventory(self):
        req=copy.deepcopy(self.req);req['scenario']['proposed_residential_far']=8
        out=self.base/'screen';engine.build(self.inventory,req,out)
        focused=self.base/'auto';engine.focus(out,load(ROOT/'config/discovery/focus/auto-parking.json'),focused)
        ir=load(focused/'ir.json')
        self.assertEqual(ir['shortlist'],['2020000003'])
        self.assertEqual(len(ir['lots']),5)
        row=next(x for x in ir['lots'] if x['bbl']=='2020000003')
        self.assertEqual(row['recorded_residential_units'],0)
        comparison=self.base/'focus-compare';engine.compare(out,focused,comparison)
        self.assertIn('2020000002',load(comparison/'comparison.json')['left_shortlist'])
        self.assertEqual(engine.verify(focused)['status'],'passed')

    def test_handoff_preserves_scenario_unknowns_and_blocks_unselected_lots(self):
        out=self.base/'screen';engine.build(self.inventory,self.req,out)
        handoff=self.base/'handoff';engine.handoff(out,handoff,1)
        req=load(handoff/'requests.json')[0]
        self.assertEqual(req['bbl'],'2020000003');self.assertIsNone(req['scenario'])
        with self.assertRaisesRegex(ValueError,'shortlist'):engine.handoff_requests(load(out/'ir.json'),['2020000001'])
        self.assertEqual(engine.verify(handoff)['status'],'passed')

    def test_shipped_outputs_and_completed_runs_are_read_only(self):
        with self.assertRaisesRegex(ValueError,'read-only'):engine.build(self.inventory,self.req,ROOT/'examples/forbidden')
        out=self.base/'screen';engine.build(self.inventory,self.req,out)
        with self.assertRaises(FileExistsError):engine.build(self.inventory,self.req,out)

    def test_project_scope_and_duplicate_receipt_boundaries(self):
        receipts=load(self.inventory/'receipts.json');receipts[-1]['id']=receipts[0]['id'];save(self.inventory/'receipts.json',receipts)
        with self.assertRaisesRegex(ValueError,'receipt identities'):collection.derive(self.inventory)

    def test_schemas_accept_worked_requests_and_reject_extra_properties(self):
        import jsonschema
        schema=load(ROOT/'src/housing_discovery/request.schema.json')
        for path in (ROOT/'config/discovery').glob('*.json'):jsonschema.validate(load(path),schema)
        req=copy.deepcopy(self.req);req['scenario']['made_up_capacity']=3
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(req,schema)


if __name__=='__main__':unittest.main()
