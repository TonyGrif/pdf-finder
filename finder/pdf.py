"""This module contains the PDF data class."""

from dataclasses import dataclass


@dataclass
class PdfFile:
    """
    PDF object responsible for storing the starting & final URLs
    and the number of bytes the PDF is.

    Attributes:
        bytes (int): number of bytes the document is.
        start_url (str): starting URL for this document.
        final_uri (str): final URI for this document post any redirects.
    """

    bytes: int
    start_url: str
    final_uri: str

    def __str__(self) -> str:
        """
        Return a string representation of this PDF.

        Returns:
            string (str): The string representation.
        """
        return f"""
        URI: {self.start_url}
        Final URI: {self.final_uri}
        Content Length: {self.bytes} Bytes
        """
