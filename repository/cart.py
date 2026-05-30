from sqlalchemy.orm import Session
from models.cart import Cart, CartItem
from schemas.cart import CartCreate, CartItemCreate


def create(db: Session, cart_create: CartCreate):
    new_cart = Cart(**cart_create.model_dump())

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


def add_item_to_cart(db: Session, item_data: CartItemCreate, user_id: int):
    # Check if a user has a cart, if not create one
    db_cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not db_cart:
        cart_create = CartCreate(user_id=user_id)
        db_cart = create(db, cart_create)

    # Check to see if that item already exists in the cart
    db_item = db.query(CartItem).filter(
        CartItem.cart_id == db_cart.id,
        CartItem.book_id == item_data.book_id
    ).first()

    # If the item exists, update the quantity
    if db_item:
        db_item.quantity += item_data.quantity
        db.commit()
        db.refresh(db_item)
        return db_item

    # If item does not exist, create it
    new_item = CartItem(
        cart_id=db_cart.id,
        book_id=item_data.book_id,
        quantity=item_data.quantity
    )
    # Add new item to database
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_cart_by_user_id(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()
