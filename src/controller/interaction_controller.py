from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder


from models.contactModel import Contact, ContactCreate, ContactUpdate
from dependencies import UserInDB, get_current_user
from models.interactionModel import Interaction, InteractionValidation


router = APIRouter()


@router.post('/')
async def create_interaction(log:InteractionValidation,user: Annotated[UserInDB, Depends(get_current_user)]):
    
    new_log= Interaction( note=log.note, date=log.date, log_type=log.log_type, contact=log.contact, user=user.id)
    
    await new_log.create()
    return {
        "message":"Logs Created Successfully",
        "data":new_log
        }
