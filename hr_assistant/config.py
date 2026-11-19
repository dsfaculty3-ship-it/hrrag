import os
from dotenv import load_dotenv

load_dotenv

groq_key = os.getenv("GROQ_API_KEY")
jina_key = os.getenv("JINA_API_KEY")

# load data
DATA_FILE_PATH = os.path.join("data", "hr_policy.txt")

# vector store


# models
LLM_MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v3"