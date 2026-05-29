from sqlalchemy.orm import Session
from models.category import Category

def list_all(db: Session):
    return db.query(Category).all()
