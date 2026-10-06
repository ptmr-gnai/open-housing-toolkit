"""Labeled synthetic packet construction; no genuine proposal acceptance. MIT."""
import copy,json,pathlib,zipfile
from scan import BASE,ROOT,fp
from coverage_engine import load,contract
import engine as eligibility

def create_files():
    path=BASE/'fixtures/packet-fixture.xlsx'
    if not path.exists():
        with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for name,data in {'[Content_Types].xml':'<Types>Synthetic test fixture only</Types>','xl/workbook.xml':'<workbook>Synthetic test fixture only</workbook>'}.items():
                item=zipfile.ZipInfo(name,date_time=(2020,1,1,0,0,0));z.writestr(item,data)
    text=BASE/'fixtures/packet-fixture.txt'
    if not text.exists():text.write_text('SYNTHETIC TEST PACKET. Not a proposal, credential or accepted professional review.\n')
    return path,text

def reviewed(payload,fingerprint):
    return {'status':'accepted','reviewer':'synthetic-test-reviewer','contract':fingerprint,'payload_fingerprint':fp(payload)}

def packet(case,accepted=True,facts=None):
    xlsx,text=create_files();sources,registry=load();fingerprint=contract(registry,sources)
    facts={'nonprofit_team':False,'nonresidential_space':True} if facts is None else facts
    artifacts={}
    for r in registry['requirements']:
        if r['case']!=case:continue
        path=xlsx if r['excel'] else text
        a={'requirement_id':r['id'],'file':str(path.relative_to(ROOT)),'sha256':eligibility.sha(path.read_bytes()),'synthetic':True}
        a['review']=reviewed(a,fingerprint) if accepted else {'status':'pending'};artifacts[r['id']]=a
    facts_evidence={'file':str(text.relative_to(ROOT)),'sha256':eligibility.sha(text.read_bytes()),'synthetic':True}
    return {'id':'synthetic_scoped_packet','kind':'synthetic','inventory_complete':True,'facts':facts,'facts_evidence':facts_evidence,'facts_review':reviewed({'facts':facts,'evidence':facts_evidence},fingerprint),'artifacts':artifacts,'required_requests':[]}
