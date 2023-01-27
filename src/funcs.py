import requests
import sys

def request(uriArg):
    try:
        response = requests.get(uriArg)
    except requests.exceptions.SSLError:
        print("Invalid website provided")
        sys.exit()
    except ValueError:
        print("Provide the URL Type (ex: HTTP://)")
        sys.exit()
    return response