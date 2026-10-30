"""Check active skill resources/routing and frozen historical instruction hashes. MIT."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEAVES = {
    'housing-investigation', 'collect-parcel-evidence', 'model-parcel-scenario',
    'publish-evidence-packet', 'run-analysis-recipe', 'compare-housing-programs',
    'prepare-rer-draft', 'build-grounded-massing', 'prepare-render-brief', 'render-site-concept',
}


def check(root=ROOT):
    problems = []
    catalog = json.loads((root / 'skills/catalog.json').read_text())
    expected = {'skills/start-here/SKILL.md'} | {f'skills/{n}/SKILL.md' for n in LEAVES}
    if catalog.get('version') != '1.0' or catalog.get('entry') != 'skills/start-here/SKILL.md':
        raise ValueError('Unsupported skill catalogue or coordinator')
    if set(catalog['active']) != expected or len(catalog['active']) != len(expected):
        raise ValueError('Active skill catalogue coverage differs')
    discovered = {str(p.relative_to(root)) for p in (root/'skills').glob('*/SKILL.md')}
    if discovered != expected or (root/'skills/current').exists():
        raise ValueError('Active skills must be directly under skills/<skill-name>/')
    historical = catalog['historical_bound']
    if {h['path'] for h in historical} != {f'archive/skill-layout-v0/skills/{n}/SKILL.md' for n in LEAVES} or len(historical) != len(LEAVES):
        raise ValueError('Historical skill inventory differs')
    for item in historical:
        path = root / item['path']
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            problems.append(f'Frozen historical skill changed: {item["path"]}')
    skills = [root / p for p in sorted(expected)]
    names = set()
    resources = []
    for skill in skills:
        if not skill.exists():
            problems.append(f'Missing active skill: {skill}')
            continue
        text = skill.read_text()
        header = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', text)
        if not header or header[1] != skill.parent.name or len(header[1]) > 64 or len(header[2]) > 1024:
            problems.append(f'{skill}: invalid name/description frontmatter')
        elif header[1] in names:
            problems.append(f'{skill}: duplicate active skill name')
        else:
            names.add(header[1])
        refs = sorted((skill.parent / 'references').glob('*.md'))
        if not refs or not all(f'references/{ref.name}' in text for ref in refs):
            problems.append(f'{skill}: execution references must link directly from SKILL.md')
        if len(text.splitlines()) > 100:
            problems.append(f'{skill}: exceeds our 100-line entry budget; move detail to references')
        if skill.parent.name != 'start-here':
            runbook=skill.parent/'references/runbook.md'
            if not runbook.exists() or runbook.read_text().splitlines()[0] != '# '+skill.parent.name+': execution reference':
                problems.append(f'{skill}: execution reference belongs to the wrong skill')
        resources.extend(refs)
    docs = [root / 'README.md', root / 'AGENTS.md', root / 'CLAUDE.md', root / 'docs/guides/first-run.md', root / 'docs/guides/setup.md', root / 'docs/reference/repository-layout.md',
            root / 'docs/guides/investigate-a-lot.md', root / 'docs/reference/module-catalog.md',
            root / 'docs/templates/review-cover-note.md', root / 'docs/guides/local-only.md',
            root / 'skills/README.md', *skills, *resources]
    for doc in docs:
        if not doc.exists():
            problems.append(f'Missing entry/resource document: {doc}')
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = (doc.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                problems.append(f'{doc.relative_to(root)}: broken/escaping link {link}')
    # The coordinator routes lazily through the module map, not by preloading leaves.
    mapping = root / 'skills/start-here/references/modules.md'
    text = mapping.read_text()
    for name in ['housing-investigation', 'run-analysis-recipe', 'compare-housing-programs',
                 'prepare-rer-draft', 'build-grounded-massing', 'prepare-render-brief', 'render-site-concept']:
        if f'../../{name}/SKILL.md' not in text:
            problems.append(f'Coordinator missing current route: {name}')
    if '../../scripts/first_run.py' not in (root / 'skills/start-here/SKILL.md').read_text():
        problems.append('Coordinator missing shared walkthrough script')
    if problems:
        raise ValueError('\n'.join(problems))
    return (f'Passed: {len(skills)} active skills, progressive-disclosure resources/routes, '
            f'{len(historical)} frozen skill hashes (not semantic skill quality)')


if __name__ == '__main__':
    try:
        print(check())
    except (ValueError, KeyError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
