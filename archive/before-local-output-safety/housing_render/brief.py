"""Compile canonical inputs into an image-provider-independent prompt. MIT."""
from .contracts import VERSION, validate_scene, validate_scenario, text


def compile_brief(scene,scenario,reference,analysis=None,analysis_sha=None):
    validate_scene(scene);validate_scenario(scenario)
    if scene['site_bbl']!=scenario['site_bbl']:raise ValueError('Scene/scenario parcel mismatch')
    bindings=[]
    if analysis is not None:
        if analysis.get('resolved_bbl')!=scene['site_bbl']:raise ValueError('Analysis is for a different parcel')
        claims=analysis.get('claims')
        if not isinstance(claims,list):raise ValueError('Canonical analysis requires a claims array')
        by_id={c['id']:c for c in claims}
        if len(by_id)!=len(claims):raise ValueError('Duplicate analysis claim IDs')
        for key in ['pluto.0.address','pluto.0.lotarea','pluto.0.unitsres','pluto.0.zonedist1','pluto.0.spdist1']:
            if key in by_id:
                c=by_id[key]
                if c.get('kind')!='fact' or not c.get('references'):raise ValueError('Context fact lacks provenance')
                bindings.append({'claim_id':key,'value':c['value'],'unit':c['unit'],'references':c['references'],'use':'site_context_only_not_geometric_constraint'})
    p=scenario['parameters'];n=p['total_stories']['value']
    caption=f'ILLUSTRATIVE CONCEPT — ASSUMED {n} STORIES'
    provider=scene['reference']['provider'];date=scene['reference']['capture_date']
    ground=p['ground_floor_use']['value'];upper=p['upper_floor_use']['value'];style=p['architectural_treatment']['value']
    prompt=(
        'Use the user-supplied original street photograph as the visual reference for an architectural concept edit. '
        'If several recent conversation images are supplied, identify the ORIGINAL white-and-blue single-story commercial building photograph; '
        'prior generated concepts are not evidence of existing conditions. '
        f'The user associates this reference with NYC tax lot {scene["site_bbl"]}; that match is {scene["site_match"]}, not independently geolocated by this module. '
        f'Viewpoint instructions: {scene["viewpoint"]} '
        f'Illustrate a hypothetical replacement building with exactly {n} stories TOTAL: one taller ground floor for {ground}, '
        f'and {n-1} upper floors for {upper}. '
        f'Architectural treatment: {style} '
        'Use approximately the visible existing building location as a visual cue only. No surveyed footprint, parcel boundary, setback distance or total floor area has been supplied. '
        'Preserve the photographed street perspective and surrounding context as closely as possible. Do not redesign neighboring properties. '
        'This is a replacement concept; do not imply that extra floors can be supported by the existing structure. '
        'Do not invent street numbers, tenant names, approved unit counts, affordability commitments or official approval. '
        'Remove large navigation UI controls while retaining source watermark/attribution. '
        f'Include a readable bottom caption with these lines: "{caption}" and "Zoning, parcel boundaries and building fit unverified." '
        f'Credit: "Base image: user-supplied {provider}, {date}." '
        'A separate area-budget analysis, if present in the packet, is context only and has not been reconciled to this massing. '
        'Generate a photorealistic illustrative streetscape, not an assertion of feasible or approved development.'
    )
    return {'version':VERSION,'module':'site-concept','site_bbl':scene['site_bbl'],'scenario_id':scenario['id'],
            'mode':'photo_referenced_illustrative_concept','prompt':prompt,'reference':reference,
            'scenario_bindings':[{'parameter':k,**v} for k,v in sorted(p.items())],
            'derived_visual_instructions':[{'id':'upper_floor_count','value':n-1,'formula':'total_stories - 1','inputs':['total_stories']}],
            'analysis':{'available':analysis is not None,'sha256':analysis_sha,'context_bindings':bindings,'geometry_or_area_budget_reconciled':False,'acceptance':'imported context values checked; analysis semantics not certified by renderer'},
            'required_caption':caption,'unverified':['photo-to-parcel match unless separately attested','surveyed footprint','height in feet','setbacks','total floor area','building fit','zoning entitlement','current occupancy','finance'],
            'execution_requirements':{'reference_resolution':'agent must resolve declared reference before generation','image_generation':'external provider; stochastic output, not byte-reproducible','review':'visual inspection required; no automatic geometry certification'}}
