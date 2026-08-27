from fastapi import FastAPI
from app.schemas import TextInput, PredictionOutput
from app.model import load_model, predict_text

app = FastAPI(title="Real-time ML NLP Text Classification", version="1.0")
model = load_model()

@app.get("/")
def home():
    return {"status": "API is running", "docs": "/docs"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: TextInput):
    result = predict_text(model, data.text)
    return result
