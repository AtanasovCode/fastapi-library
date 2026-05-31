from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from database.database import get_db
from service import cart as carts
from schemas.cart import CartSchema, CartItemCreate, CartItemScheme
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



@router.post("/{cart_id}/add-item", response_model=CartItemScheme)
async def add_item_to_cart(cart_id: int, item_data: CartItemCreate, db: Session = Depends(get_db)):
    cart_exists = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_exists:
        return JSONResponse(status_code=404, content={"message": f"cart with id {cart_id} does not exist"})

    return carts.add_item_to_cart(db, cart_id, item_data)


@router.delete("/{cart_id}/item/{item_id}")
async def remove_item(cart_id: int, item_id: int, db: Session = Depends(get_db)):
    item = carts.remove_item_from_cart(db, cart_id, item_id)

    if not item:
        return JSONResponse(status_code=404, content={"message": f"item {item_id} does not exist in cart {cart_id}"})

    return {"message": f"cart item {cart_id} removed from cart {cart_id}"}


@router.delete("/{cart_id}/clear")
async def clear_cart(cart_id: int, db: Session = Depends(get_db)):
    cart_exists = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_exists:
        return JSONResponse(status_code=404, content={"message": f"cart with id {cart_id} does not exist"})

    carts.clear_cart(db, cart_id)
    return JSONResponse(status_code=200, content={"message": f"cart {cart_id} has been cleared"})


@router.post("/{cart_id}/checkout")
async def buy_items(cart_id: int, db: Session = Depends(get_db)):
    cart_exists = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_exists:
        return JSONResponse(status_code=404, content={"message": f"cart with id {cart_id} does not exist"})

    try:
        carts.buy_items(db, cart_id)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})


    return {"message": f"items from cart {cart_id} have been purchased"}


