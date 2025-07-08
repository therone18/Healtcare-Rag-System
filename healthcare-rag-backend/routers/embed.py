from fastapi import APIRouter
from db.mongo import collection
from services.chunking_service import split_text_into_chunks
from vector.chroma_store import get_chroma

router = APIRouter()

@router.post("/embed/")
def embed_all_documents():
    chroma = get_chroma()

    # Get all documents from MongoDB
    docs = list(collection.find({}))
    added = 0

    for doc in docs:
        parsed = doc.get("parsed_json", {})
        # Convert dict to plain string for embedding
        text = "\n".join(f"{k.replace('_', ' ').title()}: {v if not isinstance(v, list) else ', '.join(v)}" for k, v in parsed.items())
        chunks = split_text_into_chunks(text)

        chroma.add_texts(
            texts=chunks,
            metadatas=[{"source_doc": doc["document_id"], "chunk_index": i} for i in range(len(chunks))]
        )
        added += len(chunks)

    return {"status": "success", "chunks_added": added}
