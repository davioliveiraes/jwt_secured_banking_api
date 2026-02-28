from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse

class ViewInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpReponse:
        pass
