from pydantic import BaseModel


class CartBase(BaseModel):
    pass

class CartCreate(BaseModel):
    user_id: int

class CartResponse(BaseModel):
    id: int
    user_id: int

    class Config:
        from_attributes = True