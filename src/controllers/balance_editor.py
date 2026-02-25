from typing import Dict
from src.models.interface.user_repository import UserRepositoryInterface
from .interfaces.balance_editor import BalanceEditorInterface

class BalanceEditor(BalanceEditorInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
    
    def edit(self, user_id: int, new_balance: float) -> Dict:
        self.__validate_balance(new_balance)
        self.__update_balance(user_id, new_balance)
        return self.__format_response(user_id, new_balance)

    def __validate_balance(self, new_balance: float) -> None:
        if new_balance < 0:
            raise Exception("O saldo não pode ser negativo")
    
    def __update_balance(self, user_id: int, new_balance: float) -> None:
        self.__user_repository.edit_balance(user_id, new_balance)
    
    def __format_response(self, user_id: int, new_balance: float) -> Dict:
        return {
            "type": "User",
            "count": 1,
            "attributes": {
                "user_id": user_id,
                "new_balance": new_balance
            }
        }
