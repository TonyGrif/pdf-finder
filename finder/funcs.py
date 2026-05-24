"""This module contains functions for the pdf finder application."""

import requests
from bs4 import BeautifulSoup
from loguru import logger

from finder.pdf import PdfFile


def request(
    uri_arg: str, connect_timeout: float = 5, read_timeout: float = 30
) -> requests.Response:
    """Request a HTTP response from a URI.

    Args:
        uri_arg: String representation of the URI to request.
        connect_timeout: Seconds to wait for connection. Defaults to 5.
        read_timeout: Seconds to wait between data chunks. Defaults to 30.
            Response body is streamed lazily; callers that need it must access response.content.

    Returns:
        An HTTP response object.

    Raises:
        requests.RequestException: If the request fails or returns an error status.
    """
    logger.debug("Request on {}", uri_arg)
    response = requests.get(
        uri_arg, timeout=(connect_timeout, read_timeout), stream=True
    )
    response.raise_for_status()
    logger.debug("Response received from {}", uri_arg)
    return response


def find_pdf(response: requests.Response) -> list[PdfFile]:
    """Locate the PDFs in a HTTP response and create a new PDF object with the
    information acquired.

    Args:
        response: HTTP response object to search for PDF links.

    Returns:
        A collection of PDF objects found within the response.
    """
    links = _find_links(response)

    pdfs = []
    for pdf in links:
        try:
            pdf_response: requests.Response = request(pdf)
        except requests.RequestException as e:
            logger.debug("{} exception caught on {}", e, pdf)
            continue

        pdfs.append(
            PdfFile(
                int(pdf_response.headers.get("content-length", 0)),
                pdf,
                pdf_response.url,
            )
        )
        logger.debug("New pdf created with {}", pdf_response.url)

    return pdfs


def _find_links(response: requests.Response) -> list[str]:
    """Return the deduplicated PDF links found within a response.

    Args:
        response: HTTP response object to parse for links.

    Returns:
        A deduplicated list of URLs ending in .pdf.
    """
    soup = BeautifulSoup(response.content, "html.parser")

    links = []
    for pdf_links in soup.find_all("a", href=True):
        if pdf_links["href"].lower().endswith(".pdf"):
            logger.debug("{} link added", pdf_links["href"])
            links.append(pdf_links["href"])

    return list(set(links))
