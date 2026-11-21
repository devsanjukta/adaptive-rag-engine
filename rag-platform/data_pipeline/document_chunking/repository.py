import json
import logging

from data_pipeline.document_chunking.chunk_model import (
    DocumentChunk,
    ProcessedTrialRecord,
)
from shared.database_repository import DatabaseRepository

logger = logging.getLogger(__name__)


class DocumentChunkingRepository:
    def __init__(self, db: DatabaseRepository) -> None:
        self.db = db

    def get_all_processed_trials(self) -> list[ProcessedTrialRecord]:
        query = """
            SELECT *
            FROM processed_clinical_trials
        """

        return self.db.fetch_all(query, ProcessedTrialRecord)

    def save_all(self, chunks_by_trial: list[list[DocumentChunk]]) -> bool:
        try:
            trial_ids = {
                chunk.trial_id for chunks in chunks_by_trial for chunk in chunks
            }

            if not trial_ids:
                return True

            delete_query = """
                DELETE FROM document_chunks
                WHERE trial_id = ANY(:trial_ids)
            """

            self.db.execute(delete_query, {"trial_ids": list(trial_ids)})

            all_chunks = [chunk for chunks in chunks_by_trial for chunk in chunks]

            insert_query = """
                INSERT INTO document_chunks (
                    trial_id,
                    chunk_index,
                    content,
                    section,
                    metadata
                )
                VALUES (
                    :trial_id,
                    :chunk_index,
                    :content,
                    :section,
                    CAST(:metadata AS JSONB)
                )
            """

            params = [
                {
                    "trial_id": chunk.trial_id,
                    "chunk_index": chunk.chunk_index,
                    "content": chunk.content,
                    "section": chunk.section,
                    "metadata": json.dumps(chunk.metadata),
                }
                for chunk in all_chunks
            ]

            self.db.execute_many(insert_query, params)

            return True

        except Exception:
            logger.exception("Failed to save document chunks")
            return False
