class ConversionChar(object):
    def __init__(self, arg):
        super(ConversionChar, self).__init__()
        self.arg = arg

    def CharToBin(self, strValue):
        number = bin(ord(strValue))[2:]
        if len(strValue) == 1:
            return number
        return number[len(number) - strValue:]

    def IntToBin(self, intValue):
        if intValue == 1:
            return intValue
        number = bin(intValue)[2:]
        return number

    def IntToHex(self, binaryNamber):
        if binaryNamber == 1:
            return binaryNamber
        number = "{0}".format(hex(binaryNamber))
        return number[2:]

    def CharToASCII(self, Character):
        if isinstance(Character, str) and len(Character) == 1:
            return dict([('int', ord(Character)), ('str', '{0}'.format(ord(Character)))])
        else:
            raise ValueError("You can only convert one letter")

    def CharToHex(self, value):
        try:
            return '{0}'.format(hex(ord(value)).replace('0x', ''))
        except Exception as e:
            raise ValueError("You can only convert one letter")

    def BinStrToDecimal(self, str_value):
        return int(str_value, 2)

    def HexToInt(self, value):
        return int(value, 16)

    def IntToByte(self, value):
        return bytes(value)


class ConversionString(object):
    def __init__(self, arg):
        super(ConversionString, self).__init__()
        self.arg = arg

    def StrToHex(self, str_value):
        related = dict()
        for char in str_value:
            unit_hex = ConversionChar.CharToHex(self, char)
            if len(unit_hex) == 1:
                unit_hex = '0' + unit_hex
            related.update({char : unit_hex})
        return related

    def StrToBytes(self, str_value):
        related = dict()
        for char in str_value:
            related.update({char: bytes(ConversionChar.CharToASCII(self, char)['int'])})
        return related

    def StrToASCII(self, str_value):
        related = dict()
        for char in str_value:
            related.update({char: ConversionChar.CharToASCII(self, char)['int']})
        return related

    def StrToBin(self, str_value):
        related = dict()
        for char in str_value:
            related.update({char: ConversionChar.CharToBin(self, char)})
        return related