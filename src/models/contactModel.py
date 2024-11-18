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
    username: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str] 
    company:Optional[str]
    notes:Optional[str]


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