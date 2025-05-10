#!/usr/bin/python3

"""The main module for the pdf-finder program.

This program scrapes an inputted URI and locates any PDFs found within.
The PDFs are taken in for analysis and then output for the user.

This file can be run as `./main.py [-h] URI`.
"""

import argparse
import logging

from finder.funcs import request, find_pdf


def main():
    """Main driver for the pdf-finder program."""
    parser = argparse.ArgumentParser(
        prog="PDF Finder",
        description="Scrapes PDF data from a URI.",
        epilog="Source code can be found at https://github.com/TonyGrif/pdf-finder",
    )

    parser.add_argument("uri", type=str, help="The URI to be searched.")
    parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable DEBUG console output logs."
    )

    args = parser.parse_args()
    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug("URI Provided: %s", args.uri)

    response = request(args.uri)

    if response is None:
        logging.debug("No response returned")
        return -1

    pdfs = find_pdf(response)
    logging.debug("%s PDFs found", len(pdfs))

    if len(pdfs) == 0:
        return -2

    for p in pdfs:
        print(p)

    return 0


if __name__ == "__main__":
    main()
