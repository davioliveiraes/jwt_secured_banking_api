import pytest
from .balance_editor import BalanceEditor

class MockUserRepository:
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass

def test_edit_balance():
    balance_editor = BalanceEditor(MockUserRepository()) # type: ignore
    response = balance_editor.edit(1, 100.0)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["attributes"]["user_id"] == 1
    assert response["attributes"]["new_balance"] == 100.0
    
def test_edit_balance_with_negative_value():
    balance_editor = BalanceEditor(MockUserRepository()) # type: ignore

    with pytest.raises(Exception):
        balance_editor.edit(1, -50.0)
