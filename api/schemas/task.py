from typing import Optional

from pydantic import BaseModel, Field # Fieldは付加情報を与える時に使う


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="机の掃除をする") # 最初の引数はデフォルト値を表す。 exampleはフィールドの値の例


class Task(TaskBase): # FastAPIのスキーマモデルであることを表す
    id: int
    done: bool = Field(False, description="完了フラグ") # descriptionは説明

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass