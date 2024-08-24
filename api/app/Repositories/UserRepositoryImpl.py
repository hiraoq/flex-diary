from typing import Optional

from app.Models.Mongo.User import User
from app.Repositories.IUserRepository import IUserRepository


class UserRepositoryImpl(IUserRepository):
    async def get_user_by_email(self, email: str) -> User | None:
        return await User.find_one(User.email == email)

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        await user.insert()
        return user

    async def update_user(self, email: str, user_data: dict) -> User | None:
        user = await self.get_user_by_email(email)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            await user.save()
        return user

    async def delete_user(self, email: str) -> User | None:
        user = await self.get_user_by_email(email)
        if user:
            await user.delete()
        return user
