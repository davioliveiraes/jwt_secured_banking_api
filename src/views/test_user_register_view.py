import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return { "alguma": "coisa" }

def test_handle_user_registry():
    body = {
        "username": "MyUsername",
        "password": "MyPassword"
    }
    request = HttpRequest(body)

    mock_controller = MockController()
    user_registry_view = UserRegisterView(mock_controller) # type: ignore

    response = user_registry_view.handle(request)

    assert isinstance(response, HttpReponse)
    assert response.body == { "data": { "alguma": "coisa" }}
    assert response.status_code == 201

def test_handle_user_registry_with_validation_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_registry_view = UserRegisterView(mock_controller) # type: ignore

    with pytest.raises(Exception):
        user_registry_view.handle(request)

