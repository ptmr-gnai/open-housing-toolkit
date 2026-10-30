"""Verify the retained new-lot case and the input identities that make it a real trial. MIT."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from housing_workflow import engine as evidence
from housing_workflow.contracts import load
from housing_recipe import engine as recipes
from housing_benefit import engine as comparisons
from housing_rer import engine as rer


def verify():
    case=Path(__file__).resolve().parent
    checks=[evidence.verify(case/'evidence'),recipes.verify(case/'area'),
            comparisons.verify(case/'comparison'),rer.verify(case/'rer')]
    if any(result['status']!='passed' for result in checks):raise ValueError('A module did not pass')
    source=load(case/'evidence/ir.json')
    if source['resolved_bbl']!='2028530012':raise ValueError('Trial parcel changed')
    if load(case/'evidence/execution.json')['mode']!='live_collection':raise ValueError('Trial must preserve its live-collection origin')
    if load(case/'area/execution.json')['mode']!='retained_snapshot_analysis':raise ValueError('Area model must disclose retained inputs')
    source_claims={c['id']:c for c in source['claims']}
    if source_claims['unknown.current_use']['kind']!='unknown':raise ValueError('Recorded units cannot clear current-use review')
    request=load(case/'inputs/comparison-request.json')
    totals={p['id']:sum(b['homes']['value'] for b in p['bins']) for p in request['programs']}
    reports=load(case/'rer/rer.json')['reports']
    for report in reports:
        total=totals[report['program_id']]
        slots={s['requirement_id']:s for s in report['slots']}
        if slots['res.total']['value']!=total:raise ValueError('Draft count differs from supplied program')
        if report['official_submission_ready']:raise ValueError('Trial does not establish submission readiness')
        for name in ['res.zsf','nonres.zsf']:
            if f'this {total}-home program' not in slots[name]['reason']:raise ValueError('Area explanation uses stale scenario quantities')
    return {'status':'passed','scope':'Four engineering verifiers and retained live-trial identity, origin and program bindings; not practitioner or image validation.'}


if __name__=='__main__':
    try:print(json.dumps(verify(),indent=2))
    except (ValueError,KeyError,OSError) as exc:
        print(json.dumps({'status':'failed','reason':str(exc)}),file=sys.stderr);raise SystemExit(2)
