from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import predict_text

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictionText(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/get_sentiment/")
async def prediction(text: str):
    p = predict_text(text)
    return {"message": p}
