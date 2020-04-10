import unittest
from intent_classifier import IntentClassifier


class TestIntentClassifier(unittest.TestCase):

    def __init__(self):
        self.ic_model = IntentClassifier()

    def test_cleaning(self):
        sentences = []
        cleaned_sentences = self.ic_model.cleaning(sentences)
        self.assertEqual(
                cleaned_sentences, sentences
        )

    def test_create_tokenizer(self):
        pass

    def test_get_max_length(self):
        pass

    def test_encoding_doc(self):
        pass

    def test_padding_doc(self):
        pass

    def test_one_hot(self):
        pass

    def test_create_model(self):
        pass

    def train_model(self):
        pass

    def test_predictions(self):
        pass

    def test_tests(self):
        self.assertEqual(2,2, "Should be 2")

#if __name__ == '__main__':
#    unnittest.main()

