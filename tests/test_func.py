import pytest

from funcs import request, find_pdf


@pytest.fixture
def good_response():
    good_url = [
        "https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
        "http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf",
    ]
    return (request(good_url[0]), request(good_url[1]))


@pytest.fixture
def bad_response():
    bad_url = [
        "www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
        "https://www.goolge.com",
    ]
    return (request(bad_url[0]), request(bad_url[1]))


class TestFunctions:
    def test_request(self, good_response, bad_response):
        assert good_response[0].status_code == 200

        assert good_response[1].status_code == 200
        assert good_response[1].headers["content-type"] == "application/pdf"
        assert good_response[1].headers["content-length"] == "994153"

        # No value check
        assert bad_response[0] is None
        # SSL error check
        assert bad_response[1] is None

    def test_pdf(self, good_response, bad_response):
        links = find_pdf(good_response[0])
        assert len(links) == 8

        links = find_pdf(bad_response[0])
        assert len(links) == 0

        url = "https://www.cs.odu.edu/~mweigle/"
        response = request(url)
        links = find_pdf(response)
        assert len(links) == 0
