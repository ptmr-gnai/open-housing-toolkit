"""Prepare a small reference pack from an independently retrieved RER PDF. MIT.

Requires Poppler pdftotext for this preparation step only. Source PDF is external;
offline comparison replay uses the retained selected passages and extraction receipt.
"""
import argparse
from pathlib import Path
import re
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from housing_workflow.contracts import digest,load,save
from housing_workflow.engine import fresh
from housing_benefit.sources import URL,validate_source


def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--retrievals',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    r=next(r for r in load(a.retrievals) if r['source_id']=='nyc-rer-guide')
    raw=a.pdf.read_bytes()
    if not raw.startswith(b'%PDF-') or digest(raw)!=r['sha256'] or r['requested_url']!=URL or r['status']!='retrieved':raise ValueError('PDF differs from actual original retrieval receipt')
    proc=subprocess.run(['pdftotext','-layout',str(a.pdf),'-'],capture_output=True,check=True)
    page=proc.stdout.decode().split('\f')[5];normal=' '.join(page.split())
    title='Table 3: Affordable rents and eligible incomes (2025 AMI)'
    if title not in normal or '1-person - 4-person' not in normal or 'Studio Two-bedroom' not in normal:raise ValueError('Unsupported table/year/column layout')
    rows=[]
    for ami in [30,60]:
        match=re.search(r'\b'+str(ami)+r'% AMI (\$[0-9,]+) (\$[0-9,]+) (\$[0-9,]+) (\$[0-9,]+)',normal)
        if not match:raise ValueError('Cannot extract selected income/rent row')
        rows.append(match[0])
    if '7/1/25' not in page:raise ValueError('Unexpected source document stamp')
    fresh(a.out);passages=title+'\n'+'\n'.join(rows)+'\n';(a.out/'passages.txt').write_text(passages)
    version=subprocess.run(['pdftotext','-v'],capture_output=True,check=True).stderr.decode().splitlines()[0]
    save(a.out/'receipt.json',{'version':'0.1.0','method':'nyc-rer-table3-selected-rows@1','url':URL,'publisher':'NYC Department of City Planning','document_stamp':'7/1/25 | Subject to Change','income_year':2025,'rent_year':2025,'page':6,'source_pdf_sha256':r['sha256'],'source_pdf_availability':'external_not_bundled','source_bytes':len(raw),'retrieved_at_utc':r['retrieved_at_utc'],'passages_sha256':digest(passages.encode()),'column_order':['ami_percent','one_person_income_usd','four_person_income_usd','studio_rent_usd','two_bedroom_rent_usd'],'extraction':{'tool':version,'command':'pdftotext -layout INPUT.pdf -; page 6; normalized selected row extraction','script_sha256':digest(Path(__file__).read_bytes()),'checked_against_pdf_at_preparation':True},'terms_url':'https://www.nyc.gov/home/terms-of-use.page'})
    validate_source(a.out);print('Prepared source-bound 2025 reference excerpts; external PDF not bundled.')

if __name__=='__main__':main()
