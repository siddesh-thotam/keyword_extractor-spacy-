import spacy 

from collections import Counter

nlp = spacy.load("en_core_web_md")

def extract_keywords(text , top_n=5):
    doc = nlp(text)

    keywords =[
        token.lemma_.lower()
        for token in doc
        if token.is_alpha
        and not token.is_stop
        and token.pos_ in("NOUN" , "PROPN" , "ADJ")
    ]

    freq = Counter(keywords)
    return freq.most_common(top_n)
