import os

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.Models.Mongo.User import User
from app.Routers import UserRouter

app = FastAPI()


@app.on_event("startup")
async def startup_db_client() -> None:
    mongo_url = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(mongo_url)
    await init_beanie(database=client.get_database("test_db"), document_models=[User])


app.include_router(UserRouter.router, prefix="/api/v1")
