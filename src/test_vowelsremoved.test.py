import unittest
from vowelsremoved import remove_vowels

def remove_vowels(given_string):
    new_string = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in given_string:
        if letter not in vowels:
            new_string += letter
    return new_string

class TestVowelsRemoved(unittest.TestCase):
    def test_remove_vowels_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_remove_vowels_no_vowels(self):
        self.assertEqual(remove_vowels("Hello"), "Hll")

    def test_remove_vowels_all_vowels(self):
        self.assertEqual(remove_vowels("aeiouAEIOU"), "")

    def test_remove_vowels_mixed_case(self):
        self.assertEqual(remove_vowels("AbCdEfG"), "bCdfG")

    def test_remove_vowels_with_numbers_and_symbols(self):
        self.assertEqual(remove_vowels("H3ll0!"), "H3ll0!")

if __name__ == '__main__':
    unittest.main()