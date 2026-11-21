from data_pipeline.clinical_trials.client import ClinicalTrialsClient
from data_pipeline.clinical_trials.repository import ClinicalTrialsRepository
from data_pipeline.clinical_trials.service import ClinicalTrialsService
from shared.database_repository import DatabaseRepository


def provide_clinical_trials_client() -> ClinicalTrialsClient:
    return ClinicalTrialsClient()


def provide_clinical_trials_service(
    client: ClinicalTrialsClient, repo: ClinicalTrialsRepository
) -> ClinicalTrialsService:
    return ClinicalTrialsService(client, repo)


def provide_clinical_trials_repository(
    db: DatabaseRepository,
) -> ClinicalTrialsRepository:
    return ClinicalTrialsRepository(db)
