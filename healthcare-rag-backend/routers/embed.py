from fastapi import APIRouter, HTTPException
from services.embedding_service import embed_all_documents
from typing import Dict

router = APIRouter()

@router.post("/embed/", response_model=Dict[str, str])
def run_embedding():
    """
    Triggers the document embedding process into the Chroma vectorstore.
    """
    try:
        result = embed_all_documents()

        if not result or result.get("status") != "done":
            raise HTTPException(status_code=500, detail="Embedding failed.")

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding error: {str(e)}")
