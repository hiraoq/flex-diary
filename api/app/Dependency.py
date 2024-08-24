from fastapi import Depends

from app.Repositories.UserRepositoryImpl import UserRepositoryImpl
from app.Services.UserService import UserService


def get_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl()


def get_user_service(
    user_repository: UserRepositoryImpl = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository)
