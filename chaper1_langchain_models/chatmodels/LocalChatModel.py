from langchain_ollama import ChatOllama

'''
In this tutorial, I am providing example with Chat Model.. 


Lets talk about the response json.
Actual response is in content. 
With the content, it provided lot more details like Total Token and so on.. 
Tokens will more useful in the local LLM tutorial cause we can chatmodel to get the response in certain number of token so you dont need to get an essage back.

(lanchain_tutorials) kasinathnalla@Srisha-Nalla-Mac-Pro lanchain_tutorials % python chaper1_langchain_models/chatmodels/LocalChatModel.py 
content='The capital of India is New Delhi.' additional_kwargs={} 
response_metadata={'model': 'llama3.2:latest', 'created_at': '2025-07-08T05:13:08.786557Z', 'done': True, 'done_reason': 'stop', 'total_duration': 3729315500, 'load_duration': 1070900125, 
'prompt_eval_count': 31, 'prompt_eval_duration': 2274466625, 'eval_count': 9, 'eval_duration': 381505958, 
'model_name': 'llama3.2:latest'} id='run--c3c0dc2c-4a58-4c74-a46f-16e9e6c29bc7-0' 

usage_metadata={'input_tokens': 31, 'output_tokens': 9, 'total_tokens': 40}

TODO: Some reason its ignoring the num_predict and stop.
'''
def print_llm():
    llm = ChatOllama(model="llama3.2:latest",
    model_kwargs={"temperature": 0.8, "num_predict": 5, "stop": ["</s>"]}) # type: ignore
    result = llm.invoke("What is the capital of USA")
    print(result)

if __name__ == "__main__":
    print_llm()

#ChatOllama(model="llama3.2:latest")