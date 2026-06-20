"""
CodeAlpha - Task 1: Language Translation Tool
Author: Tariq Jamil Khan

A simple web app where a user types text, picks a source & target
language, and gets the translated text back instantly.

Uses the 'deep-translator' library (free, no API key needed,
wraps Google Translate under the hood).
"""

from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# A useful subset of languages for the dropdowns (code: name)
LANGUAGES = {
    "auto": "Detect Language",
    "en": "English",
    "ur": "Urdu",
    "ar": "Arabic",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
    "tr": "Turkish",
    "it": "Italian",
    "pt": "Portuguese",
    "fa": "Persian",
    "ps": "Pashto",
    "bn": "Bengali",
}


@app.route("/")
def home():
    return render_template("index.html", languages=LANGUAGES)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    source = data.get("source", "auto")
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Please enter some text to translate."}), 400

    try:
        translated_text = GoogleTranslator(source=source, target=target).translate(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
