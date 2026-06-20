# 🌐 Language Translation Tool — CodeAlpha AI Internship (Task 1)

A simple, clean web app that lets a user type text, choose a source and
target language, and instantly get a translated result — with bonus
copy-to-clipboard and text-to-speech features.

## ✨ Features
- Text input box with source & target language selection
- Auto-detect source language option
- Translation powered by `deep-translator` (Google Translate backend, no API key needed)
- 🔊 Text-to-speech for both input and translated text (built-in browser API)
- 📋 One-click copy of translated text
- ⇄ Swap source/target language instantly

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **Translation:** `deep-translator` library
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Voice:** Web Speech API (`SpeechSynthesisUtterance`)

## 🚀 How to Run

1. Clone this repo and move into the folder:
   ```bash
   git clone <your-repo-link>
   cd CodeAlpha_LanguageTranslator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000/`

## 📂 Project Structure
```
CodeAlpha_LanguageTranslator/
├── app.py              # Flask backend + translation logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main UI
└── static/
    └── style.css        # Styling
```

## 📌 Task Requirements Covered
- [x] UI to enter text and select source & target languages
- [x] Translation API integration (Google Translate via deep-translator)
- [x] Sends text to API and displays translated response
- [x] Optional: copy button ✅
- [x] Optional: text-to-speech ✅

---
**Internship:** CodeAlpha — Artificial Intelligence
**Author:** Tariq Jamil Khan
