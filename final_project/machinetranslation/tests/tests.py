import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  def test_englishToFrench(self):
        self.assertNotEqual(english_to_french("None"), "") # test for null english to french
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test for the translation of the world 'Hello' and 'Bonjour'

  def test_frenchToEnglish(self):
        self.assertNotEqual(french_to_english("None"), "") # test for null french to english
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test for the translation of the world 'Bonjour' and 'Hello'

if __name__ =='__main__':
  unittest.main()