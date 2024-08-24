from fastapi import APIRouter, Depends, HTTPException

from app.Dependency import get_user_service
from app.Models.mongo.User import User
from app.Services.UserService import UserService

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_user(
    user_data: User,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.create_user(user_data.dict())
    return user


@router.get("/users/{email}", response_model=User)
async def get_user_by_email(
    email: str,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
