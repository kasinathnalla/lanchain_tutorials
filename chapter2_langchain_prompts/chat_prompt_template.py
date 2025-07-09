import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey
from langchain_core.prompts import ChatPromptTemplate, load_prompt, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import List
from langchain_core.messages import BaseMessage

def chat_prompt_template() :
    llm = ChatPromptTemplate([('system', 'You are a helpful {domain} expert'), ('human', 'Explain in simple terms, what is {topic}')]) 
    result = llm.invoke({'domain':'cricket','topic':'Dusra'})
    print(result.to_messages())
    

if __name__ == "__main__":
    chat_prompt_template()