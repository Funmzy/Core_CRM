from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from models.contactModel import Contact, ContactCreate, ContactUpdate
from dependencies import UserInDB, get_current_user


router = APIRouter()


@router.post('/')
async def create_contact(contact:ContactCreate,user: Annotated[UserInDB, Depends(get_current_user)]):
    
    new_contact= Contact(
        username=contact.username, email=contact.email, phone=contact.phone, address=contact.address, company=contact.company,
        user=user.id, notes=contact.notes)
    await new_contact.create()
    return {
        "message":"Contacted Created Success",
        "data":new_contact
        }



@router.get("/get_all")
async def get_all_contacts(user:Annotated[UserInDB, Depends(get_current_user)]):
    print('Get all contacts')
    contacts= await Contact.find().to_list()
    return {
        "message":"Contact Lists",
        "data":contacts
        }


@router.patch("/update/{contact_id}", response_model=Contact)
async def update_contact(contact_id:str, contacts:ContactUpdate, user:Annotated[UserInDB, Depends(get_current_user)]):
    print('Get all contacts')
    contact = await Contact.get(contact_id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    update_data = contacts.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    # Save the updated document
    await user.save()
    return user

    return {
        "message":"Contact Lists",
        "data":stored_item_model
        }