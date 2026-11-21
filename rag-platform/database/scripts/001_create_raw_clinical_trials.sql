
CREATE TABLE IF NOT EXISTS raw_clinical_trials (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nct_id VARCHAR(20) NOT NULL UNIQUE,
    raw_data JSONB NOT NULL,
    source_updated_at TIMESTAMPTZ,
    fetched_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_raw_clinical_trials_nct_id
    ON raw_clinical_trials (nct_id);

CREATE INDEX IF NOT EXISTS idx_raw_clinical_trials_fetched_at
    ON raw_clinical_trials (fetched_at);


CREATE TABLE ingestion_checkpoints (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    query TEXT NOT NULL,
    next_page_token TEXT,
    page_order INTEGER NOT NULL
);

CREATE INDEX idx_ingestion_checkpoints_query_page_order
    ON ingestion_checkpoints (query, page_order DESC);

  
CREATE TABLE processed_clinical_trials (
    nct_id VARCHAR(20) PRIMARY KEY,
    identification JSONB NOT NULL,
    status JSONB NOT NULL,
    description JSONB NOT NULL,
    conditions JSONB NOT NULL,
    interventions JSONB NOT NULL,
    design JSONB NOT NULL,
    eligibility JSONB NOT NULL,
    outcomes JSONB NOT NULL,
    sponsor JSONB NOT NULL,
    locations JSONB NOT NULL,
    medical_terms JSONB NOT NULL,
    processed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
