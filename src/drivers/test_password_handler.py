from .password_handler import PasswordHandler

def test_encrypt_password():
    my_password = "thesenha"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(my_password)

    assert hashed_password

def test_check_password():
    my_password = "senha_senha"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(my_password)
    password_checked = password_handler.check_password(my_password, hashed_password)

    assert password_checked
