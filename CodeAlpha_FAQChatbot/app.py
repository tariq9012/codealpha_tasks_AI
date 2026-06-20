"""
CodeAlpha - Task 2: Chatbot for FAQs
Flask web server exposing a simple chat UI.
"""

from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot

app = Flask(__name__)
bot = FAQChatbot()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.get_json().get("message", "")
    result = bot.get_response(user_message)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
