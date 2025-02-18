import logging
import sys
import PyPDF2
import xml.etree.ElementTree as ET
from io import BytesIO
from docx import Document
from exception import customexception  # Ensure correct import

def load_data(uploaded_file):
    '''
    Load data from an uploaded file (PDF, TXT, DOCX, XML).

    Parameters:
    - uploaded_file : Uploaded file object from Streamlit.

    Returns:
    - str : Extracted text content from the file.
    '''
    try:
        if uploaded_file is None:
            raise ValueError("No file uploaded")
        
        file_extension = uploaded_file.name.split(".")[-1].lower()
        logging.info(f"Loading data from uploaded file: {uploaded_file.name}")

        if file_extension == "pdf":
            pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
            text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        
        elif file_extension == "txt":
            text = uploaded_file.read().decode("utf-8")

        elif file_extension == "docx":
            doc = Document(BytesIO(uploaded_file.read()))
            text = "\n".join([para.text for para in doc.paragraphs])

        elif file_extension == "xml":
            tree = ET.parse(BytesIO(uploaded_file.read()))
            root = tree.getroot()
            text = ET.tostring(root, encoding="utf-8").decode("utf-8")
        
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        logging.info("Data loaded successfully")
        return text
    except Exception as e:
        logging.error(f"Error loading data from uploaded file: {e}")
        raise customexception(e, sys)

