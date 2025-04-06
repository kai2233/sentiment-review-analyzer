from collections import defaultdict
import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> None:
    """
    Process sentiment data by calculating the frequency of each sentiment (positive, negative, neutral, irrelevant),
    then visualize the dataset as a bar graph.

    Args:
        sentiments (list): A list of strings representing the sentiment of each corresponding review.

    Returns:
        None
    """
    sentiment_to_count = {"positive": 0, "negative": 0, "neutral": 0, "irrelevant": 0}
    
    for sen in sentiments:
        sentiment_to_count[sen] += 1
    
    sentiment = sentiment_to_count.keys()
    count = sentiment_to_count.values()
    plt.figure(figsize=(12,6))
    plt.title("sentiments review")
    fig, ax = plt.subplots()
    ax.bar(sentiment, count)
    ax.set_xlabel("sentitments")
    ax.set_ylabel("count")

    fig.savefig("./images/sentiments_result.png")