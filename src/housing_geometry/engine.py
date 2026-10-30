"""Independent geometry module, preserving verified analysis and source packages. MIT."""
from pathlib import Path
import shutil
import shapely
from housing_workflow import engine as evidence
from housing_recipe import engine as recipes
from housing_workflow.contracts import digest, load, save
from .model import compile_model
from .exports import exports
from . import sources

from housing_common.local_outputs import ROOT


def implementation():
    files=sorted(Path(__file__).resolve().parent.glob('*.py'))+sorted(Path(__file__).resolve().parent.glob('*.json'))
    files += [ROOT/'pyproject.toml',ROOT/'skills/build-grounded-massing/SKILL.md',ROOT/'config/workflows/grounded-massing.json']
    files += [ROOT/'src/housing_common/runtime.py']
    files += [ref for skill in list(files) if skill.name=='SKILL.md' for ref in sorted((skill.parent/'references').glob('*.md'))]
    return {'files':{str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in files},'shapely':shapely.__version__,'geos':shapely.geos_version_string}


def verify_analysis(folder):
    module=load(folder/'manifest.json').get('module')
    if module=='analysis-recipe':return recipes.verify(folder)
    return evidence.verify(folder)


def compile_run(folder):
    verify_analysis(folder/'analysis-run');sources.verify(folder/'parcel-source')
    ir=compile_model(load(folder/'scenario.json'),folder/'parcel-source',load(folder/'analysis-run/ir.json'),digest((folder/'analysis-run/ir.json').read_bytes()))
    return exports(ir)


def inventory(folder):
    return {str(p.relative_to(folder)):digest(evidence.safe(folder,str(p.relative_to(folder))).read_bytes())
            for p in sorted(folder.rglob('*')) if p.is_file() and p!=folder/'manifest.json'}


def verify(folder):
    m=load(folder/'manifest.json')
    if m.get('module')!='grounded-massing' or m.get('version')!='0.1.0':raise ValueError('Unsupported geometry run')
    if m['implementation']!=implementation():
        from housing_common.runtime import verify_historical
        return verify_historical('housing_geometry', folder)
    if m['files']!=inventory(folder):raise ValueError('Geometry run inventory or artifact hash changed')
    for name,content in compile_run(folder).items():
        if (folder/name).read_bytes()!=content.encode():raise ValueError('Geometry output differs from retained inputs: '+name)
    ir=load(folder/'geometry.json')
    return {'status':'passed','module':'grounded-massing','bbl':ir['site_bbl'],'visual_handoff_status':ir['visual_handoff_status'],
            'professional_review':'pending','packet':str(folder/'packet.html')}


def build(analysis,source,scenario,folder):
    verify_analysis(analysis);sources.verify(source)
    compile_model(scenario,source,load(analysis/'ir.json'),digest((analysis/'ir.json').read_bytes()))
    if folder.resolve().is_relative_to(analysis.resolve()) or folder.resolve().is_relative_to(source.resolve()):raise ValueError('Output cannot be inside an input package')
    evidence.fresh(folder)
    shutil.copytree(analysis,folder/'analysis-run');shutil.copytree(source,folder/'parcel-source');save(folder/'scenario.json',scenario)
    for name,content in compile_run(folder).items():(folder/name).write_text(content)
    save(folder/'manifest.json',{'version':'0.1.0','module':'grounded-massing','implementation':implementation(),'files':inventory(folder),
                                'validation_scope':'Source bindings, explicit geometry, mapped containment, area proxy reconciliation and deterministic exports. Not professional feasibility.'})
    return verify(folder)
