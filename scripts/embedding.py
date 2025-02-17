from llama_index.core import VectorStoreIndex,StorageContext,load_index_from_storage
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

def download_gemini_embedding(model,document):
    '''
    This function is used to download and initialize gemini embedding model

    returns:
    VectoreStoreIndex: index object
    '''
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model='models/text-embedding-004')

        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        
        logging.info("")
        index = VectorStoreIndex.from_documents(document,embed_model=gemini_embed_model)
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)