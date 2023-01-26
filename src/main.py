#!/usr/bin/python3

import argparse
import requests
from bs4 import BeautifulSoup

from pdf import PDF

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    try:
        url = requests.get(args.URI)
    except requests.exceptions.SSLError:
        print("Invalid website provided")
        return
    except ValueError:
        print("Provide the URL Type (ex: HTTP://)")
        return    

    print(url)
    
    return

if __name__ == "__main__":
    main()