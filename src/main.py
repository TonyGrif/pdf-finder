#!/usr/bin/python3

import argparse
from bs4 import BeautifulSoup

from funcs import request
from pdf import PDF

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    response = request(args.URI)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    for pdfLinks in soup.find_all('a', href=True):
        if pdfLinks['href'].lower().endswith(".pdf"):
            print(pdfLinks['href'])
    
    return

if __name__ == "__main__":
    main()