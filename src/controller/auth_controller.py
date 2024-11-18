from datetime import datetime, timedelta, timezone

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from dependencies import ACCESS_TOKEN_EXPIRE_MINUTES, Token, authenticate_user, create_access_token, get_current_user, get_password_hash
from models.userModel import User, UserCreate, UserLoginResponse, UserResponse


router= APIRouter()

@router.post("/signup")
async def signup(user:UserCreate ):
    hashed_password= get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    await new_user.create()
    return UserResponse(
        id=str(new_user.id),
        username=new_user.username,
        email=new_user.email
    )



@router.post("/login")
async def signin(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> UserLoginResponse:
    user = await authenticate_user(User, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return UserLoginResponse(username=user.username, email=user.email, access_token=access_token, token_type="bearer")




