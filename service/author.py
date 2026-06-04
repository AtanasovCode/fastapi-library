from sqlalchemy.orm import Session
from repository import author as authors

def list_all(db: Session):
    return authors.list_all(db)