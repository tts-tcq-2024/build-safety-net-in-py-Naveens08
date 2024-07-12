import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("a"), "A000")

    def test_two_characters(self):
        self.assertEqual(generate_soundex("ZZ"), "Z000")
        self.assertEqual(generate_soundex("zZ"), "Z000")

    def test_three_characters(self):
        self.assertEqual(generate_soundex("ZMN"), "Z500")

    def test_four_characters(self):
        self.assertEqual(generate_soundex("ZMNZ"), "Z520")
    
if __name__ == '__main__':
    unittest.main()
