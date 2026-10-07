"""Offline artifact integrity and interpretation-boundary checks; not expert validation."""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

def normalize(text):
    return ' '.join(text.split())

def check_claim(claim, sources, root=BASE, required_role=None):
    source = sources[claim['source']]
    if required_role and source['role'] != required_role:
        raise ValueError('source packet leakage')
    text = (root / source['text']).read_text()
    if claim.get('pdf_page'):
        text = text.split('\f')[claim['pdf_page'] - 1]
    if normalize(claim['quote']) not in normalize(text):
        raise ValueError('quote does not resolve')

def ratio(numerator, denominator):
    if denominator <= 0:
        raise ValueError('invalid area denominator')
    return numerator / denominator

def comparable_costs(a, b):
    # No default scope or price vintage; same label alone is insufficient.
    fields = ('scope', 'price_year', 'area_definition')
    return all(a.get(k) is not None and a.get(k) == b.get(k) for k in fields)

def mix_review(studios, total, base_limit, exception_evidence):
    if ratio(studios, total) <= base_limit:
        return 'within_base_limit'
    return 'exception_supported' if exception_evidence else 'needs_program_evidence'

def capacity_status(envelope, layouts, zoning_verified):
    return 'fit_supported' if envelope and layouts and zoning_verified else 'illustration_only'

def capital_required(baseline, additional):
    if baseline < 0 or additional < 0:
        raise ValueError('negative capital requirement')
    return baseline + additional

def validate(root=BASE):
    manifest = json.loads((root / 'manifest.json').read_text())
    for name, expected in manifest['files'].items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError('artifact hash mismatch: ' + name)
    src = json.loads((root / 'sources.json').read_text())
    sources = {s['id']: s for s in src}
    assert len(sources) == len(src)
    early = json.loads((root / 'early-assessment.json').read_text())
    compare = json.loads((root / 'comparison.json').read_text())
    for claim in early['facts']:
        check_claim(claim, sources, root, 'input')
    for claim in compare['claims']:
        check_claim(claim, sources, root, 'reference')
    ids = {c['id'] for c in early['facts'] + compare['claims']}
    assert len(ids) == len(early['facts']) + len(compare['claims'])
    protocol = json.loads((root / 'protocol.json').read_text())
    assert {c['id'] for c in compare['criteria']} == {c['id'] for c in protocol['criteria']}
    for c in compare['criteria']:
        assert c['status'] in {'supported', 'partial', 'failure', 'untestable'}
        assert all(i in ids for i in c['early'] + c['reference'])
    assert all(s['document_date'] <= '2015-09-28' for s in src if s['role'] == 'input')
    assert all(s['historical_bytes_certified'] is False for s in src)
    c = {x['id']: x for x in compare['calculations']}
    assert c['unit_mix_sum']['value'] == 45 + 92 + 94 + 46 == 277
    assert c['selected_to_opened_change']['value'] == 277 - 241
    assert c['lot_area_difference']['value'] == 30049 - 29161
    assert abs(c['studio_share_percent']['value'] - ratio(45,277)*100) < 1e-10
    assert abs(c['three_bed_share_percent']['value'] - ratio(46,277)*100) < 1e-10
    assert abs(c['cost_per_gross_sf']['value'] - ratio(121942998,310758)) < 1e-10
    capital = c['non_debt_illustration']
    assert abs(capital['total'] - capital_required(capital['baseline'], capital['additional'])) < 1e-6
    assert compare['professional_review'] == 'pending' and compare['protocol_deviations']
    return {'status':'passed','early_quotes':len(early['facts']),'reference_quotes':len(compare['claims']),'criteria':len(compare['criteria']),'limits':'No automatic requirement discovery, physical validation, complete underwriting, predictive accuracy or expert acceptance.'}

if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
