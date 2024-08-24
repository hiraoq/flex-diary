from beanie import Document
from pydantic import Field


class User(Document):
    name: str = Field(...)
    email: str = Field(...)

    class Settings:
        collection = "users"  # mongoDB内のコレクション名
