import pytest

from finder import find_pdf, request


@pytest.fixture()
def good_response():
    return (request("https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"),)


@pytest.fixture
def bad_uris():
    return (
        "www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html",
        "https://www.goolge.com",
    )


class TestFunctions:
    def test_request(self, pdf_res, good_response, bad_uris):
        assert good_response[0].status_code == 200

        assert pdf_res.status_code == 200
        assert pdf_res.headers["content-type"] == "application/pdf"
        assert pdf_res.headers["content-length"] == "994153"

        # No value check
        with pytest.raises(Exception):
            request(bad_uris[0])
        # SSL error check
        with pytest.raises(Exception):
            request(bad_uris[1])

    def test_pdf(self, good_response):
        links = find_pdf(good_response[0])
        assert len(links) == 8

        url = "https://www.cs.odu.edu/~mweigle/"
        response = request(url)
        links = find_pdf(response)
        assert len(links) == 0
