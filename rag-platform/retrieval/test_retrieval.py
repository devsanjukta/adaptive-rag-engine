from dependencies.common import provide_ollama_client
from dependencies.database import provide_database_repository
from dependencies.embedding_generation import provide_sentence_transformer_client
from dependencies.retrieval import (
    provide_query_classifier,
    provide_reranker,
    provide_retrieval_service,
)
from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import SearchRequest
from shared.database import provide_db_session
from shared.database_repository import DatabaseRepository


def test_retrieval(db: DatabaseRepository):
    retrieval_repository = RetrievalRepository(db)
    tranformer_client = provide_sentence_transformer_client()
    ollama_client = provide_ollama_client()
    query_classifier = provide_query_classifier(ollama_client)
    reranker = provide_reranker()
    retrieval_service = provide_retrieval_service(
        retrieval_repository, tranformer_client, query_classifier, reranker
    )

    # query="Clinical trials for lung cancer",
    query = "NCT04691817"
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
