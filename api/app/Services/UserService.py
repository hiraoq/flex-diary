from app.Models.mongo.User import User
from app.Repositories.IUserRepository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def get_user_by_email(self, email: str) -> User:
        return await self.user_repository.get_user_by_email(email)

    async def create_user(self, user_data: dict) -> User:
        return await self.user_repository.create_user(user_data)
