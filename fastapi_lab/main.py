from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    quantity: int
    bought: bool

items = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return {"message": "Item updated"}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}