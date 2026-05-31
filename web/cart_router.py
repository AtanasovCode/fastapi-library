from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from database.database import get_db
from service import cart as carts
from schemas.cart import CartSchema
from models.user import User
from models.cart import Cart



router = APIRouter(prefix="/api/cart", tags=["cart"])

@router.get("/user/{user_id}", response_model=CartSchema)
async def get_cart_by_user_id(user_id: int, db: Session = Depends(get_db)):
    cart = carts.get_cart_by_user_id(db, user_id)

    if cart:
        return cart
    return JSONResponse(status_code=404, content={"message": f"cart for user {user_id} not found"})


@router.post("/user/{user_id}", response_model=CartSchema)
async def create_cart(user_id: int, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.id == user_id).first()

    if not user_exists:
        return JSONResponse(status_code=404, content={"message": f"user with id {user_id} does not exist"})

    cart_exists = db.query(Cart).filter(Cart.user_id == user_id).first()

    if cart_exists:
        return JSONResponse(status_code=409, content={"message": "user already has a cart"})

    return carts.create_cart(db, user_id)

