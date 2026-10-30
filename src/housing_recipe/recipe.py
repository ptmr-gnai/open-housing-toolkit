"""Validate and execute a typed dependency graph without eval or dynamic imports. MIT."""
import copy
import re
from housing_workflow.contracts import Claim, Kind, digest, dumps
from .methods import METHODS, UNITS, numeric, execute

GATES = ['unknown.'+k for k in ('current_use','title','entitlement','physical_fit','environment','finance','transit','process_coverage')]
REQUIRED = {'scenario.residential_gross_sf':'gross_sf', 'scenario.residential_net_sf':'net_sf', 'scenario.home_equivalents':'home_equivalents'}


def fields(obj, required):
    if not isinstance(obj, dict) or set(obj) != set(required):
        raise ValueError('Expected exactly fields: '+', '.join(required))


def text(v):
    if not isinstance(v, str) or not v.strip():raise ValueError('Nonempty text required')


def identifier(v):
    text(v)
    if not re.fullmatch(r'(scenario|recipe)\.[a-z][a-z0-9_]*', v):
        raise ValueError('Output ID must be in scenario. or recipe. namespace')


def compile_recipe(recipe, evidence_ir):
    fields(recipe, ['version','id','revision','name','purpose','parameters','imports','steps','review_gates'])
    if recipe['version'] != '0.1.0':raise ValueError('Unsupported recipe version')
    for k in ['id','revision','name','purpose']:text(recipe[k])
    for k in ['parameters','imports','steps','review_gates']:
        if not isinstance(recipe[k], list):raise ValueError('Expected array: '+k)
    if len(recipe['review_gates']) != len(set(recipe['review_gates'])) or not set(GATES).issubset(recipe['review_gates']):
        raise ValueError('Required professional review gates cannot be removed')
    retained = [copy.deepcopy(c) for c in evidence_ir['claims'] if not c['id'].startswith('scenario.')]
    source = {c['id']:c for c in retained}
    # Never silently sever an authored judgment from its scenario dependency.
    if any(d.startswith('scenario.') for c in retained for d in c['inputs']):
        raise ValueError('Source judgment depends on replaced scenario; professional reconciliation required')
    for gate in recipe['review_gates']:
        if gate not in source or source[gate]['kind'] != 'unknown':raise ValueError('Review gate must bind a retained unknown')
    types = {}; values = {}; produced = []; trace = []; defined = set(source)
    for p in recipe['parameters']:
        fields(p, ['id','label','type','value','rationale']);identifier(p['id'])
        text(p['label']);text(p['rationale']);numeric(p['value'],p['type'])
        if p['id'] in defined:raise ValueError('Duplicate or overwritten claim ID')
        defined.add(p['id']);types[p['id']]=p['type'];values[p['id']]=p['value']
        produced.append(Claim(p['id'],Kind.ASSUMPTION,p['label'],p['value'],UNITS[p['type']],rationale=p['rationale']).to_dict())
    for imp in recipe['imports']:
        fields(imp, ['claim_id','type'])
        # The only reviewed numeric source binding in this slice. No arbitrary relabeling.
        if imp != {'claim_id':'pluto.0.lotarea','type':'recorded_lot_sf'}:
            raise ValueError('Unsupported evidence import; add a reviewed source/type adapter')
        cid=imp['claim_id']
        if cid in types:raise ValueError('Duplicate import')
        types[cid]=imp['type']
        if cid in source:
            if source[cid]['kind'] != 'fact' or not source[cid]['references']:raise ValueError('Uncited imported fact')
            from housing_workflow.model import number
            value=float(number(source[cid]['value']));numeric(value,imp['type']);values[cid]=value
    steps={}
    for step in recipe['steps']:
        fields(step, ['id','label','method','inputs','type','rationale','on_missing'])
        identifier(step['id']);text(step['label']);text(step['rationale'])
        if step['id'] in defined:raise ValueError('Duplicate or overwritten claim ID')
        if step['method'] not in METHODS:raise ValueError('Unsupported versioned method: '+str(step['method']))
        if step['on_missing'] not in {'block','skip'}:raise ValueError('Unsupported missing-input policy')
        if not isinstance(step['inputs'],list) or not all(isinstance(x,str) for x in step['inputs']):raise ValueError('Expected claim input IDs')
        defined.add(step['id']);types[step['id']]=step['type'];steps[step['id']]=step
    active=set();done=set();skipped=set()
    def visit(cid):
        if cid in done:return
        if cid in active:raise ValueError('Recipe dependency cycle')
        active.add(cid);s=steps[cid];signature,out_type,formula=METHODS[s['method']]
        if any(i not in types for i in s['inputs']):raise ValueError('Missing or untyped recipe dependency')
        if [types[i] for i in s['inputs']] != signature or s['type'] != out_type:
            raise ValueError('Method input/output semantic type mismatch: '+cid)
        for dep in s['inputs']:
            if dep in steps:visit(dep)
        missing=[i for i in s['inputs'] if i not in values]
        if missing:
            if s['on_missing']=='block' or cid in REQUIRED:raise ValueError('Required input unavailable: '+cid)
            skipped.add(cid)
            trace.append({'id':cid,'method':s['method'],'status':'skipped_missing_input','missing':missing})
        else:
            value=execute(s['method'],[values[i] for i in s['inputs']]);numeric(value,s['type']);values[cid]=value
            produced.append(Claim(cid,Kind.CALCULATION,s['label'],value,UNITS[s['type']],inputs=s['inputs'],formula=formula,rationale=s['rationale']).to_dict())
            trace.append({'id':cid,'method':s['method'],'status':'calculated','inputs':s['inputs'],'value':value,'type':s['type']})
        active.remove(cid);done.add(cid)
    for cid in steps:visit(cid)
    if any(cid not in steps or cid in skipped or types.get(cid)!=t for cid,t in REQUIRED.items()):
        raise ValueError('Required packet outputs missing or mistyped')
    ir=copy.deepcopy(evidence_ir);ir['claims']=retained+produced;ir['scenario_name']=recipe['name']
    ir['analysis_recipe']={'id':recipe['id'],'revision':recipe['revision'],'sha256':digest(dumps(recipe).encode()),'review':'unreviewed; numerical recipe is not professional clearance'}
    return ir, {'recipe':ir['analysis_recipe'],'parameters':recipe['parameters'],'imports':recipe['imports'],'steps':trace,'review_gates':[{'claim_id':g,'status':'unknown'} for g in recipe['review_gates']]}


