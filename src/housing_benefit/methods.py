"""Allowlisted arithmetic with explicit semantic signatures and exact comparisons. MIT."""
from decimal import Decimal, localcontext
from .contracts import Unit as U

# Method IDs are versioned. Signatures prevent substitution of monthly/annual costs.
SIGNATURES={
 'housing.bedroom_match@1':([U.BEDROOMS,U.BEDROOMS],U.BOOLEAN),
 'housing.cost_and_bedroom_match@1':([U.BOOLEAN,U.BOOLEAN],U.BOOLEAN),
 'housing.gross_monthly_cost@1':([U.USD_MONTH,U.USD_MONTH],U.USD_MONTH),
 'housing.annualize@1':([U.USD_MONTH],U.USD_YEAR),
 'housing.cost_burden_percent@1':([U.USD_YEAR,U.USD_YEAR],U.PERCENT),
 'housing.within_threshold@1':([U.USD_YEAR,U.USD_YEAR,U.PERCENT],U.BOOLEAN),
 'housing.monthly_budget@1':([U.USD_YEAR,U.PERCENT],U.USD_MONTH),
 'housing.sum_homes@1':(None,U.HOMES),
 'housing.selected_homes@1':(None,U.HOMES),
 'housing.difference@1':([U.HOMES,U.HOMES],U.HOMES),
}


def evaluate(method,claims):
    if method not in SIGNATURES:raise ValueError('Unsupported versioned benefit method')
    signature,unit=SIGNATURES[method];units=[U(c['unit']) for c in claims]
    if signature is not None and units!=signature:raise ValueError('Method semantic input type mismatch')
    values=[c['value'] for c in claims]
    if method=='housing.sum_homes@1':
        if any(u!=U.HOMES for u in units):raise ValueError('Expected home counts')
        return sum(values),unit
    if method=='housing.selected_homes@1':
        if len(values)%2 or any(units[i:i+2]!=[U.HOMES,U.BOOLEAN] for i in range(0,len(units),2)):raise ValueError('Expected homes/boolean selection pairs')
        return sum(values[i] for i in range(0,len(values),2) if values[i+1]),unit
    if method=='housing.bedroom_match@1':return values[0]==values[1],unit
    if method=='housing.cost_and_bedroom_match@1':return all(values),unit
    with localcontext() as ctx:
        ctx.prec=40
        v=[Decimal(str(x)) for x in values]
        if method=='housing.gross_monthly_cost@1':answer=v[0]+v[1]
        elif method=='housing.annualize@1':answer=v[0]*12
        elif method=='housing.cost_burden_percent@1':
            if v[1]<=0:raise ValueError('Non-positive household income')
            return format(v[0]*100/v[1],'.6f'),unit
        elif method=='housing.within_threshold@1':
            if v[1]<=0:raise ValueError('Non-positive household income')
            return v[0]*100<=v[1]*v[2],unit  # Compare before any display rounding.
        elif method=='housing.monthly_budget@1':answer=v[0]*v[1]/100/12
        elif method=='housing.difference@1':return int(v[0]-v[1]),unit
        return format(answer,'.2f'),unit
