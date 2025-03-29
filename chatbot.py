# Simple time-traveling chatbot

# imprting feedparser
import feedparser

# feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
latest_headline = feed.entries[0].title

print("Greetings from 2049! My name is Officer KD3-6 and I am a time traveler. Ask me anything.")

while True:
    question = input("You: ")
    question =  question.lower()
    if(question=="exit"):
        print("Time traveler: Goodbye, primitive!")
        break
    elif question == "what’s the future like?" or question == "what's the future like?":
        print(f"Time traveler: After {latest_headline},The skies glow with neon storms, and cities float on water. Weird, right?")
    elif question == "do we have flying cars?":
        print("Time traveler: Yes, but they’re mostly for cats. Humans still crash too much.")
    elif question == "who rules the world?":
        print("Time traveler: A council of AI dolphins. Don’t ask how they got the votes.")
    elif question == "are robots in charge?":
        print("Time traveler: Not fully, but they judge our dance moves now.")
    elif question == "what’s the most popular food?":
        print("Really bruh? Obviously weed")
    elif question == "is mia khalifa still alive and giving blowjobs to random people on the street?":
        print("Dont tell this to anyone. yeah she's still like that and has become wayb more busty . Now she's a MIlf and guess what, I am a MILF hunter . Hahahas")
    else:
        print("Time traveler: The future is hazy on that one. Ask something else, primitive!")