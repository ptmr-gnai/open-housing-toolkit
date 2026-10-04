import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from validate_inputs import check_document_date
class DateBoundary(unittest.TestCase):
    def test_reexport_after_cutoff_rejected(self):
        doc={'declared_issue_date':'2022-08-18','pdf_creation':'Tue Apr 23 15:45:06 2024 UTC','pdf_modified':'Wed Apr 24 16:11:45 2024 UTC'}
        with self.assertRaisesRegex(ValueError,'metadata postdates'):check_document_date(doc,'2022-11-18')
    def test_pre_cutoff_document_allowed(self):
        doc={'declared_issue_date':'2018-12-21','pdf_creation':'Thu Dec 20 19:41:39 2018 UTC','pdf_modified':'Thu Dec 20 21:12:55 2018 UTC'}
        check_document_date(doc,'2019-04-04')
    def test_post_cutoff_addendum_rejected(self):
        doc={'declared_issue_date':'2019-04-05','pdf_creation':'Thu Dec 20 19:41:39 2018 UTC','pdf_modified':'Thu Dec 20 21:12:55 2018 UTC'}
        with self.assertRaisesRegex(ValueError,'issued after'):check_document_date(doc,'2019-04-04')
if __name__=='__main__':unittest.main()
