from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    INSERT DOCSTRING HERE
    """
    # open the json object
    with open(filepath, "r") as f:
        data = json.load(f)

    # extract the reviews from the json file
    reviews = data["results"]

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
