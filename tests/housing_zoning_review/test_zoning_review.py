"""Counterexamples for monthly zoning-record completeness and conflicts. MIT."""
import copy
from pathlib import Path
import tempfile
import unittest
from housing_common.packages import digest,dumps,save
from housing_common.public_sources import PublicJSON
from housing_zoning_review.engine import FIELDS,PROVIDERS,apply,derive,queries


def parent():
    return {'counts':{'inventory':2,'recorded_nonhousing':2},'lots':[{'bbl':'2020000001','in_recorded_nonhousing_set':True,'flags':[],
            'zoning_path':{'path':'housing_permitted_by_general_use_rule','recorded_districts':['R8'],'recorded_special_districts':[],'recorded_overlays':[],'review_reasons':[]}},
            {'bbl':'2020000002','in_recorded_nonhousing_set':True,'flags':[],
             'zoning_path':{'path':'rezoning_path','recorded_districts':['C8-3'],'recorded_special_districts':[],'recorded_overlays':[],'review_reasons':[]}}]}


def fixture(root,rows=None,updated_after=1,after_version='20260930'):
    (root/'parent').mkdir();(root/'sources').mkdir();save(root/'parent/ir.json',parent())
    ids=[x['bbl'] for x in parent()['lots']];receipts=[]
    if rows is None:rows=[{'bbl':ids[0],'zoning_district_1':'R8'},{'bbl':ids[1],'zoning_district_1':'C8-3'}]
    meta=lambda updated,version:{'id':'fdkv-4t4z','rowsUpdatedAt':updated,'description':'Current version: '+version,'columns':[{'fieldName':f,'dataTypeName':'number' if f=='bbl' else 'text'} for f in FIELDS]}
    client=PublicJSON.__new__(PublicJSON);client.providers=PROVIDERS
    for i,(params,data) in enumerate([(None,meta(1,'20260930')),(queries(ids)[0],rows),(None,meta(updated_after,after_version))]):
        body=dumps(data).encode();name=f'sources/{i}-nyztl.json';(root/name).write_bytes(body)
        receipts.append({'id':str(i),'provider':'nyztl','url':client.url('nyztl',params),'params':params,'status':'ok','body_path':name,'sha256':digest(body),'bytes':len(body)})
    save(root/'receipts.json',receipts)


class ZoningReview(unittest.TestCase):
    def test_source_agreement_does_not_turn_into_professional_clearance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root);r=derive(root);ir=apply(parent(),r)
            self.assertTrue(r['metadata_stable'])
            self.assertEqual(ir['lots'][0]['zoning_record_review']['status'],'recorded_sources_agree_on_compared_fields')
            self.assertEqual(ir['lots'][0]['zoning_path']['path'],'housing_permitted_by_general_use_rule')
            self.assertIn('not a new cadastral intersection',r['meaning'])

    def test_full_districts_and_specials_reconciled_without_silent_override(self):
        rows=[{'bbl':'2020000001','zoning_district_1':'R8','zoning_district_2':'M1-2','special_district_1':'MX','commercial_overlay_1':'C2-4'}]
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root,rows);ir=apply(parent(),derive(root));row=ir['lots'][0]
            self.assertEqual(row['zoning_path']['recorded_districts'],['R8'])
            self.assertEqual(row['zoning_path']['path'],'special_or_unresolved_review')
            self.assertEqual(set(row['zoning_record_review']['differences']),{'districts_differ','special_districts_differ','commercial_overlays_differ'})
            self.assertEqual(ir['lots'][1]['zoning_record_review']['query_coverage'],'no_returned_record')
            self.assertEqual(len(ir['lots']),2)

    def test_source_drift_or_missing_version_is_unknown(self):
        for updated,version in [(2,'20260930'),(1,'20261031'),(1,'unknown')]:
            with self.subTest(updated=updated,version=version),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);fixture(root,updated_after=updated,after_version=version);review=derive(root)
                self.assertFalse(review['metadata_stable'])
                self.assertEqual(apply(parent(),review)['lots'][0]['zoning_record_review']['status'],'unresolved')

    def test_duplicate_bbl_is_review_and_not_a_last_row_selection(self):
        rows=[{'bbl':'2020000001','zoning_district_1':'R8'},{'bbl':'2020000001','zoning_district_1':'M1-2'}]
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root,rows);review=derive(root);ir=apply(parent(),review)
            self.assertEqual(review['coverage_by_bbl']['2020000001'],'multiple_returned_records')
            self.assertEqual(ir['lots'][0]['zoning_record_review']['recorded_districts'],[])

    def test_changed_query_and_response_outside_batch_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root,rows=[{'bbl':'2020009999'}])
            with self.assertRaisesRegex(ValueError,'unrequested'):derive(root)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root);import json
            receipts=json.loads((root/'receipts.json').read_text());receipts[1]['params']['$where']='bbl in (2020000001)';save(root/'receipts.json',receipts)
            with self.assertRaisesRegex(ValueError,'exact upstream'):derive(root)

    def test_unreceipted_source_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root);(root/'sources/unreceipted.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'source file inventory'):derive(root)

    def test_cap_is_missing_coverage_not_successful_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root,rows=[{'bbl':'2020000001'}]*101);review=derive(root)
            self.assertEqual(set(review['coverage_by_bbl'].values()),{'batch_row_cap_requires_review'})
            self.assertTrue(all(x['zoning_path']['path']=='special_or_unresolved_review' for x in apply(parent(),review)['lots']))


if __name__=='__main__':unittest.main()
