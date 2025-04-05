from collections import defaultdict
import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    sentiment_to_count = defaultdict(int)
    
    for sen in sentiments:
        sentiment_to_count[sen] += 1
    
    sentiment = sentiment_to_count.keys()
    count = sentiment_to_count.values()
    plt.figure(figsize=(12,6))
    plt.title("sentiments review")
    fig, ax = plt.subplots()
    ax.bar(sentiment, count)
    ax.set_xlabel("count")
    ax.set_ylabel("sentitments")

    fig.savefig("./images/test.png")