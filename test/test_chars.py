from file3.chars import Chars
from unittest import TestCase

class TestChars(TestCase):
    def test_one_plus_one_is_equal_two(self):
        based_str = "1"
        correct_value = "110001"

        result = Chars.to_binary(based_str)
        self.assertEqual(result, correct_value)
