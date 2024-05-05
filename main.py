from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class Items(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/items")
async def create_item(item: Items):
    return {"message": f"{item.name} added successfully", "item": item}

@app.get("/items")
async def get_items():
    return {"item is": "Item_name"}  

@app.get("/items/{item_id}")
async def item_id(item_id: int):
    return {"item_id": item_id}