from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import author as authors
from schemas.author import AuthorSchema

router = APIRouter(prefix="/api/authors", tags=["authors"])

@router.get("/", response_model=list[AuthorSchema])
async def list_all(db: Session = Depends(get_db)):
    return authors.list_all(db)