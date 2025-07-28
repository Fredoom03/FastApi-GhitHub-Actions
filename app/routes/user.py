from typing import Union
from fastapi import APIRouter
import app.crud as crud
from app.deps import SessionDep

from app.models.user import Message, User, UserUpdate

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
def get_users(session: SessionDep):
    return crud.get_users(session=session)


@router.get("/{user_id}")
async def get_user_by_id(session: SessionDep, user_id: int) -> User:
    return crud.get_user_by_id(session=session, id=user_id)


@router.post("/")
async def create_user(session: SessionDep, user_in: User):
    return crud.create_user(session=session, user_create=user_in)


@router.put("/")
async def update_user(session: SessionDep, user_in: UserUpdate) -> User:
    return crud.update_user(session=session, user_update=user_in)


@router.delete("/{user_id}", response_model=Union[User, Message])
async def delete_user(session: SessionDep, user_id: int) -> User | Message:
    return crud.delete_user(session=session, user_delete=user_id)
