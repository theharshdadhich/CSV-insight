from fastapi import APIRouter, HTTPException
from models.query import Query
from services.llm_service import query_llm

router = APIRouter()

@router.post("/ask/")
async def ask_question(query: Query):
    try:
        answer = query_llm(query.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")