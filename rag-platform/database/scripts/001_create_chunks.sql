CREATE TABLE document_chunks (
    id SERIAL PRIMARY KEY,
    trial_id INTEGER NOT NULL REFERENCES processed_clinical_trials(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    section VARCHAR(100) NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_trial_chunk_index UNIQUE (trial_id, chunk_index)
);

CREATE INDEX idx_document_chunks_trial_id
ON document_chunks(trial_id);