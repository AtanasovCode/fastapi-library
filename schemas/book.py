from pydantic import BaseModel
from typing import Optional
from schemas.category import CategorySchema
from schemas.author import AuthorSchema


class BookSchema(BaseModel):
    id: int
    name: str
    pages: int
    price: float
    quantity: int
    author: AuthorSchema
    category: CategorySchema

    class Config:
        from_attributes=True


class BookCreate(BaseModel):
    title: str
    pages: int
    price: float
    quantity: int
    author_id: int
    category_id: int



class BookUpdate(BaseModel):
    title: Optional[str] = None
    pages: Optional[int] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None
