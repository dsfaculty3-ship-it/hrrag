import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")


# tracing

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

# load data
DATA_DIR  = os.path.join("data", "data")

# vector store
VECTOR_STORE_PATH = os.path.join("data","faiss.index")

# models
LLM_MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v3"


## 
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# retrieval process
TOP_K_RESULTS = 3


## system instruct
SYSTEM_PROMPT = ("You are HR assistant. Always search in policy documents do not add anything beyond the hr policy")

