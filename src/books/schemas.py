from datetime import datetime, date
from sqlmodel import SQLModel
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    price: int
    created_at: datetime


class UpdateBook(BaseModel):
    description: str
    price: int


class CreateBook(BaseModel):
    title: str
    author: str
    description: str
    price: int