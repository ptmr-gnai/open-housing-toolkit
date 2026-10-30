"""Five-section documents and a separately labeled diagnostic appendix. MIT."""
import html
import re
from .contracts import Status

SECTIONS={1:'Executive summary',2:'Project specific information',3:'Community Profile Summary',4:'Affirmatively furthering fair housing and promoting equitable access to opportunity',5:'Community profile'}


def safe(v):return str(v).replace('|','/').replace('\n',' ')


def projections(ir):
    outputs={};claims={c['id']:c for c in ir['comparison_claims']}
    overview=['# RER preparation drafts','', '**Incomplete illustrative drafts — not official submissions.**','',
              'These documents follow the five-section structure of the pinned City guide and form. They show what our existing comparison can support, what has a different meaning, and what remains missing.','',
              'No applicability finding, completeness percentage, benefit ranking or professional acceptance is produced.','',
              '| Program | Draft | Coverage |','| --- | --- | --- |']
    coverage=['# Instruction-to-implementation map','',ir['scope'],'',
              'Each status concerns a mapped slot only. Filled metadata/caveats do not establish a complete report. The inventory is manually curated and has not had professional coverage review.','',
              '| Program | ID | Slot | Status | Source | Mapping reason |','| --- | --- | --- | --- | --- | --- |']
    for report in ir['reports']:
        pid=report['program_id'];overview.append('| '+safe(report['program_label'])+' | [Read draft](report-'+pid+'.md) | [Map](coverage.md) |')
        slots=report['slots'];rows=['# RER preparation draft — '+report['program_label'],'',
              '**INCOMPLETE · ILLUSTRATIVE · NOT THE OFFICIAL FORM**','',
              'Site: '+report['site_bbl']+'. Prepared by '+ir['prepared_by']+' on '+ir['prepared_on']+'. Applicability and professional review pending.','',
              '[Pinned official form]('+next(s['url'] for s in ir['source_documents'] if s['id']=='form')+') · [Detailed instruction map](coverage.md)','',
              'Status key: filled = populated slot only; illustrative = supplied assumption; missing = absent material; needs_interpretation = unresolved meaning/scope; not_applicable = conditional exclusion under a stated assumption. None certifies compliance.','',
              '## Cover and applicability','']
        for section in range(6):
            if section>0:rows += ['## Section '+str(section)+': '+SECTIONS[section],'']
            rows += ['| Field | Status | Content |','| --- | --- | --- |']
            for slot in [s for s in slots if s['section']==section]:
                value='Not populated' if slot['value'] is None else str(slot['value'])
                rows.append('| '+safe(slot['label'])+' | '+slot['status']+' | '+safe(value)+' |')
                refs='; '.join(c['document']+' p.'+str(c['pdf_page'])+' §'+c['subsection'] for c in slot['sources'])
                coverage.append('| '+pid+' | '+slot['requirement_id']+' | '+safe(slot['label'])+' | '+slot['status']+' | '+safe(refs)+' | '+safe(slot['reason'])+' |')
            rows.append('')
            if section==2:
                rows += ['### Available program inputs — not a completed RER affordability table','',
                         'The bins below are rent-offer groups, not income-restriction categories or AMI bands. Program-specific eligible incomes and guide-compatible rent fields remain unpopulated.','',
                         '| Input bin | Assumed homes | Assumed contract rent USD/month | Assumed tenant utilities USD/month | Proposed restriction years |','| --- | --- | --- | --- | --- |']
                p=next(p for p in ir['comparison_programs'] if p['id']==pid)
                for b in p['bins']:
                    rows.append('| '+b['id']+' | '+' | '.join(str(claims[b['claims'][k]]['value']) for k in ['homes','monthly_rent_usd','tenant_utilities_usd','restriction_years'])+' |')
                rows += ['', 'The previous gross-area scenario is not zoning square footage or a verified area for this program. No conversion or job estimate is made.','',
                         '**Instruction divergence:** the 2023 form and 2025 guide differ about nonresidential area reporting without identified tenants. We retain area placeholders and withhold speculative jobs pending interpretation.','']
            if section==3:rows += ['No EDDE summary or displacement map is attached. No neighborhood statistics, community-district/PUMA match or displacement conclusion has been generated.','']
            if section==4:rows += ['Narrative is awaiting an attributed practitioner/applicant interpretation supported by project and community evidence. The listed goal prompts do not independently establish legal tests or a claim that this proposal advances them.','']
            if section==5:rows += ['No validated full local/borough/city profile is attached. Applicability of the guide’s section-specific exception remains unresolved.','']
        rows += ['## Supplemental appendix A — household cost diagnostic','',
                 'This is the earlier conditional cost-and-bedroom test. It does not fill the RER income eligibility or AMI-mix fields. Profiles are hypothetical and use historical references.','',
                 '| Profile | Homes meeting diagnostic conditions |','| --- | --- |']
        p=next(p for p in ir['comparison_programs'] if p['id']==pid)
        for count in p['profile_counts']:
            profile=next(h for h in ir['comparison_profiles'] if h['id']==count['profile_id'])
            rows.append('| '+safe(profile['label'])+' | '+str(claims[count['homes_claim']]['value'])+' |')
        rows += ['', '[Original conditional comparison](comparison-run/packet.md) · [Typed RER draft and source bindings](rer.json)','',
                 '## Review and source limits','']+['- '+v for v in ir['limitations']]
        rows += ['',ir['source_verification_scope'],'']
        md='\n'.join(rows).rstrip()+'\n';outputs['report-'+pid+'.md']=md
        outputs['report-'+pid+'.html']=html_page(rows)
    overview += ['', '[Full mapping](coverage.md) · [Typed output](rer.json)','',
                 'Source versions are pinned: the guide has a July 2025 internal stamp, the form June 2023, and the criteria PDF an unresolved printed-date placeholder. Source PDF/page hashes are recorded; the external PDFs are not bundled. Normal offline verification checks those metadata bindings, not the source PDFs or their interpretation.','',
                 'The household-cost packet is preserved separately. No reference income is silently recast as eligibility, and no gross area as zoning floor area.','']
    outputs['packet.md']='\n'.join(overview).rstrip()+'\n';outputs['packet.html']=html_page(overview)
    outputs['coverage.md']='\n'.join(coverage).rstrip()+'\n'
    outputs['coverage.html']=html_page(coverage)
    return outputs


