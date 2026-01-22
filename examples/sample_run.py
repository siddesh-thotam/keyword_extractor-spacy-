from spacy_keyword_extractor.extractor import extract_keywords

text = """Natural Language Processing helps computers understand
human languages and computer systems efficiently."""

print(extract_keywords(text))
