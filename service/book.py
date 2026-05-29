from sqlalchemy.orm import Session
from repository import book as books


def list_all(db: Session):
    return books.list_all(db)