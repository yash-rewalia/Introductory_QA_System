import os
from dotenv import load_dotenv
load_dotenv()


from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex,ServiceContext,StorageContext,load_index_from_storage

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


document = SimpleDirectoryReader('D:\work_yk\QA_system\Data')
doc = document.load_data()

model = Gemini(model='models/gemini-pro',api_key=os.getenv("GOOGLE_API_KEY"))
gemini_embed_model = GeminiEmbedding(model_name='models/text-embedding-004')


Settings.llm = model
Settings.embed_model = gemini_embed_model
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)

index = VectorStoreIndex.from_documents(doc,embed_model=gemini_embed_model)

query_engine = index.as_query_engine()

response = query_engine.query("What is empirical rule?")
print(response.response)