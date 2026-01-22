# Keyword Extractor using spaCy

A beginner-friendly keyword extraction project built using **spaCy**.
This project demonstrates core NLP concepts such as tokenization,
stop-word removal, POS tagging, and lemmatization.

---

## 🚀 Features
- Tokenization
- Stopword filtering
- POS-based keyword selection
- Lemmatization
- Frequency-based keyword ranking

---

## 📦 Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

--------------------------------------------------------

▶️ Usage

from spacy_keyword_extractor.extractor import extract_keywords

Replace this text -> 
# text = """Natural Language Processing enables computers to understand
human language efficiently."""

print(extract_keywords(text))

--------------------------------------------------------

🧠 How It Works

- Text is processed using spaCy NLP pipeline

- Stopwords and punctuation are removed

- Nouns, proper nouns, and adjectives are selected

- Words are lemmatized

- Keywords are ranked by frequency

🔮 Future Improvements

- Multi-word keyword extraction

- TF-IDF scoring

- Named Entity keyword support

- REST API using FastAPI


--------------------------------------------------------

## 🌟 Why This Project Is Resume-Worthy

✔ Shows **NLP fundamentals**  
✔ Uses **industry library (spaCy)**  
✔ Clean project structure  
✔ Easy to extend  
✔ Recruiter-friendly README  

This is **not a toy project** — it’s a solid beginner NLP project.

---

## 🚀 Next Power-Up Options

1️⃣ Add **multi-word keywords** (keyphrases)  
2️⃣ Implement **TF-IDF** version  
3️⃣ Compare NLTK vs spaCy outputs  
4️⃣ Publish as **pip package**  
5️⃣ Add **FastAPI endpoint**

👉 Tell me what you want next — we’ll level this up further 💪
