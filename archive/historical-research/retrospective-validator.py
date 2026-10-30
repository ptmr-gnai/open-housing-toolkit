"""Validate immutable input/output boundary and source locators. Not semantic approval. MIT."""
import hashlib,json,pathlib
P=pathlib.Path(__file__).resolve().parent
I=P.parent/'benchmark-case-search'/'inputs'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
def validate_claims(data):
    claims=data['claims'];ids=[c['id'] for c in claims]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate claim id')
    sources={d['file']:d for d in json.loads((I/'manifest.json').read_text())['input_sources']}
    citations=0
    for c in claims:
        if c['kind'] not in {'agency_statement','calculation','inference','assumption','unknown'}:raise ValueError('Invalid kind')
        if not c['statement'].strip() or not c['citations']:raise ValueError('Untraced claim')
        for ref in c['citations']:
            if ref['file'] not in sources:raise ValueError('Source outside allowlist')
            pages=(I/sources[ref['file']]['text_file']).read_text().split('\f')
            page=ref['pdf_page']
            if type(page)!=int or not 1<=page<=sources[ref['file']]['pdf_pages']:raise ValueError('Invalid PDF page')
            quote=norm(ref['exact_quote'])
            if len(quote)<12 or quote not in norm(pages[page-1]):raise ValueError('Quote missing from cited page: '+c['id'])
            citations+=1
        if c['kind']=='calculation' and not c.get('dependencies'):raise ValueError('Untraced calculation')
        if any(d not in ids for d in c.get('dependencies',[])):raise ValueError('Unknown dependency')
    graph={c['id']:c.get('dependencies',[]) for c in claims};seen=set();active=set()
    def visit(n):
        if n in active:raise ValueError('Dependency cycle')
        if n in seen:return
        active.add(n)
        for d in graph[n]:visit(d)
        active.remove(n);seen.add(n)
    for n in graph:visit(n)
    return {'claims':len(claims),'page_matched_citations':citations}
def check_frozen(base,files):
    for name,h in files.items():
        if digest(base/name)!=h:raise ValueError("Frozen analyst output changed")
def validate():
    pre=json.loads((P/'precommit.json').read_text())
    root=P.parents[1]
    for name,h in pre['files'].items():
        if digest(root/name)!=h:raise ValueError('Input changed: '+name)
    if digest(P/'rubric.json')!=pre['rubric_sha256']:raise ValueError('Rubric changed after precommit')
    result=validate_claims(json.loads((P/'claims.json').read_text()))
    access=json.loads((P/'access-log.json').read_text())
    allowed={str(p.resolve()):digest(p) for p in I.iterdir()}
    for r in access['reads']:
        if r['file'] not in allowed or r['sha256']!=allowed[r['file']]:raise ValueError('Declared access outside boundary or bad hash')
    if (P/'freeze.json').exists():
        freeze=json.loads((P/'freeze.json').read_text())
        check_frozen(P,freeze['files'])
        if digest(P/'validate.py')!=freeze['validator_sha256'] or digest(P/'freeze.py')!=freeze['freeze_code_sha256']:raise ValueError('Frozen validation code changed')
    result.update({'technical_boundary':'pass','access_enforcement':'self-reported instruction boundary, not OS sandbox','semantic_accuracy':'requires evaluator review','practitioner_utility':'not_tested','historical_certification':'blocked'})
    return result
if __name__=='__main__':
    result=validate();(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
