from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import book as books
from schemas.book import BookSchema


router = APIRouter(prefix="/api/books", tags=["books"])


@router.get("/", response_model=list[BookSchema])
async def list_all(db: Session = Depends(get_db)):
    return books.list_all(db)