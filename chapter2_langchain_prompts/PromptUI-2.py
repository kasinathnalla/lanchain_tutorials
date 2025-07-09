import sys
import os
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.EnvLoader import getGroqKey
from langchain_core.prompts import load_prompt, PromptTemplate
import streamlit as st


def chatUI() :
    # If the temperature is 0.0, it will be more deterministic. Response will be same every time.
    # if the temperature is 1.0 or 1.5, it will be more random. Response will be different every time.
    llm = ChatGroq(model="llama3-8b-8192", api_key=getGroqKey(), temperature=0.0)  # type: ignore
    st.title("Chat Research tool with Prompts")
    st.header('Reasearch Tool')
    paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

    style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

    length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

    template = load_prompt(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/chapter2_langchain_prompts", "template.json"))



    if st.button("Generate Explanation"):
        chain = template | llm
        result = chain.invoke({'paper_input':paper_input, 'style_input':style_input, 'length_input':length_input})
        st.write(result.content)

    



if __name__ == "__main__":
    chatUI()