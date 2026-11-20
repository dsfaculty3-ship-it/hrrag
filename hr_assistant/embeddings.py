from dotenv import load_dotenv
from langchain_jina import JinaEmbeddings
from hr_assistant import config

load_dotenv()

def get_embeddings_model():
    return JinaEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME
    )