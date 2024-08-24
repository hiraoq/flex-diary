from typing import ClassVar

from beanie import Document
from pydantic import EmailStr, Field


class User(Document):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(...)

    class Settings:
        collection = "users"
        indexes: ClassVar[list[str]] = [
            "email",
        ]
