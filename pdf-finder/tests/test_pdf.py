import pytest

from src.pdf import PdfFile
from src.funcs import request

class TestPDF:
    def test_bytes(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PdfFile(response.headers['content-length'], testURI, response.url)
        assert int(result.bytes) == 994153
        
        testURI = "http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf"
        response = request(testURI)
        result = PdfFile(response.headers['content-length'], testURI, response.url)
        assert int(result.bytes) == 18995885
        
    def test_startURL(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PdfFile(response.headers['content-length'], testURI, response.url)
        # Notice http instead of https
        assert result.startURL == "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        assert result.startURL != "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        
    def test_finalURI(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PdfFile(response.headers['content-length'], testURI, response.url)
        # Notice https instead of http
        assert result.finalURI == "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        assert result.finalURI != "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        
    def test_str(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PdfFile(response.headers['content-length'], testURI, response.url)
        stringResult = str(result.__str__)
        
        assert stringResult.find("994153")
        assert stringResult.find("https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf")
        assert stringResult.find("http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf")