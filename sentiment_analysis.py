import os 
from google import genai 
from dotenv import load_dotenv 

from google.genai import types

load_dotenv()

def sentiment_analysis(sentence : str ) -> str :
    """ This function allows you to analyze a sentiment based on a sentence given by the user : 

    Args :

    Sentence : a sentence that contains a sentiment given by the user eg, "I love cakes"

    Returns : 

    A single word : either positive, negative or neutral 


    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")

    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Based on the user query just answer with one word : either positive, negative or neutral"),
    contents=sentence
)

    return response.text



test = sentiment_analysis("I love cakes")

print(test)