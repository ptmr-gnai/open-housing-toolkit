"""Small allowlisted method registry. Adding a method requires reviewed code. MIT."""
from housing_workflow.model import calculate, number

# Semantic types distinguish gross area from net area despite shared dimensions.
METHODS = {
    'area.subtract@1': (['gross_sf', 'gross_sf'], 'gross_sf', 'subtract'),
    'area.apply_efficiency@1': (['gross_sf', 'share'], 'net_sf', 'multiply'),
    'homes.net_quotient@1': (['net_sf', 'net_sf_per_home'], 'home_equivalents', 'divide'),
    'homes.gross_quotient@1': (['gross_sf', 'gross_sf_per_home'], 'home_equivalents', 'divide'),
    'area.recorded_lot_ratio@1': (['gross_sf', 'recorded_lot_sf'], 'ratio', 'divide'),
}
UNITS = {'gross_sf':'gross sf', 'net_sf':'net sf', 'share':'share',
         'net_sf_per_home':'net sf per home-equivalent',
         'gross_sf_per_home':'gross sf per home-equivalent',
         'home_equivalents':'home-equivalents; not a feasible unit count',
         'recorded_lot_sf':'square feet as recorded', 'ratio':'gross-to-lot ratio; NOT zoning FAR'}

def numeric(value, kind):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('Finite JSON number required')
    v = number(value)
    if kind not in UNITS or v < 0 or (kind != 'gross_sf' and v == 0):
        raise ValueError('Invalid value for semantic type: '+str(kind))
    if kind == 'share' and v > 1:raise ValueError('Share exceeds one')
    return value

def execute(method, values):
    formula = METHODS[method][2]
    return calculate(formula, values)
