from flask import Flask, render_template, request
import feedparser
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Fetch the latest headline for every question
        feed_url = f"http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml?{int(time.time())}"
        feed = feedparser.parse(feed_url)
        if feed.entries:
            latest_headline = feed.entries[1].title
        else:
            latest_headline = "Well, That's a bit weird.. but"

        question = request.form["question"].lower()
        if question == "exit":
            response = "Time traveler: The timeline closes. Farewell!"
        elif question == "what’s the future like?" or question == "what's the future like?":
            response = f"Time traveler: Based on '{latest_headline}', the future glows with neon storms and floating cities!"
        elif question == "do we have flying cars?":
            response = "Time traveler: Yes, but they’re mostly for cats. Humans still crash too much."
        elif question == "who rules the world?":
            response = "Time traveler: A council of AI dolphins. Don’t ask how they got the votes."
        elif question == "are robots in charge?":
            # Refresh the headline again here
            feed = feedparser.parse("http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml")
            if feed.entries:
                latest_headline = feed.entries[1].title
            else:
                latest_headline = "Well, That's a bit weird.. but"
            response = f"Time traveler: Not yet, but after '{latest_headline}', they’re judging our dance moves!"
        elif question == "what should i do today?":
            response = "Time traveler: Build a time machine. You’re late to the party!"
        elif question == "tell me a secret!":
            response = "Time traveler: In 2075, pizza grows on trees. Don’t tell the past!"
        else:
            response = "Time traveler: The future is hazy on that one. Ask something else, primitive!"
        return render_template("index.html", headline=latest_headline, response=response)

    # For GET requests, fetch the latest headline once
    feed_url = f"http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml?{int(time.time())}"
    feed = feedparser.parse(feed_url)
    if feed.entries:
        latest_headline = feed.entries[0].title
    else:
        latest_headline = "Well, That's a bit weird.. but"
    return render_template("index.html", headline=latest_headline, response=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)