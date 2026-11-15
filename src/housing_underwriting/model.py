"""Dated cash-flow projections and constrained permanent-debt sizing. MIT.

All currency arithmetic uses Decimal. Inputs are attributed scenarios, not agency
eligibility findings. Construction timing and tax-credit allocation are external.
"""
from decimal import Decimal, ROUND_HALF_UP, localcontext
import copy
import re

CATEGORIES = ['land','acquisition_closing','demolition','remediation','hard_costs',
              'hard_contingency','soft_costs','soft_contingency','offsite_infrastructure',
              'construction_interest','taxes_and_carry','business_relocation','financing_fees','developer_fee','initial_reserves','other']
D=Decimal
ZERO=D(0)


def keys(obj,names,label):
    if not isinstance(obj,dict) or set(obj)!=set(names):raise ValueError('Unknown or missing '+label+' fields')


def dec(value,label='value',minimum=ZERO,maximum=D('1e15')):
    if not isinstance(value,str) or not re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]{1,12})?',value):
        raise ValueError(label+' requires a finite decimal string, not a JSON float')
    result=D(value)
    if not minimum<=result<=maximum:raise ValueError(label+' outside supported range')
    return result


def integer(value,minimum,maximum,label):
    if type(value) is not int or not minimum<=value<=maximum:raise ValueError('Invalid '+label)
    return value


def text(value,label):
    if not isinstance(value,str) or not value.strip() or len(value)>10000:raise ValueError(label+' required')


def basis(value):
    keys(value,['kind','rationale','reference_ids'],'basis')
    if value['kind'] not in ['analyst_assumption','reported_input','source_derived_input']:raise ValueError('Unsupported input basis')
    text(value['rationale'],'Input rationale')
    if not isinstance(value['reference_ids'],list) or any(not isinstance(x,str) for x in value['reference_ids']):raise ValueError('Reference ids must be a list')


