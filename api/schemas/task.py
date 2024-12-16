from typing import Optional

from pydantic import BaseModel, Field # Fieldは付加情報を与える時に使う


class Task(BaseModel): # FastAPIのスキーマモデルであることを表す
    id: int
    title: Optional[str] = Field(None, example="机の掃除をする") # 最初の引数はデフォルト値を表す。 exampleはフィールドの値の例
    done: bool = Field(False, description="完了フラグ") # descriptionは説明