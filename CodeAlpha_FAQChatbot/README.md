# 🤖 Chatbot for FAQs — CodeAlpha AI Internship (Task 2)

An NLP-powered FAQ chatbot for an e-commerce store (Shopinza-style). It
preprocesses both the FAQ bank and the user's question, then uses
TF-IDF + cosine similarity to find the best matching answer.

## ✨ Features
- 12 common e-commerce FAQs (orders, payments, returns, delivery, etc.)
- Each FAQ has multiple alternate phrasings for better matching
- Full NLP preprocessing pipeline: lowercasing, punctuation removal,
  tokenization, stopword removal, lemmatization (NLTK)
- TF-IDF vectorization + cosine similarity for intent matching
- Confidence threshold — if no FAQ matches well, the bot says so instead
  of guessing
- Simple, clean chat UI (web-based)

## 🛠 Tech Stack
- **NLP:** NLTK (tokenization, stopwords, lemmatization)
- **Matching:** scikit-learn (TF-IDF Vectorizer, cosine similarity)
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, vanilla JavaScript

## 🚀 How to Run

1. Clone this repo and move into the folder:
   ```bash
   git clone <your-repo-link>
   cd CodeAlpha_FAQChatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web app:
   ```bash
   python app.py
   ```
   Then open `http://127.0.0.1:5000/` in your browser.

   **Or** test it directly in the terminal:
   ```bash
   python chatbot.py
   ```

## 📂 Project Structure
```
CodeAlpha_FAQChatbot/
├── app.py              # Flask server + chat route
├── chatbot.py           # NLP preprocessing + matching logic
├── faq_data.py          # FAQ knowledge base
├── requirements.txt
├── templates/
│   └── index.html       # Chat UI
└── static/
    └── style.css
```

## 📌 Task Requirements Covered
- [x] Collected FAQs (question + answer pairs)
- [x] NLP preprocessing using NLTK (tokenize, clean, lemmatize)
- [x] Matching via cosine similarity (intent matching)
- [x] Displays best matching answer as chatbot response
- [x] Optional: chat UI ✅

---
**Internship:** CodeAlpha — Artificial Intelligence
**Author:** Tariq Jamil Khan
