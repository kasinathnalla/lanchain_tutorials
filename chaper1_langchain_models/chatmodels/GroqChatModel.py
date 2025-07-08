import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey

load_dotenv()
'''
In this tutorial, I am providing example with Chat Model.. 


Lets talk about the response json.
Actual response is in content. 
With the content, it provided lot more details like Total Token and so on.. 
Tokens will more useful in the local LLM tutorial cause we can chatmodel to get the response in certain number of token so you dont need to get an essage back.

content='The capital of India is New Delhi.
' additional_kwargs={} 
response_metadata={'token_usage': 
{'completion_tokens': 9, 'prompt_tokens': 16, 'total_tokens': 25, 'completion_time': 0.006786672, 'prompt_time': 0.002398215, 'queue_time': 0.084146918, 'total_time': 0.009184887}, 
'model_name': 'llama3-8b-8192', 
'system_fingerprint': 'fp_6d1c2b0784', 'finish_reason': 'stop', 'logprobs': None} 
id='run--ff9696ec-aa0d-47ec-92d8-af3aed8fd73d-0' 
usage_metadata={'input_tokens': 16, 'output_tokens': 9, 'total_tokens': 25}

'''
def print_llm():
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey())  # type: ignore
    result = llm.invoke("What is the capital of India")
    print(result)

if __name__ == "__main__":
    print_llm()

#ChatOllama(model="llama3.2:latest")