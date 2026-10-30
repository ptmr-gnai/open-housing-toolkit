"""Strict versioned contracts and semantic quantities. Standard library. MIT."""
from dataclasses import dataclass, asdict
from decimal import Decimal
from enum import Enum
import re
import json
from housing_workflow.contracts import bbl, Kind

VERSION='0.1.0'

class Unit(str,Enum):
    HOMES='homes'
    BEDROOMS='bedrooms'
    USD_MONTH='USD per month'
    USD_YEAR='USD per year'
    YEARS='years'
    PERCENT='percent'
    BOOLEAN='boolean'
    STATUS='status'

@dataclass(frozen=True)
class Claim:
    id: str
    kind: Kind
    label: str
    value: str | int | bool | None
    unit: Unit
    inputs: tuple[str,...] = ()
    method: str | None = None
    rationale: str | None = None
    references: tuple[dict,...] = ()

    def to_dict(self):
        d=asdict(self);d['kind']=self.kind.value;d['unit']=self.unit.value
        d['inputs']=list(self.inputs);d['references']=list(self.references)
        return d


def fields(value,keys):
    if not isinstance(value,dict) or set(value)!=set(keys):raise ValueError('Expected exactly fields: '+', '.join(keys))


def text(value):
    if not isinstance(value,str) or not value.strip() or len(value)>4000:raise ValueError('Nonempty text required, at most 4000 characters')


def identifier(value):
    if not isinstance(value,str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,47}',value):raise ValueError('Invalid identifier')


def integer(value,low,high):
    if type(value)!=int or not low<=value<=high:raise ValueError('Bounded integer required; no booleans or fractional units')
    return value


def money(value):
    if not isinstance(value,str) or not re.fullmatch(r'(0|[1-9][0-9]{0,8})(\.[0-9]{1,2})?',value):
        raise ValueError('USD must be a nonnegative decimal string with at most two fractional digits')
    return Decimal(value)


def assumption(v,kind):
    fields(v,['value','rationale']);text(v['rationale'])
    if kind=='money':money(v['value'])
    elif kind=='homes':integer(v['value'],0,100000)
    elif kind=='years':integer(v['value'],1,999)
    elif kind=='percent':
        n=money(v['value'])
        if not 0<n<=100:raise ValueError('Threshold percent must be greater than zero and at most 100')
    return v['value']


def unknown(v):
    fields(v,['status','rationale'])
    if v['status']!='unknown':raise ValueError('This slice cannot clear baseline, occupancy or delivery review')
    text(v['rationale'])


def unique(items,label):
    if len(set(items))!=len(items):raise ValueError('Duplicate '+label)


def validate_request(r):
    fields(r,['version','id','site_bbl','question','objective','price_year','basis','cost_threshold_percent','profiles','programs','no_action','occupancy'])
    if r['version']!=VERSION:raise ValueError('Unsupported request version')
    identifier(r['id']);bbl(r['site_bbl']);text(r['question'])
    fields(r['objective'],['author','text']);text(r['objective']['author']);text(r['objective']['text'])
    integer(r['price_year'],1900,2200)
    if r['basis']!='illustrative_program_comparison':raise ValueError('Unsupported interpretation; no project-attributable outcome estimate')
    assumption(r['cost_threshold_percent'],'percent');unknown(r['no_action']);unknown(r['occupancy'])
    if not isinstance(r['profiles'],list) or not 1<=len(r['profiles'])<=10:raise ValueError('Provide 1–10 hypothetical household profiles')
    for p in r['profiles']:
        fields(p,['id','label','household_size','bedrooms','income_reference_id','rationale'])
        identifier(p['id']);text(p['label']);identifier(p['income_reference_id']);text(p['rationale'])
        integer(p['household_size'],1,8);integer(p['bedrooms'],0,5)
    unique([p['id'] for p in r['profiles']],'profile ID')
    if not isinstance(r['programs'],list) or len(r['programs'])!=2:raise ValueError('This slice compares exactly two explicit programs')
    for program in r['programs']:
        fields(program,['id','label','total_homes','delivery','commitment_status','bins'])
        identifier(program['id']);text(program['label']);assumption(program['total_homes'],'homes');unknown(program['delivery'])
        if program['commitment_status']!='proposed':raise ValueError('Only proposed rent restrictions supported; secured commitments need an evidence adapter')
        if not isinstance(program['bins'],list) or not 1<=len(program['bins'])<=30:raise ValueError('Provide 1–30 explicit rental offer bins')
        for row in program['bins']:
            fields(row,['id','bedrooms','homes','monthly_rent_usd','tenant_utilities_usd','restriction_years'])
            identifier(row['id']);integer(row['bedrooms'],0,5)
            for key,t in [('homes','homes'),('monthly_rent_usd','money'),('tenant_utilities_usd','money'),('restriction_years','years')]:assumption(row[key],t)
        unique([b['id'] for b in program['bins']],'program-bin ID')
        if sum(b['homes']['value'] for b in program['bins'])!=program['total_homes']['value']:raise ValueError('Program bin counts do not reconcile to total homes')
        if program['total_homes']['value']<=0:raise ValueError('Program must offer at least one explicit home')
    unique([p['id'] for p in r['programs']],'program ID')
    return r


def read_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('Duplicate JSON key: '+k)
            out[k]=v
        return out
    def constant(value):raise ValueError('Non-finite JSON constant: '+value)
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=constant)
