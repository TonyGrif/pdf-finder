import pytest

from funcs import request, findPDF

@pytest.fixture
def goodUrl():
    return ["https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
            "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"] 


@pytest.fixture
def badUrl():
    return ["www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
            "https://www.goolge.com"]


class TestFunctions:
    def test_request(self, goodUrl, badUrl):
        goodResponse = request(goodUrl[0])
        assert goodResponse.status_code == 200

        goodResponse = request(goodUrl[1])
        assert goodResponse.status_code == 200
        assert goodResponse.headers["content-type"] == "application/pdf"
        assert goodResponse.headers["content-length"] == "994153"

        # No value check
        assert request(badUrl[0]) is None
        # SSL error check
        assert request(badUrl[1]) is None

    def test_PDFs(self, goodUrl, badUrl):
        response = request(goodUrl[0])
        links = findPDF(response)
        assert len(links) == 8

        response = request(badUrl[0])
        links = findPDF(response)
        assert len(links) == 0

        testUrl = "https://www.cs.odu.edu/~mweigle/"
        response = request(testUrl)
        links = findPDF(response)
        assert len(links) == 0

        testUrl = "https:://www.odu.edu"
        response = request(testUrl)
        links = findPDF(response)
        assert len(links) == 0
