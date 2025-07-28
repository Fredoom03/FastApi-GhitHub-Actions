from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

engine = create_engine("sqlite:///person.db")
SQLModel.metadata.create_all(engine)


def create_database_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
