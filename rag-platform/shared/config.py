from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Ollama configuration
OLLAMA_MODEL_NAME = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/chat"

# Project root directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# reranker directories.
RERANKER_DATASET_DIR = PROJECT_ROOT / "reranker" / "dataset"
RERANKER_FULL_DATASET_PATH = RERANKER_DATASET_DIR / "full_dataset.csv"

RERANKING_TRAINING_PATH = RERANKER_DATASET_DIR / "training_data.csv"
RERANKING_VALIDATION_PATH = RERANKER_DATASET_DIR / "validation_data.csv"
RERANKING_TEST_PATH = RERANKER_DATASET_DIR / "test_data.csv"

RERANKING_TRAINING_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# trained model path
TRAINED_MODEL_PATH = PROJECT_ROOT / "trained_model"
RERANKING_TRAINED_MODEL_PATH = TRAINED_MODEL_PATH / "reranking"


class Settings(BaseSettings):
    DATABASE_URL: str

    # Load settings from the project's .env file.
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Ollama configuration
    OLLAMA_MODEL_NAME: str = "qwen2.5:3b"
    OLLAMA_URL: str = "http://localhost:11434/api/chat"


@lru_cache
def get_settings() -> Settings:
    return Settings()
