import pytest

from pdf import PdfFile
from funcs import request


class TestPDF:
    def test_bytes(self):
        test_uri = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        assert int(result.bytes) == 994153

        test_uri = "http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        assert int(result.bytes) == 18995885

    def test_startURL(self):
        test_uri = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        # Notice http instead of https
        assert (
            result.start_url
            == "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert (
            result.start_url
            != "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )

    def test_finalURI(self):
        test_uri = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        # Notice https instead of http
        assert (
            result.final_uri
            == "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert (
            result.final_uri
            != "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )

    def test_str(self):
        test_uri = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        str_result = str(result.__str__)

        assert str_result.find("994153")
        assert str_result.find(
            "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert str_result.find(
            "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
