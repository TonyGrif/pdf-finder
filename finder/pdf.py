"""This module contains the PDF data class."""

from dataclasses import dataclass


@dataclass
class PdfFile:
    """PDF object storing the starting & final URLs and byte size.

    Attributes:
        bytes: Number of bytes the document is.
        start_url: Starting URL for this document.
        final_uri: Final URI for this document post any redirects.
    """

    bytes: int
    start_url: str
    final_uri: str

    def __str__(self) -> str:
        """Return a string representation of this PDF.

        Returns:
            The formatted URI, final URI, and content length.
        """
        return f"""
        URI: {self.start_url}
        Final URI: {self.final_uri}
        Content Length: {self.bytes} Bytes
        """
