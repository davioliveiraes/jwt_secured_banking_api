from typing import Dict

class HttpRequest():
    def __init__(self, 
                body: Dict = None, # type: ignore
                headers: Dict = None, # type: ignore
                params: Dict = None, # type: ignore
                tokens_infos: Dict = None # type: ignore
            ) -> None:
            self.body = body,
            self.headers = headers,
            self.params = params,
            self.tokens_infos = tokens_infos

