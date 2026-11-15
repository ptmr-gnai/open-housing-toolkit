"""Read-only verification of retained rental scenarios. MIT."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from housing_underwriting.engine import verify,load,digest
BASE=Path(__file__).parent
for source in load(BASE/'sources.json')['sources']:
    assert digest((ROOT/source['file']).read_bytes())==source['sha256']
summary=load(BASE/'cases/summary.json')
for name,expected in summary.items():
    folder=BASE/'cases'/name
    assert verify(folder)['status']=='passed'
    assert digest((folder/'manifest.json').read_bytes())==expected['manifest_sha256']
    result=load(folder/'results.json')
    for key,value in expected.items():
        if key=='minimum_annual_cash_after_deductions_usd':
            from decimal import Decimal
            assert min(Decimal(x['cash_after_reserves_debt_and_below_line_usd']) for x in result['annual'])==Decimal(value)
        elif key!='manifest_sha256':assert result[key]==value,(name,key)
a=load(BASE/'cases/stanyan-supportable-loan-control/results.json')
assert a['modeled_primary_loan_usd']=='12793048.57'
assert a['annual'][0]['coverage_noi_usd']=='1272978.00'
b=load(BASE/'cases/rental-60-balloon/results.json')
assert b['annual'][-1]['primary_loan_balance_year_end_usd']=='0.00'
assert b['cashflow_shortfall_years']==[20]
c=load(BASE/'cases/rental-60-fully-paid-15/results.json')
assert all(x['dscr'] is None for x in c['annual'] if x['year']>15)
print('Rental modeling: 12 packages, source bytes, reference arithmetic, balloon and post-payoff checks passed.')
