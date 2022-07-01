class Message:
    def __init__(self, status_code: int, message: str):
        self._status_code = status_code
        self._message = message
    def value(self):
        return {'message': self._message}