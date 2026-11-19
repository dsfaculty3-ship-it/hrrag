# step 2: splitting

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

def split_into_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)