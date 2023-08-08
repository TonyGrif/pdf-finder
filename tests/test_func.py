import pytest

from funcs import request, findPDF

class TestFunctions:
    def test_request(self):
        goodUrl = "https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"
        goodResponse = request(goodUrl)
        assert goodResponse.status_code == 200
        
        goodUrl = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        goodResponse = request(goodUrl)
        assert goodResponse.status_code == 200
        assert goodResponse.headers['content-type'] == "application/pdf"
        assert goodResponse.headers['content-length'] == "994153"        
        
        noValue = "www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"
        nullVal = request(noValue)
        assert nullVal is None
                        
        sslErr = "https://www.goolge.com"
        bad = request(sslErr)
        assert bad is None
            
    def test_PDFs(self):
        testUrl = "https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"
        response = request(testUrl)
        links = findPDF(response)
        assert len(links) == 8
        
        testUrl = "https://www.cs.odu.edu/~mweigle/"
        response = request(testUrl)
        links = findPDF(response)
        assert len(links) == 0
        
        testUrl = "https:://www.odu.edu"
        response = request(testUrl)
        links = findPDF(response)
        assert len(links) == 0
