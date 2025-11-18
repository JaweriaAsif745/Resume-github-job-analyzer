import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pathlib import Path
from fuzzywuzzy import fuzz

# Ensure NLTK data is present
def ensure_nltk_data():
    resources = [
        ("tokenizers/punkt", "punkt"),
        ("corpora/stopwords", "stopwords"),
        ("corpora/wordnet", "wordnet"),
        ("corpora/omw-1.4", "omw-1.4"),
    ]
    for path, name in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(name)

ensure_nltk_data()

# Path to skills file
SKILL_FILE = Path(__file__).resolve().parents[1] / "assets" / "skills_list.txt"

# Load skills from skill list file
def load_skill_list():
    if not SKILL_FILE.exists():
        return []
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    return skills

skill_list = load_skill_list()

# Preprocessing text
_lemmatizer = WordNetLemmatizer()
_stopwords = set(stopwords.words("english"))

def preprocess(text):
    text = (text or "").lower()
    # allow + # . - (for c++, c#, node.js etc)
    text = re.sub(r"[^a-z0-9+\-#_. ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in _stopwords and len(t) > 1]
    tokens = [_lemmatizer.lemmatize(t) for t in tokens]
    return tokens

# ____build ngrams_____
def build_ngrams(tokens, max_n=3):
    ngrams = []
    L = len(tokens)
    i = 0
    while i < L:
        matched = False
        # try longer ngrams first
        for n in reversed(range(2, max_n+1)):
            if i + n <= L:
                candidate = " ".join(tokens[i:i+n])
                if candidate in skill_list:
                    ngrams.append(candidate)
                    i += n
                    matched = True
                    break
        if not matched:
            ngrams.append(tokens[i])
            i += 1
    return ngrams

def fuzzy_match_candidates(tokens, threshold=85):
    matched = set()
    for token in tokens:
        if len(token) < 3:
            continue
        for skill in skill_list:
            score = fuzz.ratio(token, skill)
            if score >= threshold:
                matched.add(skill)
    return list(matched)

# ______Extract skills from text_________
def extract_skills_from_text(text, use_fuzzy=False, fuzzy_threshold=85):
    tokens = preprocess(text)
    ngrams = build_ngrams(tokens, max_n=3)
    found = [s for s in ngrams if s in skill_list]
    if use_fuzzy:
        fuzzy_found = fuzzy_match_candidates(ngrams, threshold=fuzzy_threshold)
        found.extend(fuzzy_found)
    result = sorted(set(found))
    return result

if __name__ == '__main__':
    txt = "I have experience in Machine Learning, Deep Learning, NLP, and Python. Worked with Docker and AWS."
    print(extract_skills_from_text(txt, use_fuzzy=True))