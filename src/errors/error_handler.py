from src.views.http_types.http_response import HttpReponse
from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.http_unauthorized import HttpUnauthorizedError

def handler_errors(error: Exception) -> HttpReponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnauthorizedError)):
        return HttpReponse(
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code=error.status_code
        )
    
    return HttpReponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
