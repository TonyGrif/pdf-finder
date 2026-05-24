#!/usr/bin/python3

"""The main module for the pdf-finder program.

This program scrapes an inputted URI and locates any PDFs found within.
The PDFs are taken in for analysis and then output for the user.

This file can be run as `pdf-finder [-h] URI`.
"""

import argparse
import sys

import requests
from loguru import logger

from finder.funcs import find_pdf, request


def main(argv: list[str] | None = None) -> int:
    """Main driver for the pdf-finder program.

    Args:
        argv: Argument list to parse. Defaults to sys.argv when None.

    Returns:
        0 on success, -1 if the URI request fails, -2 if no PDFs are found.
    """
    parser = argparse.ArgumentParser(
        prog="PDF Finder",
        description="Scrapes PDF data from a URI.",
        epilog="Source code can be found at https://github.com/TonyGrif/pdf-finder",
    )

    parser.add_argument("uri", type=str, help="The URI to be searched.")
    parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable DEBUG console output logs."
    )

    args = parser.parse_args(argv)
    logger.remove()
    if args.debug is True:
        logger.add(sys.stdout, level="DEBUG")

    logger.debug("URI Provided: {}", args.uri)

    try:
        response = request(args.uri)
    except requests.RequestException as e:
        logger.error("Failed to retrieve {}: {}", args.uri, e)
        return -1

    pdfs = find_pdf(response)
    logger.debug("{} PDFs found", len(pdfs))

    if len(pdfs) == 0:
        return -2

    for p in pdfs:
        print(p)

    return 0


if __name__ == "__main__":
    main()
