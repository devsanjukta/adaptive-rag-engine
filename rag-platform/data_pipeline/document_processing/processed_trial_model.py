from pydantic import BaseModel, Field


class TrialIdentification(BaseModel):
    nct_id: str
    title: str
    official_title: str | None = None


class TrialStatus(BaseModel):
    overall_status: str | None = None
    start_date: str | None = None
    completion_date: str | None = None


class TrialDescription(BaseModel):
    brief_summary: str | None = None
    detailed_description: str | None = None


class TrialIntervention(BaseModel):
    name: str
    type: str | None = None
    description: str | None = None
    other_names: list[str] = Field(default_factory=list)


class TrialDesign(BaseModel):
    study_type: str | None = None
    phases: list[str] = Field(default_factory=list)
    enrollment_count: int | None = None


class TrialEligibility(BaseModel):
    sex: str | None = None
    minimum_age: str | None = None
    maximum_age: str | None = None
    healthy_volunteers: bool | None = None
    eligibility_criteria: str | None = None


class TrialOutcome(BaseModel):
    measure: str
    type: str
    time_frame: str | None = None
    description: str | None = None


class TrialSponsor(BaseModel):
    lead_sponsor: str | None = None
    collaborators: list[str] = Field(default_factory=list)


class TrialLocation(BaseModel):
    facility: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    zip_code: str | None = None
    status: str | None = None


class TrialMedicalTerm(BaseModel):
    id: str
    term: str
    type: str


class ProcessedTrial(BaseModel):
    nct_id: str
    identification: TrialIdentification
    status: TrialStatus
    description: TrialDescription
    conditions: list[str] = Field(default_factory=list)
    interventions: list[TrialIntervention] = Field(default_factory=list)
    design: TrialDesign
    eligibility: TrialEligibility
    outcomes: list[TrialOutcome] = Field(default_factory=list)
    sponsor: TrialSponsor
    locations: list[TrialLocation] = Field(default_factory=list)
    medical_terms: list[TrialMedicalTerm] = Field(default_factory=list)
