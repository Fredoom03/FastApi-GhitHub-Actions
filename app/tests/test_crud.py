from app import crud 
from app.models.user import UserCreate


def test_get_users(session_db, setup_and_teardown):
    users_list = crud.get_users(session=session_db)
    
    assert users_list is not None


def test_get_user_by_id(session_db, setup_and_teardown):
    user_in = UserCreate(name="Fredy", age=25)
    crud.create_user(session=session_db, user_create=user_in)
    
    
    user = crud.get_user_by_id(session=session_db, id=1)
    
    assert user is not None
    assert user.id == 1
    assert user.name == "Fredy"
    assert user.age == 25
    
    
def test_create_user(session_db, setup_and_teardown):
    user_in = UserCreate(name="Anneth", age=26)
    user = crud.create_user(session=session_db, user_create=user_in)
    
    assert user is not None
    assert user.id is not None 
    assert user.name == "Anneth"
    assert user.age == 26


def test_update_user(session_db, setup_and_teardown):
    user_create_in = UserCreate(name="Anneth", age=26)
    user_in = crud.create_user(session=session_db, user_create=user_create_in)
    
    user_update_in = user_in.model_copy(update={"age": 27})
    user_updated = crud.update_user(session=session_db, user_update=user_update_in)
    
    assert user_updated.age == 27
