from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import nltk
nltk.download('punkt')

# Define pairs
library_pairs = [
    [r"hi|hello", ["Hello! Welcome to the Library Chatbot."]],
    [r"(.*)your name?", ["I am the Library Assistant Chatbot."]],
    [r"(.*)book available (.*)", ["Let me check... Yes, we have that book available."]],
    [r"i want to borrow a book", ["Sure! Please provide the book title and your library ID."]],
    [r"how to return a book", ["You can return books at the front desk or through the return kiosk."]],
    [r"what are your opening hours", ["We are open from 9 AM to 8 PM, Monday to Saturday."]],
    [r"do you have ebooks", ["Yes, we have a collection of eBooks. Visit our digital library section."]],
    [r"how to get a library card", ["You can register online or visit the library front desk with an ID."]],
    [r"thank you|thanks", ["You're welcome!"]],
    [r"bye|goodbye", ["Goodbye! Happy reading!"]],
]

chatbot = Chat(library_pairs, reflections)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    response = chatbot.respond(user_input)
    return jsonify({"response": response or "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
