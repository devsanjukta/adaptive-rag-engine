from pydantic import BaseModel, ValidationError

from retrieval.query_type import QueryType


class QueryClassification(BaseModel):
    search_type: QueryType


class QueryClassifier:
    def __init__(self, ollama_client):
        self.ollama_client = ollama_client

    def classify(self, query: str) -> QueryType:
        prompt = f"""
        You are a query classifier for a clinical trials search system.

        Classify the query into exactly one category:

        SEMANTIC:
        The query searches for concepts, meaning, medical conditions,
        treatment approaches, or related clinical information.

        KEYWORD:
        The query searches for exact terms, drug names, gene names,
        clinical trial identifiers, or specific phrases.

        HYBRID:
        The query requires both conceptual understanding and
        specific term matching.

        Query: {query}

        Return ONLY a valid JSON object with this structure:
        {{"search_type": "SEMANTIC"}}

        Rules:
        - The search_type value must be SEMANTIC, KEYWORD, or HYBRID.
        - Do not include explanations.
        - Do not include Markdown formatting.
        - Do not wrap the JSON in code fences.
        - Return JSON only.
        
        """

        response = self.ollama_client.generate(prompt)

        try:
            result = QueryClassification.model_validate_json(response)
            return result.search_type

        except ValidationError:
            # deterministic fallback policy, safe fallback for now
            # TO DO: implement strong policy
            return QueryType.SEMANTIC
