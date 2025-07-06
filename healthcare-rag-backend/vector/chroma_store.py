from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

CHROMA_PATH = "chroma_db"

def get_chroma():
    return Chroma(
        collection_name="documents",
        embedding_function=embedding_function,
        persist_directory=CHROMA_PATH
    )