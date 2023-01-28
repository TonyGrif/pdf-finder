#!/usr/bin/python3

import argparse

from src.funcs import request, findPDF

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    response = request(args.URI)
    
    if response is None:
        print("No response returned")
        return
    
    pdfs = findPDF(response)
    
    if len(pdfs) == 0:
        print("No pdfs found")
        return
    
    for p in pdfs:
        print(p)
    
    return

if __name__ == "__main__":
    main()