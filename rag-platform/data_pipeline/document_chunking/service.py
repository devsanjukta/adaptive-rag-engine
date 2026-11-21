import logging

from data_pipeline.document_chunking.processor import DocumentChunkingProcessor
from data_pipeline.document_chunking.repository import DocumentChunkingRepository

logger = logging.getLogger(__name__)


class DocumentChunkingService:
    def __init__(
        self,
        chunk_repository: DocumentChunkingRepository,
        processor: DocumentChunkingProcessor,
    ) -> None:
        self.chunk_repository = chunk_repository
        self.processor = processor

    def chunk_trials(self) -> int:
        try:
            processed_data = self.chunk_repository.get_all_processed_trials()

            if not processed_data:
                logger.info("No processed trials found for chunking")
                return True

            chunks = self.processor.process_all(processed_data)
            saved = self.chunk_repository.save_all(chunks)

            if not saved:
                return 0

            return len(chunks)

        except Exception:
            logger.exception("Failed to chunk clinical trials")
            return 0
