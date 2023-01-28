#!/usr/bin/python3

import argparse

from funcs import request, findPDF

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    response = request(args.URI)
    pdfs = findPDF(response)
    
    for p in pdfs:
        print(p)
    
    return

if __name__ == "__main__":
    main()