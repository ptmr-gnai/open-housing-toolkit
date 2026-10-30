"""Create a page-hash source catalogue from actual DCP PDFs. Preparation only. MIT."""
from pathlib import Path
import argparse,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from housing_workflow.contracts import digest,save
from housing_common.local_outputs import destination
from housing_benefit.contracts import read_json


def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    destination(a.out)
    if a.out.exists():raise ValueError('Catalogue already exists')
    docs=[]
    for r in read_json(a.pdf_dir/'retrievals.json'):
        raw=(a.pdf_dir/(r['id']+'.pdf')).read_bytes()
        if r['status']!='retrieved' or digest(raw)!=r['sha256'] or not raw.startswith(b'%PDF-'):raise ValueError('PDF/retrieval binding changed')
        proc=subprocess.run(['pdftotext','-layout',str(a.pdf_dir/(r['id']+'.pdf')),'-'],capture_output=True,check=True)
        pages=proc.stdout.decode().split('\f')
        if not pages[-1].strip():pages.pop()
        stamp={'guide':'7/1/25 | Subject to Change','form':'06/09/23','criteria':'Printed date unresolved: [Publish Date] placeholder'}[r['id']]
        if (r['id'] in {'guide','form'} and stamp.split(' | ')[0] not in pages[0]) or (r['id']=='criteria' and '[Publish Date]' not in ''.join(pages)):raise ValueError('Source date stamp changed; review catalogue adapter')
        docs.append({**r,'version_stamp':stamp,'source_pdf_availability':'external_not_bundled','pages':[{'pdf_page':i+1,'normalized_text_sha256':digest(' '.join(text.split()).encode())} for i,text in enumerate(pages)]})
    tool=subprocess.run(['pdftotext','-v'],capture_output=True,check=True).stderr.decode().splitlines()[0]
    save(a.out,{'version':'0.1.0','extraction_tool_version':tool,'extraction_method':'pdftotext-layout-normalized-page-hashes@1','preparation_script_sha256':digest(Path(__file__).read_bytes()),'sources':docs,'scope':'Actual PDFs checked during preparation; normal replay validates metadata/page bindings, not external source re-extraction or interpretation.'})

if __name__=='__main__':main()
