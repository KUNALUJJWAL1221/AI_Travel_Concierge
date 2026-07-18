import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# Default models
CHAT_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Text splitting configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retriever configuration
TOP_K = 3