import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse
from .balance_editor_view import BalanceEditorView

class MockController:
    def edit(self, user_id, new_balance):
        return { 1: 5000.00 }

def test_handle_balance_editor():
    body = {
        "user_id": 1,
        "new_balance": 5000.00
    }
    request = HttpRequest(body)
    
    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller) # type: ignore

    response = balance_editor_view.handle(request)

    assert isinstance(response, HttpReponse)
    assert response.body == { "data": { 1: 5000.00 }}
    assert response.status_code == 200

def test_handle_balance_editor_with_validation_error():
    body = {
        "new_balance": 5000.00
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller) # type: ignore

    with pytest.raises(Exception):
        balance_editor_view.handle(request)
