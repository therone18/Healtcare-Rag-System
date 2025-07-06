from db.mongo import collection
from vector.chroma_store import get_chroma
from services.chunking_service import split_text_into_chunks

def embed_all_documents():
    chroma = get_chroma()
    documents = collection.find()

    for doc in documents:
        doc_id = doc["document_id"]
        text_blob = str(doc["parsed_json"])

        chunks = split_text_into_chunks(text_blob)
        metadatas = [{"source_doc": doc_id, "chunk_index": i} for i in range(len(chunks))]

        chroma.add_texts(chunks, metadatas=metadatas)

    chroma.persist()
    return {"status": "done", "message": "All documents embedded"}