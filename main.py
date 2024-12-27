from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
     name : str
     desctiption:str
     price:float



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item(item_id):
     return {"item_id": item_id}

@app.post("/create_item")
async def create_item(item:Item):
     return item

     
