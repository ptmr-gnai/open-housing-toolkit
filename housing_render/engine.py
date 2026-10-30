"""Prepare briefs and attach externally generated assets with review receipts. MIT."""
from pathlib import Path
from local_outputs import destination
import shutil
from .contracts import VERSION, digest, dumps, image_file, load, save, validate_review, validate_scene, validate_scenario
from .brief import compile_brief

ROOT=Path(__file__).resolve().parents[1]
WORKFLOW=ROOT/'workflows/site-concept.json'

def implementation():
    files=sorted((ROOT/'housing_render').glob('*.py'))+sorted((ROOT/'housing_render').glob('*.json'))+[WORKFLOW]
    files += [ROOT/s['skill'] for s in load(WORKFLOW)['steps']]
    files += [ROOT/'housing_runtime.py',ROOT/'local_outputs.py']
    files += [ref for skill in list(files) if skill.name=='SKILL.md' for ref in sorted((skill.parent/'references').glob('*.md'))]
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in files}

def safe(root,name):
    p=root/name
    if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('Render path escapes package')
    return p

def files_manifest(root):
    return {str(p.relative_to(root)):digest(safe(root,str(p.relative_to(root))).read_bytes()) for p in sorted(root.rglob('*')) if p.is_file() and p.name!='manifest.json'}

def write_manifest(root):
    save(root/'manifest.json',{'version':VERSION,'implementation':implementation(),'files':files_manifest(root)})

def markdown(brief):
    lines=['# Photo-referenced site concept','',f'Tax lot {brief["site_bbl"]}. Scenario: {brief["scenario_id"]}.','',
           'The reference image anchors the visual setting. Story count, program and design are explicit assumptions/preferences. No measured building model is supplied.','',
           '## Scenario inputs','']
    for p in brief['scenario_bindings']:lines.append(f'- **{p["parameter"]}**: {p["value"]} ({p["kind"]}). {p["rationale"]}')
    lines+=['','## Site reference','',brief['reference']['attribution'],'',
            'Reference storage: '+brief['reference']['storage']+'. Source bytes hash: '+str(brief['reference']['sha256'])+'.',
            'An external conversation reference has no local source-byte hash; source-image reproduction needs that attachment.','',
            '## Optional analysis context','',
            'Analysis supplied: '+str(brief['analysis']['available'])+'. Analysis SHA256: '+str(brief['analysis']['sha256'])+'.',
            '**Area-budget reconciliation: not performed.** The assumed building is not scaled to any earlier home-equivalent calculation.','']
    for c in brief['analysis']['context_bindings']:lines.append(f'- {c["claim_id"]}: {c["value"]} ({c["unit"]}); source pointers and hashes retained in render-brief.json and inputs/analysis.json.')
    lines+=['','## Unverified','']+['- '+x for x in brief['unverified']]
    lines+=['','## Provider-independent prompt','',brief['prompt'],'']
    return '\n'.join(lines)

def prepare(scene,scenario,out,analysis=None,photo=None):
    destination(out)
    validate_scene(scene);validate_scenario(scenario)
    if out.exists() and any(out.iterdir()):raise ValueError('Use a new empty render directory')
    if scene['site_bbl']!=scenario['site_bbl']:raise ValueError('Scene/scenario parcel mismatch')
    out.mkdir(parents=True,exist_ok=True);(out/'inputs').mkdir()
    save(out/'inputs/scene.json',scene);save(out/'inputs/scenario.json',scenario)
    ref={**scene['reference'],'site_match':scene['site_match'],'storage':scene['reference']['availability'],'path':None,'sha256':None}
    if ref['storage']=='local_file':
        if photo is None:raise ValueError('Local-file reference requires --photo')
        data,suffix=image_file(photo);ref['path']='inputs/reference'+suffix
        (out/ref['path']).write_bytes(data);ref['sha256']=digest(data)
    elif photo is not None:raise ValueError('A local photo requires local_file reference availability')
    analysis_data=None;analysis_sha=None
    if analysis is not None:
        data=Path(analysis).read_bytes();(out/'inputs/analysis.json').write_bytes(data)
        analysis_data=load(out/'inputs/analysis.json');analysis_sha=digest(data)
    brief=compile_brief(scene,scenario,ref,analysis_data,analysis_sha)
    save(out/'render-brief.json',brief);save(out/'workflow.json',load(WORKFLOW))
    (out/'prompt.txt').write_text(brief['prompt']+'\n');(out/'brief.md').write_text(markdown(brief))
    write_manifest(out);verify(out)
    return brief

def expected_brief(root):
    scene=load(root/'inputs/scene.json');scenario=load(root/'inputs/scenario.json')
    validate_scene(scene);validate_scenario(scenario)
    ref={**scene['reference'],'site_match':scene['site_match'],'storage':scene['reference']['availability'],'path':None,'sha256':None}
    if ref['storage']=='local_file':
        matches=[p for p in (root/'inputs').glob('reference.*') if p.suffix in {'.png','.jpg'}]
        if len(matches)!=1:raise ValueError('Reference file missing or ambiguous')
        data,_=image_file(matches[0]);ref['path']=str(matches[0].relative_to(root));ref['sha256']=digest(data)
    analysis=load(root/'inputs/analysis.json') if (root/'inputs/analysis.json').exists() else None
    h=digest((root/'inputs/analysis.json').read_bytes()) if analysis is not None else None
    return compile_brief(scene,scenario,ref,analysis,h)

