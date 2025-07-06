from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["healthcare_rag"]
collection = db["parsed_documents"]

def insert_parsed_document(document: dict):
    collection.insert_one(document)
