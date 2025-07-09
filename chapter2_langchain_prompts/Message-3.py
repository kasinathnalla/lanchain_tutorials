import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def message3() :
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey(), temperature=0.0)  # type: ignore
    messages = [ SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')]
    result = llm.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(messages)



if __name__ == "__main__" :
    message3()
