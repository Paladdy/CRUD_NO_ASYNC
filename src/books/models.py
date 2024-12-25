from sqlmodel import SQLModel, Field, Column
from pydantic import BaseModel
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, date

class Book(SQLModel, table=True):
    __tablename__ = "All_books"
    id: int = Field(default=None, primary_key=True)
    title: str
    author: str
    description: str
    price: int

    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Book {self.title}>"
