from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter() # APIRouterを使ってパスをまとめる
# リソースごとにファイスを分けることでファイルが肥大化しても見通しが確保しやすくなる


@router.get("/tasks", response_model=List[task_schema.Task]) # レスポンススキーマをセット。複数返すためリスト
async def list_tasks():
    return [task_schema.Task(id=1, title="No1. task")] # ひとまずダミーデータを返す

@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass