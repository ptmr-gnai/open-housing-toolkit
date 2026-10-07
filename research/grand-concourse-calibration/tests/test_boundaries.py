import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

B = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('grand_validate', B/'validate.py')
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

class Boundaries(unittest.TestCase):
    def test_retained_claims(self):
        sources = {x['id']:x for x in json.loads((B/'sources.json').read_text())}
        for c in json.loads((B/'early-assessment.json').read_text())['facts']:
            v.check_claim(c, sources, required_role='input')
    def test_quote_and_reference_injection(self):
        sources = {x['id']:x for x in json.loads((B/'sources.json').read_text())}
        c = json.loads((B/'comparison.json').read_text())['claims'][0]
        with self.assertRaisesRegex(ValueError,'leakage'):v.check_claim(c,sources,required_role='input')
        c=copy.deepcopy(c);c['quote']='The project is fully funded and legally approved.'
        with self.assertRaisesRegex(ValueError,'resolve'):v.check_claim(c,sources)
    def test_source_revision_invalidates_quotes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'source.text').write_text('Changed account of site risk')
            with self.assertRaisesRegex(ValueError,'resolve'):
                v.check_claim({'source':'s','quote':'No ground risk'}, {'s':{'text':'source.text','role':'input'}},p)
    def test_capital_baseline_cannot_disappear(self):
        self.assertAlmostEqual(v.capital_required(45965346.7,45651124.197426),91616470.897426)
        self.assertEqual(v.capital_required(45965346.7,0),45965346.7)
    def test_cost_scope_and_vintage_required(self):
        self.assertFalse(v.comparable_costs({'amount':178000000},{'amount':121942998}))
        self.assertFalse(v.comparable_costs({'scope':'total','price_year':2022,'area_definition':'gross'},{'scope':'unresolved','price_year':2022,'area_definition':'gross'}))
        a={'scope':'total','price_year':2022,'area_definition':'gross'}
        self.assertTrue(v.comparable_costs(a,a))
    def test_studio_exception_not_noncompliance(self):
        self.assertEqual(v.mix_review(45,277,.15,False),'needs_program_evidence')
        self.assertEqual(v.mix_review(45,277,.15,True),'exception_supported')
    def test_area_is_not_a_layout(self):
        self.assertEqual(v.capacity_status(False,False,True),'illustration_only')
        with self.assertRaises(ValueError):v.ratio(100,0)

if __name__=='__main__':unittest.main()
