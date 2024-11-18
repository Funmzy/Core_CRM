from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder


from models.contactModel import Contact, ContactCreate, ContactUpdate
from dependencies import UserInDB, get_current_user


router = APIRouter()


@router.post('/')
async def create_interaction(contact:ContactCreate,user: Annotated[UserInDB, Depends(get_current_user)]):
    
    new_contact= Contact(
        username=contact.username, email=contact.email, phone=contact.phone, address=contact.address, company=contact.company,
        user=user.id, notes=contact.notes)
    await new_contact.create()
    return {
        "message":"Contacted Created Success",
        "data":new_contact
        }