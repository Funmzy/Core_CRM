from typing import Optional
from datetime import datetime
from enum import Enum


from pydantic import BaseModel, Field

from beanie import Document

class Priority(str, Enum):
    high = 'high'
    medium = 'medium'
    low ='low'


# Input Validation for Task
class Task_Validation(BaseModel):
    title : str
    description: str
    due_date: str
    priority: Priority




class Task(Document):
    title:str = Field(..., min_length=3, max_length=50)
    description:str
    due_date:datetime
    priority:Priority
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "Task"