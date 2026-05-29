from sqlalchemy.orm import Session
from repository import category as categories

def list_all(db: Session):
    return categories.list_all(db)