from sqlalchemy.orm import Session
from models.author import Author


def list_all(db: Session):
    return db.query(Author).all()