from fastapi import APIRouter # type: ignore
from pydantic import BaseModel # type: ignore
from rag.query_processing import generate_response

router = APIRouter()

class Query(BaseModel):
    question: str
#api for query
@router.post("/query")
async def get_answer(query: Query):
    answer = generate_response(query.question)
    return {"answer": answer}
