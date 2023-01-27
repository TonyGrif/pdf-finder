class PDF:
    def __init__(self, b) -> None:
        self._bytes = b
    
    @property
    def bytes(self) -> int:
        return self._bytes
    
    @bytes.setter
    def bytes(self, b) -> None:
        self._bytes = b