def impact(old_ir, old_recipe, new_ir, new_recipe):
    old={c['id']:c for c in old_ir['claims']};new={c['id']:c for c in new_ir['claims']}
    a={s['id']:s for s in old_recipe['steps']};b={s['id']:s for s in new_recipe['steps']}
    def authored(c):
        if c is None:return None
        return {k:v for k,v in c.items() if not (c['kind']=='calculation' and k=='value')}
    seeds={k for k in set(old)|set(new) if authored(old.get(k))!=authored(new.get(k))}
    seeds.update(k for k in set(a)|set(b) if a.get(k)!=b.get(k))
    affected=set(seeds)
    while True:
        more={k for k,c in list(old.items())+list(new.items()) if set(c['inputs']) & affected}
        if more <= affected:break
        affected |= more
    changed=old_recipe!=new_recipe
    return {'directly_changed_claims_or_steps':sorted(seeds),'affected_claims':sorted(affected),
            'numerically_changed_claims':sorted(k for k in set(old)&set(new) if old[k]['value']!=new[k]['value']),
            'requires_regeneration':['ir.json','trace.json','packet.md','packet.html','calculation-steps.csv','image-prompts.json'] if changed else [],
            'review':'Dependency impact, not a decision-quality assessment. Existing runs remain immutable.'}
