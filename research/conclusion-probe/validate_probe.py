"""Verify frozen inputs and byte-identical whole-experiment replay. MIT."""
import argparse, json, pathlib, tempfile
from conclusion_engine import BASE, ROOT, check_pinned, sha, load
from run_probe import run

def validate():
    check_pinned();out=BASE/'outputs';m=load(out/'manifest.json')
    for name,h in m['inputs'].items():
        if sha((ROOT/name).read_bytes())!=h: raise ValueError('Changed implementation input: '+name)
    for name,h in m['outputs'].items():
        if sha((out/name).read_bytes())!=h: raise ValueError('Changed output: '+name)
    with tempfile.TemporaryDirectory() as d:
        target=pathlib.Path(d);summary=run(target)
        if {p.name for p in target.iterdir()}!={p.name for p in out.iterdir()}:raise ValueError('Output inventory differs')
        for p in target.iterdir():
            if p.read_bytes()!=(out/p.name).read_bytes():raise ValueError('Replay differs: '+p.name)
    return {**summary,'replay':'byte_identical','independent_human_review':'pending'}

if __name__=='__main__':print(json.dumps(validate(),indent=2))
