from unittest.mock import MagicMock, patch

import requests

from finder.__main__ import main
from finder.pdf import PdfFile


class TestMain:
    def test_main_success(self, capsys):
        mock_pdf = PdfFile(
            12345, "https://example.com/doc.pdf", "https://example.com/doc.pdf"
        )
        with patch("finder.__main__.request") as mock_request, patch(
            "finder.__main__.find_pdf", return_value=[mock_pdf]
        ):
            mock_request.return_value = MagicMock()
            result = main(["https://example.com"])
        assert result == 0
        captured = capsys.readouterr()
        assert "12345" in captured.out

    def test_main_no_pdfs(self):
        with patch("finder.__main__.request") as mock_request, patch(
            "finder.__main__.find_pdf", return_value=[]
        ):
            mock_request.return_value = MagicMock()
            result = main(["https://example.com"])
        assert result == -2

    def test_main_request_failure(self):
        with patch(
            "finder.__main__.request", side_effect=requests.RequestException("fail")
        ):
            result = main(["https://example.com"])
        assert result == -1
