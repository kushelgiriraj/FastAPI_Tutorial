from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool | None = False
    tax: int | None = None

items_db = [{"fruit": "banana", "veggie": "carrot", "meat": "chicken"}]

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item is:", item_id}
    if q: 
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a test description"})
    return item

@app.post("/items")
async def create_item(item: Item):
    return {"message": f"{item.name} added successfully", "item": item}

@app.get("/serach_items")
async def search_items(q: str 
                       | None = Query(
                            None, 
                            min_length = 2, 
                            max_length = 10,
                            alias = "item_query")):
       return {"item_query": q}


