from fastapi import FastAPI

from typing import Optional

app = FastAPI()


@app.get("/")
def read_root(): # rootで待つ
    return {"Hello": "World"}


@app.get("/items/{item_id}") # パスパラメータの設定
def read_item(item_id: int, q: Optional[str] = None): # qはクエリパラメータ. qである必要はない
    return {"item_id": item_id, "q": q}