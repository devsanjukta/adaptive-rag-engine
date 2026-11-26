import httpx

from shared.config import OLLAMA_MODEL_NAME, OLLAMA_URL


class OllamaClient:
    def __init__(self):
        self.url = OLLAMA_URL
        self.model = OLLAMA_MODEL_NAME

    def generate(self, prompt: str) -> str:
        response = httpx.post(
            self.url,
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            },
            timeout=60.0,
        )

        response.raise_for_status()

        return response.json()["message"]["content"]
