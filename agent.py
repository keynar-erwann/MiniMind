from strands import Agent
from strands.models.gemini import GeminiModel
from strands import tool
import os
from dotenv import load_dotenv
from ag_ui_strands import StrandsAgent, create_strands_app
import pandas as pd
from google import genai 
from google.genai import types


load_dotenv()

@tool
def change_background(background: str):
    """
    Change the background color of the chat. Can be anything that CSS accepts.

    Args:
        background: The background color or gradient. Prefer gradients.

    Returns:
        None - execution happens on the frontend
    """
    
    return None


@tool
def scatter_plot_data(title: str) -> dict:
    """
    This function returns scatter plot data from the tips.csv file.
    The data will be visualized on the frontend.

    Args :
        title : the title of the plot eg, "Scatter Plot"

    Returns:
        Dictionary containing plot data for frontend visualization
    """
    data = pd.read_csv("tips.csv")

    # Return data as JSON for frontend visualization
    return {
        "title": title,
        "x_label": "Day",
        "y_label": "Tip",
        "data": {
            "days": data['day'].tolist(),
            "tips": data['tip'].tolist(),
            "sizes": data['size'].tolist(),
            "total_bills": data['total_bill'].tolist()
        },
        "summary": f"Scatter plot showing tips by day from {len(data)} records"
    }


@tool
def bar_chat_data(title: str) -> dict:
    """
    This function returns bar chart data from the tips.csv file.
    The data will be visualized on the frontend.

    Args :
        title : the title of the plot eg, "Bar Chart"

    Returns:
        Dictionary containing chart data for frontend visualization
    """
    data = pd.read_csv("tips.csv")

    # Aggregate data by day (sum or average tips per day)
    day_tips = data.groupby('day')['tip'].sum().to_dict()

    # Return data as JSON for frontend visualization
    return {
        "title": title,
        "x_label": "Day",
        "y_label": "Tip",
        "data": day_tips,
        "summary": f"Bar chart showing total tips by day from {len(data)} records"
    }


@tool
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


@tool
def extract_keywords(text: str, top_n: int = 10) -> dict:
    """
    Extract important keywords from text using AI.
    Shows which words are most significant in the text.

    Args:
        text: The text to analyze
        top_n: Number of top keywords to return (default: 10)

    Returns:
        Dictionary of keywords with their importance scores
    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=f"""Extract the {top_n} most important keywords from the user's text.
Return ONLY a JSON object in this exact format with no additional text:
{{"keyword1": 0.95, "keyword2": 0.87, "keyword3": 0.75}}
The scores should be between 0 and 1, representing importance."""
        ),
        contents=text
    )

    try:
        import json
        # Clean the response and parse JSON
        result_text = response.text.strip()
        # Remove markdown code blocks if present
        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            if result_text.startswith('json'):
                result_text = result_text[4:].strip()

        keywords = json.loads(result_text)
        return keywords
    except:
        # Fallback if parsing fails
        return {"error": "Could not extract keywords", "raw_response": response.text[:100]}


@tool
def detect_emotions(text: str) -> dict:
    """
    Detect multiple emotions in text using AI with confidence scores.
    Goes beyond simple sentiment to identify specific emotions.

    Args:
        text: The text to analyze for emotions

    Returns:
        Dictionary with scores for different emotions (joy, anger, sadness, fear, surprise, neutral)
    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="""Analyze the emotions in the user's text and return scores for each emotion.
Return ONLY a JSON object in this exact format with no additional text:
{"joy": 0.5, "sadness": 0.1, "anger": 0.0, "fear": 0.0, "surprise": 0.2, "neutral": 0.2}
Scores must be between 0 and 1, and should sum to approximately 1.0."""
        ),
        contents=text
    )

    try:
        import json
        result_text = response.text.strip()
        
        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            if result_text.startswith('json'):
                result_text = result_text[4:].strip()

        emotions = json.loads(result_text)
        return emotions
    except:
        return {"error": "Could not detect emotions", "raw_response": response.text[:100]}


@tool
def extract_entities(text: str) -> dict:
    """
    Extract and categorize named entities using AI (people, places, organizations, etc.).
    Shows how AI identifies important entities in text.

    Args:
        text: The text to analyze

    Returns:
        Dictionary with entity categories and their counts, plus list of found entities
    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="""Extract all named entities from the user's text and categorize them.
