from fastapi import APIRouter, UploadFile, File
from typing import List
from services.docling_services import parse_with_docling
from db.mongo import insert_pdf_with_parsed_json
import uuid
import datetime

router = APIRouter()

@router.post("/upload/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    document_ids = []

    for file in files:
        file_bytes = await file.read()

        #  Save temp file to parse with DocLing
        with open("temp.pdf", "wb") as f:
            f.write(file_bytes)

        parsed_result = parse_with_docling("temp.pdf")

        #  Save both binary and parsed result to MongoDB
        document_id = insert_pdf_with_parsed_json(
            file_bytes=file_bytes,
            filename=file.filename,
            parsed_result=parsed_result
        )

        document_ids.append(document_id)

    return {"status": "success", "document_ids": document_ids}
