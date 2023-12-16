#!/usr/bin/python3

"""The main module for the pdf-finder program.

This program scrapes an inputted URI and locates any PDFs found within.
The PDFs are taken in for analysis and then output for the user.

This file can be run as `./main.py [-h] URI`.
"""

import argparse
import logging

from src.funcs import request, find_pdf


def main():
    """Main driver for the pdf-finder program."""
    parser = argparse.ArgumentParser(
        prog="PDF Finder",
        description="Scrapes PDF data from a URI.",
        epilog="Source code can be found at https://github.com/TonyGrif/pdf-finder",
    )

    parser.add_argument("uri", type=str, help="The URI to be searched.")
    parser.add_argument(
        "--debug", action="store_true", help="Enable DEBUG console output logs."
    )

    args = parser.parse_args()
    if args.debug == True:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"URI Provided: {args.uri}")

    response = request(args.uri)

    if response is None:
        print("No response returned")
        return

    pdfs = find_pdf(response)

    if len(pdfs) == 0:
        print("No pdfs found")
        return

    for p in pdfs:
        print(p)

    return


if __name__ == "__main__":
    main()
