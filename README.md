# ML Text Classification FastAPI

Real-time ML NLP text classification microservice using PyTorch, FastAPI, and Docker.

## Features
- FastAPI endpoint
- PyTorch model loading
- Docker containerized
- Pytest

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload

Open http://localhost:8000/docs

## Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api

## API
GET / -> health
POST /predict -> {"text": "I love this!"}
