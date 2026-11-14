from fastapi import APIRouter

router = APIRouter()


@router.get("/welcome")
async def welcome():
    return {"message": "Welcome to Adaptive RAG Platform!"}
