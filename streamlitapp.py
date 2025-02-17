import streamlit as st
from scripts.data_ingestion import load_data
from scripts.embedding import download_gemini_embedding
from scripts.model_api import load_model

def main():
    st.set_page_config(page_title="QA System", page_icon="🧊", layout="wide")

    doc = st.file_uploader("Upload your document")

    st.header("QA with documents (Information Retrieval) using Gemini Embedding")

    user_question = st.text_input("Ask your question")

    if st.button("Submit & process"):
        if doc is not None:
            with st.spinner("Processing..."):
                document = load_data(doc)
                model = load_model()
                index = download_gemini_embedding(model, document)
                response = index.query(user_question)
                st.write(response.response)
        else:
            st.write("Please upload a document")

if __name__ == "__main__":
    main()