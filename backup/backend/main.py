import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
from abstraction import get_all_json_from_path





class Character(BaseModel):
    _id: int
    name: str
    nick: str
    gender: str
    age: int
    desc: str
    image: str
    actions: int
    attributes: dict
    potencial: dict
    resistances: dict
    attacks: List[int]
    lines: dict


class Characters(BaseModel):
    characters: List[Character]


app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = json.load(open('config/config.json'))
path_character = config['characters_path']
chara_data: list[dict] = get_all_json_from_path(path_character,'characters')


memory_db = {"characters": chara_data}

@app.get("/characters")
def get_characters():
    return memory_db

@app.post("/fruits", response_model=Character)
def add_fruit(fruit: Character):
    print(fruit)
    memory_db["characters"].append(fruit)
    return fruit


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




