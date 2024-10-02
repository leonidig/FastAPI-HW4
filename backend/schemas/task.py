from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    author: str
    content: str


class CreateTask(BaseModel):
    author: str
    content: str


class ReadTask(BaseModel):
    email: str


class TaskInfo(BaseModel):
    user: str


class TaskDelete(BaseModel):
    task_id: int
    user: str