"""This module contains functions for the pdf finder application.
"""

import logging
from typing import List, Optional, Union

import requests
from bs4 import BeautifulSoup

from src.pdf import PdfFile


def request(uri_arg: str) -> Union[requests.Response, None]:
    """Function to request a HTTP response from a URI.

    Args:
        uri_arg (str): string representation of the URI requesting.

    Returns:
        An HTTP response object if a response was returned, None otherwise.
    """
    try:
        logging.debug("Request on %s", uri_arg)
        response = requests.get(uri_arg, timeout=2.50)
    except Exception as e:
        logging.debug("%s exception caught on %s", e, uri_arg)
        return None
    logging.debug("Response recieved from %s", uri_arg)
    return response


def find_pdf(response: requests.Response) -> List[PdfFile]:
    """Locate the PDFs in a HTTP response and create a new PDF object with the
    information aquired.

    Args:
        response (requests.Response): HTTP response object.

    Returns:
        A collection of PDF objects found within the response.
    """
    if response is None:
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    links = []
    for pdf_links in soup.find_all("a", href=True):
        if pdf_links["href"].lower().endswith(".pdf"):
            logging.debug("%s link added", pdf_links["href"])
            links.append(pdf_links["href"])

    links = list(set(links))
    pdfs = []
    for pdf in links:
        try:
            pdf_response: Optional[requests.Response] = request(pdf)
        except Exception as e:
            logging.debug("%s exception caught on %s", e, pdf)
            continue

        if pdf_response is None:
            logging.debug("%s returned no response", pdf)
            continue

        pdfs.append(
            PdfFile(int(pdf_response.headers["content-length"]), pdf, pdf_response.url)
        )
        logging.debug("New pdf created with %s", pdf_response.url)

    return pdfs
