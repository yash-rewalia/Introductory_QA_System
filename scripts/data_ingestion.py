from llama_index.core import SimpleDirectoryReader
import sys

from exception import customexception
from logger import logging


def load_data(data):
    '''
    Load pdf data from the given directory

    Parameters:
    - data : str : path to the directory containing pdf files

    return:
    - A list of loaded pdf docuemnts
    '''
    try:
        logging.info("Loading data from the given directory")
        document = SimpleDirectoryReader("Data")
        doc = document.load_data()
        logging.info("Data loaded successfully")
        return doc
    except Exception as e:
        logging.error("Error loading data from the given directory")
        raise customexception(e,sys)