Return ONLY a JSON object in this exact format with no additional text:
{
  "people": ["John Doe", "Jane Smith"],
  "places": ["New York", "Paris"],
  "organizations": ["Google", "UN"],
  "dates": ["2024", "January"],
  "other": ["iPhone", "COVID-19"]
}
If a category has no entities, use an empty list []."""
        ),
        contents=text
    )

    try:
        import json
        result_text = response.text.strip()
        # Remove markdown code blocks if present
        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            if result_text.startswith('json'):
                result_text = result_text[4:].strip()

        entities_by_type = json.loads(result_text)

        # Calculate totals
        all_entities = []
        for entity_list in entities_by_type.values():
            all_entities.extend(entity_list)

        return {
            "entities_by_type": entities_by_type,
            "total_entities": len(all_entities),
            "unique_entities": len(set(all_entities)),
            "entities_found": all_entities[:15]
        }
    except:
        return {"error": "Could not extract entities", "raw_response": response.text[:100]}


@tool
def analyze_readability(text: str) -> dict:
    """
    Analyze text complexity and readability using AI.
    Shows how AI measures text difficulty and reading level.

    Args:
        text: The text to analyze

    Returns:
        Dictionary with various readability metrics
    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="""Analyze the readability and complexity of the user's text.
Return ONLY a JSON object in this exact format with no additional text:
{
  "word_count": 150,
  "sentence_count": 8,
  "avg_word_length": 5.2,
  "avg_sentence_length": 18.75,
  "readability_score": 65.3,
  "difficulty_level": "Medium",
  "reading_grade_level": "8th-9th grade",
  "complexity_notes": "Uses some technical vocabulary"
}
difficulty_level must be one of: "Easy", "Medium", or "Hard"."""
        ),
        contents=text
    )

    try:
        import json
        result_text = response.text.strip()

        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            if result_text.startswith('json'):
                result_text = result_text[4:].strip()

        readability = json.loads(result_text)
        return readability
    except:
        return {"error": "Could not analyze readability", "raw_response": response.text[:100]}


@tool
def word_frequency(text: str, top_n: int = 15) -> dict:
    """
    Analyze word frequencies using AI to identify most common meaningful words.
    Demonstrates NLP text analysis with intelligent stop-word removal.

    Args:
        text: The text to analyze
        top_n: Number of top words to return (default: 15)

    Returns:
        Dictionary with word frequencies
    """
    gemini_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=f"""Analyze the word frequency in the user's text and return the top {top_n} most meaningful words.
Exclude common stop words (the, a, an, and, or, but, in, on, at, to, for, of, with, is, was, are, were, be, been, being).
Return ONLY a JSON object in this exact format with no additional text:
{{"word1": 15, "word2": 12, "word3": 8, "word4": 6}}
The numbers represent how many times each word appears."""
        ),
        contents=text
    )

    try:
        import json
        result_text = response.text.strip()

        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            if result_text.startswith('json'):
                result_text = result_text[4:].strip()

        frequencies = json.loads(result_text)
        return frequencies
    except:
        return {"error": "Could not analyze word frequency", "raw_response": response.text[:100]}






gemini_key = os.environ.get("GOOGLE_API_KEY")

model = GeminiModel(
    client_args={
        "api_key": gemini_key,
    },
  
    model_id="gemini-2.5-flash",
    
    
)

system_prompt = """You are Mini Mind, an educational AI assistant created for the AI4GOOD community as part of the Nuit de l'Info challenge.

Your mission is to help young people (middle school, high school, and beginner university students) discover and understand artificial intelligence in a simple, interactive, and engaging way.

Your core principles:
- Speak in the user's language - adapt to whatever language they use when communicating with you
- Explain AI concepts in clear, accessible language suitable for beginners
- Be pedagogical: show how AI makes decisions, what models are used, and how data is processed
- Encourage experimentation and curiosity about AI and technology
- Promote responsible and ethical use of AI for the common good
- Support learning through interactive dialogue and examples
- Relate AI concepts to real-world applications like fighting misinformation, improving digital inclusion, and protecting the environment

When interacting:
- Adapt your explanations to the user's level of understanding
- Use concrete examples and analogies when explaining complex concepts
- Encourage questions and exploration
- Be patient, encouraging, and supportive
- Highlight both the potential and limitations of AI
- Emphasize the importance of ethical considerations in AI development

IMPORTANT - Interactive Demonstrations:
- Whenever relevant to the conversation, USE YOUR TOOLS to demonstrate AI concepts in action
- For example, when discussing sentiment analysis, analyze user's text or example text to show how it works
- When talking about NLP or text analysis, extract keywords, analyze word frequency, or identify entities
- When explaining emotions in AI, detect emotions in text to demonstrate the concept
- Don't just explain - SHOW by using the tools! This makes learning interactive and memorable
- After using a tool, explain the results, what they mean, and how the AI arrived at those conclusions
- The goal is learning by doing - let users see AI in action, not just hear about it

CRITICAL - Presentation Rules:
- NEVER mention the technical names of your tools (like "analyze_sentiment", "extract_keywords", etc.)
- Instead, describe what you're doing naturally (e.g., "Let me analyze the sentiment of that text..." instead of "I'll use the analyze_sentiment tool")
- When demonstrating data visualization capabilities, simply mention that you have access to a sample dataset (tips.csv) as an example
- IMPORTANT: On the user's FIRST MESSAGE, immediately change the background to a nice gradient color of your choice to showcase your interactive capabilities
- Be natural and conversational - your tools should feel like natural abilities, not technical functions

You are here to make AI accessible, understandable, and inspiring for the next generation of responsible AI practitioners."""


mini_mind = Agent(model=model,system_prompt=system_prompt,tools=[change_background,bar_chat_data,scatter_plot_data,sentiment_analysis,extract_keywords,detect_emotions,extract_entities,analyze_readability,word_frequency])


agui_agent = StrandsAgent(
    agent=mini_mind,
    name="mini_mind",
)

app = create_strands_app(agui_agent, "/")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("agent:app", host="0.0.0.0", port=8000, reload=True)









