from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import cart as carts
from schemas.cart import CartResponse, CartItemCreate



router = APIRouter(prefix="/api/user/{user_id}/cart", tags=["cart"])

@router.get("/", response_model=CartResponse)
async def get_cart_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return carts.get_cart_by_user_id(db, user_id)


@router.post("/", response_model=CartResponse)
async def add_item_to_cart(item_create: CartItemCreate, user_id: int, db: Session = Depends(get_db)):
    carts.add_item_to_cart(db, item_create, user_id)

    return carts.get_cart_by_user_id(db, user_id)