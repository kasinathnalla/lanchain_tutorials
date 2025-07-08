from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from langchain_huggingface import HuggingFaceEmbeddings

def huggingFace() :
    embedings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = embedings.embed_query("Delhi is the capital of India")
    print(vector)





if __name__ == "__main__":
    huggingFace()
   




