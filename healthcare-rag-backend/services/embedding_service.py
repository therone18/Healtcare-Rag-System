from db.mongo import collection
from vector.chroma_store import get_chroma
from services.chunking_service import split_text_into_chunks


def format_for_embedding(doc_json: dict) -> str:
    """Convert structured patient info into a single plain-text format."""
    return (
        f"Patient Name: {doc_json.get('patient_name', 'N/A')}\n"
        f"Visit Date: {doc_json.get('visit_date', 'N/A')}\n"
        f"Diagnosis: {doc_json.get('diagnosis', 'N/A')}\n"
        f"Medications: {', '.join(doc_json.get('medications', []))}\n"
        f"Physician: {doc_json.get('physician', 'N/A')}"
    )


def embed_all_documents():
    """
    Pulls all documents from MongoDB, chunks them,
    and adds them to the Chroma vectorstore with metadata.
    """
    chroma = get_chroma()
    documents = collection.find()
    doc_count = 0
    chunk_count = 0

    for doc in documents:
        doc_id = doc.get("document_id")
        parsed = doc.get("parsed_json")

        if not doc_id or not parsed:
            print(f"⚠️ Skipping invalid document: {doc.get('_id')}")
            continue

        formatted_text = format_for_embedding(parsed)

        # Split into overlapping chunks (helps RAG precision)
        chunks = split_text_into_chunks(
            formatted_text,
            max_tokens=500,
            overlap=50
        )

        # Base metadata (added to every chunk)
        metadata_base = {
            "source_doc": doc_id,
            "diagnosis": parsed.get("diagnosis", "N/A"),
            "physician": parsed.get("physician", "N/A"),
            "medications": parsed.get("medications", []),
        }

        metadatas = [
            {**metadata_base, "chunk_index": i}
            for i in range(len(chunks))
        ]

        chroma.add_texts(chunks, metadatas=metadatas)

        doc_count += 1
        chunk_count += len(chunks)

    chroma.persist()

    return {
        "status": "done",
        "message": f"Embedded {doc_count} documents with {chunk_count} total chunks."
    }
