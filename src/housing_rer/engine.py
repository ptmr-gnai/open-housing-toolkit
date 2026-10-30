"""Independent immutable report preparation with full upstream verification. MIT."""
from pathlib import Path
import shutil
from housing_benefit import engine as comparisons
from housing_benefit.contracts import read_json as load
from housing_workflow.contracts import digest,dumps,save
from housing_workflow.engine import safe,fresh
from .contracts import validate_request,Status
from .model import compile_drafts,validate_catalog
from .packet import projections

from housing_common.local_outputs import ROOT


def implementation():
    paths=sorted(Path(__file__).resolve().parent.glob('*.py'))+sorted(Path(__file__).resolve().parent.glob('*.json'))
    paths += [ROOT/'config/workflows/rer-preparation.json',ROOT/'skills/prepare-rer-draft/SKILL.md',ROOT/'scripts/prepare_rer_guidance.py']
    paths += [ROOT/'src/housing_common/runtime.py']
    paths += [ref for skill in list(paths) if skill.name=='SKILL.md' for ref in sorted((skill.parent/'references').glob('*.md'))]
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def catalogue():
    c=load(ROOT/'src/housing_rer/requirements.json');g=load(ROOT/'src/housing_rer/guidance.json');validate_catalog(c,g);return c,g


def compile_run(folder):
    comparisons.verify(folder/'comparison-run');c,g=catalogue()
    parent=load(folder/'comparison-run/ir.json');site=load(folder/'comparison-run/analysis-run/ir.json')
    ir=compile_drafts(load(folder/'request.json'),parent,digest((folder/'comparison-run/ir.json').read_bytes()),site,digest((folder/'comparison-run/analysis-run/ir.json').read_bytes()),c,g)
    for report in ir['reports']:
        for slot in report['slots']:
            if slot['status'] in {Status.MISSING.value,Status.INTERPRET.value,Status.NA.value} and slot['value'] is not None:raise ValueError('Unresolved slot promoted to populated')
            for b in slot['bindings']:
                path=safe(folder,b['file'])
                if digest(path.read_bytes())!=b['sha256']:raise ValueError('Input binding hash mismatch')
                value=load(path)
                for token in b['pointer'].strip('/').split('/'):
                    value=value[int(token)] if isinstance(value,list) else value[token]
                if value!=b['value'] or type(value)!=type(b['value']):raise ValueError('Bound field value differs')
    return ir


def outputs(folder):
    ir=compile_run(folder)
    return {'rer.json':dumps(ir),'requirements.json':dumps(catalogue()[0]),'guidance.json':dumps(catalogue()[1]),**projections(ir)}


def inventory(folder):
    return {str(p.relative_to(folder)):digest(safe(folder,str(p.relative_to(folder))).read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}


def verify(folder):
    m=load(folder/'manifest.json')
    if m.get('module')!='rer-preparation' or m.get('version')!='0.1.0':raise ValueError('Unsupported RER preparation manifest')
    if m['implementation']!=implementation():
        from housing_common.runtime import verify_historical
        return verify_historical('housing_rer', folder)
    if m['files']!=inventory(folder):raise ValueError('RER inventory or artifact hash changed')
    for name,text in outputs(folder).items():
        if (folder/name).read_bytes()!=text.encode():raise ValueError('RER output differs from retained inputs: '+name)
    return {'status':'passed','module':'rer-preparation','draft_status':'incomplete_illustrative_draft','official_submission_ready':False,'applicability':'not_determined','professional_review':'pending','packet':str(folder/'packet.html')}


def build(parent,req,folder):
    validate_request(req);comparisons.verify(parent);c,g=catalogue()
    compile_drafts(req,load(parent/'ir.json'),digest((parent/'ir.json').read_bytes()),load(parent/'analysis-run/ir.json'),digest((parent/'analysis-run/ir.json').read_bytes()),c,g)
    if folder.resolve().is_relative_to(parent.resolve()):raise ValueError('Output must be outside parent package')
    fresh(folder);shutil.copytree(parent,folder/'comparison-run');save(folder/'request.json',req)
    for name,text in outputs(folder).items():(folder/name).write_text(text)
    save(folder/'manifest.json',{'version':'0.1.0','module':'rer-preparation','implementation':implementation(),'files':inventory(folder),'scope':'Draft slot coverage, known omission checks, source-page metadata bindings and deterministic projections; not legal applicability, semantic completeness or professional acceptance.'})
    return verify(folder)


def replay(source,folder,req=None):
    verify(source);return build(source/'comparison-run',req if req is not None else load(source/'request.json'),folder)
