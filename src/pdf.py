class PdfFile:
    """
    PDF object responsible for storing the starting & final URLs
    and the number of bytes the PDF is.

    Attributes:
        bytes (int): number of bytes the document is.
        start_url (str): starting URL for this document.
        final_uri (str): final URI for this document post any redirects.
    """

    def __init__(self, byte: int, s_url: str, f_uri: str) -> None:
        """
        The constructor for the PDF class.

        Parameters:
            bytest (int): number of bytes.
            s_url (str): starting URL string.
            f_url (str): final URL string.
        """
        self.bytes = byte
        self.start_url = s_url
        self.final_uri = f_uri

    @property
    def bytes(self) -> int:
        """
        Return the number of bytes.

        Returns:
            bytes (int): number of bytes.
        """
        return self._bytes

    @bytes.setter
    def bytes(self, byte: int) -> None:
        """
        Set the number of bytes for this PDF.

        Parameters:
            b (int): the number of bytes.
        """
        self._bytes = byte

    @property
    def start_url(self) -> str:
        """
        Return the starting URL.

        Returns:
            start_url (str): the starting URL.
        """
        return self._start_url

    @start_url.setter
    def start_url(self, s_url: str) -> None:
        """
        Set the starting URL of this PDF.

        Parameters:
            s_url (str): the starting URL.
        """
        self._start_url = s_url

    @property
    def final_uri(self) -> str:
        """
        Return the final URI of this PDF.

        Return:
            final_uri (str): the final URI.
        """
        return self._finalURI

    @final_uri.setter
    def final_uri(self, f_uri: str) -> None:
        """
        Set the final URI.

        Parameters:
            f_uri (str): the final URI.
        """
        self._finalURI = f_uri

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
