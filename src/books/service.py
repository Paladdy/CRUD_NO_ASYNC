from typing import List
from .schemas import Book, CreateBook, UpdateBook
from sqlmodel import select, desc, Session
from .models import Book

class BookService:
    def get_all_books(self, session: Session) -> List[Book]:
        statement = select(Book).order_by(Book.created_at.desc())
        result = self.session.exec(statement)
        return result.all()






