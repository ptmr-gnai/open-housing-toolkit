import importlib.util,pathlib,tempfile,unittest
P=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('run_validator',P/'validate.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
class Boundary(unittest.TestCase):
    def setUp(self):
        self.data={'claims':[{'id':'c1','kind':'agency_statement','statement':'Document identity','citations':[{'file':'97-west-169th-st-rfp.pdf','pdf_page':1,'exact_quote':'December 21, 2018'}]}]}
    def test_exact_page_quote_passes(self):self.assertEqual(v.validate_claims(self.data)['page_matched_citations'],1)
    def test_wrong_page_rejected(self):
        self.data['claims'][0]['citations'][0]['pdf_page']=102
        with self.assertRaisesRegex(ValueError,'Quote missing'):v.validate_claims(self.data)
    def test_unallowlisted_source_rejected(self):
        self.data['claims'][0]['citations'][0]['file']='outcome.pdf'
        with self.assertRaisesRegex(ValueError,'allowlist'):v.validate_claims(self.data)
    def test_invented_quote_rejected(self):
        self.data['claims'][0]['citations'][0]['exact_quote']='Survey proves one hundred homes feasible'
        with self.assertRaisesRegex(ValueError,'Quote missing'):v.validate_claims(self.data)
    def test_cyclic_dependency_rejected(self):
        self.data['claims'][0]['dependencies']=['c1']
        with self.assertRaisesRegex(ValueError,'cycle'):v.validate_claims(self.data)
    def test_frozen_artifact_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            base=pathlib.Path(folder);f=base/'assessment.md';f.write_text('original')
            files={'assessment.md':v.digest(f)};v.check_frozen(base,files)
            f.write_text('rewritten after reveal')
            with self.assertRaisesRegex(ValueError,'Frozen analyst output changed'):v.check_frozen(base,files)
    def test_untraced_calculation_rejected(self):
        self.data['claims'][0]['kind']='calculation'
        with self.assertRaisesRegex(ValueError,'Untraced calculation'):v.validate_claims(self.data)
if __name__=='__main__':unittest.main()
