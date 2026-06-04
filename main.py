from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from database.database import get_db
from database.database import engine, Base
from database.seed import seed
from models.cart import Cart
from models.user import User
import models

# Routers
from web.book_router import router as book_api_router
from web.category_router import router as category_api_router
from web.user_router import router as user_api_router
from web.cart_router import router as cart_api_router



Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    seed()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_api_router)
app.include_router(category_api_router)
app.include_router(user_api_router)
app.include_router(cart_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/debug/db")
async def debug(db: Session = Depends(get_db)):
    return {
        "users": db.query(User).all(),
        "carts": db.query(Cart).all()
    }