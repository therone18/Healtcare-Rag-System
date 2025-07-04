
# Healthcare Document RAG System

A technical interview project to demonstrate a working Retrieval-Augmented Generation (RAG) system for healthcare-related document querying using parsed PDFs and large language models (LLMs).

Backend: Python (FastAPI)  
LLM: Ollama + LangChain  
Parsing: IBM DocLing  
Database: MongoDB  
Vector Store: FAISS/Chroma  
Frontend: Streamlit (or Angular)

---

## Project Objectives

- Upload and parse large healthcare PDFs (e.g., nursing notes, OASIS forms)
- Extract structured JSON using IBM DocLing
- Chunk and embed document data and store in a vector database
- Use Ollama and LangChain to implement a secure, on-premise RAG pipeline
- Provide a chat interface where users can ask natural-language questions about patient data

---

## Current Features (Day 1)

### PDF Upload and Parsing
- Upload single or multiple PDFs via `/api/upload/`
- Store PDFs locally (or to S3)
- Parse documents using simulated or real IBM DocLing API
- Store extracted structured JSON in MongoDB

---

## Tech Stack

| Component        | Technology               |
|------------------|--------------------------|
| Backend API      | FastAPI (Python)         |
| File Storage     | Local Disk / Amazon S3   |
| Document Parsing | IBM DocLing              |
| Database         | MongoDB                  |
| Vector Store     | FAISS / Chroma / MongoDB |
| Embedding Model  | Ollama (e.g., Mistral)   |
| RAG Framework    | LangChain                |
| Frontend         | Streamlit / Angular      |

---

## How to Run

1. Clone and Install

    git clone https://github.com/yourname/healthcare-doc-rag.git
    cd healthcare-doc-rag
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2. Set Environment Variables

    Create a `.env` file with:

    MONGO_URI=mongodb://localhost:27017
    DOC_LING_API_KEY=your-docling-key-if-any

3. Run the Server

    uvicorn main:app --reload

4. Test Upload (with curl)

    curl -X POST http://localhost:8000/api/upload/ \
    -F "files=@/path/to/document1.pdf" \
    -F "files=@/path/to/document2.pdf"

---

## Project Structure

    backend/
    ├── main.py                    # FastAPI entry point
    ├── routers/
    │   └── upload.py              # Handles upload endpoints
    ├── services/
    │   └── docling_service.py     # IBM DocLing interface (simulated)
    ├── utils/
    │   └── storage.py             # Local/S3 file handling
    ├── db/
    │   └── mongo.py               # MongoDB integration
    ├── .env                       # Environment variables
    └── requirements.txt

---

## Sample Use Cases (Planned Final Features)

- "What medications is patient John Doe currently taking?"
- "Summarize all nursing visits in the last 30 days."
- "What orders did Dr. Smith sign this month?"
- "What’s the OASIS SOC assessment result for Jane Doe?"

---

## Upcoming Features

| Feature                    | Status |
|----------------------------|--------|
| Document chunking          | Day 2  |
| Embedding via Ollama       | Day 2  |
| Vector DB storage          | Day 2  |
| LangChain RAG chain        | Day 3  |
| Streamlit chat interface   | Day 4  |
| Search by patient/date     | Day 5  |
| Final cleanup and docs     | Day 6  |

---

## License

This project is for demonstration and technical interview purposes only.
