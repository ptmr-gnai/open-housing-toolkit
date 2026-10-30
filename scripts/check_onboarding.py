"""Validate repository skill discovery, local resource links and walkthrough routes. MIT."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    problems = []
    names = set()
    for skill in skills:
        text = skill.read_text()
        header = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', text)
        if not header or header[1] != skill.parent.name:
            problems.append(f'{skill}: missing/invalid name and description frontmatter')
        elif header[1] in names:
            problems.append(f'{skill}: duplicate skill name')
        else:
            names.add(header[1])
    docs = [root / 'AGENTS.md', root / 'CLAUDE.md', root / 'docs/first-run.md', *skills,
            *sorted((root / 'skills/start-here/references').glob('*.md'))]
    for doc in docs:
        if not doc.exists():
            problems.append(f'Missing entry document: {doc}')
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = (doc.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                problems.append(f'{doc.relative_to(root)}: broken/escaping link {link}')
    entry = root / 'skills/start-here/SKILL.md'
    if entry.exists():
        text = entry.read_text()
        for name in ['housing-investigation', 'run-analysis-recipe', 'compare-housing-programs', 'prepare-rer-draft']:
            if f'../{name}/SKILL.md' not in text:
                problems.append(f'Coordinator missing route: {name}')
        if '../../scripts/first_run.py' not in text:
            problems.append('Coordinator missing executable walkthrough link')
    if problems:
        raise ValueError('\n'.join(problems))
    return f'Passed: {len(skills)} skills, entry documents, local resource links and core routes (not semantic skill quality)'


if __name__ == '__main__':
    try:
        print(check())
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