def validate(req):
    keys(req,['version','id','question','price_basis','program','capital','operations','debt','sources','basis','references'],'underwriting request')
    if req['version']!='1.0' or not isinstance(req['id'],str) or not re.fullmatch('[a-z0-9-]{1,80}',req['id']):raise ValueError('Unsupported request id/version')
    text(req['question'],'Question');text(req['price_basis'],'Price/year basis');basis(req['basis'])
    refs=req['references']
    if not isinstance(refs,list):raise ValueError('References must be a list')
    ids=[]
    for ref in refs:
        keys(ref,['id','title','url','locator'],'reference')
        for k in ref:text(ref[k],'Reference '+k)
        if not ref['url'].startswith('https://'):raise ValueError('HTTPS reference URL required')
        ids.append(ref['id'])
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate reference ids')
    all_basis=[req['basis']]
    p=req['program'];keys(p,['homes','gross_area_sf','basis'],'program')
    integer(p['homes'],1,10000,'proposed homes');dec(p['gross_area_sf'],'proposed gross area',D('0.01'));basis(p['basis']);all_basis.append(p['basis'])
    capital=req['capital'];keys(capital,['lines'],'capital')
    if not isinstance(capital['lines'],list):raise ValueError('Capital lines required')
    cats=[]
    for line in capital['lines']:
        keys(line,['category','measure','usd','basis'],'capital line')
        cats.append(line['category']);dec(line['usd'],'Capital cost')
        if line['measure'] not in ['fixed','per_home','per_gross_sf']:raise ValueError('Unsupported capital measure')
        basis(line['basis']);all_basis.append(line['basis'])
    if sorted(cats)!=sorted(CATEGORIES):raise ValueError('Declare every capital category exactly once, including explicit zero assumptions')
    op=req['operations'];keys(op,['first_calendar_year','horizon_years','income','expenses','replacement_reserve','reserve_deducted_for_coverage','below_line'],'operations')
    integer(op['first_calendar_year'],1900,2200,'first year');h=integer(op['horizon_years'],1,40,'projection horizon')
    if type(op['reserve_deducted_for_coverage']) is not bool:raise ValueError('Declare coverage treatment of replacement reserve')
    row_ids=[]
    for collection in ['income','expenses','below_line']:
        if not isinstance(op[collection],list) or len(op[collection])>100:raise ValueError('Bounded operating line list required')
        for line in op[collection]:
            fields=['id','annual_usd','annual_growth','basis']
            if collection=='income':fields+=['vacancy_rate','start_year','end_year']
            keys(line,fields,collection+' line');text(line['id'],'Operating id');row_ids.append(line['id'])
            dec(line['annual_usd'],'Annual amount');dec(line['annual_growth'],'Annual growth',D('-0.5'),D('0.5'))
            if collection=='income':
                dec(line['vacancy_rate'],'Vacancy/collection loss',ZERO,D('1'))
                integer(line['start_year'],1,h,'income start year');integer(line['end_year'],line['start_year'],h,'income end year')
            basis(line['basis']);all_basis.append(line['basis'])
    if not op['income'] or not op['expenses']:raise ValueError('Declare income and operating expenses explicitly')
    if len(row_ids)!=len(set(row_ids)):raise ValueError('Operating line ids must be unique across all groups')
    reserve=op['replacement_reserve'];keys(reserve,['annual_usd','annual_growth','basis'],'replacement reserve')
    dec(reserve['annual_usd']);dec(reserve['annual_growth'],'Reserve growth',D('-0.5'),D('0.5'));basis(reserve['basis']);all_basis.append(reserve['basis'])
    debt=req['debt'];keys(debt,['annual_interest_rate','amortization_years','term_years','minimum_dscr','minimum_dscr_by_year','sizing_years','maximum_total_ltc','maximum_ltv','appraised_value_usd','absolute_cap_usd','other_annual_debt_service_usd','basis'],'debt')
    dec(debt['annual_interest_rate'],'Loan interest rate',ZERO,D('0.3'))
    amort=integer(debt['amortization_years'],1,50,'amortization years')
    term=integer(debt['term_years'],1,amort,'term years')
    if term<h and term!=amort:raise ValueError('A balloon loan cannot project beyond maturity without a separate refinancing model')
    integer(debt['sizing_years'],1,h,'debt sizing years');dec(debt['minimum_dscr'],'Minimum coverage',D('1'),D('5'))
    schedule=debt['minimum_dscr_by_year']
    if schedule is not None:
        if not isinstance(schedule,list) or len(schedule)!=h:raise ValueError('Coverage schedule must cover every projection year')
        for v in schedule:dec(v,'Annual minimum coverage',D('1'),D('5'))
    for key in ['maximum_total_ltc','maximum_ltv']:
        if debt[key] is not None:dec(debt[key],key,D('0.000001'),D('1'))
    for key in ['appraised_value_usd','absolute_cap_usd']:
        if debt[key] is not None:dec(debt[key],key)
    if debt['maximum_ltv'] is not None and debt['appraised_value_usd'] is None:raise ValueError('An LTV limit needs an explicitly supplied property value')
    dec(debt['other_annual_debt_service_usd']);basis(debt['basis']);all_basis.append(debt['basis'])
    if not isinstance(req['sources'],list) or len(req['sources'])>100:raise ValueError('Bounded financing-source list required')
    source_ids=[]
    for source in req['sources']:
        keys(source,['id','kind','amount_usd','status','basis'],'capital source');text(source['id'],'Capital source id');source_ids.append(source['id'])
        if source['kind'] not in ['equity','grant','soft_loan','other']:raise ValueError('Unsupported source kind')
        if source['status'] not in ['committed','proposed']:raise ValueError('Source status must be committed or proposed')
        dec(source['amount_usd']);basis(source['basis']);all_basis.append(source['basis'])
    if len(source_ids)!=len(set(source_ids)):raise ValueError('Duplicate financing source ids')
    for b in all_basis:
        if not set(b['reference_ids'])<=set(ids):raise ValueError('Input basis cites an unknown reference')
        if b['kind'] in ['reported_input','source_derived_input'] and not b['reference_ids']:raise ValueError('A reported input needs a source reference')
    return req


def money(value):return D(value).quantize(D('.01'),rounding=ROUND_HALF_UP)
def serial(value):return format(value,'f')


def constant(annual_rate,years):
    """Annual debt service / initial principal for monthly end-period payments."""
    r=annual_rate/12;n=years*12
    if r==0:return D(1)/years
    return (r/(D(1)-(D(1)+r)**(-n)))*12


def balance(principal,annual_rate,amort_years,elapsed_years):
    r=annual_rate/12;n=elapsed_years*12
    if r==0:return max(ZERO,principal*(D(1)-D(elapsed_years)/amort_years))
    payment=principal*constant(annual_rate,amort_years)/12
    factor=(D(1)+r)**n
    return max(ZERO,principal*factor-payment*(factor-1)/r)


