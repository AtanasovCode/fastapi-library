from pydantic import BaseModel
from schemas.user import UserResponse

class CartItemScheme(BaseModel):
    id: int
    book_id: int
    quantity: int

    class Config:
        from_attributes=True


class CartItemCreate(BaseModel):
    book_id: int
    quantity: int


class CartSchema(BaseModel):
    id: int
    user: UserResponse
    items: list[CartItemScheme] = []

    class Config:
        from_attributes = True


class CartCreate(BaseModel):
    user_id: int