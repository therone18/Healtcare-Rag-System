from pymongo import MongoClient
from bson.binary import Binary
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

db = client["healthcare_rag"]
collection = db["uploaded_documents"]

def insert_parsed_document(document: dict):
    from bson.binary import Binary  # ensures safe binary format
    document["pdf_data"] = Binary(document["pdf_data"])  # Optional if already bytes
    return collection.insert_one(document)


def save_pdf_with_parsed_data(filename: str, binary_data: bytes, parsed_json: dict):
    document = {
        "filename": filename,
        "upload_date": datetime.datetime.utcnow(),
        "pdf_data": binary_data,
        "parsed_output": parsed_json
    }
    result = collection.insert_one(document)
    return str(result.inserted_id)

def insert_pdf_with_parsed_json(file_bytes, filename, parsed_result):
    from uuid import uuid4
    import datetime

    document = {
        "document_id": str(uuid4()),
        "original_filename": filename,
        "upload_date": datetime.datetime.utcnow(),
        "file_data": Binary(file_bytes),
        "parsed_json": parsed_result,
    }

    collection.insert_one(document)
    return document["document_id"]