#!/usr/bin/env python3
"""Development validation against published JSON schemas. MIT."""
import json
import jsonschema
from referencing import Registry,Resource
from pipeline import ROOT,read_json

play=read_json(ROOT/'schemas/playbook.schema.json')
schema=read_json(ROOT/'schemas/ir.schema.json')
jsonschema.Draft202012Validator.check_schema(play)
jsonschema.Draft202012Validator.check_schema(schema)
jsonschema.Draft202012Validator(play).validate(read_json(ROOT/'probe.json'))
registry=Registry().with_resource('playbook.schema.json',Resource.from_contents(play))
jsonschema.Draft202012Validator(schema,registry=registry).validate(read_json(ROOT/'outputs/ir.json'))
print(json.dumps({'status':'passed','checks':['DSL JSON Schema','IR JSON Schema']}))
