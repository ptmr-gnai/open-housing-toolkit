"""Explicit current-use focus over a verified complete screen. MIT."""
from collections import Counter
import copy
from .common import keys


def apply(ir, spec, top_n):
    keys(spec,['version','label','building_class_prefixes','landuse_codes','rationale'],'focus')
    if spec['version']!='1.0' or not all(isinstance(spec[k],str) and spec[k].strip() for k in ['label','rationale']):
        raise ValueError('Explain and label the current-use focus')
    if (not isinstance(spec['building_class_prefixes'],list) or not isinstance(spec['landuse_codes'],list)
        or not spec['building_class_prefixes']+spec['landuse_codes']
        or any(not isinstance(x,str) or len(x)!=1 or not 'A'<=x<='Z' for x in spec['building_class_prefixes'])
        or any(x not in [str(i) for i in range(1,12)] for x in spec['landuse_codes'])):
        raise ValueError('Unsupported building-class or land-use focus')
    result=copy.deepcopy(ir)
    result['focus']=spec;result['evidence_prefix']='parent/evidence'
    result['request_id']+='-focused'
    for row in result['lots']:
        match=(str(row['recorded_building_class'] or '')[:1] in spec['building_class_prefixes']
               or str(row['recorded_landuse'] or '').split('.')[0] in spec['landuse_codes'])
        row['matches_use_focus']=match
        if not match:
            row['hold_reasons']=sorted(set(row['hold_reasons']+['outside_declared_current_use_focus']))
        row['route']='scenario_screen_shortlist_pool' if not row['hold_reasons'] else 'held_for_reason_or_different_mission'
    ranked=sorted([r for r in result['lots'] if not r['hold_reasons']],key=lambda r:(-r['additional_zoning_area_proxy_sf'],r['bbl']))
    rank={r['bbl']:i for i,r in enumerate(ranked,1)}
    result['shortlist']=[r['bbl'] for r in ranked[:top_n]]
    for row in result['lots']:
        row['rank_in_screen_pool']=rank.get(row['bbl']);row['shortlisted']=row['bbl'] in result['shortlist']
    result['counts']={'inventory':len(result['lots']),'screen_pool':len(ranked),'shortlist':len(result['shortlist']),
                      'held':len(result['lots'])-len(ranked),'by_hold_reason':dict(sorted(Counter(r for x in result['lots'] for r in x['hold_reasons']).items()))}
    result['methods']['rank']+=' Current-use focus: '+spec['label']+'. '+spec['rationale']
    return result
