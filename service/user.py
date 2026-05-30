from sqlalchemy.orm import Session
from repository import user as users
from schemas.user import UserCreate


def list_all(db: Session):
    return users.list_all(db)


def save(db: Session, user_create: UserCreate):
    return users.save(db, user_create)