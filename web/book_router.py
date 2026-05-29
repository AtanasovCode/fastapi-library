from fastapi import APIRouter, Depends, HTTPException, status
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
    db_book = books.find_by_id(db, book_id)

    if db_book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )

    return db_book


@router.post("/", response_model=BookSchema)
async def save(book_create: BookCreate, db: Session = Depends(get_db)):
    return books.save(db, book_create)


@router.put("/{book_id}", response_model=BookSchema)
async def update(book_update: BookUpdate, book_id: int, db: Session = Depends(get_db)):
    return books.update(db, book_update, book_id)


@router.delete("/{book_id}", response_model=BookSchema)
async def delete(book_id: int, db: Session = Depends(get_db)):
    return books.delete(db, book_id)