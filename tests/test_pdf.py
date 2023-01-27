import pytest

from src.pdf import PDF
from src.funcs import request

class TestPDF:
    def test_bytes(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PDF(response.headers['content-length'], response.url)
        assert int(result.bytes) == 994153
        
        testURI = "http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf"
        response = request(testURI)
        result = PDF(response.headers['content-length'], response.url)
        assert int(result.bytes) == 18995885
        
    def test_finalURI(self):
        testURI = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(testURI)
        result = PDF(response.headers['content-length'], response.url)
        # Notice https instead of http
        assert result.finalURI == "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        assert result.finalURI != "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"