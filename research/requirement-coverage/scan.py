"""Independent source-region enumeration, not semantic completeness certification. MIT."""
import hashlib,json,pathlib,re
BASE=pathlib.Path(__file__).resolve().parent;ROOT=BASE.parents[1]
def norm(s):return ' '.join(s.split())
def fp(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
SCOPES={'west169':{'submission':[26,27,28,29,30,31,32]},'stanns':{'submission':[22,23,24,25,26,27]}}
def discover(sources):
    units=[]
    for doc in sources['sources']:
        path=ROOT/doc['text'];raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=doc['text_sha256']:raise ValueError('Changed source text')
        pages=raw.decode().split('\f');case=doc['case'];tab='';optional=False
        if doc['id'].endswith('_rfp'):
            for pn in SCOPES[case]['submission']:
                page=re.sub(r'\n\s*\d+\s*$','',pages[pn-1])
                # Ignore preceding material at start of the detailed-content section.
                if case=='stanns' and pn==22:page=page[page.index('TAB A'):]
                for block in re.split(r'\n\s*\n',page):
                    s=norm(block)
                    if not s or s.isdigit() or len(s)<20:continue
                    heading=re.search(r'\bTAB\s+([A-N])\s*[–−-]',s,re.I)
                    if heading:
                        tab=heading.group(1).upper();optional='optional' in s.lower()
                        if len(s)<100:continue
                    if s.lower()=='optional:':optional=True;continue
                    if case=='west169' and '\uf06f' not in block:continue
                    segments=re.split('\uf06f',block) if case=='west169' else [block]
                    if case=='west169':
                        if 'optional:' in segments[0].lower():optional=True
                        segments=segments[1:]
                    for segment in segments:
                        quote=norm(segment)
                        if len(quote)<25 or quote.isdigit():continue
                        # The source page, tab and exact text determine identity; registry does not.
                        key=fp({'source':doc['id'],'page':pn,'quote':quote})[:16]
                        units.append({'id':doc['id']+':'+key,'case':case,'source_id':doc['id'],'pdf_page':pn,'quote':quote,'kind':'submission_segment','tab':tab,'optional_context':optional})
        else:
            for pn,page in enumerate(pages,1):
                marks=list(re.finditer(r'\bQ(\d+)\s*:',page))
                for n,mark in enumerate(marks):
                    end=marks[n+1].start() if n+1<len(marks) else len(page)
                    quote=norm(page[mark.start():end]);quote=re.sub(r'\s+\d+$','',quote)
                    units.append({'id':f"{doc['id']}:Q{mark.group(1)}",'case':case,'source_id':doc['id'],'pdf_page':pn,'quote':quote,'kind':'addendum_question','question':int(mark.group(1)),'tab':'','optional_context':False})
    ids=[u['id'] for u in units]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate source anchor requires reconciliation')
    return units
if __name__=='__main__':
    ss=json.loads((ROOT/'research/eligibility-gates/sources.json').read_text());units=discover(ss)
    (BASE/'outputs/source-units.json').write_text(json.dumps({'scope':SCOPES,'limits':['Text segments are review units, not necessarily atomic requirements.','Question continuations across pages and referenced appendices require separate review.'],'units':units},indent=2)+'\n')
    for case in SCOPES:print(case,[(k,sum(u['case']==case and u['kind']==k for u in units)) for k in ['submission_segment','addendum_question']])
