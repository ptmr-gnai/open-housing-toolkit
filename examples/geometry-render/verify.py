"""Verify a saved geometry-reference image experiment; not image fidelity. MIT."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from housing_workflow.contracts import digest,load
from housing_workflow.engine import safe
from housing_geometry.engine import verify


def main():
    folder=Path(__file__).resolve().parent;manifest=load(folder/'manifest.json')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!=set(manifest['files'])|{'manifest.json'}:raise ValueError('Experiment inventory changed')
    for name,h in manifest['files'].items():
        if digest(safe(folder,name).read_bytes())!=h:raise ValueError('Experiment artifact changed: '+name)
    brief=load(folder/'brief.json');source=safe(ROOT,brief['source_run']);verify(source)
    if not load(source/'visual-handoff.json')['eligible_as_schematic_reference']:raise ValueError('Source handoff is blocked')
    for name,h in brief['source_bindings'].items():
        if digest(safe(source,name).read_bytes())!=h:raise ValueError('Source geometry binding changed')
    for name,h in brief['references'].items():
        if digest(safe(folder,name).read_bytes())!=h:raise ValueError('Reference binding changed')
    if digest((folder/'prompt.txt').read_bytes())!=brief['prompt_sha256']:raise ValueError('Prompt changed')
    invocation=load(folder/'invocation.json')
    if invocation['brief_sha256']!=digest((folder/'brief.json').read_bytes()) or invocation['prompt_sha256']!=brief['prompt_sha256']:raise ValueError('Invocation binding changed')
    if invocation['parameters']['referenced_image_paths']!=list(brief['references']):raise ValueError('Invocation references differ')
    if invocation['output_file']!='render.png' or invocation['output_sha256']!=digest((folder/'render.png').read_bytes()):raise ValueError('Output binding changed')
    review=load(folder/'review.json')
    if review['image_sha256']!=invocation['output_sha256'] or review['overall']!='illustrative_only_not_metric_validation':raise ValueError('Review binding changed')
    print('PASS: source, prompt, references, invocation, output and review bindings; geometric fidelity unverified.')

if __name__=='__main__':main()
