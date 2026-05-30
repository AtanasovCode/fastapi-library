from pydantic import BaseModel
from typing import Optional
from schemas.cart import CartResponse

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    cart: Optional[CartResponse] = None

    class Config:
        from_attributes = True
