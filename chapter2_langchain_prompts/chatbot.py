import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey
from langchain_core.prompts import load_prompt, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import List
from langchain_core.messages import BaseMessage

def chatbot() :
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey(), temperature=0.0)  # type: ignore
    chat_history :  List[BaseMessage] = [ SystemMessage(content='You are a helpful customer support agent') ]
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        chat_history.append(HumanMessage(content=user_input))
        result = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print(f"Assistant: {result.content}")

    print(chat_history)
  
if __name__ == "__main__":
    chatbot()