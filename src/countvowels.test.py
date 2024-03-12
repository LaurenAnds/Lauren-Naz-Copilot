import unittest
from countvowels import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_count_vowels_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels('xyz'), 0)

    def test_count_vowels_all_vowels(self):
        self.assertEqual(count_vowels('aeiouAEIOU'), 10)

    def test_count_vowels_mixed_case(self):
        self.assertEqual(count_vowels('AbcDeFG'), 2)

    def test_count_vowels_repeated_vowels(self):
        self.assertEqual(count_vowels('aaeeiioouu'), 10)

if __name__ == '__main__':
    unittest.main()
