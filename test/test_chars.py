from file3.chars import Chars
from unittest import TestCase, result

class TestChars(TestCase):
    def test_chars_to_binary_by_string(self):
        based_str = "9"
        correct_value = "111001"

        result = Chars.to_binary(based_str)
        self.assertEqual(result, correct_value)

    def test_chars_to_ascii_by_string(self):
        base_str = "9"
        result_str = "57"
        result_int= 57

        result = Chars.to_ascii(base_str)

        self.assertEqual(result_int, result["int"])
        self.assertEqual(result_str, result["str"])

    def test_chars_to_hexadecimal_by_string(self):
        base_str = "b"
        result_str = '62'

        result = Chars.to_hexadecimal(base_str)
        self.assertEqual(result_str, result)
