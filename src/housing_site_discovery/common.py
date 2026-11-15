"""Immutable packages and explicit discovery inputs. MIT."""
from pathlib import Path
import base64
import re
from housing_discovery.common import bbl, digest, dumps, fresh, keys, load, number, save
from housing_common.local_outputs import ROOT

GUIDANCE_URLS = {
    'residence':'https://zr.planning.nyc.gov/article-ii/chapter-2/22-121',
    'commercial':'https://zr.planning.nyc.gov/article-iii/chapter-2/32-121',
    'commercial_limits':'https://zr.planning.nyc.gov/article-iii/chapter-2/32-122',
    'manufacturing':'https://zr.planning.nyc.gov/article-iv/chapter-2/42-12',
    'manufacturing_geography':'https://zr.planning.nyc.gov/article-iv/chapter-2/42-314',
    'mixed_use':'https://zr.planning.nyc.gov/article-xii/chapter-3/123-20',
    'building_classes':'https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html',
}


def validate_request(req):
    keys(req,['version','id','question','scope','display_per_group'],'site-discovery request')
    if req['version']!='1.0' or not isinstance(req['id'],str) or not re.fullmatch(r'[a-z0-9-]{1,80}',req['id']):
        raise ValueError('Unsupported request version or id')
    if not isinstance(req['question'],str) or not req['question'].strip():raise ValueError('Question required')
    if type(req['display_per_group']) is not int or not 1<=req['display_per_group']<=20:
        raise ValueError('Choose 1 to 20 displayed examples per group; all lots remain in CSV/IR')
    # Reuse the existing bounded NYC geography contract without introducing a model.
    from housing_discovery.common import validate_request as validate_inventory
    validate_inventory(transport_request(req))
    return req


def transport_request(req):
    """Compatibility with the existing collector only; scenario is never evaluated."""
    return {'version':'1.0','id':req['id'],'question':req['question'],'scope':req['scope'],
            'scenario':{'label':'UNUSED collector transport fields','proposed_residential_far':1,
                        'gross_per_zoning_sf':1,'residential_share':1,'net_efficiency':1,
                        'net_sf_per_home_equivalent':1,
                        'rationale':'Required by the retained inventory wire contract only. Not supplied by the user, not evaluated, and not used for nonhousing discovery.'},
            'selection':{'min_lot_area_sf':0,'max_lot_area_sf':0,'min_additional_area_proxy_sf':0,
                         'max_recorded_residential_units':None,'mission':'all_with_flags',
                         'hold_active_applications':False,'top_n':1}}


def guidance(pack):
    if pack.get('version')!='1.0' or {x['id']:x['url'] for x in pack['sources']}!=GUIDANCE_URLS or len(pack['sources'])!=len(GUIDANCE_URLS):
        raise ValueError('Unsupported guidance sources')
    for row in pack['sources']:
        body=base64.b64decode(row['body_base64'],validate=True)
        if row['http_status']!=200 or digest(body)!=row['sha256'] or len(body)!=row['bytes']:
            raise ValueError('Guidance source receipt differs from retained bytes')
    return pack


def implementation(kind):
    module=Path(__file__).parent
    paths=([module/name for name in (['__init__.py','common.py','evidence.py']+(['context.py'] if kind=='context' else []))]
           if kind in ['evidence','context'] else sorted(module.glob('*.py'))+sorted(module.glob('*.json')))
    paths += [ROOT/'src/housing_discovery'/n for n in ['__init__.py','common.py','collection.py','providers.json']]
    paths += [ROOT/'src/housing_common/local_outputs.py']
    if kind not in ['evidence','context']:
        skill=ROOT/'skills/discover-nonhousing-sites/SKILL.md'
        paths += [skill]+sorted((skill.parent/'references').glob('*.md'))
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def seal(folder,kind):
    files={str(p.relative_to(folder)):digest(p.read_bytes()) for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}
    save(folder/'manifest.json',{'version':'1.0.0','kind':kind,'implementation':implementation(kind),'files':files})


def verify_files(folder,kind):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('version')!='1.0.0' or m.get('kind')!=kind or m.get('implementation')!=implementation(kind):
        raise ValueError('Unknown or changed site-discovery implementation')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!=set(m['files'])|{'manifest.json'}:raise ValueError('Package file inventory changed')
    for name,expected in m['files'].items():
        path=folder/name
        if path.is_symlink() or not path.resolve().is_relative_to(folder) or digest(path.read_bytes())!=expected:
            raise ValueError('Changed or escaping package file: '+name)
    return m
