"""Explicit contracts for scene, assumed visual scenario and review. MIT."""
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import re

VERSION='0.1.0'

def digest(data):return hashlib.sha256(data).hexdigest()
def dumps(value):return json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+'\n'
def load(path):return json.loads(Path(path).read_text())
def save(path,value):Path(path).write_text(dumps(value))
def exact(obj,fields):
    if not isinstance(obj,dict) or set(obj)!=set(fields):raise ValueError('Unexpected or missing contract fields: '+','.join(fields))
def text(value):
    if not isinstance(value,str) or not value.strip() or len(value)>4000:raise ValueError('Nonempty bounded text required')
def site(value):
    if not isinstance(value,str) or not re.fullmatch(r'[1-5][0-9]{9}',value):raise ValueError('Expected NYC 10-digit BBL')

@dataclass(frozen=True)
class Assumption:
    value: object
    kind: str
    rationale: str

    @classmethod
    def parse(cls,obj,kind):
        exact(obj,['value','kind','rationale']);text(obj['rationale'])
        if obj['kind']!=kind:raise ValueError('Unsupported parameter basis: '+kind)
        return cls(**obj)

def validate_scene(s):
    exact(s,['version','site_bbl','site_match','reference','viewpoint'])
    if s['version']!=VERSION:raise ValueError('Unsupported scene version')
    site(s['site_bbl']);text(s['viewpoint'])
    if s['site_match'] != 'user_asserted':raise ValueError('This slice supports user-asserted photo/site matches only; no independent geolocation attestation')
    r=s['reference'];exact(r,['id','origin','provider','capture_date','capture_date_basis','attribution','availability'])
    for k in r:
        if k!='availability':text(r[k])
    if r['origin']!='user_supplied':raise ValueError('This adapter accepts user-supplied reference images')
    if r['availability'] not in {'local_file','conversation_attachment'}:raise ValueError('Unsupported reference availability')
    return s

def validate_scenario(s):
    exact(s,['version','id','site_bbl','label','parameters','geometry_status','analysis_reconciliation'])
    if s['version']!=VERSION:raise ValueError('Unsupported scenario version')
    site(s['site_bbl']);text(s['id']);text(s['label'])
    p=s['parameters'];exact(p,['total_stories','ground_floor_use','upper_floor_use','architectural_treatment'])
    n=Assumption.parse(p['total_stories'],'assumption').value
    if isinstance(n,bool) or not isinstance(n,int) or not 2<=n<=30:raise ValueError('Supported illustrative story count is an integer from 2 to 30; this is not a zoning limit')
    for k in ['ground_floor_use','upper_floor_use']:text(Assumption.parse(p[k],'assumption').value)
    text(Assumption.parse(p['architectural_treatment'],'design_preference').value)
    if s['geometry_status']!='unverified':raise ValueError('This slice cannot certify measured geometry')
    if s['analysis_reconciliation']!='not_reconciled_to_area_budget':raise ValueError('No area-to-massing reconciliation is implemented')
    return s

def image_file(path):
    data=Path(path).read_bytes()
    if not (data.startswith(b'\x89PNG\r\n\x1a\n') or data.startswith(b'\xff\xd8\xff')):raise ValueError('Provide a PNG or JPEG image')
    if len(data)>30_000_000:raise ValueError('Image exceeds the 30 MB slice limit')
    return data,'.png' if data.startswith(b'\x89PNG') else '.jpg'

def validate_review(review):
    exact(review,['reviewer_kind','summary','checks'])
    if review['reviewer_kind'] not in {'assistant_visual_inspection','human_visual_inspection'}:raise ValueError('Review is a visual inspection, not professional acceptance')
    text(review['summary'])
    required={'reference_setting','story_count','caption','invented_site_details','geometry_fidelity'}
    if {c.get('id') for c in review['checks']}!=required or len(review['checks'])!=len(required):raise ValueError('Missing visual review coverage')
    for c in review['checks']:
        exact(c,['id','status','note']);text(c['note'])
        if c['status'] not in {'consistent_by_inspection','issue_observed','not_verified'}:raise ValueError('Unsupported review status')
    geom=next(c for c in review['checks'] if c['id']=='geometry_fidelity')
    if geom['status']!='not_verified':raise ValueError('Visual inspection cannot certify geometry')
    return review
