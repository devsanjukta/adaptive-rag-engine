from data_pipeline.document_chunking.processor import DocumentChunkingProcessor
from data_pipeline.document_chunking.repository import DocumentChunkingRepository
from data_pipeline.document_chunking.service import DocumentChunkingService
from shared.database_repository import DatabaseRepository


def provide_document_chunking_processor() -> DocumentChunkingProcessor:
    return DocumentChunkingProcessor()


def provide_document_chunking_repository(
    db: DatabaseRepository,
) -> DocumentChunkingRepository:
    return DocumentChunkingRepository(db)


def provide_document_chunking_service(
    repository: DocumentChunkingRepository, processor: DocumentChunkingProcessor
) -> DocumentChunkingService:
    return DocumentChunkingService(
        repository,
        processor,
    )
