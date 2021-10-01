class Chars(object):
    def __init__(self) -> None:
        super().__init__()

    def to_binary(char_value: str) -> str:
        number = bin(ord(char_value))[2:]
        if len(char_value) == 1:
            return number
        return number[len(number) - char_value :]

    def to_ascii(char_value: str) -> dict:
        if isinstance(char_value, str) and len(char_value) == 1:
            return dict([
                ("int", ord(char_value)),
                ("str", "{0}".format(ord(char_value)))
            ])
        else:
            raise ValueError("You can only convert one letter")

    def to_hexadecimal(char_value: str) -> str:
        try:
            return "{0}".format(hex(ord(char_value)).replace("0x", ""))
        except Exception:
            raise ValueError("You can only convert one letter")
