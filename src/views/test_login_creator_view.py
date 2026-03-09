import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse
from .login_creator_view import LoginCreatorView

class MockController:
    def create(self, username, password):
        return { "alguma": "coisa" }

def test_handle_login_creator():
    body = {
        "username": "MyUsername",
        "password": "MyPassword"
    }
    request = HttpRequest(body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller) # type: ignore

    response = login_creator_view.handle(request)

    assert isinstance(response, HttpReponse)
    assert response.body == { "data": { "alguma": "coisa" }}
    assert response.status_code == 200

def test_handle_login_creator_with_validation_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)  # type: ignore

    with pytest.raises(Exception):
        login_creator_view.handle(request)
