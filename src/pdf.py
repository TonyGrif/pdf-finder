class PdfFile:
    """
    PDF object responsible for storing the starting & final URLs and the number of bytes the PDF is.

    Attributes:
        bytes (int): Number of bytes the document is.
        startURL (str): The starting URL for this document.
        finalURI (str): The final URI for this document post any redirects.
    """

    def __init__(self, b: int, s: str, u: str) -> None:
        """
        The constructor for the PDF class.

        Parameters:
            b (int): The number of bytes.
            s (str): The starting URL string.
            u (str): The final URL string.
        """
        self._bytes = b
        self._startURL = s
        self._finalURI = u

    @property
    def bytes(self) -> int:
        """
        Get the number of bytes this PDF is.

        Returns:
            bytes (int): The number of bytes.
        """
        return self._bytes

    @bytes.setter
    def bytes(self, b: int) -> None:
        """
        Set the number of bytes this PDF is.

        Parameters:
            b (int): The number of bytes.
        """
        self._bytes = b

    @property
    def startURL(self) -> str:
        """
        Get the starting URL of this PDF.

        Returns:
            startURL (str): The starting URL.
        """
        return self._startURL

    @startURL.setter
    def startURL(self, s: str) -> None:
        """
        Set the starting URL of this PDF.

        Parameters:
            s (str): The starting URL.
        """
        self._startURL = s

    @property
    def finalURI(self) -> str:
        """
        Get the final URI of this PDF.

        Return:
            finalURI (str): The final URI.
        """
        return self._finalURI

    @finalURI.setter
    def finalURI(self, u: str) -> None:
        """
        Set the final URI.

        Parameters:
            u (str): The final URI.
        """
        self._finalURI = u

    def __str__(self) -> str:
        """
        Return a string representation of this PDF.

        Returns:
            string (str): The string representation.
        """
        return (
            "URI: "
            + str(self.startURL)
            + "\n"
            + "Final URI: "
            + str(self.finalURI)
            + "\n"
            + "Content Length: "
            + str(self.bytes)
            + " Bytes"
            + "\n"
        )
