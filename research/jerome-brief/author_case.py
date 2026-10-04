"""Reviewed extraction definitions; model assumptions and unknowns are explicit. MIT."""
import json,pathlib
P=pathlib.Path(__file__).resolve().parent
claims=[]
def observed(id,value,unit,source,locator,quote=None,selector=None,scope='Agency statement or recorded attribute; not independently certified'):
    claims.append(dict(id=id,kind='observed',value=value,unit=unit,evidence={'source_id':source,'locator':locator,**({'quote':quote} if quote else {}),**({'selector':selector} if selector else {})},scope=scope))
def unknown(id,reason):claims.append(dict(id=id,kind='unknown',value=None,unit=None,reason=reason))
def assumption(id,value,unit,reason):claims.append(dict(id=id,kind='assumption',value=value,unit=unit,reason=reason))
observed('parcel_bbl',2028560051,'BBL','pluto','row 0, bbl',selector=['0','bbl'])
for id,field,unit in [('lot_area','lotarea','square feet'),('existing_bldg_area','bldgarea','square feet'),('existing_units','unitsres','dwelling units'),('existing_built_far','builtfar','FAR'),('standard_far','residfar','FAR'),('affordable_far','affresfar','FAR')]:
    row=json.loads((P/'cache/pluto.body').read_text())[0];observed(id,float(row[field]),unit,'pluto','row 0, '+field,selector=['0',field])
for id,field in [('district','zonedist1'),('overlay','overlay1'),('special_district','spdist1'),('owner_label','ownername'),('irregular_lot','irrlotcode'),('mih_option1','mih_opt1'),('mih_option3','mih_opt3')]:
    row=json.loads((P/'cache/pluto.body').read_text())[0];observed(id,row[field],None,'pluto','row 0, '+field,selector=['0',field])
observed('building_bin',2008295,'BIN','geosearch','exact-address candidate, features[0].properties.addendum.pad.bin',selector=['features','0','properties','addendum','pad','bin'])
observed('coop_flip_tax',0.10,'minimum share of resale proceeds','open_door','PDF page 3',quote='Apartment resales are subject to a minimum 10% flip tax paid out of sales proceeds to the HDFC cooperative.')
observed('coop_reserves','Capitalized/operating budget reserves and monthly operating/replacement reserves',None,'open_door','PDF page 3',quote='Underwriting for cooperative buildings will be required to include monthly operating and/or replacement reserves in the monthly maintenance charges.')
observed('city_land_debt','Nominal $1 disposition with balance of appraised value in enforcement note/mortgage',None,'open_door','PDF page 2 Land Acquisition',quote='For City-owned sites, disposition will be for $1 per lot with the balance of appraised value in an enforcement note and mortgage')
observed('program','Open Door',None,'jerome_project','Project Background',quote='The site will be developed using HPD’s Open Door program')
observed('past_use','City pest control facility until 2013',None,'jerome_project','Site Overview',quote='City pest control facility until 2013')
observed('agency_vacancy','vacant one-story commercial building',None,'jerome_project','Site Overview',quote='a vacant one-story commercial building')
observed('rfp_status','community visioning; RFP planned Fall 2026',None,'jerome_project','Request for Proposals',quote='developers selected from the Neighborhood Builders Pre-Qualified List in Fall 2026')
observed('community_response_due','October 16; year not repeated in deadline sentence',None,'jerome_project','How to Get Involved',quote='Project Questionnaire by October 16!')
for id,value,unit,quote in [('agency_current_far',7.2,'FAR','Max. Residential 7.20 9.02 Floor Area Ratio'),('agency_rezone_far',9.02,'FAR','Max. Residential 7.20 9.02 Floor Area Ratio'),('agency_current_height',175,'feet','Max. Height 175’ 185’'),('agency_rezone_height',185,'feet','Max. Height 175’ 185’'),('agency_current_units',48,'estimated homes','Est. Units 48 60'),('agency_rezone_units',60,'estimated homes','Est. Units 48 60')]:
 observed(id,value,unit,'jerome_cb4','PDF page 7',quote=quote,scope='HPD September 14, 2026 planning concept; not independently verified buildable or approved capacity')
