from pydantic import BaseModel
from schemas.book import BookSchema



class CartItemResponse(BaseModel):
    id: int
    book_id: int
    quantity: int
    book: BookSchema

    class Config:
        from_attributes = True

class CartCreate(BaseModel):
    user_id: int

class CartResponse(BaseModel):
    id: int
    user_id: int
    items: list[CartItemResponse] = []

    class Config:
        from_attributes = True