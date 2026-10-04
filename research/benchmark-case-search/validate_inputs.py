"""Enforce the declared document boundary without claiming full historical certification. MIT."""
import datetime,hashlib,json,pathlib
P=pathlib.Path(__file__).resolve().parent

def check_document_date(doc,cutoff):
    cutoff=datetime.date.fromisoformat(cutoff)
    if datetime.date.fromisoformat(doc['declared_issue_date'])>cutoff:raise ValueError('Document issued after cutoff')
    for key in ['pdf_creation','pdf_modified']:
        value=doc.get(key)
        if not value:raise ValueError('Missing date metadata requires explicit version review')
        if datetime.datetime.strptime(value,'%a %b %d %H:%M:%S %Y %Z').date()>cutoff:raise ValueError('PDF metadata postdates cutoff; reconcile version before promotion')

def validate():
    base=P/'inputs';m=json.loads((base/'manifest.json').read_text());allowed={'manifest.json','task.md'}
    for doc in m['input_sources']:
        check_document_date(doc,m['cutoff'])
        for file_key,hash_key in [('file','pdf_sha256'),('text_file','text_sha256')]:
            name=doc[file_key]
            if pathlib.Path(name).name!=name:raise ValueError('Input path escapes controlled folder')
            allowed.add(name);b=(base/name).read_bytes()
            if hashlib.sha256(b).hexdigest()!=doc[hash_key]:raise ValueError('Input bytes changed: '+name)
        text=(base/doc['text_file']).read_text()
        cover=' '.join(text.split('\f')[0].split())
        date=datetime.date.fromisoformat(doc['declared_issue_date']);expected=f'{date.strftime("%B")} {date.day}, {date.year}'
        if expected not in cover:raise ValueError('Declared issue date not supported on cover')
    if {f.name for f in base.iterdir()}!=allowed:raise ValueError('Unallowlisted file in analyst inputs; possible reference leakage')
    if m['historical_bytes_certified']:raise ValueError('No independent historical snapshot supports certification')
    if not m['curator_exposed_to_outcomes'] or not m['analyst_requires_fresh_context']:raise ValueError('Discovery exposure cannot be hidden')
    return {'document_input_integrity':'pass','pdfs':len(m['input_sources']),'cutoff':m['cutoff'],'certified_historical_backtest':'blocked','reasons':['Exact historical byte equivalence not independently established','Historical zoning, market and parcel data not yet assembled'],'experiment':'not_run','expert_usefulness':'not_tested'}
if __name__=='__main__':
    result=validate();(P/'input-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
