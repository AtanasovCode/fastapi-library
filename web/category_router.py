from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import category as categories
from schemas.category import CategorySchema


router = APIRouter(prefix="/api/categories", tags=["categories"])


@router.get("/", response_model=list[CategorySchema])
async def list_all(db: Session = Depends(get_db)):
    return categories.list_all(db)