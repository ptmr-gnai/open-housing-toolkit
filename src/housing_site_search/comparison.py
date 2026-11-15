"""Compare explicit search/model changes on exactly the same reviewed evidence. MIT."""
from pathlib import Path
import shutil
from housing_common.packages import digest,load,save,fresh
from . import engine as search


def differences(left,right):
    left,right=Path(left),Path(right)
    if digest((left/'discovery/manifest.json').read_bytes())!=digest((right/'discovery/manifest.json').read_bytes()):raise ValueError('Search comparison requires identical retained reviewed site evidence')
    a,b=load(left/'results.json'),load(right/'results.json')
    old,new={x['id']:x for x in a['trials']},{x['id']:x for x in b['trials']}
    changes=[]
    for identity in sorted(set(old)|set(new)):
        if identity not in old:changes.append({'id':identity,'change':'added_scenario','after':new[identity]});continue
        if identity not in new:changes.append({'id':identity,'change':'removed_scenario','before':old[identity]});continue
        fields=sorted((set(old[identity])|set(new[identity]))-{'id'})
        delta={k:{'before':old[identity].get(k,{'missing':True}),'after':new[identity].get(k,{'missing':True})} for k in fields if k not in old[identity] or k not in new[identity] or old[identity][k]!=new[identity][k]}
        if delta:changes.append({'id':identity,'bbl':old[identity]['bbl'],'changes':delta})
    match=lambda r:{x['bbl'] for x in r['trials'] if x['status']=='matches_declared_targets'}
    return {'meaning':'Same-evidence finite-scenario sensitivity. Changed targets and/or financial assumptions are explicit; no causal housing effect or globally best site is inferred.',
            'left_counts':a['counts'],'right_counts':b['counts'],'entered_matching_lots':sorted(match(b)-match(a)),
            'left_matching_lots':sorted(match(a)-match(b)),'changed_trials':changes,
            'left_search_request':load(left/'request.json'),'right_search_request':load(right/'request.json'),
            'left_financial_request':load(left/'underwriting-template/request.json'),'right_financial_request':load(right/'underwriting-template/request.json')}


def text(result):
    return '# Search sensitivity comparison\n\n'+result['meaning']+'\n\nLeft matching lots: '+str(result['left_counts']['lots_by_status'].get('matches_declared_targets',0))+'. Right matching lots: '+str(result['right_counts']['lots_by_status'].get('matches_declared_targets',0))+'.\n\nEntered matching set: '+', '.join(result['entered_matching_lots'])+'\n\nLeft matching set: '+', '.join(result['left_matching_lots'])+'\n\ncomparison.json retains every changed field/status/value in the trial records and both complete search/financial requests. The original packages remain under left/ and right/.\n'


def build(left,right,out):
    left,right=Path(left),Path(right);search.verify(left);search.verify(right);result=differences(left,right)
    out=fresh(out);shutil.copytree(left,out/'left');shutil.copytree(right,out/'right');save(out/'comparison.json',result);(out/'packet.md').write_text(text(result))
    from .pipeline_handoff import seal
    seal(out,'site-search-comparison');return verify(out)


def verify(folder):
    folder=Path(folder).resolve();m=load(folder/'manifest.json')
    if m.get('kind')!='site-search-comparison' or m.get('version')!='1.0.0' or m.get('implementation')!=search.implementation():raise ValueError('Unknown or changed search comparison')
    if {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}!=set(m['files'])|{'manifest.json'}:raise ValueError('Comparison inventory changed')
    for name,sha in m['files'].items():
        p=folder/name
        if p.is_symlink() or not p.resolve().is_relative_to(folder) or digest(p.read_bytes())!=sha:raise ValueError('Changed comparison file: '+name)
    search.verify(folder/'left');search.verify(folder/'right');result=differences(folder/'left',folder/'right')
    if load(folder/'comparison.json')!=result or (folder/'packet.md').read_text()!=text(result):raise ValueError('Comparison differs from recomputation')
    return {'status':'passed','changed_trials':len(result['changed_trials']),'entered_matching_lots':len(result['entered_matching_lots']),'left_matching_lots':len(result['left_matching_lots'])}
