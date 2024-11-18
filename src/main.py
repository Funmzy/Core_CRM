import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI

from controller.auth_controller import router as auth_router
from controller.contact_controller import router as contact_router
from controller.task_controller import router as task_router
from controller.interaction_controller import router as log_router
from models.dbConfig import db_lifespan
from dotenv import load_dotenv
from swagger_config import custom_openapi

load_dotenv()

app = FastAPI(lifespan=db_lifespan)

# Assign the custom OpenAPI schema
app.openapi = lambda: custom_openapi(app)

port = int(os.environ.get("PORT", 8000))

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(contact_router, prefix="/contact", tags=["Contact"])
app.include_router(task_router, prefix="/task", tags=["Task"])
app.include_router(log_router, prefix="/interaction", tags=["Interaction"])



@app.get('/')
def intro():
    return('Welcome to Core CRM')

