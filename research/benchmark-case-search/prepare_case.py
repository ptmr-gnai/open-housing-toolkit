"""Freeze document inputs separately from outcome references; no evaluation run. MIT."""
import datetime,hashlib,json,pathlib,re,shutil,subprocess,zipfile
P=pathlib.Path(__file__).resolve().parent

def digest(b):return hashlib.sha256(b).hexdigest()
def save(n,v):(P/n).write_text(json.dumps(v,indent=2)+'\n')
source=json.loads((P/'cache/candidate_0_inputs.receipt.json').read_text())
inputs=P/'inputs';inputs.mkdir(exist_ok=True)
files=[('97-west-169th-st-rfp.pdf','2018-12-21'),('97-west-169th-street-rfp-addendum.pdf','2019-02-19'),('97-west-169th-street-rfp-addendum2.pdf','2019-03-13'),('97-west-169th-street-rfp-addendum3.pdf','2019-03-26')]
manifest={'version':'0.1','case':'97 West 169th Street, Bronx','cutoff':'2019-04-04','experiment_status':'prepared_not_run','scope':'Document-bounded retrospective reconstruction, not certified historical data or independent expert evaluation','input_sources':[],'excluded':['designation announcements','current project pages','HPD archive narratives','later building data','curator rubric and case-search notes'],'historical_bytes_certified':False,'archive_check':'Internet Archive availability query for one www1 ZIP URL returned no snapshot; this does not establish that no archival copy exists.','curator_exposed_to_outcomes':True,'analyst_requires_fresh_context':True,'historical_raw_data_added':False}
for filename,date in files:
    original=P/'extracted/candidate_0'/filename;destination=inputs/filename;shutil.copyfile(original,destination)
    text=original.with_suffix('.text');shutil.copyfile(text,inputs/text.name)
    proc=subprocess.run(['pdfinfo',str(original)],capture_output=True,text=True,check=True)
    meta={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in proc.stdout.splitlines() if ':' in line}
    manifest['input_sources'].append({'file':filename,'text_file':text.name,'declared_issue_date':date,'date_evidence':'RFP or addendum cover, PDF page 1','source_url':source['url'],'source_zip_sha256':source['sha256'],'zip_member':'97-west-169th-street-rfp/'+filename,'pdf_sha256':digest(original.read_bytes()),'text_sha256':digest(text.read_bytes()),'pdf_creation':meta.get('CreationDate'),'pdf_modified':meta.get('ModDate'),'pdf_pages':int(meta['Pages']),'text_transform':'pdftotext -layout'})
manifest['input_files_sha256']=digest(json.dumps(manifest['input_sources'],sort_keys=True).encode())
(inputs/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
task='''# Initial site assessment task

Act as a housing practitioner assessing 97 West 169th Street in the Bronx using
only the four supplied HPD solicitation PDFs and addenda available by April 4,
2019. Do not browse the web or consult the case-search directory, outcome
announcement, current data, later proposals or the curator rubric.

Produce a reviewable initial assessment addressing:

1. Existing site condition and identity, including contradictory evidence.
2. Development pathways worth investigating and why.
3. Constraints that could invalidate or materially change those pathways.
4. Missing evidence and professional judgments.
5. The next action and the role responsible for it.

Cite document and PDF page for every consequential claim. Separate agency
statements, calculations, assumptions and unknowns. Explain how addenda supersede
or clarify the original solicitation. Keep legal capacity, physical fit and
financial feasibility distinct. Do not manufacture a survey, site visit, lender
quote, cost estimate or professional acceptance. Any numeric scenario must expose
its inputs, units, formula and limitations.

The task is not to guess the selected developer, match its unit count, copy its
amenities or reproduce its final design. RFP requirements are legitimate inputs;
repeating them does not demonstrate independently discovered feasibility.

Freeze the assessment and its assumptions before consulting a later reference.
This input packet uses currently retrieved agency documents whose printed dates
and PDF metadata precede the cutoff. The source ZIP was repackaged later and exact
historical byte equivalence is not independently certified. Historical PLUTO,
zoning maps, market data and site investigations have not been added. These limits
must remain visible in the assessment.
'''
(inputs/'task.md').write_text(task)
reference=json.loads((P/'cache/candidate_0_reference.receipt.json').read_text())
save('case-selection.json',{'recommendation':'97 West 169th Street','basis':['Bronx CD4 and geographically close to original corridor probe','Single development site comprised of two parcels','Original RFP and three addenda physically retrieved and internally dated pre-cutoff','Concrete terrain, parkland, identity and program constraints','Later dated agency selection summary physically retrieved'],'stage':'Developer designation announced 2019-12-05; construction completion not verified','reference':reference,'input_manifest':'inputs/manifest.json','full_submitted_proposal_available':False,'strict_historical_backtest_ready':False,'document_reconstruction_ready':True,'practitioner_utility_test_ready':False,'limitations':['No independently verified pre-cutoff archive copy','Discovery curator has seen reference outcomes','Public designation summary is not full submitted proposal or underwriting','Expert usefulness/time-savings hypothesis needs real practitioner feedback'],'alternatives':[{'name':'351 Powers Avenue','stage':'Designation 2024-02-16','input_issue':'Printed RFP date 2022-08-18, but retrieved PDF created/modified April 2024, after designation; strict use deferred pending version reconciliation','strength':'Complete CVR, RFP, two addenda and conference; partial-tax-lot, parking and climate constraints'},{'name':'425 Grand Concourse','stage':'Designation 2016-04-28','strength':'2015 RFP and addenda; complex mixed-use/high-rise and rezoning case','reason_not_first':'Larger, more complex scope and longer historical-data reconstruction'},{'name':"St. Ann’s Avenue / East 142nd Street",'stage':'Designation 2016-01-14','strength':'2015 RFP, addenda, launch and designation summaries','reason_not_first':'Older mixed-use/rezoning reconstruction; useful subsequent case'}]})
archive=pathlib.Path('/workspace/97-west-169th-input-packet.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in sorted(inputs.iterdir()):
        info=zipfile.ZipInfo('inputs/'+f.name,date_time=(2026,10,4,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,f.read_bytes())
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print('Prepared',len(files),'pre-reference input PDFs;',archive.stat().st_size,'byte input-only archive')
