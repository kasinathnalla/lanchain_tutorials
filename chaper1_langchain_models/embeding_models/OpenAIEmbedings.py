from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from numpy import savez_compressed
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from utils.EnvLoader import getOpenAIKey

def opeA() :
    embedding = OpenAIEmbeddings(model="text-embedding-3-small", api_key=getOpenAIKey(), dimensions=32)  # type: ignore
    # Just to see how it creates tokens/scores
    result = embedding.embed_query("Delhi is the capital of India")
    print("This is just printing single query embedding :- "+ str(result))

    # This is for collection

    result = embedding.embed_documents(["Delhi is the capital of India", "Kolkata is the capital of West Bengal", "Paris is the capital of France"])
    print("This is printing document embedding as a collection :- "+str(result))
   
    # This is for question and answer
    printSimilarity(embedding)


def printSimilarity(embedding) :
    print("This is for question and answer on the documents")
    documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "Virat is an Indian cricketer known for his solid batting and leadership.",
   
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
    dataEmbeding = embedding.embed_documents(documents)
    query = "Tell me about Virat?"
    queryEmbeding = embedding.embed_query(query)
    scoresArray = cosine_similarity([queryEmbeding], dataEmbeding)
    # Scores is an array insdie an array. which 2X1 array. So we have to get the first element
    scores = scoresArray[0]
    #print(scores)
    sortedScores = sorted(list(enumerate(scores)), key=lambda x: x[1])
    # Since Its sorted assending order, so we need to get the last element. Hence we are using -1
    print(sortedScores)
    print(sortedScores[-1][0])
    print(sortedScores[-1][1])
    print("The most similar document is :- "+documents[sortedScores[-1][0]])

if __name__ == "__main__":
    opeA()
   