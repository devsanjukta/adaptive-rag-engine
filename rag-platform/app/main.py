from fastapi import FastAPI

from app.endpoints import health

app = FastAPI(
    title="Adaptive RAG Platform",
    description="Advanced Hybrid RAG Engine",
    version="1.0.0",
)

app.include_router(health.router, prefix="/api/v1")
