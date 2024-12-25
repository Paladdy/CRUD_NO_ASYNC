from sqlmodel import SQLModel
from src.config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True
)

def db_init():
    with engine.connect() as connection:
        SQLModel.metadata.create_all(connection)

def get_session():

    session = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False
    )

    with session() as session:
        yield session

