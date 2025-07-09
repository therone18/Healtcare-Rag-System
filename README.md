
# Healthcare RAG System (Retrieval-Augmented Generation)

A local document-based Question Answering system built for healthcare documents. This project uses **LangChain**, **Ollama** (LLM), **IBM DocLing** (or simulated parser), and **Chroma** for vector search. Users can upload patient PDFs, extract structured information, and query patient data in natural language.


---

## Tech Stack

| Component           | Tech Used                               |
|---------------------|------------------------------------------|
| **Backend**         | FastAPI (Python)                         |
| **Frontend**        | Streamlit or Angular (optional)          |
| **LLM**             | Mistral (via Ollama)                     |
| **RAG Framework**   | LangChain                                |
| **Embeddings**      | HuggingFace `MiniLM`                     |
| **Vector Store**    | Chroma                                   |
| **PDF Parser**      | IBM DocLing API *(simulated)*            |
| **File Storage**    | MongoDB (stores PDFs + parsed JSON)      |
| **Database**        | MongoDB                                  |

---

## Features

- Upload multiple patient PDFs  
- Auto-parsing via IBM DocLing (simulated with mock data)  
- Store structured JSON and file data in MongoDB  
- Text chunking and vector embedding with HuggingFace  
- RAG: Contextual QA via Mistral (Ollama)  
- Chat-style interface (Postman or UI frontend)

---

## Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/healthcare-rag-system.git
cd healthcare-rag-system/healthcare-rag-backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file with:

```env
MONGO_URI=mongodb://localhost:27017
```

Make sure MongoDB is running locally.

---

## Ollama Setup (LLM)

1. [Install Ollama](https://ollama.com/download)
2. Pull the **Mistral** model:

```bash
ollama pull mistral
```

3. Run Ollama locally:

```bash
ollama run mistral
```

Backend will connect to this instance at `http://localhost:11434`

---

## Run the Backend API

```bash
uvicorn main:app --reload
```

You’ll have access to endpoints like:

- `POST /api/upload/` → Upload PDF files
- `POST /api/embed/` → Parse + Chunk + Embed documents
- `POST /api/rag/query` → Ask questions to the model

Use **Postman** or your frontend to send queries.
https://www.postman.com/aviation-cosmologist-88514797/workspace/public/collection/45790656-cdb4519e-4e48-46ab-9d9d-4e31f7067137?action=share&source=copy-link&creator=45790656
---

## Sample API Query (Postman)

**POST** `/api/rag/query`

```json
{
  "question": "Give me a run down of all the patients"
}
```

---

##  Folder Structure

```
healthcare-rag-backend/
│
├── main.py                      # FastAPI entrypoint
├── services/
│   ├── rag_service.py
│   ├── docling_services.py      # Simulated parser
│   ├── chunking_service.py
├── vector/
│   └── chroma_store.py
├── db/
│   └── mongo.py
├── routers/
│   ├── query.py
│   ├── embed.py
│   └── upload.py
├── utils/
│   └── storage.py
├── chroma_db/                   # Vector store (auto-created)
├── venv/
└── .env
```

---

## Known Limitations

- IBM DocLing is mocked. For production, replace with actual DocLing API integration.
- Ollama must run **locally**; deployment to cloud requires switching to a hosted LLM.
- No user authentication or access control (for demo simplicity).

---


Developed for the technical project interview for Strongwill Information Technology Solutions.

*Thank you Strongwill IT Solutions for the opportunity*