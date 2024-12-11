import unittest
from requests.exceptions import Timeout
from unittest.mock import patch, MagicMock
from .main import add, len_joke, get_joke


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    @patch("python_mocks_testing.main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "A joke"
        self.assertEqual(len_joke(), 6)

    """
    Mocking the requests using the patch and mocking the response using MagicMock.
    To say patch also creates an instance of MagicMock
    """

    @patch("python_mocks_testing.main.requests")
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "A mock joke"}
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "A mock joke")

    @patch("python_mocks_testing.main.requests")
    def test_get_joke_invalid_status_code(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = "No jokes"
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")

    @patch("python_mocks_testing.main.requests")
    def test_get_joke_advance_timeout_exception(self, mock_requests):
        """
        A side_effect explicitely imposes exception whenever a function is called
        """
        mock_requests.get.side_effect = Timeout("A mock joke")

        with self.assertRaises(Timeout) as context:
            get_joke()
        self.assertEqual(context.exception.args[0], "A mock joke")


if __name__ == "__main__":
    unittest.main()