def html_page(rows):
    def inline(value):
        escaped=html.escape(value)
        def link(match):
            label,target=match[1],match[2]
            if not (target.startswith('https://www.nyc.gov/') or re.fullmatch(r'(report-[a-z0-9_]+\.md|coverage\.md|rer\.json|comparison-run/packet\.md)',target)):return label
            if target.endswith('.md'):target=target[:-3]+'.html'
            return '<a href="'+target+'">'+label+'</a>'
        escaped=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,escaped)
        return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',escaped)
    parts=[];table=False
    for line in rows:
        if line.startswith('|'):
            if not table:parts.append('<table>');table=True
            if set(line.replace('|','').replace(' ',''))=={'-'}:continue
            parts.append('<tr>'+''.join('<td>'+inline(x.strip())+'</td>' for x in line.strip('|').split('|'))+'</tr>');continue
        if table:parts.append('</table>');table=False
        if line.startswith('### '):parts.append('<h3>'+html.escape(line[4:])+'</h3>')
        elif line.startswith('## '):parts.append('<h2>'+html.escape(line[3:])+'</h2>')
        elif line.startswith('# '):parts.append('<h1>'+html.escape(line[2:])+'</h1>')
        elif line:parts.append('<p>'+inline(line)+'</p>')
    if table:parts.append('</table>')
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Incomplete RER preparation draft</title><style>body{font:17px/1.5 system-ui;max-width:1100px;margin:30px auto;padding:20px;color:#223542}table{border-collapse:collapse;display:block;overflow:auto}td{border:1px solid #ccd6dc;padding:9px}tr:first-child{background:#eef3f5}p{overflow-wrap:anywhere}h2{margin-top:2em}</style><main>'+''.join(parts)+'</main></html>\n'
