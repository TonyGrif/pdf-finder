import requests
import sys
from bs4 import BeautifulSoup

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

def findPDF(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for pdfLinks in soup.find_all('a', href=True):
        links.append(pdfLinks['href'])

    pdfs = []
    # Could also be done in the above for loop
    for pdf in links:
        response = request(pdf)
        
        if(response.headers['content-type'] == "application/pdf"):
            pdfs.append(pdf)
        else:
            continue
    
    return pdfs