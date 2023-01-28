class PdfFile:
    def __init__(self, b, s, u) -> None:
        self._bytes = b
        self._startURL = s
        self._finalURI = u
    
    @property
    def bytes(self) -> int:
        return self._bytes
    
    @bytes.setter
    def bytes(self, b) -> None:
        self._bytes = b
        
    @property
    def startURL(self) -> str:
        return self._startURL
    
    @startURL.setter
    def startURL(self, s) -> None:
        self._startURL = s
        
    @property
    def finalURI(self) -> str:
        return self._finalURI
    
    @finalURI.setter
    def finalURI(self, u) -> None:
        self._finalURI = u  
        
    def __str__(self) -> str:
        return "URI: " + str(self.startURL) + "\n" + "Final URI: " + str(self.finalURI) + "\n" + "Content Length: " + str(self.bytes) + " Bytes" + "\n"
    