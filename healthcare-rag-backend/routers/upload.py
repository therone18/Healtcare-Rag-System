from fastapi import APIRouter, UploadFile, File
from typing import List
from utils.storage import save_pdf_file
from services.docling_services import parse_with_docling
from db.mongo import insert_parsed_document
import uuid, datetime

router = APIRouter()

@router.post("/upload/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    document_ids = []

    for file in files:
        saved_path = save_pdf_file(file)
        parsed_result = parse_with_docling(saved_path)

        doc = {
            "document_id": str(uuid.uuid4()),
            "original_filename": file.filename,
            "internal_file_path": saved_path,
            "upload_date": datetime.datetime.utcnow(),
            "parsed_json": parsed_result
        }

        insert_parsed_document(doc)
        document_ids.append(doc["document_id"])

    return {"status": "success", "document_ids": document_ids}
