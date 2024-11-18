from typing import Optional
from datetime import datetime
from enum import Enum

from contactModel import Contact


from pydantic import Field

from beanie import Document, Indexed, Link

class Type(str, Enum):
    call = 'call'
    email = 'email'
    meeting ='meeting'


class Interaction(Document):
    Contact:Link[Contact]
    note:str
    date:datetime
    type:Type
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "Interaction"