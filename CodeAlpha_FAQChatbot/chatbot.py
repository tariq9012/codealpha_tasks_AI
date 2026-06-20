"""
CodeAlpha - Task 2: Chatbot for FAQs
Author: Tariq Jamil Khan

Matches a user's question against a bank of FAQs using NLP preprocessing
(tokenization, stopword removal, lemmatization) + TF-IDF cosine similarity.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import FAQS

# Make sure required NLTK data is available
for resource in ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]:
    try:
        nltk.data.find(f"tokenizers/{resource}" if "punkt" in resource else
                        f"corpora/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)

lemmatizer = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words("english"))


def preprocess(text: str) -> str:
    """Lowercase, remove punctuation, tokenize, remove stopwords, lemmatize."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in STOP_WORDS]
    return " ".join(tokens)


class FAQChatbot:
    def __init__(self, faqs=None, similarity_threshold: float = 0.25):
        self.faqs = faqs or FAQS
        self.similarity_threshold = similarity_threshold

        # Build a flat list of all phrasings (main question + alt phrasings)
        # mapped back to their FAQ index, so more phrasings = better matching.
        self.corpus = []
        self.corpus_to_faq_index = []

        for i, faq in enumerate(self.faqs):
            phrasings = [faq["question"]] + faq.get("alt", [])
            for p in phrasings:
                self.corpus.append(preprocess(p))
                self.corpus_to_faq_index.append(i)

        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    def get_response(self, user_input: str):
        cleaned = preprocess(user_input)
        if not cleaned.strip():
            return {
                "answer": "Could you please type your question in a bit more detail?",
                "matched_question": None,
                "confidence": 0.0,
            }

        user_vec = self.vectorizer.transform([cleaned])
        similarities = cosine_similarity(user_vec, self.tfidf_matrix).flatten()

        best_idx = similarities.argmax()
        best_score = similarities[best_idx]

        if best_score < self.similarity_threshold:
            return {
                "answer": "Sorry, I couldn't find a matching answer for that. "
                          "Try rephrasing your question, or contact our support team for help.",
                "matched_question": None,
                "confidence": round(float(best_score), 3),
            }

        faq_index = self.corpus_to_faq_index[best_idx]
        matched_faq = self.faqs[faq_index]

        return {
            "answer": matched_faq["answer"],
            "matched_question": matched_faq["question"],
            "confidence": round(float(best_score), 3),
        }


if __name__ == "__main__":
    # Quick CLI test
    bot = FAQChatbot()
    print("FAQ Chatbot ready! Type 'quit' to exit.\n")
    while True:
        q = input("You: ")
        if q.lower() in ("quit", "exit"):
            break
        result = bot.get_response(q)
        print(f"Bot: {result['answer']}  (confidence: {result['confidence']})\n")
