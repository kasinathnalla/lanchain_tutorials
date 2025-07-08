from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey

load_dotenv()
os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',

    pipeline_kwargs=dict(temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)