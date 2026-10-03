#!/usr/bin/env python3
"""Validate a saved run's code, source and output digests, and evidence graph. MIT."""
import json,pathlib,sys
import pipeline

def validate(out):
    manifest=pipeline.read_json(out/'manifest.json')
    for path,expected in manifest['code_and_config_sha256'].items():
        if pipeline.digest(pipeline.ROOT/path)!=expected:raise ValueError('Changed code/config: '+path)
    ir=pipeline.read_json(out/'ir.json')
    for key,source in ir['sources'].items():
        if source['status']=='ok' and pipeline.digest(pipeline.ROOT/source['cache_path'])!=source['sha256']:
            raise ValueError('Changed source: '+key)
    for path,expected in manifest['output_sha256'].items():
        if pipeline.digest(out/path)!=expected:raise ValueError('Changed output: '+path)
    g=pipeline.Graph(ir['config'],pipeline.ROOT/'probe.json');g.claims=ir['claims'];g.validate()
    summary={'status':'passed','source_hashes_verified':sum(s['status']=='ok' for s in ir['sources'].values()),'claim_graph_verified':len(ir['claims']),'output_hashes_verified':len(manifest['output_sha256']),'professional_acceptance':'pending both advisor reviews'}
    pipeline.write_json(out/'validation.json',summary)
    return summary

if __name__=='__main__':
    out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pipeline.ROOT/'outputs'
    print(json.dumps(validate(out)))
