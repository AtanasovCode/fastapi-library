from pydantic import BaseModel, EmailStr
from typing import Optional
from schemas.cart import CartResponse


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    cart: Optional[CartResponse] = None

    class Config:
        from_attributes = True
