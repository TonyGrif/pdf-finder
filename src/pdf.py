class PdfFile:
    """PDF object responsible for storing the starting & final URLs and the number of bytes the PDF is.
    
        ...
        Attributes
        ----------
        bytes : int
            Number of bytes the document is.
        startURL : str
            The starting URL for this document.
        finalURI : str
            The final URI for this document post any redirects.    
    """
    
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
    