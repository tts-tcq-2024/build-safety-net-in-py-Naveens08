import unittest
from Soundex import generate_soundex
from Soundex import add_padding_to_code
from Soundex import if_break

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

    def test_padding(self):
        self.assertEqual(add_padding_to_code("AB", '0', 4), "AB00")

    def test_if_break(self):
        self.assertEqual(if_break("A100"), True)
        self.assertEqual(if_break("A1"), False)
    
if __name__ == '__main__':
    unittest.main()
