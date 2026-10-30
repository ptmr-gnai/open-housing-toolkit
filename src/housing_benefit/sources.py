"""Bounded, reproducible extraction of two historical RER Table 3 rows. MIT."""
import re
from housing_workflow.contracts import digest
from housing_workflow.engine import safe
from .contracts import fields

URL='https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a'

from .contracts import read_json as load


def validate_source(folder):
    m=load(folder/'receipt.json')
    fields(m,['version','method','url','publisher','document_stamp','income_year','rent_year','page','source_pdf_sha256','source_pdf_availability','source_bytes','retrieved_at_utc','passages_sha256','column_order','extraction','terms_url'])
    fields(m['extraction'],['tool','command','script_sha256','checked_against_pdf_at_preparation'])
    if m['column_order']!=['ami_percent','one_person_income_usd','four_person_income_usd','studio_rent_usd','two_bedroom_rent_usd'] or m['extraction']['checked_against_pdf_at_preparation'] is not True:
        raise ValueError('Unsupported source column mapping or unverified extraction preparation')
    if m.get('version')!='0.1.0' or m.get('method')!='nyc-rer-table3-selected-rows@1' or m.get('url')!=URL:
        raise ValueError('Unsupported reference extraction adapter')
    if m.get('source_pdf_availability')!='external_not_bundled' or m.get('page')!=6:raise ValueError('Reference source provenance changed')
    if not re.fullmatch('[0-9a-f]{64}',m.get('source_pdf_sha256','')) or not m.get('retrieved_at_utc'):raise ValueError('Missing original document version receipt')
    if type(m['income_year'])!=int or type(m['rent_year'])!=int or type(m['source_bytes'])!=int or m['source_bytes']<=0:
        raise ValueError('Invalid reference schedule metadata types')
    if m['publisher']!='NYC Department of City Planning' or m['terms_url']!='https://www.nyc.gov/home/terms-of-use.page':raise ValueError('Unexpected reference publisher/terms')
    if not re.fullmatch('[0-9a-f]{64}',m['extraction']['script_sha256']):raise ValueError('Missing extraction implementation binding')
    actual={str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual!={'receipt.json','passages.txt'}:raise ValueError('Unexpected reference package inventory')
    raw=safe(folder,'passages.txt').read_bytes()
    if digest(raw)!=m['passages_sha256']:raise ValueError('Reference passage hash changed')
    lines=raw.decode().splitlines()
    header=re.fullmatch(r'Table 3: Affordable rents and eligible incomes \(([0-9]{4}) AMI\)',lines[0])
    if not header or len(lines)!=3:raise ValueError('Unsupported reference table excerpt')
    year=int(header[1])
    if m.get('income_year')!=year or m.get('rent_year')!=year:raise ValueError('Mixed-vintage reference schedules or stale table metadata')
    rows=[]
    for index,line in enumerate(lines[1:]):
        match=re.fullmatch(r'(30|60)% AMI \$([0-9,]+) \$([0-9,]+) \$([0-9,]+) \$([0-9,]+)',line)
        if not match:raise ValueError('Unresolved reference row passage')
        ami=int(match[1]);values=[str(int(x.replace(',','')))+'.00' for x in match.groups()[1:]]
        for field,value,hh,bedroom in [('income_one',values[0],1,None),('income_four',values[1],4,None),('rent_studio',values[2],None,0),('rent_two',values[3],None,2)]:
            rows.append({'id':f'ami{ami}_{field}','value':value,'year':year,'household_size':hh,'bedrooms':bedroom,
                         'ami_percent':ami,'quantity':'annual_income_usd' if hh else 'reference_monthly_rent_usd','quote':line,'passage_line':index+2,
                         'reference':{'url':m['url'],'source_pdf_sha256':m['source_pdf_sha256'],'page':6,'table':'3','quote':line,'excerpt_file':'reference-source/passages.txt','excerpt_sha256':m['passages_sha256'],'extraction_method':m['method']}})
    if len({r['ami_percent'] for r in rows})!=2:raise ValueError('Missing/duplicate selected AMI band')
    return {'income_year':year,'rent_year':year,'rows':rows,'receipt':m,
            'scope':'Historical rounded guidance values; excerpt binds to an externally identified PDF. Ordinary offline verification does not re-download or re-extract that PDF.'}
