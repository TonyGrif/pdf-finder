import pytest

from src.funcs import request


@pytest.fixture(scope="session")
def pdf_uri():
    return "https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf"


@pytest.fixture(scope="session")
def pdf_res(pdf_uri):
    return request(pdf_uri)
