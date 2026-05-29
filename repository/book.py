from sqlalchemy.orm import Session
from models.book import Book


def list_all(db: Session):
    return db.query(Book).all()