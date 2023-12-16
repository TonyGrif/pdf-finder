import pytest

from funcs import request, find_pdf


@pytest.fixture
def good_url():
    return [
        "https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
        "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf",
    ]


@pytest.fixture
def bad_url():
    return ["www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html", "https://www.goolge.com"]


class TestFunctions:
    def test_request(self, good_url, bad_url):
        assert request(good_url[0]).status_code == 200

        response = request(good_url[1])
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/pdf"
        assert response.headers["content-length"] == "994153"

        # No value check
        assert request(bad_url[0]) is None
        # SSL error check
        assert request(bad_url[1]) is None

    def test_PDFs(self, good_url, bad_url):
        response = request(good_url[0])
        links = find_pdf(response)
        assert len(links) == 8

        response = request(bad_url[0])
        links = find_pdf(response)
        assert len(links) == 0

        test_url = "https://www.cs.odu.edu/~mweigle/"
        response = request(test_url)
        links = find_pdf(response)
        assert len(links) == 0
