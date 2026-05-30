from sqlalchemy.orm import Session
from repository import cart as carts
from schemas.cart import CartCreate, CartItemCreate


def create(db: Session, cart_create: CartCreate):
    return carts.create(db, cart_create)


def add_item_to_cart(db: Session, item_data: CartItemCreate, user_id: int):
    return carts.add_item_to_cart(db, item_data, user_id)


def get_cart_by_user_id(db: Session, user_id: int):
    return carts.get_cart_by_user_id(db, user_id)