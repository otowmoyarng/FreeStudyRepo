from typing import List
from pydantic import BaseModel, Field


class ProgrammerListItem(BaseModel):
    """_summary_
    一覧用プログラマー情報
    Args:
        name:名前
    """
    name: str

    class Config:
        orm_mode = True


class ProgrammerDetail(BaseModel):
    """_summary_
    一覧用プログラマー情報
    Args:
        name:名前
    """
    name: str
    twitter_id: str
    languages: List[str] = Field(
        ..., min_items=1, max_items=3
    )
