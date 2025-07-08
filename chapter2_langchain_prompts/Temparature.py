import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey

def temparatureTestUsingDifferentValues() :
    # If the temperature is 0.0, it will be more deterministic. Response will be same every time.
    # if the temperature is 1.0 or 1.5, it will be more random. Response will be different every time.
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey(), temperature=0.0)  # type: ignore
    print(llm.invoke("write 5 lines about cat").content)



if __name__ == "__main__":
    temparatureTestUsingDifferentValues()