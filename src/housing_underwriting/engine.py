"""Verified local packages and step-by-step input/output trace. MIT."""
from pathlib import Path
import hashlib
import json
import shutil
from housing_common.local_outputs import ROOT,destination
from .model import evaluate,validate
from .packet import project


def digest(data):return hashlib.sha256(data).hexdigest()
def load(path):return json.loads(Path(path).read_text())
def dumps(value):return json.dumps(value,sort_keys=True,indent=2,allow_nan=False)+'\n'
def save(path,value):Path(path).write_text(dumps(value))


def fresh(out):
    out=destination(out);out.mkdir(parents=True,exist_ok=False);return out


def implementation():
    paths=sorted(Path(__file__).parent.glob('*.py'))+sorted(Path(__file__).parent.glob('*.json'))+[ROOT/'src/housing_common/local_outputs.py']
    skill=ROOT/'skills/model-rental-underwriting/SKILL.md'
    if skill.exists():paths+=[skill]+sorted((skill.parent/'references').glob('*.md'))
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def seal(folder,kind):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':kind,'implementation':implementation(),'files':files})


def verify_files(folder,kind):
    folder=Path(folder).resolve();manifest=load(folder/'manifest.json')
    if manifest.get('kind')!=kind or manifest.get('version')!='1.0.0' or manifest.get('implementation')!=implementation():raise ValueError('Unknown or changed underwriting implementation')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(manifest['files'])|{'manifest.json'}:raise ValueError('Underwriting package inventory changed')
    for name,sha in manifest['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Changed or escaping file: '+name)
    return manifest


def trace(req,result):
    nodes=[]
    def node(identity,value,unit,method,dependencies):nodes.append({'id':identity,'value':value,'unit':unit,'kind':'calculation','method':method,'dependencies':dependencies})
    for row in result['capital_lines']:
        node('capital.'+row['category'],row['amount_usd'],'USD','explicit rate × declared program measure',['request.json#/capital/lines/'+str(next(i for i,x in enumerate(req['capital']['lines']) if x['category']==row['category'])),'request.json#/program'])
    node('capital.total',result['total_development_cost_usd'],'USD','sum cost lines',['capital.'+x['category'] for x in result['capital_lines']])
    for row in result['annual']:
        prefix='year.'+str(row['year'])+'.'
        node(prefix+'income',row['effective_gross_income_usd'],'USD/year','sum stream effective amounts after growth, active period and vacancy',['request.json#/operations/income'])
        node(prefix+'expenses',row['operating_expenses_usd'],'USD/year','sum expense rows after growth',['request.json#/operations/expenses'])
        node(prefix+'reserve',row['replacement_reserve_usd'],'USD/year','annual deposit × explicit growth',['request.json#/operations/replacement_reserve'])
        node(prefix+'coverage_noi',row['coverage_noi_usd'],'USD/year','income - expenses - reserve if explicitly elected',[prefix+'income',prefix+'expenses',prefix+'reserve','request.json#/operations/reserve_deducted_for_coverage'])
    node('debt.principal',result['modeled_primary_loan_usd'],'USD','minimum declared debt capacities, rounded down',['year.'+str(y['year'])+'.coverage_noi' for y in result['annual'][:result['debt_sizing_years']]]+['capital.total','request.json#/debt','request.json#/sources'])
    for row in result['annual']:
        prefix='year.'+str(row['year'])+'.'
        node(prefix+'dscr',row['dscr'],'ratio','coverage NOI / primary and other annual debt service; undefined with zero debt',[prefix+'coverage_noi','debt.principal','request.json#/debt'])
        node(prefix+'cash',row['cash_after_reserves_debt_and_below_line_usd'],'USD/year','income - expenses - reserve - primary debt service - other debt service - below-line expenses - maturity principal due',[prefix+'income',prefix+'expenses',prefix+'reserve','debt.principal','request.json#/debt','request.json#/operations/below_line'])
    node('capital.unallocated',result['unallocated_capital_after_modeled_loan_and_all_declared_sources_usd'],'USD','max(0, uses - modeled debt - all declared sources)',['capital.total','debt.principal','request.json#/sources'])
    return {'meaning':'Calculation trace. Input JSON pointers contain attribution; value is not approval.','nodes':nodes}


def reference_records(req,files=None):
    files=files or {};ids={x['id'] for x in req['references']}
    if not set(files)<=ids:raise ValueError('Supplied bytes have an unknown reference id')
    result=[]
    for ref in req['references']:
        record={**ref,'retention':'declared_link_only_not_byte_verified'}
        if ref['id'] in files:
            p=Path(files[ref['id']]);body=p.read_bytes()
            if len(body)>32*1024*1024:raise ValueError('Reference source exceeds 32 MiB')
            record.update(retention='retained_bytes',body_path='sources/'+str(len(result))+p.suffix.lower(),sha256=digest(body),bytes=len(body))
        result.append(record)
    return result


def build(req,out,source_files=None):
    validate(req);result=evaluate(req);refs=reference_records(req,source_files);out=fresh(out)
    save(out/'request.json',req);save(out/'results.json',result);save(out/'trace.json',trace(req,result));save(out/'references.json',refs)
    for ref in refs:
        if ref['retention']=='retained_bytes':
            target=out/ref['body_path'];target.parent.mkdir(exist_ok=True);shutil.copyfile(source_files[ref['id']],target)
    for name,body in project(req,result).items():(out/name).write_text(body)
    seal(out,'underwriting');return verify(out)


def verify(folder):
    folder=Path(folder);verify_files(folder,'underwriting');req=load(folder/'request.json');result=evaluate(req)
    if result!=load(folder/'results.json') or trace(req,result)!=load(folder/'trace.json'):raise ValueError('Underwriting differs from recomputation')
    for name,body in project(req,result).items():
        if (folder/name).read_text()!=body:raise ValueError('Changed underwriting projection: '+name)
    refs=load(folder/'references.json')
    if len(refs)!=len(req['references']):raise ValueError('Reference inventory changed')
    for index,(ref,declared) in enumerate(zip(refs,req['references'])):
        if any(ref[k]!=v for k,v in declared.items()):raise ValueError('Declared reference changed')
        if ref['retention']=='retained_bytes':
            p=Path(ref['body_path'])
            if p.is_absolute() or len(p.parts)!=2 or p.parts[0]!='sources' or p.stem!=str(index):raise ValueError('Unexpected reference body path')
            body=(folder/p).read_bytes()
            if len(body)!=ref['bytes'] or digest(body)!=ref['sha256']:raise ValueError('Reference source changed')
        elif ref['retention']!='declared_link_only_not_byte_verified':raise ValueError('Unknown reference retention')
    return {'status':'passed','years':len(result['annual']),'coverage_breach_years':result['coverage_breach_years'],'packet':str(folder/'packet.html'),'professional_review':'pending'}