observed('agency_timeline','RFP before year-end; submissions early spring 2027; designation late spring/early summer 2027',None,'jerome_cb4','PDF page 10',quote='Spring 2027',scope='Agency planning schedule, not binding procurement deadlines; webpage says Fall 2026')
observed('open_door_version','2025-06-30',None,'open_door','PDF page 1 footer',quote='Updated – 06.30.2025')
observed('housing_cost_share',0.33,'share of annual household income','open_door','PDF page 1 Sales Prices',quote='cap housing costs at 33% of total annual income')
observed('sales_income_range','70–120% AMI or as dictated by market',None,'open_door','PDF page 1 Sales Prices',quote='between 70-120% AMI, or as dictated by market')
observed('market_discount',0.10,'minimum share','open_door','PDF page 1 Sales Prices',quote='A minimum 10% discount to market will be required.')
observed('coop_regulatory_years',40,'minimum years','open_door','PDF page 3 Regulatory Requirements',quote='Cooperative projects will be subject to a minimum 40-year Regulatory Agreement')
observed('maintenance_escalation',0.02,'minimum annual share','open_door','PDF page 3 Regulatory Requirements',quote='Minimum annual maintenance increases of 2% per year.')
observed('subsidy_caps',[445000,430000,365000,355000],'USD per dwelling unit by AMI tier','open_door','PDF page 1 table',quote='Up to 80% $445,000 81%-90% $430,000 91%-100% $365,000 101%-120% $355,000',scope='Maximum contingent amounts, not awarded subsidy; AHOP/AHC availability and HPD determination apply')
observed('subsidy_contingency','AHOP up to 100% AMI; AHC at 101–120%',None,'open_door','PDF page 1',quote='contingent upon the availability of AHOP funds for units up to 100% AMI and AHC funds for units between 101% and 120% AMI.')
observed('hdfc_ownership','HDFC during construction',None,'open_door','PDF page 1 Eligible Borrowers',quote='the property must be owned by a Housing Development Fund')
observed('guideline_effective','2026-10-01 design consultation submissions',None,'design_process','PDF page 1 Applicability',quote='Design Consultation on or after October 1, 2026.')
observed('environmental_review_rule','Phase I unless BCP or hazardous-material E-designation pathway; noise screening also required',None,'design_process','PDF page 4 note',quote='require the submission of a Phase I Environmental Site Assessment (ESA), unless the site is going through the Brownfield Cleanup Program or subject to (E)-Designation for hazardous materials; noise screening is also required.')
observed('zoning_141_25_condition','R8A special height branch requires outside MIH and within 100 feet of wide street',None,'jerome_zoning','Section 141-25',quote='within 100 feet of a wide street located outside of Mandatory Inclusionary Housing areas, the underlying height and setback provisions applicable to an R8 District')
observed('zoning_141_23_condition','Elevated-rail height/setback branch outside Subdistrict A',None,'jerome_zoning','Section 141-23',quote='within 100 feet of street lines along the elevated rail structure on Jerome or River Avenues, and located outside Subdistrict A')
observed('expedited_density_description',0.30,'maximum increase in HPD example, not complete eligibility test','expedited_housing','ELURP-CPC section',quote='increasing allowable floor area in a medium-density district by no more than 30%')
observed('income_2026_3person',[106890,122160,152700,183240],'USD annual at 70, 80, 100, 120% AMI','ami','2026 income table, family size 3',quote='3 $30,540 $45,810 $61,080 $76,350 $91,620 $106,890 $122,160 $137,430 $152,700 $167,970 $183,240 $198,510 $251,955 $267,225',scope='2026 regional AMI income benchmarks; not local household income or actual buyer eligibility')
observed('e_screen',0,'returned rows','e_designation','complete bounded BBL query response',selector=['length'],scope='No rows returned for queried tax BBL; does not clear environmental conditions, lot history or other instruments')
assumption('analysis_no_action','Existing recorded nonresidential use remains; no residential redevelopment',None,'A comparison assumption for this brief only; no independently accepted CEQR No-Action scenario or forecast.')
assumption('budget_household_size',3,'persons','Illustrative comparison using a single household size. Unit bedroom/household-size mapping and final project mix unresolved.')
unknowns={'legal_envelope':'No reviewed survey, zoning-lot geometry, MIH/subdistrict mapping or written rule reconciliation; agency planning values remain attributed.',
'community_priorities':'Questionnaire ongoing; completed Jerome community visioning report not located in the captured project-page links. No priorities inferred from generic citywide policy.',
'site_control':'Agency owner label is not a title opinion or development agreement; disposition, easements and current legal control unverified.',
'occupancy':'Agency vacancy description not independently checked by site visit, lease or occupant verification.',
'environment':'No Phase I/BCP/E-pathway documents, noise/air assessment, geotechnical or remediation acceptance reviewed.',
'finance':'No project costs, lenders, costed design, mix, sales prices, maintenance, reserves, confirmed subsidy or operating model.',
'approval_path':'HPD slide labels ELURP; no legal eligibility determination, application or final approvals reviewed.',
'qualified_team':'No proposed developer or confirmation of pre-qualified eligibility.',
'usable_transit':'Transit proximity stated by agency; no verified pedestrian route, step-free access, door-to-door routing or reliability estimate.',
'buyer_access':'No local eligible-buyer income/assets/credit distribution, down-payment assistance or closing-cost analysis.',
'procurement_requirements':'Jerome RFP, final program/mix, addenda and completeness checklist not available in captured materials.',
'professional_design':'No surveyed architectural scheme or cost estimate independently prepared or reviewed.'}
for k,v in unknowns.items():unknown(k,v)
requirements=[
('zoning','Reconcile legal envelope and agency concept','legal_envelope','Architect / zoning counsel','Written zoning memo tied to survey, mapped MIH/subdistrict boundaries, special elevated-rail rules and affordable housing qualification.'),
('community','Use actual community priorities','community_priorities','HPD / community engagement lead','Published Jerome CVR and traceable proposal response; avoid fabricating survey results.'),
('control','Confirm legal control and disposition','site_control','Title counsel / HPD','Current title, restrictions/easements and disposition/development documents.'),
('occupants','Verify existing occupants and obligations','occupancy','Developer / housing counsel','Site/lease verification and any relocation or tenant protection requirements.'),
('environment','Determine environmental pathway and costs','environment','Environmental professional / HPD/OER','Applicable Phase I or alternate BCP/E materials, noise/air assessment and review disposition.'),
('finance','Underwrite co-op development and buyer affordability','finance','Housing finance advisor / lender / HPD','Complete sources/uses and sales/maintenance/reserve model; funding availability and rates.'),
('approvals','Determine approvals and schedule','approval_path','Land-use counsel / HPD/DCP','Written eligibility and approvals roadmap; separate public-land disposition from zoning change.'),
('team','Verify developer/program qualifications','qualified_team','Sponsor / HPD','Pre-qualified status and applicable HDFC/sponsor experience evidence.'),
('transit','Measure usable transit access','usable_transit','Transport analyst','Dated pedestrian route plus scheduled/reliability-aware travel comparisons and accessibility limits.'),
('buyers','Test who can actually buy and remain','buyer_access','Housing finance / fair housing advisor','Income/assets/credit, down payment and closing costs; maintenance escalation, reserves and resale restrictions.'),
('rfp','Complete site-specific procurement requirements','procurement_requirements','Sponsor / HPD','Issued Jerome RFP, amendments and final threshold checklist; no borrowing another site’s criteria.'),
('design','Provide dimensioned professional design','professional_design','Architect / engineer / estimator','Survey-based plans, areas, core/lift layout, program and amenity mix, accessibility and signed cost estimate.')]
case={'schema_version':'0.1','case_id':'jerome-1337','as_of':'2026-10-04','address':'1337 Jerome Avenue, Bronx','purpose':'Independent advisor-review benchmark for an open housing playbook; not an RFP response','claims':claims,'requirements':[dict(id=a,title=b,unknown_claim=c,review_owner=d,acceptance=e,status='unresolved') for a,b,c,d,e in requirements],'decision':'Determine whether the agency’s additional ~12-home rezoning concept warrants more detailed review after envelope, community and economic checks. Do not recommend development or a bidder yet.'}
extractors={
'coop_flip_tax':{'pattern':r'minimum (\d+)% flip tax','groups':[1],'scale':0.01},
'agency_current_far':{'pattern':r'Max\. Residential (\d+\.\d+) (\d+\.\d+)','groups':[1],'scale':1},
'agency_rezone_far':{'pattern':r'Max\. Residential (\d+\.\d+) (\d+\.\d+)','groups':[2],'scale':1},
'agency_current_height':{'pattern':r'Max\. Height (\d+)’ (\d+)’','groups':[1],'scale':1},
'agency_rezone_height':{'pattern':r'Max\. Height (\d+)’ (\d+)’','groups':[2],'scale':1},
'agency_current_units':{'pattern':r'Est\. Units (\d+) (\d+)','groups':[1],'scale':1},
'agency_rezone_units':{'pattern':r'Est\. Units (\d+) (\d+)','groups':[2],'scale':1},
'housing_cost_share':{'pattern':r'cap housing costs at (\d+)%','groups':[1],'scale':0.01},
'market_discount':{'pattern':r'minimum (\d+)% discount','groups':[1],'scale':0.01},
'coop_regulatory_years':{'pattern':r'minimum (\d+)-year Regulatory','groups':[1],'scale':1},
'maintenance_escalation':{'pattern':r'increases of (\d+)%','groups':[1],'scale':0.01},
'expedited_density_description':{'pattern':r'no more than (\d+)%','groups':[1],'scale':0.01},
'subsidy_caps':{'all_currency_indices':[0,1,2,3],'scale':1},
'income_2026_3person':{'all_currency_indices':[5,6,8,10],'scale':1}}
for claim in claims:
    if claim['id'] in extractors:claim['evidence']['extraction']=extractors[claim['id']]
(P/'case.json').write_text(json.dumps(case,indent=2,ensure_ascii=False)+'\n')
print('Authored',len(claims),'claims and',len(requirements),'requirements')
