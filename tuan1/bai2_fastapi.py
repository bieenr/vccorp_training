import sys
import os

# Lấy đường dẫn tới thư mục hiện tại của script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Thêm đường dẫn hiện tại vào sys.path
sys.path.append(current_dir)

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from bai1_split_string import add_space_to_string


tags_metadata = [
    {
        "name": "create_item",
        "description": "Returns all instances that can split the string into dictionary words. The algotithm is **backtracking**",
        "externalDocs": {
            "description": "Backtracking algorithm",
            "url": "https://en.wikipedia.org/wiki/Backtracking"
        }

    }
]
app = FastAPI(openapi_tags=tags_metadata)
class Infor_(BaseModel):
    username : str
    old : int

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    infor: Union[Infor_, None] = None

class add_space_to_string_(BaseModel):
    string: str
    wordDict: list

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, item_price: Union[float,None] = None):
    return {"item_name": item.name, "item_id": item_id, "item_price": item_price }

@app.post("/items/", tags= ["create_item"])    
def create_item(item: add_space_to_string_):
    return add_space_to_string(item.string, item.wordDict)