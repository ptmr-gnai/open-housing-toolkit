#!/usr/bin/env python3
"""Offline byte-for-byte replay gate. MIT."""
import json,pathlib,tempfile
import pipeline

with tempfile.TemporaryDirectory() as directory:
    out=pathlib.Path(directory)
    ir=pipeline.build(pipeline.ROOT/'probe.json')
    pipeline.export(ir,out,pipeline.ROOT/'probe.json')
    files=['ir.json','shortlist.csv','dossiers.json','probe-report.md','advisor-brief.md','advisor-explorer.html','media-draft.md']
    for name in files:
        if (out/name).read_bytes()!=(pipeline.ROOT/'outputs'/name).read_bytes():
            raise ValueError('Offline replay differs: '+name)
print(json.dumps({'status':'passed','byte_identical_outputs':len(files)}))
