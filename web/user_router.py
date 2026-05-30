from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.user import UserCreate, UserResponse
from service import user as users


router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
async def list_all(db: Session = Depends(get_db)):
    return users.list_all(db)


@router.post("/", response_model=UserResponse)
async def create(user_create: UserCreate, db: Session = Depends(get_db)):
    return users.save(db, user_create)