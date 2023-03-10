import requests
from bs4 import BeautifulSoup

from .pdf import PdfFile

def request(uriArg) -> requests.Response:
    """Function to request a HTTP response from a URI.

    Args:
        uriArg (str): A string representation of the URI requesting.

    Returns:
        Response : An HTTP response.
    """
    try:
        response = requests.get(uriArg, timeout=2.50)
    except requests.exceptions.SSLError:
        return
    except ValueError:
        return
    except ConnectionError:
        return
    return response

def findPDF(response):
    """Locate the PDFs in a HTTP response. Create a new PDF object with the information aquired.

    Args:
        response (requests.Response): HTTP request created by the requests library.

    Returns:
        Array[PDF]: An array of PDF objects found within this response.
    """
    if response is None:
        pdfs = []
        return pdfs
    
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