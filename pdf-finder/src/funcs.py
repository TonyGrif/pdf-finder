import requests
from bs4 import BeautifulSoup

from .pdf import PdfFile

def request(uriArg):
    try:
        response = requests.get(uriArg)
    except requests.exceptions.SSLError:
        return
    except ValueError:
        return
    except ConnectionError:
        return
    return response

def findPDF(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for pdfLinks in soup.find_all('a', href=True):
        if pdfLinks['href'].lower().endswith(".pdf"):
            links.append(pdfLinks['href'])

    links = list(set(links))
    pdfs = []
    for pdf in links:
        try:
            response = request(pdf)
        except Exception:
            continue
        
        if response is None:
            continue     
        
        pdfs.append(PdfFile(response.headers['content-length'], pdf, response.url))
    
    return pdfs