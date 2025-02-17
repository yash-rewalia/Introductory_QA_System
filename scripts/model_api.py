import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from logger import logging

from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model = Gemini(model='models/gemini-pro',api_key=os.getenv("GOOGLE_API_KEY"))
        Settings.llm = model
        # Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        return model
    except Exception as e:
        raise customexception(e,sys)