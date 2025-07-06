from fastapi import APIRouter
from services.embedding_service import embed_all_documents

router = APIRouter()

@router.post("/embed/")
def run_embedding():
    return embed_all_documents()