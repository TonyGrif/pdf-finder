import pytest

from src.funcs import request

class TestFunctions:
    def test_request(self):
        goodUrl = "https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"
        goodResponse = request(goodUrl)
        
        assert goodResponse.status_code == 200
        
        noValue = "www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html"
        with pytest.raises(SystemExit):
            bad = request(noValue)
            
        sslErr = "https://www.goolge.com"
        with pytest.raises(SystemExit):
            bad = request(sslErr)
