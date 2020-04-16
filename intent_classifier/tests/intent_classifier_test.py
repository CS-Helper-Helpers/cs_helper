import unittest
from intent_classifier import IntentClassifier

# ic = IntentClassifier()
# print(ic)
# ic.clean_utterance([])
# print(ic.cleaning(["Hello  !"]))


class TestIntentClassifier(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("Setting up test case...")
        self.ic = IntentClassifier()

    @classmethod
    def tearDownClass(self):
        print("Tearing down test case... ")

    def test_cleaning(self):
        sentences = ["I am a sentence.", "you   are ?? a sentence", "WE ARE THE SENTENCES!!!"]
        cleaned_sentences = self.ic.cleaning(sentences)
        expected_sentences = [['i', 'am', 'a', 'sentence'], ['you', 'are', 'a', 'sentence'], ['we', 'are', 'the', 'sentences']]
        self.assertEqual(
                cleaned_sentences, expected_sentences
        )

    def test_cleaning_empty_set(self):
        sentences = []
        cleaned_sentences = self.ic.cleaning(sentences)
        expected_sentences = []
        self.assertEqual(cleaned_sentences, expected_sentences)

    def test_cleaning_nonstring_entry(self):
        sentences = ["The next entry", 2, "is a number"]
        with self.assertRaises(TypeError):
            self.ic.cleaning(sentences)

    # def test_create_tokenizer(self):
    #     pass

    def test_get_max_length(self):
        words = ["this", "is", "a", "list", "of", "words"]
        expected_max = 5
        given_max = self.ic.get_max_length(words)
        self.assertEqual(given_max, expected_max)

    def test_get_max_length_empty_set(self):
        with self.assertRaises(ValueError):
            result = self.ic.get_max_length([])


    # def test_encoding_doc(self):
    #     pass

    # def test_padding_doc(self):
    #     pass

    # def test_one_hot(self):
    #     pass

    # def test_create_model(self):
    #     pass

    # def train_model(self):
    #     pass

    # def test_predictions(self):
    #     pass

    # def test_tests(self):
    #     self.assertEqual(2, 2, "Should be 2")


# #if __name__ == '__main__':
# #    unnittest.main()
