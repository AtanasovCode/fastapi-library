import hashlib
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate



def list_all(db: Session):
    return db.query(User).all()


def save(db: Session, user_create: UserCreate):
    user_data = user_create.model_dump()

    raw_password = user_data.pop("password")
    hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
    user_data["hashed_password"] = hashed_password

    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user