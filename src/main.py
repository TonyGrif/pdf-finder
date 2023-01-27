#!/usr/bin/python3

import argparse

from funcs import request, findPDF
from pdf import PDF

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    response = request(args.URI)
    pdfs = findPDF(response)
    
    print(pdfs)
    
    return

if __name__ == "__main__":
    main()