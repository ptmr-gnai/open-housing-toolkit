"""Byte integrity and deterministic replay of bounded coverage outputs. MIT."""
import json,pathlib,tempfile
from scan import BASE,ROOT
from build_coverage import build
import engine as eligibility

def validate():
    m=json.loads((BASE/'outputs/manifest.json').read_text())
    for name,h in m['files'].items():
        if eligibility.sha((ROOT/name).read_bytes())!=h:raise ValueError('Changed input: '+name)
    for name,h in m['outputs'].items():
        if eligibility.sha((BASE/'outputs'/name).read_bytes())!=h:raise ValueError('Changed output: '+name)
    with tempfile.TemporaryDirectory() as folder:
        p=pathlib.Path(folder);result=build(p)
        if {f.name for f in p.iterdir()}!={f.name for f in (BASE/'outputs').iterdir()}:raise ValueError('Replay inventory differs')
        for f in p.iterdir():
            if f.read_bytes()!=(BASE/'outputs'/f.name).read_bytes():raise ValueError('Replay bytes differ: '+f.name)
    return {**result,'replay':'byte_identical','actual_proposal':'not_supplied','expert_review':'pending','practitioner_utility':'not_tested'}
if __name__=='__main__':print(json.dumps(validate(),indent=2))
