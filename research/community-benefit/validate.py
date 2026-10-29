"""Research bibliography/backlog integrity only; not source interpretation. MIT."""
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent

def load(name):return json.loads((ROOT/name).read_text())

def main():
    bibliography=load('sources.json');sources=bibliography['sources'];ids={s['id'] for s in sources}
    if len(ids)!=len(sources):raise ValueError('Duplicate reference ID')
    for s in sources:
        if urlparse(s['url']).scheme!='https' or not s['inspection_extent'] or not s['limits']:raise ValueError('Unscoped research reference')
        if s['integration_status']!='research_reference_not_integrated':raise ValueError('Research reference promoted to integration')
    backlog=load('methods.json');methods=backlog['methods']
    if len({m['id'] for m in methods})!=len(methods):raise ValueError('Duplicate method ID')
    for m in methods:
        if m['implementation_status']!='not_implemented' or m['professional_review']!='pending':raise ValueError('Backlog promoted to validated implementation')
        if not set(m['source_ids'])<=ids or not m['blocked_interpretations']:raise ValueError('Unresolved method references/limits')
    receipts=load('retrievals.json')
    for r in receipts:
        if r['source_id'] not in ids or r['status']!='retrieved' or r['http_status']!=200 or len(r['sha256'])!=64:raise ValueError('Invalid research retrieval metadata')
        if r!=next(s['byte_receipt'] for s in sources if s['id']==r['source_id']):raise ValueError('Retrieval differs from source register')
    print(f'PASS: {len(sources)} references, {len(receipts)} retrieval receipts, {len(methods)} unimplemented candidate methods. Metadata integrity only; no benefit estimator or expert acceptance.')

if __name__=='__main__':main()
