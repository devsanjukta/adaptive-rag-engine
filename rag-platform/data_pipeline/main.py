from dependencies.clinical_trials import (
    provide_clinical_trials_client,
    provide_clinical_trials_repository,
    provide_clinical_trials_service,
    provide_trial_processing_repository,
    provide_trial_processing_service,
)
from dependencies.database import provide_database_repository
from dependencies.document_chunking import (
    provide_document_chunking_processor,
    provide_document_chunking_repository,
    provide_document_chunking_service,
)
from dependencies.embedding_generation import (
    provide_embedding_repository,
    provide_embedding_service,
    provide_sentence_transformer_client,
)
from shared.database import provide_db_session
from shared.database_repository import DatabaseRepository


def run_clinical_trials_pipeline(db: DatabaseRepository) -> None:
    with provide_clinical_trials_client() as client:
        repository = provide_clinical_trials_repository(db)
        service = provide_clinical_trials_service(client, repository)

        result = service.ingest_studies(condition="lung cancer")

    print(f"Processed: {result.processed}")
    print(f"Changed: {result.changed}")
    print(f"Unchanged: {result.unchanged}")


def run_trial_processing_pipeline(db: DatabaseRepository) -> None:
    repository = provide_trial_processing_repository(db)
    service = provide_trial_processing_service(repository)

    processed_count = service.process_trials()

    print(f"Processed: {processed_count}")


def run_document_chunking(db: DatabaseRepository) -> None:
    repository = provide_document_chunking_repository(db)
    processor = provide_document_chunking_processor()
    service = provide_document_chunking_service(repository, processor)

    chunks = service.chunk_trials()

    print(f"Total Chunks: {chunks}")


def run_embedding_generation(db: DatabaseRepository) -> None:
    repository = provide_embedding_repository(db)
    client = provide_sentence_transformer_client()

    service = provide_embedding_service(
        repository,
        client,
    )

    total_embeddings = service.generate_embeddings()

    print(f"Total Embeddings: {total_embeddings}")


def main():
    with provide_db_session() as session:
        db = provide_database_repository(session)

        # run_clinical_trials_pipeline(db)
        # run_trial_processing_pipeline(db)
        # run_document_chunking(db)
        run_embedding_generation(db)


if __name__ == "__main__":
    main()
