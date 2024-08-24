from abc import ABC, abstractmethod
from typing import Optional

from app.Models.mongo.User import User


class IUserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    async def create_user(self, user_data: dict) -> User:
        pass
