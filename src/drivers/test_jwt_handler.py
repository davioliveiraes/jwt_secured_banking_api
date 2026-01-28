from .jwt_handler import JwtHandler

def test_create_jwt_token():
    jwt_handler = JwtHandler()
    body = {
        "username": "olaMundo",
        "aqui": "estou aqui",
        "lalala": "" 
    }

    token = jwt_handler.create_jwt_token(body)

    assert token is not None
    assert isinstance(token, str)

def test_decode_jwt_token():
    jwt_handler = JwtHandler()

    body = {
        "username": "teste2",
        "estou": "aqui estou",
        "rsrsrsrs": ""
    }

    token = jwt_handler.create_jwt_token(body)
    token_informations = jwt_handler.decode_jwt_token(token)

    assert token_informations["username"] == body["username"]
    assert token_informations["rsrsrsrs"] == body["rsrsrsrs"]
