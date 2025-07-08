from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"

# Initialize a single consistent embedding function
embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_chroma():
    return Chroma(
        collection_name="documents",
        embedding_function=embedding_function,
        persist_directory=CHROMA_PATH
    )

def get_retriever():
    vectorstore = Chroma(
        collection_name="documents",  
        embedding_function=embedding_function,  
        persist_directory=CHROMA_PATH
    )
    return vectorstore.as_retriever(search_kwargs={"k": 4})
