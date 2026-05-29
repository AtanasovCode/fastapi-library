from sqlalchemy.orm import Session
from repository import book as books
from schemas.book import BookCreate, BookUpdate


def list_all(db: Session):
    return books.list_all(db)


def find_by_id(db: Session, book_id: int):
    return books.find_by_id(db, book_id)

def save(db: Session, book_create: BookCreate):
    return books.save(db, book_create)


def update(db: Session, book_update: BookUpdate, book_id: int):
    return books.update(db, book_update, book_id)


def delete(db: Session, book_id: int):
    return books.delete(db, book_id)