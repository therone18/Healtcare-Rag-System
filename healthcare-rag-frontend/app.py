import streamlit as st
from utils import ask_question, upload_pdfs, embed_all

st.set_page_config(page_title="Healthcare RAG", layout="wide")

st.title("Healthcare Document Q&A Assistant (Powered by Mistral)")

# Upload Section
st.sidebar.header("Upload PDFs")
uploaded_files = st.sidebar.file_uploader("Upload patient PDFs", type="pdf", accept_multiple_files=True)

if st.sidebar.button("Upload"):
    if uploaded_files:
        with st.spinner("Uploading..."):
            upload_response = upload_pdfs(uploaded_files)
            embed_response = embed_all()
            st.success(f"{len(upload_response['document_ids'])} documents uploaded.")
            st.success(f"{embed_response['chunks_added']} chunks embedded.")
    else:
        st.warning("Please upload at least one PDF.")

# Chat Section
st.header("Ask a medical question")
user_input = st.text_input("Type your question here...", placeholder="Give me a run down of all current patients")

if st.button("Submit Question"):
    if user_input:
        with st.spinner("Querying LLM..."):
            response = ask_question(user_input)
            st.markdown(f"**🧠 Answer:** {response['answer']}")
            if response["sources"]:
                st.markdown("**Sources:**")
                for src in response["sources"]:
                    st.json(src)
    else:
        st.warning("Please enter a question.")
