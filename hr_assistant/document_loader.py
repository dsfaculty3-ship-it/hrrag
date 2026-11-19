# step 1: read data
from langchain_community.document_loaders import TextLoader
from hr_assistant import config


def load_document(file_path:str=config.DATA_FILE_PATH):
    loader = TextLoader()
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents