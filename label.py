from openai import OpenAI
from config import error_message
import json

def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    client = OpenAI()

    if not text or any(isinstance(val,int) for val in text):
        return error_message
    
    system_prompt = """
    You are a psychologist with 20 years of experience, you can easily detect the real meaning behind people's words.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    """
    result = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"developer", "content":system_prompt},
            {"role":"user", "content":prompt}
        ]
    )
    data = json.loads(result.choices[0].message.content)
    return data["sentiments"]