def _evaluate(req):
    validate(req);p=req['program'];op=req['operations'];debt=req['debt']
    basis_units={'fixed':D(1),'per_home':D(p['homes']),'per_gross_sf':dec(p['gross_area_sf'])}
    capital=[{'category':x['category'],'amount_usd':serial(money(dec(x['usd'])*basis_units[x['measure']])),
              'measure':x['measure'],'basis':x['basis']} for x in req['capital']['lines']]
    cost=sum((D(x['amount_usd']) for x in capital),ZERO)
    annual=[]
    def grow(line,year):return money(dec(line['annual_usd'])*(D(1)+dec(line['annual_growth'],minimum=D('-.5')))**(year-1))
    for year in range(1,op['horizon_years']+1):
        income=[]
        for line in op['income']:
            scheduled=grow(line,year) if line['start_year']<=year<=line['end_year'] else ZERO
            loss=money(scheduled*dec(line['vacancy_rate']))
            income.append({'id':line['id'],'scheduled_usd':serial(scheduled),'vacancy_loss_usd':serial(loss),'effective_usd':serial(scheduled-loss)})
        expenses=[{'id':line['id'],'amount_usd':serial(grow(line,year))} for line in op['expenses']]
        effective=sum((D(x['effective_usd']) for x in income),ZERO)
        expense=sum((D(x['amount_usd']) for x in expenses),ZERO)
        replacement=grow(op['replacement_reserve'],year)
        noi=effective-expense
        coverage_noi=noi-(replacement if op['reserve_deducted_for_coverage'] else ZERO)
        below=sum((grow(line,year) for line in op['below_line']),ZERO)
        annual.append({'year':year,'calendar_year':op['first_calendar_year']+year-1,'income_lines':income,'expense_lines':expenses,
                       'effective_gross_income_usd':serial(effective),'operating_expenses_usd':serial(expense),
                       'noi_before_replacement_reserve_usd':serial(noi),'replacement_reserve_usd':serial(replacement),
                       'coverage_noi_usd':serial(coverage_noi),'below_line_usd':serial(below)})
    mortgage_constant=constant(dec(debt['annual_interest_rate']),debt['amortization_years'])
    other=dec(debt['other_annual_debt_service_usd']);minimum=dec(debt['minimum_dscr'])
    def floor_for(year):return dec(debt['minimum_dscr_by_year'][year-1]) if debt['minimum_dscr_by_year'] is not None else minimum
    sizing=annual[:min(debt['sizing_years'],debt['term_years'])]
    allowed_service=min(D(y['coverage_noi_usd'])/floor_for(y['year'])-other for y in sizing)
    dscr_capacity=max(ZERO,allowed_service/mortgage_constant)
    caps={'dscr':dscr_capacity}
    other_principal=sum((dec(x['amount_usd']) for x in req['sources'] if x['kind']=='soft_loan'),ZERO)
    if debt['maximum_total_ltc'] is not None:caps['loan_to_cost']=max(ZERO,cost*dec(debt['maximum_total_ltc'])-other_principal)
    if debt['maximum_ltv'] is not None:caps['loan_to_value']=dec(debt['appraised_value_usd'])*dec(debt['maximum_ltv'])
    if debt['absolute_cap_usd'] is not None:caps['absolute_cap']=dec(debt['absolute_cap_usd'])
    maximum_capacity=min(caps.values())
    declared_sources=sum((dec(x['amount_usd']) for x in req['sources']),ZERO)
    caps['funding_need']=max(ZERO,cost-declared_sources)
    # Round DOWN so the displayed principal never exceeds a sizing cap or the
    # scenario funding need. Proposed sources remain explicitly conditional.
    principal=min(caps.values()).quantize(D('.01'),rounding='ROUND_FLOOR')
    service=money(principal*mortgage_constant)
    balloon=money(balance(principal,dec(debt['annual_interest_rate']),debt['amortization_years'],debt['term_years']))
    breaches=[];cash_shortfalls=[]
    for y in annual:
        coverage=D(y['coverage_noi_usd']);noi=D(y['noi_before_replacement_reserve_usd'])
        this_service=service if y['year']<=debt['term_years'] else ZERO
        total_service=this_service+other
        required=floor_for(y['year'])
        maturity_due=balloon if y['year']==debt['term_years'] else ZERO
        ratio=coverage/total_service if total_service>0 else None
        # Compare unrounded principal-level debt service, avoiding a cent-rounding false breach.
        exact_total=(principal*mortgage_constant if y['year']<=debt['term_years'] else ZERO)+other
        meets=(coverage>=required*exact_total) if total_service>0 else None
        cash=noi-D(y['replacement_reserve_usd'])-total_service-D(y['below_line_usd'])-maturity_due
        support=max(ZERO,money(required*exact_total-coverage)) if total_service>0 else None
        y.update(primary_debt_service_usd=serial(this_service),other_debt_service_usd=serial(other),
                 required_dscr=serial(required) if total_service>0 else None,maturity_principal_due_usd=serial(maturity_due),
                 dscr=serial(ratio.quantize(D('.000001'))) if ratio is not None else None,
                 meets_declared_dscr=meets,cash_after_reserves_debt_and_below_line_usd=serial(cash),
                 additional_effective_income_for_coverage_usd=serial(support) if support is not None else None,
                 primary_loan_balance_before_maturity_payment_usd=serial(maturity_due) if y['year']==debt['term_years'] else None,
                 primary_loan_balance_year_end_usd=serial(money(balance(principal,dec(debt['annual_interest_rate']),debt['amortization_years'],y['year']))) if y['year']<debt['term_years'] else '0.00')
        if meets is False:breaches.append(y['year'])
        if cash<0:cash_shortfalls.append(y['year'])
    committed=sum((dec(x['amount_usd']) for x in req['sources'] if x['status']=='committed'),ZERO)
    proposed=sum((dec(x['amount_usd']) for x in req['sources']),ZERO)
    missing=[]
    financing_breaches=[]
    if debt['maximum_total_ltc'] is None:missing.append('No combined loan-to-cost cap evaluated')
    if debt['maximum_total_ltc'] is not None and other_principal>cost*dec(debt['maximum_total_ltc']):
        financing_breaches.append('declared_subordinate_principal_exceeds_combined_ltc_limit')
        missing.append('Declared subordinate loans already exceed the combined loan-to-cost cap')
    if debt['maximum_ltv'] is None:missing.append('No loan-to-value cap or appraisal evaluated')
    if debt['sizing_years']<op['horizon_years']:missing.append('Debt sized to fewer years than the cash-flow projection; later coverage can fail')
    if balloon>0:missing.append('Maturity principal is a scheduled cash obligation; repayment/refinancing arrangements and accumulated reserves are not verified')
    return {'version':'1.0.0','request_id':req['id'],'meaning':'Conditional rental-project underwriting diagnostic; no legal/physical feasibility, financing award or investor-return finding.',
            'program':copy.deepcopy(p),'capital_lines':capital,'total_development_cost_usd':serial(cost),
            'annual_mortgage_constant':serial(mortgage_constant),'debt_sizing_years':debt['sizing_years'],'primary_debt_sizing_years':len(sizing),
            'debt_caps_usd':{k:serial(money(v)) for k,v in caps.items()},
            'binding_debt_caps':sorted(k for k,v in caps.items() if abs(v-min(caps.values()))<D('.01')),
            'maximum_primary_loan_capacity_usd':serial(money(maximum_capacity)),
            'unused_primary_loan_capacity_usd':serial(money(max(ZERO,maximum_capacity-principal))),
            'modeled_primary_loan_usd':serial(principal),'modeled_primary_loan_is_committed':False,
            'committed_other_sources_usd':serial(money(committed)),'all_declared_other_sources_usd':serial(money(proposed)),
            'unallocated_capital_after_modeled_loan_and_all_declared_sources_usd':serial(money(max(ZERO,cost-principal-proposed))),
            'capital_not_covered_by_committed_sources_usd':serial(money(max(ZERO,cost-committed))),
            'surplus_after_modeled_loan_and_all_declared_sources_usd':serial(money(max(ZERO,principal+proposed-cost))),
            'debt_balance_basis':'Scheduled balances assume all payments including maturity principal are made; negative cash years identify a funding need, not proof of payment.',
            'balloon_at_term_usd':serial(balloon),'coverage_breach_years':breaches,'financing_limit_breaches':financing_breaches,'cashflow_shortfall_years':cash_shortfalls,'annual':annual,'missing_financing_checks':missing,
            'unresolved':['Entitlement, physical fit, existing occupancy and business relocation','Land price/title/control and environmental scope',
                          'Construction draws, interest carry timing, lease-up and conversion','Tax-credit/program eligibility, tax treatment and actual commitments',
                          'Subordinate loan repayment/balloons: only explicitly supplied annual debt service is included',
                          'Investor return, exit value/taxes, refinancing and complete project feasibility'],
            'methods':{'capital':'Sum rounded explicit cost lines; zero costs require attributed input assumptions.',
                       'income':'Each annual income stream grows from year-one dollars; start/end years gate receipt, loss applies by stream.',
                       'noi':'Effective income less operating expenses; replacement reserve treatment for coverage is explicit.',
                       'debt':'Minimum of declared DSCR, LTC, LTV and absolute capacities plus scenario funding need after declared sources; monthly fixed-rate amortization.',
                       'gap':'Uses minus modeled primary debt and declared other sources; proposed is not committed and gap is not a subsidy award.'}}


def evaluate(req):
    with localcontext() as ctx:
        ctx.prec=40
        return _evaluate(req)
