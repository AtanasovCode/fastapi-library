from sqlalchemy.orm import Session
from repository import cart as carts
from schemas.cart import CartCreate, CartItemCreate


def get_cart_by_user_id(db: Session, user_id: int):
    return carts.get_cart_by_user_id(db, user_id)


def create_cart(db: Session, user_id: int):
    return carts.create_cart(db, user_id)


def add_item_to_cart(db: Session, cart_id: int, item_data: CartItemCreate):
    return carts.add_item_to_cart(db, cart_id, item_data)


def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    return carts.remove_item_from_cart(db, cart_id, item_id)


def clear_cart(db: Session, cart_id: int):
    return carts.clear_cart(db, cart_id)


def get_cart_items(db: Session, cart_id: int):
    return carts.get_cart_items(db, cart_id)


def buy_items(db: Session, cart_id: int):
    return carts.buy_items(db, cart_id)

