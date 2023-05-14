"""Translation tool test"""

import unittest
import sys
sys.path.append('../translator')
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_frenchToEnglish(self):
        french_text = "Bonjour, comment ça va ?"
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, "Hello, how are you?")
    
    def test_englishToFrench(self):
        english_text = "Hello, how are you?"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, "Bonjour, comment ça va ?")

if __name__ == '__main__':
    unittest.main()
