import unittest
from Soundex import generate_soundex
from Soundex import add_padding_to_code
from Soundex import if_break
from Soundex import if_continue
from Soundex import if_append
from Soundex import get_soundex_code
from Soundex import process_characters
from Soundex import process_character

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
        self.assertEqual(add_padding_to_code("A123", '0', 4), "A123")

    def test_if_break(self):
        self.assertEqual(if_break("A100"), True)
        self.assertEqual(if_break("A1"), False)

    def test_if_continue(self):
        self.assertEqual(if_continue("0"), True)
        self.assertEqual(if_continue("A"), False)

    def test_if_append(self):
        self.assertEqual(if_append("0", "A"), True)
        self.assertEqual(if_append("A", "A"), False)

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code("M"), '5')
        self.assertEqual(get_soundex_code("1"), '0')
        self.assertEqual(get_soundex_code("a"), '0')
        self.assertEqual(get_soundex_code("r"), '6')

    def test_process_characters(self):
        self.assertEqual(process_characters('Robert'), 'R163')
        self.assertEqual(process_characters('Rupert'), 'R163')
        self.assertEqual(process_characters('Ashcraft'), 'A261')

    def test_process_character(self):
        self.assertEqual(process_character('A', 'B', '0'), ('A1', '1'))
        self.assertEqual(process_character('A', 'A', '0'), ('A', '0'))
        self.assertEqual(process_character('A', 'B', '1'), ('A', '1'))

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex('Robert'), 'R163')
        self.assertEqual(generate_soundex('Rupert'), 'R163')
        
if __name__ == '__main__':
    unittest.main()
