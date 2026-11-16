"""Massing-grounded concept render: elevation drawing + fixed prompt + recorded generation and review. MIT.

The prompt is compiled from typed numbers (stories, heights, widths, setback) taken
from a verified massing and from two short choices (style, ground floor). The agent
cannot append text to it. The image itself is generated outside this module (Codex's
image tool) with the site photo and the elevation drawing as references, then
attached with a fixed review.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

from housing_common.local_outputs import ROOT, destination
from . import elevation

VERSION = '1.0.0'
HERE = Path(__file__).resolve().parent
STYLES = {
    'brick': 'warm red-brown brick with regular punched windows and simple trim',
    'light_masonry': 'light buff or grey masonry with regular punched windows',
    'metal_glass': 'metal panels and glass in a regular window grid',
}
GROUND_USES = {
    'shops': 'new shopfronts with large glass windows and plain sign bands carrying no brand names',
    'shops_and_supermarket': 'a new supermarket frontage and smaller shopfronts with large glass windows; sign bands are plain, with no brand names',
    'community': 'a glazed community space',
}
CHECKS = {
    'story_count': 'The new building shows exactly the stated number of stories (count the window rows).',
    'existing_buildings_removed': 'No part of the existing buildings, signs or awnings on the lot remains.',
    'shape_matches_elevation': 'Width, ground-floor height and upper-floor setback follow the elevation drawing.',
    'context_preserved': 'Street, neighbours, trees, vehicles, light and camera position match the photo.',
    'caption_and_credit': 'The caption bar and photo credit are present and legible.',
}
STATUSES = {'consistent', 'not_consistent', 'not_verified'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def dumps(value):
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + '\n'


def save(path, value):
    Path(path).write_text(dumps(value))


def implementation():
    files = sorted(HERE.glob('*.py')) + sorted(HERE.glob('*.json'))
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in files}


def inventory(folder):
    folder = Path(folder)
    return {str(p.relative_to(folder)): digest(p.read_bytes()) for p in sorted(folder.rglob('*'))
            if p.is_file() and p != folder / 'manifest.json' and '__pycache__' not in p.parts}


def _short(value, name, limit):
    if not isinstance(value, str) or not value.strip() or len(value) > limit or '\n' in value:
        raise ValueError('%s must be one line of at most %d characters' % (name, limit))
    return value.strip()


def _image(path):
    data = Path(path).read_bytes()
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return data, '.png'
    if data.startswith(b'\xff\xd8\xff'):
        return data, '.jpg'
    raise ValueError('Provide a PNG or JPEG image: %s' % path)


def _ft(value):
    return str(int(round(value)))


def compile_concept(folder):
    """Everything derived: elevation numbers, prompt, caption. Recomputed by verify."""
    folder = Path(folder)
    request = load(folder / 'request.json')
    geometry = load(folder / 'inputs/massing/geometry.json')
    elev = elevation.project(geometry, request['frontage_edge'])
    floors = elev['floors']
    ground, upper = floors[0], floors[1:]
    n = len(floors)
    upper_h = round(upper[0]['top_ft'] - upper[0]['base_ft'], 1) if upper else None
    upper_w = max(f['width_ft'] for f in upper) if upper else None
    setback = round(upper[0]['street_setback_ft'] - ground['street_setback_ft'], 1) if upper else 0
    setback_phrase = (', set back about %s ft from the street wall of the ground floor' % _ft(setback)) if setback >= 2 else \
        ', rising flush with the ground floor'
    caption = 'Illustrative concept: %d stories from the schematic massing. Zoning and site fit unverified.' % n
    credit = 'Base image: %s, %s (user-supplied)' % (request['photo']['provider'], request['photo']['capture_date'])
    lines = [
        'Edit Image 1, a street photograph of the site, into a photorealistic architectural concept.',
        'Replace the existing buildings on the lot with ONE new building. Image 2 is a front elevation of the new building, '
        'drawn to scale from the schematic massing: follow its outline, floor count and proportions.',
        'The new building has %d stories and is about %s ft tall.' % (n, _ft(elev['height_ft'])),
        'Ground floor: about %s ft tall and %s ft wide along the street. It has %s. Add a separate residential entrance.'
        % (_ft(ground['top_ft'] - ground['base_ft']), _ft(ground['width_ft']), GROUND_USES[request['ground_use']]),
    ]
    if upper:
        lines.append('Floors 2 to %d: apartments, about %s ft wide%s, in %s. Each upper floor is about %s ft tall; '
                     'show %d clearly countable rows of windows above the ground floor.'
                     % (n, _ft(upper_w), setback_phrase, STYLES[request['style']], _ft(upper_h), n - 1))
    lines += [
        'The existing buildings on the lot, with their signs, awnings and rooflines, are removed; no part of them remains.',
        'Keep everything outside the lot as in Image 1: the street, sidewalks, neighbouring buildings, trees, vehicles, light and camera position.',
        'Do not add brand names, street numbers or any other text, except a caption bar along the bottom reading "%s" '
        'and the credit "%s".' % (caption, credit),
    ]
    prompt = '\n'.join(lines) + '\n'
    return {'version': VERSION, 'site_bbl': geometry['site_bbl'], 'massing_id': geometry['scenario_id'],
            'stories': n, 'height_ft': elev['height_ft'], 'ground_floor_height_ft': round(ground['top_ft'] - ground['base_ft'], 1),
            'ground_floor_width_ft': ground['width_ft'], 'upper_floor_height_ft': upper_h, 'upper_floor_width_ft': upper_w,
            'upper_setback_ft': setback, 'lot_width_ft': elev['lot_width_ft'], 'frontage_edge': elev['frontage_edge'],
            'available_edges': elev['available_edges'], 'style': request['style'], 'ground_use': request['ground_use'],
            'caption': caption, 'credit': credit, 'photo': request['photo'],
            'references': ['Image 1: inputs/reference%s (site photo)' % request['photo']['suffix'],
                           'Image 2: elevation.png (front elevation from the massing)'],
            'prompt_sha256': digest(prompt.encode()), 'elevation': elev}, prompt, elev


def prepare(massing, photo, out, style, ground_use, provider, capture_date, frontage_edge=None):
    from housing_geometry.engine import verify as verify_massing
    if style not in STYLES:
        raise ValueError('style must be one of ' + ', '.join(STYLES))
    if ground_use not in GROUND_USES:
        raise ValueError('ground_use must be one of ' + ', '.join(GROUND_USES))
    massing = Path(massing)
    verify_massing(massing)
    out = destination(out) if Path(out).resolve().is_relative_to(ROOT) else Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty; prepare a new folder for each attempt')
    data, suffix = _image(photo)
    out.mkdir(parents=True, exist_ok=True)
    shutil.copytree(massing, out / 'inputs/massing', ignore=shutil.ignore_patterns('__pycache__'))
    (out / ('inputs/reference' + suffix)).write_bytes(data)
    save(out / 'request.json', {'version': '1.0', 'style': style, 'ground_use': ground_use, 'frontage_edge': frontage_edge,
                                'photo': {'provider': _short(provider, 'provider', 40), 'capture_date': _short(capture_date, 'capture date', 20),
                                          'suffix': suffix, 'sha256': digest(data), 'origin': 'user_supplied'}})
    write_outputs(out)
    seal(out)
    result = verify(out)
    concept = load(out / 'concept.json')
    result.update({'next': 'Generate one image with Image 1 = %s and Image 2 = %s, using prompt.txt exactly; then '
                           'python -m housing_concept attach --run %s --image IMAGE --provider "..." --review REVIEW.json '
                           '(python -m housing_concept review-template writes REVIEW.json)'
                           % (out / ('inputs/reference' + suffix), out / 'elevation.png', out),
                   'frontage_edge': concept['frontage_edge'], 'available_edges': concept['available_edges']})
    return result


def write_outputs(folder):
    concept, prompt, elev = compile_concept(folder)
    save(Path(folder) / 'concept.json', concept)
    (Path(folder) / 'prompt.txt').write_text(prompt)
    (Path(folder) / 'elevation.png').write_bytes(elevation.png(elev))
    (Path(folder) / 'elevation.svg').write_text(elevation.svg(elev))


def seal(folder):
    save(Path(folder) / 'manifest.json', {'version': VERSION, 'module': 'massing-concept', 'implementation': implementation(),
                                          'files': inventory(folder),
                                          'validation_scope': 'Prompt and elevation recomputed from the retained massing; image bound by hash '
                                                              'with an attributed review. Not a design, survey or zoning check.'})


def review_template(out):
    out = Path(out)
    if out.exists():
        raise ValueError('Refusing to overwrite ' + str(out))
    save(out, {'reviewer': 'AGENT NAME', 'checks': {k: {'status': 'not_verified', 'note': ''} for k in CHECKS},
               '_how': 'Look at the generated image. For each check set status to consistent, not_consistent or not_verified, '
                       'with a note of at most 160 characters. If story_count or existing_buildings_removed is not_consistent, '
                       'regenerate instead of attaching. Delete this _how line.'})
    return {'status': 'written', 'review': str(out), 'checks': CHECKS}


def _validate_review(review):
    if set(review) != {'reviewer', 'checks'} or set(review['checks']) != set(CHECKS):
        raise ValueError('Review needs reviewer and exactly these checks: ' + ', '.join(CHECKS))
    _short(review['reviewer'], 'reviewer', 60)
    for key, c in review['checks'].items():
        if set(c) != {'status', 'note'} or c['status'] not in STATUSES:
            raise ValueError('Check %s needs status (consistent, not_consistent, not_verified) and note' % key)
        if not isinstance(c['note'], str) or len(c['note']) > 160 or '\n' in c['note']:
            raise ValueError('Check %s note is limited to one line of 160 characters' % key)
    for key in ('story_count', 'existing_buildings_removed'):
        if review['checks'][key]['status'] == 'not_consistent':
            raise ValueError('%s is not consistent: regenerate the image instead of attaching it' % key)
    return review


def attach(run, image, provider, review):
    run = Path(run)
    verify(run)
    if (run / 'render.png').exists() or (run / 'render.jpg').exists():
        raise ValueError('An image is already attached; prepare a new folder for another attempt')
    review = _validate_review(load(review))
    data, suffix = _image(image)
    (run / ('render' + suffix)).write_bytes(data)
    concept = load(run / 'concept.json')
    save(run / 'review.json', review)
    save(run / 'generation.json', {'provider': _short(provider, 'provider', 60), 'image': 'render' + suffix,
                                   'image_sha256': digest(data), 'prompt_sha256': concept['prompt_sha256'],
                                   'reference_sha256': {'photo': concept['photo']['sha256'],
                                                        'elevation': digest((run / 'elevation.png').read_bytes())},
                                   'attached_at': datetime.now(timezone.utc).isoformat()})
    seal(run)
    return verify(run)


def verify(run):
    run = Path(run)
    manifest = load(run / 'manifest.json')
    if manifest.get('module') != 'massing-concept' or manifest.get('version') != VERSION:
        raise ValueError('Not a massing-concept package')
    if manifest['implementation'] != implementation():
        raise ValueError('Built by a different version of housing_concept; prepare again into a new folder')
    if manifest['files'] != inventory(run):
        raise ValueError('Concept package files were added, removed or changed')
    from housing_geometry.engine import verify as verify_massing
    verify_massing(run / 'inputs/massing')
    concept, prompt, elev = compile_concept(run)
    if load(run / 'concept.json') != concept or (run / 'prompt.txt').read_text() != prompt:
        raise ValueError('Prompt or concept differs from the massing it was compiled from')
    if (run / 'elevation.png').read_bytes() != elevation.png(elev) or (run / 'elevation.svg').read_text() != elevation.svg(elev):
        raise ValueError('Elevation drawing differs from the massing')
    request = load(run / 'request.json')
    photo = run / ('inputs/reference' + request['photo']['suffix'])
    if photo.exists() and digest(photo.read_bytes()) != request['photo']['sha256']:
        raise ValueError('Site photo changed')
    stage = 'prompt_prepared'
    if (run / 'generation.json').exists():
        gen = load(run / 'generation.json')
        _validate_review(load(run / 'review.json'))
        if gen['prompt_sha256'] != concept['prompt_sha256'] or digest((run / gen['image']).read_bytes()) != gen['image_sha256']:
            raise ValueError('Generated image or its prompt binding changed')
        if gen['reference_sha256']['elevation'] != digest((run / 'elevation.png').read_bytes()) or \
                gen['reference_sha256']['photo'] != request['photo']['sha256']:
            raise ValueError('Generation references differ from this package')
        stage = 'generated_and_reviewed'
    return {'status': 'passed', 'stage': stage, 'site_bbl': concept['site_bbl'], 'massing_id': concept['massing_id'],
            'stories': concept['stories'], 'prompt': str(run / 'prompt.txt'), 'elevation': str(run / 'elevation.png')}
