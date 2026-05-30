from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.database import engine, Base
from database.seed import seed
# Routers
from web.book_router import router as book_api_router
from web.category_router import router as category_api_router
from web.user_router import router as user_api_router



Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    seed()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(book_api_router)
app.include_router(category_api_router)
app.include_router(user_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
