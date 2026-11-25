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
        top_k=10,
    )

    result = retrieval_service.search(request)
    print(result)
    print("search completed")


def main():
    with provide_db_session() as session:
        db = provide_database_repository(session)
        test_retrieval(db)


if __name__ == "__main__":
    main()
