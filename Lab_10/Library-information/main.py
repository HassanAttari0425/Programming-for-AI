from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.chat.util import Chat, reflections

nltk.download("punkt")
nltk.download('vader_lexicon')

app = Flask(__name__)

# Chat Pairs
Pairs = [
    [r"hello|hi", ["Hello! How can I assist you with library information?"]],
    [r"bye|goodbye", ["Okay, goodbye! Have a great day."]],
    [r"what are the library hours\??", ["Our library is open from 9 AM to 8 PM, Monday through Saturday."]],
    [r"is the library open on sunday\??", ["The library is closed on Sundays."]],
    [r"how can i get a library card\??", ["You can get a library card by visiting the front desk with a valid ID and proof of address."]],
    [r"how many books can i borrow\??", ["You can borrow up to 5 books at a time."]],
    [r"what is the late fee for books\??", ["The late fee is $0.50 per day for each overdue book."]],
    [r"do you have e-books\??", ["Yes, we offer a collection of e-books."]],
    [r"can i reserve a book\??", ["Yes, you can reserve a book online or by speaking with a librarian."]],
    [r"do you offer printing services\??", ["Yes, printing services are available."]],
    [r"can i use the computer at the library\??", ["Yes, computers are available with a valid library card."]],
    [r"do you have study rooms\??", ["Yes, we have study rooms available."]],
]

chatbot = Chat(Pairs, reflections)
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "positive"
    elif score["compound"] <= -0.05:
        return "negative"
    else:
        return "neutral"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["message"]
    if user_input.lower() == "sentiment":
        return jsonify(response="Tell me a sentence to analyze.")
    
    elif user_input.lower().startswith("analyze:"):
        sentence = user_input[8:].strip()
        sentiment_result = get_sentiment(sentence)
        return jsonify(response=f"Sentiment Analysis result: {sentiment_result}")
    
    response = chatbot.respond(user_input)
    if response:
        return jsonify(response=response)
    else:
        return jsonify(response="I am not sure how to respond.")

@app.route("/suggest", methods=["POST"])
def suggest():
    text = request.json["input"]
    all_prompts = [
        "what are the library hours?",
        "is the library open on sunday?",
        "how can i get a library card?",
        "how many books can i borrow?",
        "do you have e-books?",
        "can i reserve a book?",
        "do you offer printing services?",
        "can i use the computer at the library?",
        "do you have study rooms?"
    ]
    suggestions = [q for q in all_prompts if text.lower() in q.lower()]
    return jsonify(suggestions=suggestions[:5])

if __name__ == "__main__":
    app.run(debug=True)
