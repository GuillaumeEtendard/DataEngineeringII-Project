from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import predict_text, load_model
from pydantic import BaseModel

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

items = {}


class PredictionData(BaseModel):
    text: str


@app.on_event("startup")
async def startup_event():
    model, tokenizer, labels = load_model()
    items["model"] = model
    items["tokenizer"] = tokenizer
    items["labels"] = labels


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/get_sentiment/")
async def prediction(data: PredictionData):
    p = predict_text(items['model'], data.text,
                     items['tokenizer'], items['labels'])
    return {"message": p}
