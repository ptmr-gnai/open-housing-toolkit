"""Verify saved photomontage bindings; not placement or image fidelity. MIT."""
from pathlib import Path
import runpy
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from housing_workflow.contracts import digest,load
from housing_workflow.engine import safe


def main():
    folder=Path(__file__).resolve().parent;m=load(folder/'manifest.json')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!=set(m['files'])|{'manifest.json'}:raise ValueError('Experiment inventory changed')
    for name,h in m['files'].items():
        if digest(safe(folder,name).read_bytes())!=h:raise ValueError('Changed experiment artifact: '+name)
    runpy.run_path(str(ROOT/'examples/geometry-render/verify.py'),run_name='__main__')
    r=load(folder/'invocation.json')
    for name,h in r['design_source_bindings'].items():
        if digest(safe(ROOT,name).read_bytes())!=h:raise ValueError('Design-source binding changed')
    if r['prompt_sha256']!=digest((folder/'prompt.txt').read_bytes()) or r['output_sha256']!=digest((folder/'render.png').read_bytes()):raise ValueError('Invocation/output binding changed')
    if r['parameters']!={'num_last_images_to_include':2,'transparent_background':False}:raise ValueError('Invocation reference selector changed')
    if r['photo_reference']['sha256'] is not None or r['source_photo_byte_bound']:raise ValueError('External photo cannot claim a local byte binding')
    review=load(folder/'review.json')
    if review['image_sha256']!=r['output_sha256'] or review['overall']!='illustrative_with_observed_fidelity_issues':raise ValueError('Review binding changed')
    print('PASS: photomontage bindings; photo bytes, camera registration and geometric fidelity remain unverified.')

if __name__=='__main__':main()
