from pydantic import BaseModel

class AuthorSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes=True

class AuthorCreate(BaseModel):
    name: str
