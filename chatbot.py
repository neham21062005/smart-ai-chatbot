import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("intents.json") as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    user_input = user_input.lower()

    # keyword check first (important)
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello!"

    if any(word in user_input for word in ["project", "ai"]):
        return "Try Resume Analyzer, Chatbot, or Prediction models."

    if any(word in user_input for word in ["bye"]):
        return "Goodbye!"

    # fallback NLP
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    score = similarity.max()

    if score < 0.7:
        return "Sorry, I didn't understand that."

    index = similarity.argmax()
    tag = tags[index]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
