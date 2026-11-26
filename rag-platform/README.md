# Medical Research Intelligence Platform (RAG)

A Retrieval-Augmented Generation (RAG) platform designed to search, retrieve, and analyze medical research documents, starting with clinical trials.

## 1. Overview

The platform uses semantic search and machine learning to identify relevant medical research documents and provide reliable, context-based answers.

The initial focus is on clinical trial data, with plans to expand into more advanced retrieval, reranking, and grounded answer generation.

## 2. Technology Stack

- **Language:** Python 3.12
- **Database:** PostgreSQL + pgvector
- **Database Access:** SQLAlchemy Core / Raw SQL
- **Data Processing:** Pandas
- **Validation:** Pydantic
- **Embeddings:** Sentence Transformers
- **Reranking:** Cross-Encoder
- **Local LLM:** Ollama
- **API:** FastAPI (planned)

## 3. Project Structure

```text
rag-platform/
├── data_pipeline/
│   ├── clinical_trials/
│   ├── document_processing/
│   ├── document_chunking/
│   ├── embedding_generation/
│   ├── models/
│   └── main.py
│
├── retrieval/
│   ├── retrieval_model.py
│   ├── repository.py
│   └── service.py
│
├── reranker/
│   ├── dataset/
│   │   ├── training_data.csv
│   │   └── ...
│   ├── models.py
│   ├── dataset_validator.py
│   ├── dataset_record_validator.py
│   ├── ai_label_reviewer.py
│   └── main.py
│
├── shared/
│   ├── config.py
│   ├── database.py
│   ├── database_repository.py
│   ├── external_endpoints.py
│   ├── sentence_transformer_client.py
│   └── utils.py
│
├── dependencies/
└── database/
    └── scripts/
```

## 4. Implementation Progress

### Data Pipeline

- Integrated ClinicalTrials.gov data ingestion.
- Ingested 500 lung cancer clinical trials.
- Stored raw and processed data separately.
- Implemented document chunking (500 tokens, 50-token overlap).
- Generated normalized embeddings using `all-MiniLM-L6-v2`.
- Stored document chunks and embeddings in PostgreSQL.

### Semantic Retrieval

- Implemented vector similarity search using pgvector.
- Used cosine distance to rank documents.
- Implemented top-K retrieval.
- Completed integration testing.

### Reranker

**Candidate model:** `cross-encoder/ms-marco-MiniLM-L-6-v2`

Dataset preparation:
- 2,200 query-document pairs.
- 500 unique clinical trials.
- 974 positive and 1,226 negative examples.
- 1,075 hard negatives and 151 easy negatives.
- 9 query categories.

Completed:
- Dataset loading and validation.
- Pydantic-based record validation.
- Required field, label, and negative type checks.
- Successfully validated all 2,200 records.
- AI-assisted label review.
- Evaluate the pretrained reranker.
- Fine-tune using the prepared dataset.
- Implement hard-negative mining.


**Note:** Dataset labels are generated using keyword-based rules and have not been expert-verified. AI-assisted review will help identify potentially incorrect labels. Human review remains the final decision.

Next:

Implement adaptive query routing.

Implement custom hybrid retrieval.

## 5. Architecture Principles

- Keep data ingestion, retrieval, and reranking as separate components.
- Use repositories for database operations.
- Use services and processors for business logic.
- Inject dependencies through `provide_*` functions.
- Reuse existing ML clients and avoid duplicate model loading.
- Keep deterministic validation separate from AI-assisted review.
- Preserve original datasets and store review results separately.

## 6. Roadmap

1. **Reranker Development**
   - Review dataset labels.
   - Evaluate and fine-tune the reranker.
   - Implement hard-negative mining.

2. **Advanced Retrieval**
   - Adaptive query routing.
   - Custom hybrid retrieval.
   - Combine semantic and keyword search.

3. **RAG Evaluation**
   - Build evaluation datasets and metrics.
   - Run ablation studies.
   - Compare retrieval and reranking strategies.

4. **Scalable Infrastructure**
   - Distributed indexing.
   - Fault-tolerant processing.

5. **Grounded Generation**
   - Generate answers using retrieved research.
   - Implement claim verification.
   - Improve answer reliability and traceability.

## Retrieval Implementation Roadmap (Adaptive Query Routing)

### Router Decides one of following Search type based on query

### 1. Semantic Search
- Vector similarity search using pgvector.
- Cosine similarity ranking.

### 2. Keyword Search
- PostgreSQL Full-Text Search (`tsvector`, `tsquery`).
- GIN indexing.
- Keyword relevance ranking using `ts_rank_cd()`.

### 3. Hybrid Search
- Combine semantic and keyword results.
- Reciprocal Rank Fusion (RRF).
- Configurable retrieval limits.
- Duplicate result handling.

### 4. Metadata Filtering
- Filter by trial phase, status, condition, and intervention.
- Combine filters with retrieval strategies.

### 5. Retrieval Evaluation
- Recall@K.
- Precision@K.
- MRR@K.
- nDCG@K.
- Compare semantic, keyword, and hybrid retrieval.

### 6. Performance Evaluation
- Query latency.
- Database query performance.
- Index effectiveness.
- Retrieval scalability.