from dotenv import load_dotenv
from langchain_openai import OpenAI
import os

load_dotenv()

def getGroqKey():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return api_key

def getOpenAIKey():
    api_key = os.getenv("OPEN_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    return api_key