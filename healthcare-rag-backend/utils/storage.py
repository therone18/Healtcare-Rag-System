import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_pdf_file(file: UploadFile) -> str:
    """
    Saves the uploaded file to disk and returns its local path.
    """
    unique_filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOAD_DIR, unique_filename)
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    return filepath
