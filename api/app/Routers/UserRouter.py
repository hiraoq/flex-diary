from fastapi import APIRouter, Depends, HTTPException

from app.Dependency import get_user_service
from app.Models.Mongo.User import User
from app.Schemas.UserSchema import UserCreate, UserResponse, UserUpdate
from app.Services.UserService import UserService

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_user(
    user_data: User,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    user = await user_service.create_user(user_data.dict())
    return UserResponse.model_validate(user)


@router.get("/users/{email}", response_model=User)
async def get_user_by_email(
    email: str,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    user = await user_service.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@router.put("/users/{email}", response_model=UserResponse)
async def update_user(
    email: str,
    user_data: UserUpdate,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    user = await user_service.update_user(email, user_data.dict(exclude_unset=True))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@router.delete("/users/{email}", response_model=UserResponse)
async def delete_user(
    email: str,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    user = await user_service.delete_user(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)
