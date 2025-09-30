from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from intent.intent_extraction import get_intent
from Chess import *

app = FastAPI()
board = Chess()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    input: str

@app.get("/api/hello")
def root():
    return "yolo"

@app.post("/api/input")
def input(input: Input):
    intent =  get_intent(input.input)

    if intent["intent"] == "make_move":
        fen = board.make_move(intent["move"])
    
    return fen
