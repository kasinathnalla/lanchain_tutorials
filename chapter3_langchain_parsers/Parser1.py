# with structured outputtypeddict without using annotations
import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import List
from langchain_core.messages import BaseMessage
from utils.EnvLoader import getOpenAIKey

from typing import TypedDict


class Review(TypedDict):
    summary: str
    sentiment: str



promptString = """
The hardware is great, but the software feels bloated. There are too many pre installed apps that I can't remove.Also the UI looks outdated compared to other brands.
Hoping for a software update to fix this soon.
"""


def callLLM():
    llm = ChatOpenAI(api_key=getOpenAIKey())  # type: ignore
    llm_with_structured_output = llm.with_structured_output(Review)
    result = llm_with_structured_output.invoke(promptString)
    print(result)
    print(result['summary'])
    print(result['sentiment'])





if __name__ == "__main__":
    callLLM()