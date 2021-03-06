
class Integers(object):
    def __init__(self) -> None:
        super().__init__()

    def to_binary(int_value: int) -> int:
        if int_value == 1:
            return int_value
        number = bin(int_value)[2:]
        return number

    def to_hexadecimal(int_value: int) -> int:
        if int_value == 1:
            return int_value
        number = "{0}".format(hex(int_value))
        return number[2:]

    def to_byte(int_value: int) -> bytes:
        return bytes(int_value)
