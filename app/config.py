import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    GROQ_FAILOVER_KEY=os.getenv("GROQ_FAILOVER_KEY")
    GROQ_MODEL="llama-3.3-70b-versatile"

    QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")
    QDRANT_END_POINT=os.getenv("QDRANT_END_POINT")
    QDRANT_COLLECTION="RAG-Enterprise"

    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

setting = Settings()