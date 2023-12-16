#!/usr/bin/python3

"""The main driver for the pdf-finder program.
This program scrapes an inputted URI and locates any PDFs found within.
The PDFs are taken in for analysis and then output for the user.
"""

import argparse

from src.funcs import request, find_pdf

def main():
    """Main driver for the pdf-finder program.
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    response = request(args.URI)
    
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
