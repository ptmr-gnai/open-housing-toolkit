import copy
import json
from pathlib import Path
import tempfile
import unittest
from housing_workflow import contracts as c, engine, model, packet, router

EXAMPLE=engine.ROOT/'examples/parcel-investigation'
REQ=c.load(EXAMPLE/'request.json')

def payloads(parcel='2028710002'):
    return {
        'pluto':[{'bbl':parcel+'.00000000','address':'TEST SITE','lotarea':'10000','unitsres':'0'}],
        'dob_bis':[{'bbl':parcel,'job__':'old-job','doc__':'01','proposed_dwelling_units':'9','pre__filing_date':'02/13/2003','job_description':'Historical proposal, not current occupancy.'}],
        'dob_now':[], 'hpd_violations':[]}

def transport(data, failed=None):
    def call(url):
        sid=next(s for s,v in router.REGISTRY.items() if '/'+v['dataset']+'.json?' in url)
        if sid==failed:return 200,b'{"error":true,"message":"not an array"}'
        return 200,json.dumps(data[sid]).encode()
    return call

def make_run(folder,req=None,data=None,failed=None):
    req=copy.deepcopy(req or REQ)
    engine.fresh(folder);c.save(folder/'request.json',req)
    router.collect(req,folder,transport=transport(data or payloads(),failed))
    engine.build(folder)
    return c.load(folder/'ir.json')

