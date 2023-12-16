#!/usr/bin/python3

"""The main module for the pdf-finder program.

This program scrapes an inputted URI and locates any PDFs found within.
The PDFs are taken in for analysis and then output for the user.

This file can be run as `./main.py [-h] URI`.
"""

import argparse

from src.funcs import request, find_pdf


def main():
    """Main driver for the pdf-finder program."""
    parser = argparse.ArgumentParser(
        prog="PDF Finder",
        description="Scrapes PDF data from a URI.",
        epilog="Source code can be found at https://github.com/TonyGrif/pdf-finder",
    )

    parser.add_argument("uri", type=str, help="The URI to be searched.")
    args = parser.parse_args()

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
