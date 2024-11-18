from typing import Optional
from datetime import datetime
from enum import Enum


from pydantic import BaseModel, Field

from beanie import Document, Link

from models.contactModel import Contact
from models.userModel import User

class Priority(str, Enum):
    high = 'high'
    medium = 'medium'
    low ='low'

class Task_Status(str, Enum):
    to_do='to_do'
    in_progress = 'in_progress'
    done = 'done'



# Input Validation for Task
class Task_Validation(BaseModel):
    title : str
    description: str
    due_date: str
    priority: Priority
    task_status: Task_Status
    contact_id:str


class TaskUpdate(BaseModel):
    title : Optional[str]= None
    description: Optional[str]= None
    due_date: Optional[str]= None
    priority: Optional[Priority]= None
    task_status: Optional[Task_Status]= None
    contact_id:Optional[str]= None



class Task(Document):
    title:str = Field(..., min_length=3, max_length=50)
    description:str
    due_date:datetime
    priority:Priority
    task_status:Task_Status
    user: Link[User]
    contact_id:Link[Contact]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "Task"