"""Typed draft slots and explicit incompleteness states. MIT."""
from dataclasses import asdict,dataclass
from datetime import date
from enum import Enum
from housing_benefit.contracts import fields,text,read_json,identifier

class Status(str,Enum):
    FILLED='filled'
    ILLUSTRATIVE='illustrative'
    MISSING='missing'
    INTERPRET='needs_interpretation'
    NA='not_applicable'

@dataclass(frozen=True)
class Slot:
    requirement_id: str
    section: int
    label: str
    status: Status
    value: str | int | None
    reason: str
    bindings: tuple[dict,...]
    sources: tuple[dict,...]

    def to_dict(self):
        x=asdict(self);x['status']=self.status.value;x['bindings']=list(self.bindings);x['sources']=list(self.sources);return x

# Independent minimum inventory: changing the map cannot quietly remove an obligation.
# This detects known omissions; it does not certify that all professional requirements were discovered.
REQUIRED_IDS=frozenset('''cover.name cover.contact cover.preparer cover.date cover.application cover.consistency cover.version_stage
summary.project summary.context summary.narrative
res.scope res.zsf res.total res.classification res.band_counts res.band_shares res.ami res.programs res.mih res.rents res.incomes res.years res.timing res.market_method
nonres.scope nonres.area_conflict nonres.zsf nonres.unknown_area nonres.known_area nonres.jobs nonres.workforce
construction.gsf construction.duration construction.person_years construction.workers
community.geography community.summary community.displacement
narrative.statement narrative.goal1 narrative.goal2 narrative.goal3 narrative.goal4 narrative.goal5 narrative.goal6
appendix.scope appendix.local appendix.borough appendix.city appendix.all_indicators'''.split())


def validate_request(r):
    fields(r,['version','id','prepared_by','prepared_on','application','contact','nonresidential_tenants'])
    if r['version']!='0.1.0':raise ValueError('Unsupported draft request version')
    identifier(r['id']);text(r['prepared_by']);text(r['prepared_on'])
    try:day=date.fromisoformat(r['prepared_on'])
    except ValueError as exc:raise ValueError('Use an ISO prepared_on date') from exc
    if day.isoformat()!=r['prepared_on']:raise ValueError('Use canonical ISO date')
    for key in ['application','contact']:
        fields(r[key],['status','rationale'])
        if r[key]['status']!='unknown':raise ValueError('Application/contact evidence adapter not implemented; keep unknown')
        text(r[key]['rationale'])
    t=r['nonresidential_tenants'];fields(t,['status','rationale','attribution'])
    if t['status'] not in {'unknown','none_identified'}:raise ValueError('Known-tenant jobs adapter not implemented')
    text(t['rationale']);text(t['attribution'])
    return r
