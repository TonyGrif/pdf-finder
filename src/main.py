#!/usr/bin/python3

import argparse
import urllib.request
import requests

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("URI", type=str, help="URI to be searched")
    args = parser.parse_args()
    
    try:
        url = urllib.request.urlopen(args.URI)
    except urllib.error.URLError:
        print("Invalid website provided")
        return
    except ValueError:
        print("Provide the URL Type (ex: HTTP://)")
        return    

    print(url)
    
    return

if __name__ == "__main__":
    main()