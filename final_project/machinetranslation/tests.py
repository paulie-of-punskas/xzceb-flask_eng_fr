import unittest
from translator import frenchToEnglish, englishToFrench

class TestFrench(unittest.TestCase):
    def testNullFrenchToEnglish(self):
        self.assertEqual(frenchToEnglish(), "Input parameter cannot be empty")

    def testNotNullFrenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


class TestEnglish(unittest.TestCase):
    def testNullEnglishToFrench(self):
        self.assertEqual(englishToFrench(), "Input parameter cannot be empty")

    def testNotNullEnglishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()