class Workflow(unittest.TestCase):
    def test_real_demo_preserves_historical_housing_signal(self):
        engine.verify(EXAMPLE)
        ir=c.load(EXAMPLE/'ir.json');claims={x['id']:x for x in ir['claims']}
        self.assertEqual(claims['pluto.0.unitsres']['value'],'0')
        self.assertTrue(any(claims[i]['value']=='9' for i in ir['housing_signal_claims']))
        self.assertEqual(claims['review.housing_signals']['value'],'reconciliation_needed')
        self.assertEqual(claims['scenario.home_equivalents']['value'],34)
    def test_second_live_example_has_no_invented_scenario(self):
        second=engine.ROOT/'examples/jerome-evidence-only'
        engine.verify(second)
        ir=c.load(second/'ir.json')
        self.assertEqual(ir['resolved_bbl'],'2028560051')
        self.assertIsNone(ir['scenario_name'])
        self.assertNotIn('scenario.home_equivalents',{x['id'] for x in ir['claims']})
    def test_schema_contracts(self):
        import jsonschema
        jsonschema.validate(REQ,c.load(engine.ROOT/'housing_workflow/request.schema.json'))
        jsonschema.validate(c.load(EXAMPLE/'ir.json'),c.load(engine.ROOT/'housing_workflow/ir.schema.json'))
    def test_replay_is_byte_identical_in_a_new_directory(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.replay(EXAMPLE,root)
            for name in c.load(EXAMPLE/'manifest.json')['files']:
                self.assertEqual((root/name).read_bytes(),(EXAMPLE/name).read_bytes(),name)
    def test_changed_assumption_recomputes_and_rebinds_prompt(self):
        req=copy.deepcopy(REQ);req['scenario']['average_net_home_sf']['value']=680
        req['scenario']['average_net_home_sf']['rationale']='Explicit sensitivity test.'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.replay(EXAMPLE,root,req)
            ir=c.load(root/'ir.json');claims={x['id']:x for x in ir['claims']}
            self.assertEqual(claims['scenario.home_equivalents']['value'],40)
            self.assertEqual(claims['unknown.physical_fit']['value'],None)
            brief=c.load(root/'image-prompts.json')
            self.assertEqual(next(x['value'] for x in brief['bindings'] if x['claim_id']=='scenario.home_equivalents'),40)
            self.assertNotEqual(brief['model_sha256'],c.load(EXAMPLE/'image-prompts.json')['model_sha256'])
    def test_evidence_only_does_not_invent_scenario(self):
        req=copy.deepcopy(REQ);req['scenario']=None
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root,req)
            self.assertNotIn('scenario.home_equivalents',{x['id'] for x in ir['claims']})
            self.assertEqual(c.load(root/'image-prompts.json')['bindings'],[])
            engine.verify(root)
    def test_http_200_error_is_unknown_not_empty_success(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root,failed='dob_now')
            self.assertEqual(next(x for x in ir['sources'] if x['source']=='dob_now')['status'],'failed')
            self.assertIn('source.dob_now.unknown',{x['id'] for x in ir['claims']})
            self.assertNotIn('dob_now.returned_rows',{x['id'] for x in ir['claims']})
            engine.verify(root)
    def test_truncated_records_preserve_incomplete_coverage(self):
        data=payloads();data['dob_now']=[{'bbl':REQ['bbl'],'job_filing_number':str(i)} for i in range(501)]
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root,data=data)
            self.assertIn('source.dob_now.coverage',{x['id'] for x in ir['claims']})
            self.assertTrue(next(x for x in ir['sources'] if x['source']=='dob_now')['truncated'])
    def test_foreign_parcel_response_rejected_as_evidence(self):
        data=payloads();data['dob_bis'][0]['bbl']='2028560051'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root,data=data)
            self.assertEqual(next(x for x in ir['sources'] if x['source']=='dob_bis')['status'],'failed')
            self.assertFalse(ir['housing_signal_claims'])
    def test_reusing_evidence_for_different_parcel_rejected(self):
        req=copy.deepcopy(REQ);req['bbl']='2028560051'
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,'different parcel'):engine.replay(EXAMPLE,Path(d)/'run',req)
    def test_missing_receipt_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';make_run(root)
            receipts=c.load(root/'receipts.json');receipts.pop()
            with self.assertRaisesRegex(ValueError,'Missing'):engine.validate_evidence(REQ,receipts,root)
    def test_altered_source_even_with_rehashed_receipt_stales_claims(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root)
            source=root/'sources/pluto.json';data=c.load(source);data[0]['unitsres']='12';c.save(source,data)
            receipts=c.load(root/'receipts.json');r=next(x for x in receipts if x['id']=='pluto')
            r['sha256']=c.digest(source.read_bytes());r['bytes']=source.stat().st_size
            with self.assertRaisesRegex(ValueError,'version-mismatched'):engine.validate_claims(ir,receipts,root)
    def test_corrupted_output_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';make_run(root);(root/'image-prompts.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'hash mismatch'):engine.verify(root)
    def test_removed_unknown_and_cycle_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root);receipts=c.load(root/'receipts.json')
            unknown=next(x for x in ir['claims'] if x['id']=='unknown.physical_fit');unknown['value']='cleared'
            with self.assertRaisesRegex(ValueError,'promoted'):engine.validate_claims(ir,receipts,root)
            unknown['value']=None;unknown['inputs']=['unknown.physical_fit']
            with self.assertRaisesRegex(ValueError,'cycle'):engine.validate_claims(ir,receipts,root)
    def test_invalid_scenario_and_formula_rejected(self):
        for value in [float('nan'),True,-1,0]:
            req=copy.deepcopy(REQ);req['scenario']['average_net_home_sf']['value']=value
            with self.assertRaises(ValueError):c.validate_request(req)
        with self.assertRaisesRegex(ValueError,'Unknown formula'):model.calculate('__import__',[1,2])
    def test_input_question_does_not_become_html(self):
        with tempfile.TemporaryDirectory() as d:
            req=copy.deepcopy(REQ);req['question']='<script>alert(1)</script> [bad](javascript:alert)'
            root=Path(d)/'run';make_run(root,req)
            page=(root/'packet.html').read_text()
            self.assertNotIn('<script>',page);self.assertNotIn('href="javascript:',page)
    def test_address_resolution_is_unique_or_blocked(self):
        req=copy.deepcopy(REQ);del req['bbl'];req['address']='1240 Edward L Grant Highway'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';ir=make_run(root,req)
            self.assertEqual(ir['resolved_bbl'],REQ['bbl'])
            engine.verify(root)
        data=payloads();data['pluto']*=2
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,'ambiguous'):make_run(Path(d)/'run',req,data)
    def test_existing_runs_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';make_run(root)
            with self.assertRaisesRegex(ValueError,'new empty'):make_run(root)
    def test_source_paths_cannot_escape_packet(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';make_run(root)
            with self.assertRaisesRegex(ValueError,'escapes'):engine.safe(root,'../secret')
    def test_unsupported_jurisdiction_and_arbitrary_urls_rejected(self):
        for value in ['1000010001',"2' OR 1=1",'https://example.com']:
            with self.assertRaises(ValueError):router.parcel_url('pluto',value)
        req=copy.deepcopy(REQ);req['api_url']='https://example.com'
        with self.assertRaisesRegex(ValueError,'Unsupported'):c.validate_request(req)

if __name__=='__main__':unittest.main()
