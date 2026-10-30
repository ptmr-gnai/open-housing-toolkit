#!/usr/bin/env python3
"""Small artifact and boundary linter; fail closed on broken evidence exports. MIT."""
import ast,json,pathlib,re
from pipeline import ROOT,read_json,validate_config

def lint(out=None):
    out=pathlib.Path(out) if out is not None else ROOT/'outputs'
    problems=[]
    for path in list(ROOT.glob('*.py'))+list((ROOT/'tests').glob('*.py')):
        try:ast.parse(path.read_text(),filename=str(path))
        except SyntaxError as e:problems.append(str(e))
    for path in list(ROOT.glob('*.json'))+list((ROOT/'schemas').glob('*.json')):
        try:read_json(path)
        except ValueError as e:problems.append(str(path)+': '+str(e))
    try:validate_config(read_json(ROOT/'probe.json'))
    except (ValueError,KeyError,TypeError) as e:problems.append(str(e))
    for path in out.glob('*.md'):
        text=path.read_text()
        if '|\n\n|' in text:problems.append(str(path)+': blank lines inside table')
        if re.search(r'__(?:ADDRESS|MAP|ROWS|CARDS|DATA)__',text):problems.append(str(path)+': unresolved template token')
    path=out/'advisor-explorer.html'
    if path.exists():
        text=path.read_text()
        if re.search(r'__(?:ADDRESS|MAP|ROWS|CARDS|DATA)__',text):problems.append('HTML has unresolved template token')
        if 'https://' in text.split('<head>',1)[-1].split('</head>',1)[0]:problems.append('Explorer has external head dependency')
        if 'not represented as available' not in text and 'No site is represented as available' not in text:problems.append('Conditional site notice missing')
    if problems:raise ValueError('\n'.join(problems))
    return {'status':'passed','checks':['Python syntax','JSON syntax','supported DSL','Markdown tables','template completeness','self-contained viewer','conditional site notice']}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=pathlib.Path);args=parser.parse_args()
    print(json.dumps(lint(args.run)))
