from typing import Optional
from datetime import datetime


from pydantic import BaseModel, Field, EmailStr

from beanie import Document, Indexed, Link, init_beanie

from models.userModel import User


class ContactCreate(BaseModel):
    username: str
    email: EmailStr
    phone: str
    address: str 
    company:str
    notes:str



class ContactUpdate(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    phone: Optional[str]=None
    address: Optional[str]=None 
    company:Optional[str]=None
    notes:Optional[str]=None


class Contact(Document):
    
    username:str = Field(..., min_length=3, max_length=50)
    email:EmailStr
    phone: str
    address: str
    company:str
    notes:str
    user: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "Contact"