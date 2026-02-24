import pytest
from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)

def test_creator():
    login_creator = LoginCreator(MockUserRepository()) # type: ignore
    response = login_creator.create(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["authentication"] is not None

def test_creator_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository()) # type: ignore

    with pytest.raises(Exception):
        login_creator.create(username, "AsenhaErrada")
