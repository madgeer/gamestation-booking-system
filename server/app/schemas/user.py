from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.user import UserRole

# Base Schema
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Optional[UserRole] = UserRole.CUSTOMER

# Schema untuk INPUT
class UserCreate(UserBase):
    password: str

# Schema untuk Output
class UserResponse(UserBase):
    id: int
    created_at: datetime
    avatar_url: Optional[str] = None

    class Config:
        from_atrributes = True

