from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root(): # rootで待つ
    return {"Hello": "World"}


@app.get("/items/{item_id}") # パスパラメータの設定
def read_item(item_id: int, q: Optional[str] = None): # qはクエリパラメータ. qである必要はない
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}