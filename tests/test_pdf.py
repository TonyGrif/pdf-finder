import pytest

from pdf import PdfFile
from funcs import request


@pytest.fixture
def pdf():
    test_uri = "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
    response = request(test_uri)
    return PdfFile(response.headers["content-length"], test_uri, response.url)


class TestPDF:
    def test_bytes(self, pdf):
        assert int(pdf.bytes) == 994153

        test_uri = "http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf"
        response = request(test_uri)
        result = PdfFile(response.headers["content-length"], test_uri, response.url)
        assert int(result.bytes) == 18995885

    def test_startURL(self, pdf):
        # Notice http instead of https
        assert (
            pdf.start_url
            == "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert (
            pdf.start_url
            != "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )

    def test_finalURI(self, pdf):
        # Notice https instead of http
        assert (
            pdf.final_uri
            == "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert (
            pdf.final_uri
            != "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )

    def test_str(self, pdf):
        str_result = str(pdf.__str__)

        assert str_result.find("994153")
        assert str_result.find(
            "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
        assert str_result.find(
            "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"
        )
