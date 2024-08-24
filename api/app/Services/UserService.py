from app.Models.Mongo.User import User
from app.Repositories.IUserRepository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    async def get_user_by_email(self, email: str) -> User | None:
        return await self.user_repository.get_user_by_email(email)

    async def create_user(self, user_data: dict) -> User:
        return await self.user_repository.create_user(user_data)

    async def update_user(self, email: str, user_data: dict) -> User | None:
        return await self.user_repository.update_user(email, user_data)

    async def delete_user(self, email: str) -> User | None:
        return await self.user_repository.delete_user(email)
