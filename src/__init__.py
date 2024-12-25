from fastapi import FastAPI
from src.books.routes import book_router
from src.db.main import db_init


def life_span(app: FastAPI):
    print("Сервер запущен")
    yield
    print("Сервер выключен")

version = "v1"
app = FastAPI(
    title="Books_API_SYNC",
    description="Books API Sync",
    version=version,
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])