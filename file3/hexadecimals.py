class Hexadecimal(object):
    def __init__(self) -> None:
        super().__init__()

    def to_integer(value: str) -> int:
        return int(value, 16)
