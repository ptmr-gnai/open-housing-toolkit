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

VERSION = '1.1.0'
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
    'shape_matches_massing': 'Width, ground-floor height and how the upper floors sit follow the 3D massing and elevation.',
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
    setback_phrase = (' and set back about %s ft behind the ground-floor street wall' % _ft(setback)) if setback >= 2 else \
        ', rising flush with the ground-floor street wall'
    caption = 'Illustrative concept: %d stories from the schematic massing. Zoning and site fit unverified.' % n
    credit = 'Base image: %s, %s (user-supplied)' % (request['photo']['provider'], request['photo']['capture_date'])
    ground_h = ground['top_ft'] - ground['base_ft']
    ratio = (ground_h / upper_h) if upper else None
    lines = [
        'Edit Image 1, a street photograph of the site, into a photorealistic architectural concept of a planned building.',
        '',
        'The reference images, in order:',
        '- Image 1: the real street today. Keep everything outside the lot as it is: the street, sidewalk, vehicles, trees, '
        'neighbouring buildings, the light and the camera position.',
        '- Image 2: the planned building as a simple 3D model seen from across the street. Blue is the ground floor; orange is '
        'the apartment floors above, with one line per floor: count them, there are %d orange floors above 1 blue floor. '
        'Match this volume: its proportions, its floor count and how the upper floors sit on the ground floor.' % (n - 1),
        '- Image 3: the front elevation of the planned building, drawn to scale. Use it for proportions%s.'
        % (': the ground floor is %s times as tall as each apartment floor' % format(round(ratio, 1), 'g') if ratio else ''),
        '- Image 4: the site plan. The grey band at the bottom is the street; the thick dark line is the street frontage; blue is '
        'the ground-floor footprint; orange is the upper-floor footprint.',
        '',
        'The planned building replaces the existing buildings on the lot completely; no part of them, their signs, awnings or '
        'rooflines remains. It has %d stories and is about %s ft tall: a %s ft ground floor running about %s ft along the street'
        % (n, _ft(elev['height_ft']), _ft(ground_h), _ft(ground['width_ft'])) +
        (', and %d apartment floors of %s ft each, about %s ft wide%s. Show %d clearly countable rows of windows above the '
         'ground floor, one row per apartment floor; do not merge or drop floors to make the building fit.'
         % (n - 1, _ft(upper_h), _ft(upper_w), setback_phrase, n - 1) if upper else '.'),
        '',
        'Framing: show the whole building, its roof and some sky above it. If the building does not fit in the frame of '
        'Image 1, extend the scene upward (a taller image, or the camera tilted slightly up) rather than shortening the '
        'building. Keep the street and sidewalk at the bottom as in Image 1.',
        '',
        'Ground floor: %s, plus a separate residential entrance.' % GROUND_USES[request['ground_use']] +
        (' Apartment floors: %s.' % STYLES[request['style']] if upper else ''),
        '',
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
            'references': ['inputs/reference%s' % request['photo']['suffix'], 'massing-3d.png', 'elevation.png', 'site-plan.png'],
            'reference_roles': ['site photo', '3D massing from across the street', 'front elevation to scale', 'site plan'],
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
    refs = [out / r for r in concept['references']]
    result.update({'next': 'Generate one image with these reference images in this order: %s; prompt = the exact contents of %s. '
                           'Then python -m housing_concept attach --run %s --image IMAGE --provider "..." --review REVIEW.json '
                           '(python -m housing_concept review-template writes REVIEW.json)'
                           % (', '.join(str(r) for r in refs), out / 'prompt.txt', out),
                   'reference_images': [str(r) for r in refs],
                   'frontage_edge': concept['frontage_edge'], 'available_edges': concept['available_edges']})
    return result


def write_outputs(folder):
    concept, prompt, elev = compile_concept(folder)
    save(Path(folder) / 'concept.json', concept)
    (Path(folder) / 'prompt.txt').write_text(prompt)
    (Path(folder) / 'elevation.png').write_bytes(elevation.png(elev))
    (Path(folder) / 'elevation.svg').write_text(elevation.svg(elev))
    view, plan = render_views(folder, concept)
    (Path(folder) / 'massing-3d.png').write_bytes(view)
    (Path(folder) / 'site-plan.png').write_bytes(plan)


def render_views(folder, concept):
    from . import views
    geometry = load(Path(folder) / 'inputs/massing/geometry.json')
    frame = elevation.frontage_frame(geometry['source_geometry']['polygon_ft'], concept['frontage_edge']['index']
                                     if concept['frontage_edge']['rule'] == 'chosen edge' else None)
    return views.street_view(geometry, frame)[0], views.site_plan(geometry, frame)[0]


def _png_pixels(data):
    """Decode the filter-0 RGB PNGs written by this module."""
    import struct as _s
    import zlib as _z
    import numpy as np
    width, height = _s.unpack('>II', data[16:24])
    pos, idat = 8, b''
    while pos < len(data):
        length = _s.unpack('>I', data[pos:pos + 4])[0]
        tag = data[pos + 4:pos + 8]
        if tag == b'IDAT':
            idat += data[pos + 8:pos + 8 + length]
        pos += 12 + length
    raw = np.frombuffer(_z.decompress(idat), dtype=np.uint8).reshape(height, 1 + width * 3)
    return raw[:, 1:].reshape(height, width, 3)


def _same_view(stored, fresh, tolerance=0.002):
    """Raster views can differ by a few edge pixels across CPUs; accept at most 0.2% differing pixels."""
    if stored == fresh:
        return True
    a, b = _png_pixels(stored), _png_pixels(fresh)
    return a.shape == b.shape and float((a != b).any(axis=2).mean()) <= tolerance


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
                                                        'massing_3d': digest((run / 'massing-3d.png').read_bytes()),
                                                        'elevation': digest((run / 'elevation.png').read_bytes()),
                                                        'site_plan': digest((run / 'site-plan.png').read_bytes())},
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
    view, plan = render_views(run, concept)
    if not _same_view((run / 'massing-3d.png').read_bytes(), view) or not _same_view((run / 'site-plan.png').read_bytes(), plan):
        raise ValueError('Massing views differ from the massing')
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
        refs = {'massing_3d': 'massing-3d.png', 'elevation': 'elevation.png', 'site_plan': 'site-plan.png'}
        if any(gen['reference_sha256'][k] != digest((run / f).read_bytes()) for k, f in refs.items()) or \
                gen['reference_sha256']['photo'] != request['photo']['sha256']:
            raise ValueError('Generation references differ from this package')
        stage = 'generated_and_reviewed'
    return {'status': 'passed', 'stage': stage, 'site_bbl': concept['site_bbl'], 'massing_id': concept['massing_id'],
            'stories': concept['stories'], 'prompt': str(run / 'prompt.txt'), 'elevation': str(run / 'elevation.png')}
