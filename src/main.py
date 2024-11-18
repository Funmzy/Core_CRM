import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
import uvicorn

from controller.auth_controller import router as auth_router
from controller.contact_controller import router as contact_router
from models.dbConfig import db_lifespan
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(lifespan=db_lifespan)

port = int(os.environ.get("PORT", 8000))

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(contact_router, prefix="/contact", tags=["Contact"])



@app.get('/')
def intro():
    return('Welcome to Core CRM')

