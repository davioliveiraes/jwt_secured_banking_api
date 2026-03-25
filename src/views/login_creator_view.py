from typing import Any
from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse
from .interfaces.view_interface import ViewInterface
from src.errors.types.http_bad_request import HttpBadRequestError

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpReponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")
        self.__validate_inputs(username, password)

        response = self.__controller.create(username, password) # type: ignore
        return HttpReponse(body={ "data": response }, status_code=200)
    
    def __validate_inputs(self, username: Any, password: Any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise HttpBadRequestError("Invalid Input")
