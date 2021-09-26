from file3.chars import Chars


class Strings(object):
    def __init__(self) -> None:
        super().__init__()

    def to_hexadecimal(str_value: str) -> str:
        related = dict()
        for char in str_value:
            unit_hex = Strings.ToHexadecimal(char)
            if len(unit_hex) == 1:
                unit_hex = "0" + unit_hex
            related.update({char: unit_hex})
        return related

    def to_byte(str_value: str):
        related = dict()
        for char in str_value:
            related.update({char: bytes(Chars.to_ascii(char)["int"])})
        return related

    def to_ascii(str_value: str):
        related = dict()
        for char in str_value:
            related.update({char: Chars.to_ascii(char)["int"]})
        return related

    def to_binary(str_value: str):
        related = dict()
        for char in str_value:
            related.update({char: Chars.to_binary(char)})
        return related
