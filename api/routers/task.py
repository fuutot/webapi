from fastapi import APIRouter

router = APIRouter() # APIRouterを使ってパスをまとめる
# リソースごとにファイスを分けることでファイルが肥大化しても見通しが確保しやすくなる


@router.get("/tasks")
async def list_tasks():
    pass


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass