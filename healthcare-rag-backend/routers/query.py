from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_service import query_rag

router = APIRouter()

# Pydantic request schema
class QueryRequest(BaseModel):
    question: str

# Endpoint: /api/rag/query
@router.post("/rag/query")
def ask_question(req: QueryRequest):
    """
    Accepts a medical question and returns a context-aware RAG-based answer.
    """
    result = query_rag(req.question)

    # Safety fallback if model gives an empty or templated response
    if not result["answer"].strip() or result["answer"].strip().startswith("You are"):
        result["answer"] = "I don't know based on the context."

    return result
