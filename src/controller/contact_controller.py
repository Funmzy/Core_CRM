from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder


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



@router.get("/")
async def get_all_contacts(user:Annotated[UserInDB, Depends(get_current_user)]):
    print('Get all contacts')
    contacts= await Contact.find().to_list()
    return {
        "message":"Contact Lists",
        "data":contacts
        }


@router.patch("/{contact_id}", response_model=Contact)
async def update_contact(contact_id:str, contacts:ContactUpdate, user:Annotated[UserInDB, Depends(get_current_user)]):

    contact = await Contact.get(contact_id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    
    update_data = contacts.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(contact, key, value)

    # Save the updated document
    await contact.save()
    return contact



@router.delete("/{contact_id}")
async def delete_contact(contact_id:str, user:Annotated[UserInDB, Depends(get_current_user)]):
    contact = Contact.find(Contact.id == contact_id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    await contact.delete()

    return {f"message: Contact Deleted Successfully"}