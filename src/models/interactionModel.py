from typing import Optional
from datetime import datetime
from enum import Enum

from models.contactModel import Contact


from pydantic import BaseModel, Field

from beanie import Document, Indexed, Link

from models.userModel import User

class Log_Type(str, Enum):
    call = 'call'
    email = 'email'
    meeting ='meeting'


class InteractionValidation(BaseModel):
    note: str
    date: str
    log_type: Log_Type
    contact:str




class Interaction(Document):
    note:str
    date:datetime
    log_type:Log_Type
    contact:Link[Contact]
    user:Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "Interaction"