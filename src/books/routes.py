from typing import List
from fastapi import FastAPI, APIRouter, Depends, Header
from src.db.main import get_session
from src.books.service import BookService
from sqlmodel import Session
from src.books.schemas import Book, CreateBook, UpdateBook

book_router = APIRouter()

@book_router.get("/")
def check_out():
    return {"Сервер":"Работает"}



@book_router.get("/books", response_model=List[Book])
def get_all_books(session: Session, book_service: BookService = Depends()):
    books = book_service.get_all_books(session)
    return books



