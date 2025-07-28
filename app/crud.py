from app.deps import SessionDep
from app.models.user import (
    Message,
    UserPublic,
    User,
    UserCreate,
    UserUpdate,
)

from sqlmodel import select


def get_users(session: SessionDep) -> UserPublic:
    select_stmt = select(User)

    user_list = session.exec(select_stmt).all()

    return UserPublic(count=len(user_list), data=user_list)


def get_user_by_id(session: SessionDep, id: int) -> User:
    user = session.get(User, id)
    return user


def create_user(session: SessionDep, user_create: UserCreate) -> User:
    db_obj = User.model_validate(user_create)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    return db_obj


def update_user(session: SessionDep, user_update: UserUpdate) -> User:
    db_user = get_user_by_id(session=session, id=user_update.id)
    db_user.sqlmodel_update(user_update)

    session.commit()
    session.refresh(db_user)

    return db_user


def delete_user(session: SessionDep, user_delete: int) -> User | Message:
    db_user = get_user_by_id(session=session, id=user_delete)

    if not db_user:
        return Message(message="User not found.")

    session.delete(db_user)
    session.commit()

    return db_user
