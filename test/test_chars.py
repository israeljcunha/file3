from file3.chars import Chars


def test_to_binary():
    based_str = "12"
    correct_value = "1100"

    process_value = Chars.to_binary(based_str)
    assert process_value == correct_value
