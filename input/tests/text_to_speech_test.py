import unittest
from input import TTS


class TestTTS(unittest.TestCase):
    def test_set_output(self):
        tts = TTS()
        assert tts.output == None
        tts._set_output("TEST")
        assert tts.output == "TEST"
