from dependencies.clinical_trials import (
    provide_clinical_trials_client,
    provide_clinical_trials_repository,
    provide_clinical_trials_service,
)
from dependencies.database import provide_database_repository
from shared.database import provide_db_session


def run_clinical_trials_pipeline() -> None:
    with (
        provide_clinical_trials_client() as client,
        provide_db_session() as session,
    ):
        db = provide_database_repository(session)
        repository = provide_clinical_trials_repository(db)
        service = provide_clinical_trials_service(client, repository)

        result = service.ingest_studies(condition="lung cancer")

    print(f"Processed: {result.processed}")
    print(f"Changed: {result.changed}")
    print(f"Unchanged: {result.unchanged}")


if __name__ == "__main__":
    run_clinical_trials_pipeline()
