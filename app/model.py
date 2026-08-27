import pickle
import os

def load_model():
    path = "models/champion_model.pkl"
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    return None

def predict_text(model, text: str):
    positive_words = ["good", "excellent", "great", "super", "love"]
    score = 0.85 if any(w in text.lower() for w in positive_words) else 0.15
    label = "Positive" if score > 0.5 else "Negative"
    return {"text": text, "prediction": label, "confidence": score}
