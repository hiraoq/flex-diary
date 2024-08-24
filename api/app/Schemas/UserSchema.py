from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(...)


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=50)
    email: EmailStr | None = Field(None)


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr

    model_config = {
        "from_attributes": True,
    }
