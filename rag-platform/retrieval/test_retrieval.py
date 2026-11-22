from dependencies.database import provide_database_repository
from dependencies.embedding_generation import provide_sentence_transformer_client
from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import SearchRequest
from retrieval.service import RetrievalService
from shared.database import provide_db_session
from shared.database_repository import DatabaseRepository


def test_retrieval(db: DatabaseRepository):
    retrieval_repository = RetrievalRepository(db)
    client = provide_sentence_transformer_client()
    retrieval_service = RetrievalService(retrieval_repository, client)

    # query="Clinical trials for lung cancer",
    query = "Enhanced COPD Management"
    request = SearchRequest(
        query=query,
        top_k=5,
    )

    results = retrieval_service.search(request)

    for result in results:
        print(f"NCT ID: {result.nct_id}")
        print(f"Section: {result.section}")
        print(f"Similarity: {result.similarity_score:.4f}")
        print(f"Content: {result.content[:200]}")
        print("-" * 50)

    print("search completed")


def main():
    with provide_db_session() as session:
        db = provide_database_repository(session)
        test_retrieval(db)


if __name__ == "__main__":
    main()
