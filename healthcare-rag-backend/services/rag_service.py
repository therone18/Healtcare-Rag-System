from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Path to persisted Chroma vector store
CHROMA_PATH = "chroma_db"

# 1. Embedding model (MiniLM from HuggingFace)
embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Load Chroma vector store
vectorstore = Chroma(
    collection_name="documents",
    embedding_function=embedding_function,
    persist_directory=CHROMA_PATH
)

# 3. Setup retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 4. Load Mistral from Ollama
llm = OllamaLLM(
    model="mistral",
    base_url="http://localhost:11434",
    temperature=0.2,
    top_p=0.9,
    num_ctx=2048
)

# 5. Prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are a helpful AI assistant with medical knowledge. "
        "Answer the question using the information from the context below.\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n\n"
        "Answer:"
    )
)

# 6. Build RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template},
    input_key="question" 
)


# 7. Query function
def query_rag(question: str):
    try:
        result = rag_chain.invoke({"question": question})
        return {
            "answer": result.get("result", "").strip(),
            "sources": [doc.metadata for doc in result.get("source_documents", [])]
        }
    except Exception as e:
        return {
            "answer": f"[Error] {str(e)}",
            "sources": []
        }
