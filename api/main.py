from fastapi import FastAPI

from api.routers import task, done


app = FastAPI()

# FastAPIインスタンスに読み込ませる。読み込ませることでドキュメントに現れる
app.include_router(task.router)
app.include_router(done.router)