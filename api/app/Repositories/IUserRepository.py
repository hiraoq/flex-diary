from abc import ABC, abstractmethod
from typing import Optional

from app.Models.Mongo.User import User


class IUserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    async def create_user(self, user_data: dict) -> User:
        pass

    @abstractmethod
    async def update_user(self, email: str, user_data: dict) -> User | None:
        pass

    @abstractmethod
    async def delete_user(self, email: str) -> User | None:
        pass
