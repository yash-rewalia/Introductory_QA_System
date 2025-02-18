from llama_index.core import VectorStoreIndex
from llama_index.core.schema import Document
from llama_index.embeddings.gemini import GeminiEmbedding


from scripts.data_ingestion import load_data
from scripts.model_api import load_model

import sys
from exception import customexception
from logger import logging

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai

from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

def download_gemini_embedding(model, document_text):
    '''
    This function is used to download and initialize Gemini embedding model.

    Parameters:
    - model : The language model.
    - document_text : str : The extracted text from the document.

    Returns:
    - query_engine : VectorStoreIndex query object.
    '''
    try:
        logging.info("Initializing Gemini Embedding Model...")
        gemini_embed_model = GeminiEmbedding(model='models/text-embedding-004')

        # Set LLM settings
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        
        logging.info("Converting text to document format...")
        documents = [Document(text=document_text)]  # Convert text to document
        
        logging.info("Creating Vector Store Index...")
        index = VectorStoreIndex.from_documents(documents, embed_model=gemini_embed_model)
        
        logging.info("Initializing Query Engine...")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e, sys)