from pydantic import BaseModel


class AgencyObligations(BaseModel):
    awarding_agency_name: str
    sum_obl: float


class AwardTypeTotals2cat(BaseModel):
    assistance: float
    procurement: float


class MonthTotals2cat(BaseModel):
    year: str
    month: str
