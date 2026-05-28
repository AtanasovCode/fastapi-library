from pydantic import BaseModel

class AuthorSchema(BaseModel):
    id: int
    name: str

class AuthorCreate(BaseModel):
    name: str
