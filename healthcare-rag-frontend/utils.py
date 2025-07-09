import requests

BASE_URL = "http://localhost:8000/api"

def ask_question(query: str):
    res = requests.post(f"{BASE_URL}/rag/query", json={"question": query})
    return res.json()

def upload_pdfs(files):
    files_payload = [("files", (f.name, f, "application/pdf")) for f in files]
    res = requests.post(f"{BASE_URL}/upload/", files=files_payload)
    return res.json()

def embed_all():
    res = requests.post(f"{BASE_URL}/embed/")
    return res.json()
