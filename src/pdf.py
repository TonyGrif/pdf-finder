class PDF:
    def __init__(self, b, u) -> None:
        self._bytes = b
        self._finalURI = u
    
    @property
    def bytes(self) -> int:
        return self._bytes
    
    @bytes.setter
    def bytes(self, b) -> None:
        self._bytes = b
        
    @property
    def finalURI(self) -> str:
        return self._finalURI
    
    @finalURI.setter
    def finalURI(self, u) -> None:
        self._finalURI = u  
        
    def __str__(self) -> str:
        print("Final URI:", self.finalURI, "\n")
        print("Content Length:", self.bytes, "\n")
    