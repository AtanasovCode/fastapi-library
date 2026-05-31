from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models.cart import Cart, CartItem
from models.book import Book
from schemas.cart import CartItemCreate


def get_cart_by_user_id(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()


def create_cart(db: Session, user_id: int):
    new_cart = Cart(user_id=user_id)

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


def add_item_to_cart(db: Session, cart_id: int, item_data: CartItemCreate):
    new_item = CartItem(
        cart_id = cart_id,
        **item_data.model_dump()
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    item = db.query(CartItem).filter(
        CartItem.cart_id == cart_id,
        CartItem.id == item_id
    ).first()

    if not item:
        return None

    db.delete(item)
    db.commit()
    return item


def clear_cart(db: Session, cart_id: int):
    db.query(CartItem).filter(
        CartItem.cart_id == cart_id
    ).delete()
    db.commit()



def get_cart_items(db: Session, cart_id: int):
    return db.query(CartItem).filter(
        CartItem.cart_id == cart_id
    ).all()


def buy_items(db: Session, cart_id: int):
    cart_items = get_cart_items(db, cart_id)

    for item in cart_items:
        book = db.query(Book).filter(
            Book.id == item.book_id
        ).first()
        if not book or book.quantity < item.quantity:
            raise ValueError("Insufficient stock for product")
        book.quantity -= item.quantity

    db.query(CartItem).filter(
        CartItem.cart_id == cart_id
    ).delete()

    db.commit()
