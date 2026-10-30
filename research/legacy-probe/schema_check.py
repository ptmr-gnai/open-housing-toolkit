#!/usr/bin/env python3
"""Development validation against published JSON schemas. MIT."""
import json
import argparse
from pathlib import Path
import pipeline
import jsonschema
from referencing import Registry,Resource
from pipeline import ROOT,read_json

play=read_json(ROOT/'schemas/playbook.schema.json')
schema=read_json(ROOT/'schemas/ir.schema.json')
jsonschema.Draft202012Validator.check_schema(play)
jsonschema.Draft202012Validator.check_schema(schema)
jsonschema.Draft202012Validator(play).validate(read_json(ROOT/'probe.json'))
registry=Registry().with_resource('playbook.schema.json',Resource.from_contents(play))
parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path);args=parser.parse_args()
ir=read_json(args.run/'ir.json') if args.run else pipeline.build(ROOT/'probe.json')
jsonschema.Draft202012Validator(schema,registry=registry).validate(ir)
print(json.dumps({'status':'passed','checks':['DSL JSON Schema','IR JSON Schema']}))
