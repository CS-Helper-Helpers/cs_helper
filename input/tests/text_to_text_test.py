import unittest
from unittest.mock import patch
from input import TTT
import builtins


class TestTTT(unittest.TestCase):
    def test_get_input(self):
        ttt = TTT()
        with patch("builtins.input", return_value="test"):
            assert ttt.get_input() == "test"
