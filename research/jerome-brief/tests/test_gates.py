"""Behavioral rejection tests for evidence promotion and review validity. MIT."""
import copy,importlib.util,pathlib,sys,unittest
P=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
import build,validate
class EvidenceGates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.case=build.load('case.json');cls.ir=build.bind(cls.case)
    def test_unknown_cannot_be_zero(self):
        case=copy.deepcopy(self.case);next(c for c in case['claims'] if c['id']=='finance')['value']=0
        with self.assertRaises(validate.InvalidPacket):validate.validate_case(case)
    def test_gate_cannot_be_removed(self):
        case=copy.deepcopy(self.case);case['requirements']=case['requirements'][:-1]
        with self.assertRaises(validate.InvalidPacket):validate.validate_case(case)
    def test_failed_source_cannot_support_claim(self):
        case=copy.deepcopy(self.case);c=next(c for c in case['claims'] if c['id']=='program');c['evidence']['source_id']='zoning_mih_bronx'
        with self.assertRaisesRegex(ValueError,'Failed source'):build.bind(case)
    def test_quote_scope_rejects_wrong_page(self):
        case=copy.deepcopy(self.case);next(c for c in case['claims'] if c['id']=='agency_current_units')['evidence']['locator']='PDF page 6'
        with self.assertRaisesRegex(ValueError,'Quote not found'):build.bind(case)
    def test_agency_unit_count_cannot_be_overridden(self):
        case=copy.deepcopy(self.case);next(c for c in case['claims'] if c['id']=='agency_rezone_units')['value']=100
        with self.assertRaisesRegex(ValueError,'Numeric passage extraction mismatch'):build.bind(case)
    def test_recorded_numeric_value_cannot_be_overridden(self):
        case=copy.deepcopy(self.case);next(c for c in case['claims'] if c['id']=='lot_area')['value']=7000
        with self.assertRaisesRegex(ValueError,'Numeric extraction mismatch'):build.bind(case)
    def test_changed_assumption_invalidates_old_reviews(self):
        case=copy.deepcopy(self.case);next(c for c in case['claims'] if c['id']=='analysis_no_action')['reason']+=' altered'
        new=build.bind(case);review=self.complete('A','Advisor One');self.assertIn('stale packet fingerprint',validate.review_errors(review,new))
    def complete(self,slot,name):
        r=build.review_template(slot,self.ir);r.update(status='completed',reviewer_name=name,expertise='Housing',reviewed_at='2026-10-04',independent_first_pass=True,disposition='accept_for_second_site',answers={key:'Scoped feedback supplied' for key,_ in build.QUESTIONS});return r
    def test_same_reviewer_is_not_two_independent_advisors(self):
        reviews=[self.complete('A','Same Person'),self.complete('B',' same person ')];self.assertFalse(validate.gates(self.ir,reviews)['second_site_workflow']['allowed'])
    def test_two_workflow_reviews_do_not_approve_project(self):
        reviews=[self.complete('A','Advisor One'),self.complete('B','Advisor Two')];g=validate.gates(self.ir,reviews);self.assertTrue(g['second_site_workflow']['allowed']);self.assertFalse(g['agency_proposal']['allowed'])
    def test_missing_answer_blocks_review_acceptance(self):
        r=self.complete('A','Advisor One');r['answers']['zoning']=None;self.assertIn('missing answer zoning',validate.review_errors(r,self.ir))
    def test_empty_environment_screen_stays_unknown(self):
        by={c['id']:c for c in self.ir['claims']};self.assertEqual(by['e_screen']['value'],0);self.assertIsNone(by['environment']['value'])
    def test_pending_reviews_block_second_site_gate(self):
        g=validate.gates(self.ir,[build.review_template(s,self.ir) for s in ['A','B']]);self.assertTrue(g['advisor_packet']['allowed']);self.assertFalse(g['second_site_workflow']['allowed'])
    def test_missing_financial_inputs_remain_null(self):
        self.assertTrue(all(v is None for v in build.load('finance-inputs.json')['inputs'].values()))
if __name__=='__main__':unittest.main()
