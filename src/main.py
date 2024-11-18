
from fastapi import FastAPI

from controller.auth_controller import router as auth_router
from controller.contact_controller import router as contact_router
from models.dbConfig import db_lifespan


app = FastAPI(lifespan=db_lifespan)



app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(contact_router, prefix="/contact", tags=["Contact"])



@app.get('/')
def intro():
    return('Welcome to Core CRM')
