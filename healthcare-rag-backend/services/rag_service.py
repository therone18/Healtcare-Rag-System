from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

CHROMA_PATH = "chroma_db"

# 1. Setup vector DB + retriever
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    collection_name="documents",
    embedding_function=embedding_function,
    persist_directory=CHROMA_PATH
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 2. Setup Ollama LLM wrapper
llm = Ollama(model="mistral")  # Change to your model name

# 3. Prompt template (LangChain style)
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant for healthcare-related queries. Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""
)

# 4. Define RAG Chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

def query_rag(question: str):
    result = rag_chain({"query": question})
    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    }