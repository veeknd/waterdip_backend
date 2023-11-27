from pydantic import BaseModel
from typing import List
class TaskBase(BaseModel):
    title: str
    is_completed : bool

class Task(TaskBase):
    id:int
    class Config:
        orm_mode=True
