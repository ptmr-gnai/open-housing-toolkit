"""Validate retained fingerprints and portable deterministic replay. MIT."""
import json,pathlib,tempfile
from engine import BASE,ROOT,compile_case,sha
from build import build

def validate():
    manifest=json.loads((BASE/'outputs/manifest.json').read_text())
    for name,h in manifest['files'].items():
        if sha((ROOT/name).read_bytes())!=h:raise ValueError('Changed build input: '+name)
    for name,h in manifest['outputs'].items():
        if sha((BASE/'outputs'/name).read_bytes())!=h:raise ValueError('Changed output: '+name)
    sources=json.loads((BASE/'sources.json').read_text());count=0;citations=0
    for file in (BASE/'cases').glob('*.json'):
        case=json.loads(file.read_text());compiled=compile_case(case,sources);count+=len(case['gates']);citations+=sum(len(g['citations']) for g in case['gates'])
        if compiled['fingerprint']!=manifest['case_fingerprints'][case['id']]:raise ValueError('Stale compiled case')
    with tempfile.TemporaryDirectory() as tmp:
        target=pathlib.Path(tmp);build(target)
        expected={p.name for p in (BASE/'outputs').iterdir()};observed={p.name for p in target.iterdir()}
        if expected!=observed:raise ValueError('Replay file inventory differs')
        for name in sorted(expected):
            if (target/name).read_bytes()!=(BASE/'outputs'/name).read_bytes():raise ValueError('Non-identical replay: '+name)
    return {'source_documents':len(sources['sources']),'cases':len(manifest['case_fingerprints']),'typed_gates':count,'exact_page_citations':citations,'replay':'byte_identical','source_integrity':'pass','actual_readiness':'blocked','expert_acceptance':'not_tested','independent_holdout':'not_run','historical_certification':'unverified'}
if __name__=='__main__':print(json.dumps(validate(),indent=2))
