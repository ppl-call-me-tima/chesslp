from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from intent.intent_extraction import get_intent

app = FastAPI()

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
    print(f"input request received at api: {input.input}")
    return get_intent(input.input)
