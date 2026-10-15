
import json
from fastapi import FastAPI

app = FastAPI()

def load_books():
    with open("books.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to Digital Library"}

@app.get("/books")
def show_books():
    return load_books()
