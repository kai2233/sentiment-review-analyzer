from openai import OpenAI
from config import error_message
import json

def get_sentiment(text: list) -> list:
    """
    Utilize gpt-4o-mini model to anaylze each reviews and categorize them as
    positive, neutral, negative, or irrelevant.

    Args:
        text (list): A list of strings that contain customer's review

    Returns:
        list[str]: A list of strings representing the sentiment of each corresponding review.
    """
    client = OpenAI()

    if not text or any(isinstance(val,int) for val in text):
        return error_message
    
    system_prompt = """
    You are a sentiment analyst with 20 years of experience, you can easily identify the sentiment behind people's review.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review as either positive, neutral, negative, or irrelevant.
    Use only a one-word response per line. Do not include any numbers. Total response size should exactly match the input size.

    Input size: {len(text)}
    Here are the input string:
    {text}
    """

    result = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"developer", "content":system_prompt},
            {"role":"user", "content":prompt},
            {"role":"assistant", "content": "Format the result as a json object. For instance:{ \"sentiments\":[\"positive\", \"negative\",\"neutral\",\"irrelevant\"], \"line_count\": 4} and do not include ``` json ```."}
        ]
    )

    data = json.loads(result.choices[0].message.content)
    return data["sentiments"]
