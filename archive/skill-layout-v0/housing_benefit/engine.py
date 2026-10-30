"""Immutable standalone comparisons with verified upstream and reference bindings. MIT."""
from pathlib import Path
import shutil
from housing_workflow import engine as evidence
from housing_recipe import engine as recipes
from housing_workflow.contracts import digest, dumps, save
from .contracts import validate_request
from .sources import validate_source
from .model import compile_model,validate_claims
from .packet import project
from .methods import SIGNATURES

ROOT=Path(__file__).resolve().parents[1]

from .contracts import read_json as load


def implementation():
    files=sorted((ROOT/'housing_benefit').glob('*.py'))+sorted((ROOT/'housing_benefit').glob('*.json'))
    files += [ROOT/'workflows/housing-program-comparison.json',ROOT/'skills/compare-housing-programs/SKILL.md',ROOT/'scripts/prepare_benefit_reference.py']
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in files}


def verify_analysis(folder):
    if load(folder/'manifest.json').get('module')=='analysis-recipe':return recipes.verify(folder)
    return evidence.verify(folder)


def validate_method_registry():
    metadata=load(ROOT/'housing_benefit/methods.json')['methods']
    if {m['id'] for m in metadata}!=set(SIGNATURES) or len(metadata)!=len(SIGNATURES):raise ValueError('Method registry coverage differs from implementation')
    for m in metadata:
        inputs,out=SIGNATURES[m['id']]
        expected=[u.value for u in inputs] if inputs is not None else ('repeated homes/boolean pairs' if 'selected' in m['id'] else 'zero or more homes')
        if m['input_units']!=expected or m['output_unit']!=out.value or m['professional_review']!='pending':raise ValueError('Method registry signature/review mismatch')


def compile_run(folder,req=None):
    validate_method_registry()
    verify_analysis(folder/'analysis-run');ref=validate_source(folder/'reference-source')
    req=req if req is not None else load(folder/'request.json')
    req_sha=digest(dumps(req).encode())
    ir=compile_model(req,ref,load(folder/'analysis-run/ir.json'),digest((folder/'analysis-run/ir.json').read_bytes()),req_sha,digest((folder/'reference-source/receipt.json').read_bytes()))
    validate_claims(ir)
    return ir,ref


def outputs(folder):
    ir,ref=compile_run(folder)
    return {'ir.json':dumps(ir),**project(ir,ref)}


def inventory(folder):
    return {str(p.relative_to(folder)):digest(evidence.safe(folder,str(p.relative_to(folder))).read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}


def verify(folder):
    m=load(folder/'manifest.json')
    if m.get('module')!='housing-program-comparison' or m.get('version')!='0.1.0':raise ValueError('Unsupported comparison manifest')
    if m['implementation']!=implementation():raise ValueError('Comparison implementation changed; rebuild in a new directory')
    if m['files']!=inventory(folder):raise ValueError('Comparison inventory or artifact hash changed')
    for name,value in outputs(folder).items():
        if (folder/name).read_bytes()!=value.encode():raise ValueError('Comparison differs from retained inputs: '+name)
    return {'status':'passed','module':'housing-program-comparison','packet':str(folder/'packet.html'),'basis':'illustrative_program_comparison','professional_review':'pending','eligibility':'not_determined','overall_ranking':None}


def build(analysis,reference,req,folder):
    validate_method_registry();validate_request(req);verify_analysis(analysis);ref=validate_source(reference)
    ir=compile_model(req,ref,load(analysis/'ir.json'),digest((analysis/'ir.json').read_bytes()),digest(dumps(req).encode()),digest((reference/'receipt.json').read_bytes()))
    validate_claims(ir)
    if any(folder.resolve().is_relative_to(p.resolve()) for p in [analysis,reference]):raise ValueError('Output must be outside input packages')
    evidence.fresh(folder)
    shutil.copytree(analysis,folder/'analysis-run');shutil.copytree(reference,folder/'reference-source');save(folder/'request.json',req)
    for name,value in outputs(folder).items():(folder/name).write_text(value)
    save(folder/'manifest.json',{'version':'0.1.0','module':'housing-program-comparison','implementation':implementation(),'files':inventory(folder),
                                'validation_scope':'Typed conditional arithmetic, source excerpt and upstream byte bindings, dependency graph and deterministic exports. Not complete professional interpretation, eligibility or causal welfare.'})
    return verify(folder)


def replay(source,folder,req=None):
    verify(source)
    return build(source/'analysis-run',source/'reference-source',req if req is not None else load(source/'request.json'),folder)


def impact(source,req):
    verify(source);new,_=compile_run(source,req);old=load(source/'ir.json')
    a={c['id']:c for c in old['claims']};b={c['id']:c for c in new['claims']}
    def authored(c):return None if c is None else {k:v for k,v in c.items() if not (c['kind']=='calculation' and k=='value')}
    seeds={cid for cid in set(a)|set(b) if authored(a.get(cid))!=authored(b.get(cid))};affected=set(seeds)
    while True:
        more={cid for cid,c in list(a.items())+list(b.items()) if set(c['inputs'])&affected}
        if more<=affected:break
        affected |= more
    return {'directly_changed_claims':sorted(seeds),'affected_claims':sorted(affected),
            'changed_values':sorted(cid for cid in set(a)&set(b) if a[cid]['value']!=b[cid]['value']),
            'requires_regeneration':list(outputs(source)) if req!=load(source/'request.json') else [],
            'scope':'Dependency impact, not a benefit ranking. Invalid input/vintage changes block preview. Rebuild in a new run.'}
