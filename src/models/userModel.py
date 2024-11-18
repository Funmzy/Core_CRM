from typing import Optional
from datetime import datetime


from pydantic import BaseModel, EmailStr, Field

from beanie import Document


# Input/Output Validation with BaseModel
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  # Will not be returned in the response

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
   


class UserLogin(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    username: str
    email: str
    access_token: str
    token_type: str


class User(Document):
    username:str = Field(..., min_length=3, max_length=50)
    email:EmailStr
    password:str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


    class Settings:
        name = "User"