import os
from beanie import init_beanie
from fastapi import Depends, FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from logging import info

from models.userModel import User 
from models.contactModel import Contact

from dotenv import load_dotenv

load_dotenv()


CONNECTION_STRING = os.getenv('MONGODB_URL')
DB_NAME = os.getenv('DB_NAME')



@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    # Create a MongoDB client
    app.mongodb_client = AsyncIOMotorClient(CONNECTION_STRING)
    db_name = DB_NAME
    app.database =  app.mongodb_client[db_name]
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")
        print("Connected to database cluster.")

    
    # Initialize Beanie with the database and document models
    await init_beanie(database=app.database, document_models=[User, Contact])

    
    yield
    # Shutdown
    app.mongodb_client.close()




async def get_database():
    client = AsyncIOMotorClient(CONNECTION_STRING)
    db_name = DB_NAME
    db =  client[db_name]
    # db = client.get_default_database()
    return db