"""Housing-signal review counterexamples; synthetic records only. MIT."""
from pathlib import Path
import tempfile
import unittest
from housing_site_review import engine
from housing_site_discovery.common import bbl,digest,dumps,load,save


class Review(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);(self.root/'discovery').mkdir();(self.root/'sources').mkdir()
        self.ids=['2020000001','2020000002']
        self.ir={'lots':[{'bbl':x,'address':'TEST '+x,'flags':[],'in_recorded_nonhousing_set':True,'current_use_category':'recorded_nonhousing'} for x in self.ids]+[{'bbl':'2020000003','address':'TEST HOUSING','flags':[],'in_recorded_nonhousing_set':False,'current_use_category':'housing_recorded'}]}
        save(self.root/'discovery/ir.json',self.ir);self.receipts=[]

    def tearDown(self):self.temp.cleanup()

    def record(self,provider,params,data,status='ok'):
        rid=str(len(self.receipts));row={'id':rid,'provider':provider,'url':engine.url(provider,params),'params':params,'status':status}
        if data is not None:
            body=dumps(data).encode();path=f'sources/{rid}-{provider}.json';(self.root/path).write_bytes(body);row.update(body_path=path,sha256=digest(body),bytes=len(body))
        self.receipts.append(row);save(self.root/'receipts.json',self.receipts)

    def meta(self,provider,version=1):
        return {'id':engine.REGISTRY[provider]['dataset'],'rowsUpdatedAt':version,'columns':[{'fieldName':f,'dataTypeName':'number' if (engine.REGISTRY[provider]['join']=='bbl_number' and f=='bbl') or (engine.REGISTRY[provider]['join']=='borough_block_lot' and f in ['boroid','block','lot']) else 'text'} for f in engine.REGISTRY[provider]['fields']]}

    def full(self,bis_rows=None,now_rows=None,failed=False,changed=False,split=False,reg_rows=None,prod_rows=None):
        rows_by_provider={'dob_bis':bis_rows or [],'dob_now':now_rows or [],'hpd_registrations':reg_rows or [],'hpd_production':prod_rows or []}
        for provider in engine.REGISTRY:
            rows=rows_by_provider[provider]
            self.record(provider,None,self.meta(provider))
            if split and provider=='dob_bis':
                self.record(provider,engine.params(provider,self.ids),[{'bbl':self.ids[0]}]*engine.CAP)
                self.record(provider,engine.params(provider,self.ids[:1]),bis_rows or [])
                self.record(provider,engine.params(provider,self.ids[1:]),[])
            else:
                self.record(provider,engine.params(provider,self.ids),None if failed and provider=='dob_now' else rows,'failed' if failed and provider=='dob_now' else 'ok')
                if failed and provider=='dob_now' and len(self.ids)>5:
                    for child in engine.split(self.ids):self.record(provider,engine.params(provider,child),None,'failed')
            self.record(provider,None,self.meta(provider,2 if changed and provider=='dob_now' else 1))
        return engine.derive(self.root)

    def test_positive_existing_and_proposed_signals_are_historical_and_source_bound(self):
        r=self.full(bis_rows=[{'bbl':self.ids[0],'existing_dwelling_units':'5','proposed_dwelling_units':'6','job__':'TEST1','job_status_descrp':'SIGNED OFF'}])
        row=r['lots'][self.ids[0]];self.assertEqual(row['status'],'positive_returned_housing_signal');self.assertEqual(len(row['positive_signals']),2)
        self.assertEqual(row['positive_signals'][0]['reference']['pointer'],'/0/existing_dwelling_units')
        self.assertIsNone(row['actual_current_homes'])
        self.assertEqual(r['lots'][self.ids[1]]['status'],'no_positive_returned_housing_signal')

    def test_empty_success_unknown_failure_and_missing_numeric_fields_are_distinct(self):
        r=self.full(bis_rows=[{'bbl':self.ids[0],'job__':'TEST'}],failed=True)
        row=r['lots'][self.ids[0]];self.assertEqual(row['status'],'housing_signal_coverage_unknown')
        self.assertEqual(row['coverage_by_source']['dob_bis']['rows_without_any_numeric_dwelling_field'],1)
        self.assertEqual(row['coverage_by_source']['dob_now']['status'],'failed')
        self.assertEqual(r['lots'][self.ids[1]]['coverage_by_source']['dob_bis']['status'],'query_complete_empty')

    def test_before_after_source_update_change_is_unknown(self):
        r=self.full(changed=True)
        self.assertEqual(r['lots'][self.ids[0]]['status'],'housing_signal_coverage_unknown')
        self.assertFalse(r['source_coverage']['dob_now']['metadata_stable'])

    def test_truncated_parent_is_split_and_does_not_duplicate_positive_observations(self):
        r=self.full(bis_rows=[{'bbl':self.ids[0],'existing_dwelling_units':'2'}],split=True)
        self.assertEqual(len(r['lots'][self.ids[0]]['positive_signals']),1)
        self.assertEqual(r['lots'][self.ids[0]]['coverage_by_source']['dob_bis']['status'],'query_complete_rows')
        self.assertEqual(r['lots'][self.ids[1]]['coverage_by_source']['dob_bis']['status'],'query_complete_empty')

    def test_single_lot_cap_remains_unknown_not_a_clean_negative(self):
        self.ids=self.ids[:1];self.ir['lots']=self.ir['lots'][:1];save(self.root/'discovery/ir.json',self.ir)
        r=self.full(bis_rows=[{'bbl':self.ids[0]}]*engine.CAP)
        self.assertEqual(r['lots'][self.ids[0]]['coverage_by_source']['dob_bis']['status'],'truncated')
        self.assertEqual(r['lots'][self.ids[0]]['status'],'housing_signal_coverage_unknown')

    def test_other_bbl_or_changed_query_cannot_be_rehashed_into_valid_coverage(self):
        with self.assertRaisesRegex(ValueError,'different parcel'):self.full(bis_rows=[{'bbl':'2020000999'}])

    def test_all_discovery_lots_and_membership_remain_unchanged(self):
        r=self.full(bis_rows=[{'bbl':self.ids[0],'existing_dwelling_units':'2'}]);out=engine.augment(self.ir,r)
        self.assertEqual([x['bbl'] for x in out['lots']],[x['bbl'] for x in self.ir['lots']])
        self.assertEqual([x['in_recorded_nonhousing_set'] for x in out['lots']],[x['in_recorded_nonhousing_set'] for x in self.ir['lots']])
        self.assertIn('positive_historical_dwelling_signal_requires_reconciliation',out['lots'][0]['flags'])
        self.assertIsNone(out['lots'][-1]['dwelling_review'])
        self.assertNotIn('dwelling_review',self.ir['lots'][0])

    def test_missing_extra_or_duplicate_query_receipts_do_not_pass(self):
        self.full();self.receipts.append(self.receipts[-1]);save(self.root/'receipts.json',self.receipts)
        with self.assertRaisesRegex(ValueError,'duplicate'):engine.derive(self.root)

    def test_retained_raw_import_recomputes_signals_without_new_http(self):
        import shutil
        from unittest.mock import patch
        self.full(bis_rows=[{'bbl':self.ids[0],'existing_dwelling_units':'3'}])
        engine.seal(self.root)
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp);shutil.copytree(self.root/'discovery',out/'discovery')
            shutil.copytree(self.root,out/'imported',ignore=shutil.ignore_patterns('discovery'))
            save(out/'capture-mode.json',{'mode':'retained_raw_replay_with_live_recovery','source_capture_manifest_sha256':digest((self.root/'manifest.json').read_bytes())})
            f=engine.Fetcher(out,None,1,engine.raw_import(out))
            with patch('urllib.request.urlopen',side_effect=AssertionError('Unexpected new HTTP')):
                for provider in engine.REGISTRY:
                    f.fetch(provider);f.fetch(provider,engine.params(provider,self.ids));f.fetch(provider)
            result=engine.derive(out)
            self.assertEqual(result['replayed_receipts'],12);self.assertEqual(result['new_receipts'],0)
            self.assertEqual(result['lots'][self.ids[0]]['status'],'positive_returned_housing_signal')
            self.assertTrue(result['lots'][self.ids[0]]['positive_signals'][0]['reference']['body_path'].startswith('imported/'))
            self.assertEqual(f.attempts,0)

    def test_raw_import_requires_known_runtime_and_original_hashes(self):
        import shutil
        self.full();engine.seal(self.root)
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp);shutil.copytree(self.root/'discovery',out/'discovery');shutil.copytree(self.root,out/'imported',ignore=shutil.ignore_patterns('discovery'))
            manifest=load(out/'imported/manifest.json');manifest['implementation']={};save(out/'imported/manifest.json',manifest)
            with self.assertRaisesRegex(ValueError,'Unrecognized'):engine.raw_import(out)
            manifest['implementation']=engine.implementation();save(out/'imported/manifest.json',manifest)
            (out/'imported/receipts.json').write_text('[]')
            with self.assertRaisesRegex(ValueError,'bytes differ'):engine.raw_import(out)

    def test_failed_multi_lot_batch_has_bounded_smaller_recovery_groups(self):
        ids=[str(2020000000+i) for i in range(1,26)]
        groups=engine.split(ids)
        self.assertEqual([len(g) for g in groups],[5]*5)
        self.assertEqual([x for g in groups for x in g],ids)
        self.assertEqual([len(g) for g in engine.split(ids,capped=True)],[12,13])


    def test_hpd_registration_uses_exact_composite_keys_and_is_not_current_occupancy(self):
        rows=[{'boroid':'2','block':'2000','lot':'1','registrationid':'TEST-R','lastregistrationdate':'2020-01-01','registrationenddate':'2021-01-01'}]
        r=self.full(reg_rows=rows);record=r['lots'][self.ids[0]]
        self.assertEqual(record['status'],'positive_returned_housing_signal')
        self.assertEqual(record['positive_signals'][0]['kind'],'housing_registration_record')
        self.assertIsNone(record['actual_current_homes'])
        self.assertIn('boroid=2 AND block=2000 AND lot=1',engine.params('hpd_registrations',self.ids)['$where'])
        with self.assertRaises(ValueError):engine.row_bbl('hpd_registrations',{'bbl':self.ids[0]})

    def test_hpd_program_record_and_unit_fields_are_historical_not_completion(self):
        r=self.full(prod_rows=[{'bbl':self.ids[1],'project_id':'TEST-P','total_units':'40','project_start_date':'2010-01-01','project_completion_date':None}])
        row=r['lots'][self.ids[1]]
        self.assertEqual(row['status'],'positive_returned_housing_signal')
        self.assertEqual(len(row['positive_signals']),2)
        self.assertEqual(row['positive_signals'][0]['kind'],'affordable_housing_program_record')
        self.assertIsNone(row['actual_current_homes'])


    def test_raw_import_rejects_manifest_traversal_and_symlink_bodies(self):
        import shutil
        self.full();engine.seal(self.root)
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp);shutil.copytree(self.root/'discovery',out/'discovery');shutil.copytree(self.root,out/'imported',ignore=shutil.ignore_patterns('discovery'))
            manifest=load(out/'imported/manifest.json');manifest['files']['discovery/../../outside.txt']='0'*64;save(out/'imported/manifest.json',manifest)
            with self.assertRaisesRegex(ValueError,'Escaping'):engine.raw_import(out)
            external=out/'external.txt';external.write_text('TEST EXTERNAL')
            link=self.root/'sources/link';link.symlink_to(external)
            with self.assertRaisesRegex(ValueError,'Escaping'):engine.safe_path(self.root,'sources/link')

    def test_nested_offline_replay_does_not_freshen_old_metadata_vintage(self):
        import shutil,io
        from unittest.mock import patch
        self.full();engine.seal(self.root)
        def prepare(source,out,offline):
            shutil.copytree(source/'discovery',out/'discovery')
            shutil.copytree(source,out/'imported',ignore=lambda p,n:{'discovery'} if Path(p)==source else set())
            save(out/'capture-mode.json',{'mode':'retained_raw_offline_replay' if offline else 'retained_raw_replay_with_live_recovery','source_capture_manifest_sha256':digest((source/'manifest.json').read_bytes())})
            return engine.Fetcher(out,None,2,engine.raw_import(out),offline)
        def replay(f):
            for provider in engine.REGISTRY:
                f.fetch(provider);f.fetch(provider,engine.params(provider,self.ids));f.fetch(provider)
        class Response(io.BytesIO):
            status=200
            def __enter__(self):return self
            def __exit__(self,*args):self.close()
        with tempfile.TemporaryDirectory() as temp:
            first=Path(temp)/'first';first.mkdir();f=prepare(self.root,first,False)
            f.cache.pop(engine.signature('dob_bis',None))
            with patch('urllib.request.urlopen',side_effect=lambda *a,**k:Response(dumps(self.meta('dob_bis',2)).encode())):replay(f)
            original=engine.derive(first)
            self.assertEqual(original['lots'][self.ids[0]]['status'],'housing_signal_coverage_unknown')
            engine.seal(first)
            second=Path(temp)/'second';second.mkdir();g=prepare(first,second,True)
            with patch('urllib.request.urlopen',side_effect=AssertionError('Offline replay made HTTP')):replay(g)
            repeated=engine.derive(second)
            self.assertEqual(repeated['lots'][self.ids[0]]['status'],'housing_signal_coverage_unknown')
            self.assertEqual(repeated['lots'][self.ids[0]]['coverage_by_source']['dob_bis']['source_rows_updated_at'],1)
            self.assertFalse(repeated['lots'][self.ids[0]]['coverage_by_source']['dob_bis']['metadata_stable'])
            self.assertEqual(g.attempts,0)



if __name__=='__main__':unittest.main()
