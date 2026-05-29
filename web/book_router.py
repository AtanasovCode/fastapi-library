from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import book as books
from schemas.book import BookSchema, BookCreate, BookUpdate


router = APIRouter(prefix="/api/books", tags=["books"])


@router.get("/", response_model=list[BookSchema])
async def list_all(db: Session = Depends(get_db)):
    return books.list_all(db)


@router.get("/{book_id}", response_model=BookSchema)
async def find_by_id(book_id: int, db: Session = Depends(get_db)):
    return books.find_by_id(db, book_id)


@router.post("/create", response_model=BookSchema)
async def save(book_create: BookCreate, db: Session = Depends(get_db)):
    return books.save(db, book_create)


@router.put("/update/book/{book_id}", response_model=BookSchema)
async def update(book_update: BookUpdate, book_id: int, db: Session = Depends(get_db)):
    return books.update(db, book_update, book_id)


@router.delete("/delete/{book_id}", response_model=BookSchema)
async def delete(book_id: int, db: Session = Depends(get_db)):
    return books.delete(db, book_id)