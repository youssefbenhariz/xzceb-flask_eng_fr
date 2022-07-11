import unittest
from translator import frenchtoenglish,englishtofrench
class TestStringMethods(unittest.TestCase):
    def test_frenchtoenglish(self):
        self.assertNotEqual(frenchtoenglish("Hello"),"Bonjour")
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
    def test_englishtofrench(self):
        self.assertNotEqual(englishtofrench("Bonjour"),"Hello")
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
if __name__=='__main__':
    unittest.main()