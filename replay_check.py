#!/usr/bin/env python3
"""Offline deterministic replay into fresh local scratch; no shipped report writes. MIT."""
import argparse,json,pathlib,tempfile
import pipeline

p=argparse.ArgumentParser();p.add_argument('--run',type=pathlib.Path);args=p.parse_args()
files=['ir.json','shortlist.csv','dossiers.json','probe-report.md','advisor-brief.md','advisor-explorer.html','media-draft.md']
with tempfile.TemporaryDirectory() as directory:
    root=pathlib.Path(directory);first=args.run or root/'first';second=root/'second'
    ir=pipeline.build(pipeline.ROOT/'probe.json')
    if not args.run:pipeline.export(ir,first,pipeline.ROOT/'probe.json')
    pipeline.export(ir,second,pipeline.ROOT/'probe.json')
    for name in files:
        if (first/name).read_bytes()!=(second/name).read_bytes():raise ValueError('Offline replay differs: '+name)
print(json.dumps({'status':'passed','byte_identical_outputs':len(files),'shipped_files_written':False}))
