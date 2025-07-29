from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel


DEV_URL =  "sqlite:///dev.db"

engine = create_engine(DEV_URL)
SQLModel.metadata.create_all(engine)


def create_database_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
