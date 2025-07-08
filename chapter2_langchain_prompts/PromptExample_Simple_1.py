import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey
from langchain_core.prompts import PromptTemplate

# This is the first class in this chapter.
# In the previous chapter, We always did model.invoke() to get the response. When we called the invoke, we are passing a text. That text can be called as prompt
# There are 3 types of prompts
# 1. Plain text prompt - Just plain test as a prompt in the invoke() method
# 2. Prompt template - You pass a PromptTemplate object to the invoke() method
# 3. Prompt template with dynamic variables - You pass a PromptTemplate object to the invoke() method with dynamic variables defined in the prompt template.

# Also there are 3 categories of prompts
# 1. System prompt
#       This is the prompt that you pass to the model to set the context of the conversation.
#       For example, if you want to generate a poem about a cat, you can pass the following prompt:
#       "You are a poet. You are writing a poem about a cat."

# 2. User prompt
#     This is the prompt that you pass to the model to ask a question.
#     For example, if you want to generate a poem about a cat, you can pass the following prompt:
#     "Write a poem about a cat"

# 3. Assistant prompt ( AI prompt)
#    This is the prompt that the model returns to you.
#    For example, if you want to generate a poem about a cat, the model will return the following prompt:
#    "The cat is a pet animal. It is a good pet. It is a cat."

# Now lets get started with the code.


# here we are passing a variable to the prompt template. That variable can be dynamic
def chatExample() :
    # If the temperature is 0.0, it will be more deterministic. Response will be same every time.
    # if the temperature is 1.0 or 1.5, it will be more random. Response will be different every time.
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey(), temperature=1.0)  # type: ignore
    template2 =PromptTemplate(
        template='Greet this person in 5 languages. The name of the person is {name}.',
        input_variables=['name']
    )
    prompt = template2.invoke({'name':'kasinath'})
    print(prompt)
    content = llm.invoke(prompt).content
    print(content)



if __name__ == "__main__":
    chatExample()