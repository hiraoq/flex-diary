from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.Models.mongo.User import User
from app.Routers import UserRouter

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.test_db, document_models=[User])


app.include_router(UserRouter.router, prefix="/api/v1")