def verify(root):
    manifest=load(root/'manifest.json')
    if manifest['implementation']!=implementation():
        from housing_runtime import verify_historical
        return verify_historical('housing_render', root)
    if manifest['files']!=files_manifest(root):raise ValueError('Render package inventory or bytes changed')
    for name in manifest['files']:safe(root,name)
    brief=expected_brief(root)
    if load(root/'render-brief.json')!=brief or (root/'prompt.txt').read_text()!=brief['prompt']+'\n':raise ValueError('Render brief differs from scene/scenario/analysis')
    if (root/'brief.md').read_text()!=markdown(brief) or load(root/'workflow.json')!=load(WORKFLOW):raise ValueError('Brief projection or workflow changed')
    if (root/'render-receipt.json').exists():
        receipt=load(root/'render-receipt.json');review=load(root/'review.json');validate_review(review)
        invocation=load(root/'invocation.json');validate_invocation(invocation,brief,root)
        if receipt!=make_receipt(root,brief,invocation,review,receipt['image_path']):raise ValueError('Generation receipt bindings changed')
        if (root/'packet.md').read_text()!=render_packet(brief,review,receipt['image_path']):raise ValueError('Render packet projection changed')
    return {'status':'passed','stage':'generated_and_reviewed' if (root/'render-receipt.json').exists() else 'brief_prepared','source_image_byte_bound':brief['reference']['sha256'] is not None,'geometry_verified':False,'professional_acceptance':'pending'}

def validate_invocation(invocation,brief,root):
    required={'provider','prompt_sha256','brief_sha256','reference_id','reference_delivery','parameters','executed_at','execution_note'}
    if set(invocation)!=required:raise ValueError('Missing or unexpected invocation fields')
    if invocation['prompt_sha256']!=digest(brief['prompt'].encode()) or invocation['brief_sha256']!=digest((root/'render-brief.json').read_bytes()):raise ValueError('Invocation prompt/brief is stale')
    if invocation['reference_id']!=brief['reference']['id']:raise ValueError('Invocation reference mismatch')
    expected='conversation_attachment' if brief['reference']['storage']=='conversation_attachment' else 'local_file'
    if invocation['reference_delivery']!=expected:raise ValueError('Provider reference delivery differs from declared asset')
    if not isinstance(invocation['parameters'],dict) or not invocation['provider'] or not invocation['executed_at'] or not invocation['execution_note']:raise ValueError('Incomplete execution record')
    if expected=='conversation_attachment' and not isinstance(invocation['parameters'].get('num_last_images_to_include'),int):raise ValueError('Record actual conversation reference selection')

def make_receipt(root,brief,invocation,review,image_path):
    if image_path not in {'render.png','render.jpg'}:raise ValueError('Unsupported generated-image path')
    image_file(safe(root,image_path))
    return {'version':VERSION,'provider':invocation['provider'],'site_bbl':brief['site_bbl'],'scenario_id':brief['scenario_id'],
            'brief_sha256':digest((root/'render-brief.json').read_bytes()),'prompt_sha256':digest(brief['prompt'].encode()),
            'scenario_sha256':digest((root/'inputs/scenario.json').read_bytes()),'scene_sha256':digest((root/'inputs/scene.json').read_bytes()),
            'analysis_sha256':brief['analysis']['sha256'],'reference':brief['reference'],
            'invocation_sha256':digest((root/'invocation.json').read_bytes()),'image_path':image_path,'image_sha256':digest(safe(root,image_path).read_bytes()),
            'review_sha256':digest((root/'review.json').read_bytes()),'reviewer_kind':review['reviewer_kind'],
            'visual_review_status':'issues_observed' if any(x['status']=='issue_observed' for x in review['checks']) else 'inspected_with_limits',
            'geometry_verified':False,'professional_acceptance':'pending','reproduction':'Prompt and bytes bound; image provider stochastic. External conversation reference bytes unavailable locally.' if brief['reference']['storage']=='conversation_attachment' else 'Inputs and output bytes bound; image generation remains stochastic.'}

def attach(root,image,invocation,review):
    destination(root)
    verify(root)
    if (root/'render-receipt.json').exists():raise ValueError('Generation already attached; preserve it and create a new run')
    brief=load(root/'render-brief.json');validate_invocation(invocation,brief,root);validate_review(review)
    data,suffix=image_file(image);path='render'+suffix
    (root/path).write_bytes(data);save(root/'invocation.json',invocation);save(root/'review.json',review)
    receipt=make_receipt(root,brief,invocation,review,path);save(root/'render-receipt.json',receipt)
    (root/'packet.md').write_text(render_packet(brief,review,path));write_manifest(root)
    return verify(root)


def render_packet(brief,review,path):
    report=markdown(brief)+'\n## Generated illustration\n\n![Illustrative site concept]('+path+')\n\n## Visual review\n\n'+review['summary']+'\n\n'
    report+='\n'.join('- **'+x['id']+' — '+x['status']+'**: '+x['note'] for x in review['checks'])+'\n\nReview is an attested visual inspection, not independent professional acceptance.\n'
    return report
