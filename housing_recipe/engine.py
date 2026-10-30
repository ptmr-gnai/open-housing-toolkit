"""Immutable recipe runs, exact source preservation, deterministic exports. MIT."""
from pathlib import Path
import shutil
from housing_workflow import engine as evidence, packet
from housing_workflow.contracts import digest, dumps, load, save
from .recipe import compile_recipe, impact

ROOT=Path(__file__).resolve().parents[1]

def implementation():
    paths=sorted((ROOT/'housing_recipe').glob('*.py'))+sorted((ROOT/'housing_recipe').glob('*.json'))
    paths += [ROOT/'skills/run-analysis-recipe/SKILL.md']
    paths += [ROOT/'housing_runtime.py']
    paths += [ref for skill in list(paths) if skill.name=='SKILL.md' for ref in sorted((skill.parent/'references').glob('*.md'))]
    return {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in paths}


def projections(ir, receipts, recipe):
    md,page,csv=packet.projections(ir,receipts)
    note='Analysis recipe: '+recipe['id']+' revision '+recipe['revision']+'; SHA256 '+ir['analysis_recipe']['sha256']+'. Professional review pending.'
    md += '\n## Analysis recipe\n\n'+note+'\n\nSee recipe.json and trace.json for assumptions, versioned methods, execution order and review gates. The retained evidence-run contains the original source packet; its prior scenario has been replaced in this packet.\n'
    import html
    page=page.replace('</main>','<h2>Analysis recipe</h2><p>'+html.escape(note)+'</p><p>See recipe.json and trace.json. The evidence-run retains the original packet and its prior scenario.</p></main>')
    prompts=packet.prompts(ir);prompts['model_sha256']=digest(dumps(ir).encode())
    return {'packet.md':md,'packet.html':page,'calculation-steps.csv':csv,'image-prompts.json':dumps(prompts)}


def compiled(folder):
    evidence.verify(folder/'evidence-run')
    r=load(folder/'recipe.json');ir,trace=compile_recipe(r,load(folder/'evidence-run/ir.json'))
    receipts=load(folder/'evidence-run/receipts.json')
    evidence.validate_claims(ir,receipts,folder/'evidence-run')
    outputs={'ir.json':dumps(ir),'trace.json':dumps(trace),**projections(ir,receipts,r)}
    # Packets link sources/ relative to their own directory, not evidence-run/.
    return outputs


def inventory(folder):
    return {str(p.relative_to(folder)):digest(evidence.safe(folder,str(p.relative_to(folder))).read_bytes())
            for p in sorted(folder.rglob('*')) if p.is_file() and p != folder/'manifest.json'}


def verify(folder):
    m=load(folder/'manifest.json')
    if m.get('module')!='analysis-recipe':raise ValueError('Not a recipe run')
    if m['implementation']!=implementation():
        from housing_runtime import verify_historical
        return verify_historical('housing_recipe', folder)
    if m['files']!=inventory(folder):raise ValueError('Recipe run inventory or artifact hash changed')
    for name,value in compiled(folder).items():
        if (folder/name).read_bytes()!=value.encode():raise ValueError('Recipe projection differs: '+name)
    # Duplicated source bodies exist for portable packet links; both copies must agree.
    for p in (folder/'evidence-run/sources').iterdir():
        if (folder/'sources'/p.name).read_bytes()!=p.read_bytes():raise ValueError('Packet source copy changed')
    return {'status':'passed','module':'analysis-recipe','recipe':load(folder/'ir.json')['analysis_recipe'],
            'packet':str(folder/'packet.html'),'professional_review':'pending'}


def source_packet(source):
    if load(source/'manifest.json').get('module')=='analysis-recipe':
        verify(source);return source/'evidence-run'
    evidence.verify(source);return source


def build(source, recipe, folder):
    base=source_packet(source)
    # Validate everything before creating outputs.
    ir,_=compile_recipe(recipe,load(base/'ir.json'))
    evidence.validate_claims(ir,load(base/'receipts.json'),base)
    if folder.resolve().is_relative_to(source.resolve()):raise ValueError('Output must be outside source run')
    evidence.fresh(folder)
    shutil.copytree(base,folder/'evidence-run')
    shutil.copytree(base/'sources',folder/'sources')
    save(folder/'recipe.json',recipe)
    for name,value in compiled(folder).items():(folder/name).write_text(value)
    save(folder/'origin.json',{'source_manifest_sha256':digest((source/'manifest.json').read_bytes()),
                              'evidence_manifest_sha256':digest((base/'manifest.json').read_bytes()),
                              'source_kind':'recipe' if base!=source else 'parcel-investigation'})
    save(folder/'manifest.json',{'version':'0.1.0','module':'analysis-recipe','implementation':implementation(),
                                'files':inventory(folder),'validation_scope':'Typed arithmetic, retained evidence, recipe bindings and deterministic exports. Not professional interpretation or completeness.'})
    return verify(folder)


def preview(source, recipe):
    verify(source)
    ir,_=compile_recipe(recipe,load(source/'evidence-run/ir.json'))
    evidence.validate_claims(ir,load(source/'evidence-run/receipts.json'),source/'evidence-run')
    return impact(load(source/'ir.json'),load(source/'recipe.json'),ir,recipe)
