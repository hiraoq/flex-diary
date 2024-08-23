# api/app/main.py
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://root:example@mongodb:27017")
    app.mongodb = app.mongodb_client["flex-diary"]
    print("Connected to MongoDB!")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Flex Diary API"}

@app.get("/test-mongodb")
async def test_mongodb():
    document = await app.mongodb["test_collection"].find_one()
    if document:
        return {"status": "Connected", "document": document}
    else:
        return {"status": "Connected, but no documents found"}

# Additional API endpoints can be added here
