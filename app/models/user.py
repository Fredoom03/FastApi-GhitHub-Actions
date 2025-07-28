from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int


class UserCreate(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int


class UserUpdate(SQLModel):
    id: int
    name: str
    age: int


class UserDelete(SQLModel):
    id: int


class UserPublic(SQLModel):
    count: int
    data: list[User]


class Message(SQLModel):
    message: str
