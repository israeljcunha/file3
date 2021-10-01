## Install App

    pip install file3

## Chars Conversion

For character conversion, simply import the features.

    from file3 import Chars

To use, simply log in this way:

- Performs the conversion from String to Binary, with the answer in string format

        Chars.to_binary("1") => Return '110001'

- Performs the conversion from String to ASCII, with the answer in dict format

        Chars.to_ascii("1") => Return {'int': 49, 'str': '49'}

- Performs the conversion from String to hexadecimal, with the response in dict format

        Chars.to_hexadecimal("1") => return '31'

## Hexadecimal Conversion

For hexadecimal conversion, just import the resources.

    from file3 import Hexadecimal

To use, simply log in this way:

- Performs hexadecimal to integer conversion, with response in integer format

        Hexadecimal.to_integer("1") => return 1

## Integer Conversion

For Integers conversion, just import the resources.

    from file3 import Integers

To use, simply log in this way:

- Performs integer to binary conversion, with the response in integer format

        Integers.to_binary(1) => return 1

- Performs integer to hexadecimal conversion, with response in integer format

        Integers.to_hexadecimal(1) => return 1

- Performs integer to byte conversion, with response in bytes format

        Integers.to_byte(1) => return b'\x00'

## Binary Conversion

For Integers conversion, just import the resources.

    from file3 import binarys

- Performs string-to-binary conversion, with integer-formatted response

        binarys.to_decimal("11000011") => return 195

## String Conversion

For Integers conversion, just import the resources.

    from file3 import Strings

- Performs string to hexadecimal conversion, with dict formatted response

        Strings.to_hexadecimal("1") => return {'1': '31'}

- Performs string-to-byte conversion, with dict formatted response

        Strings.to_byte("1") => return {'1': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}

- Performs string-to-ascii conversion, with dict formatted response

        Strings.to_ascii("1") => Return {'1': 49}

- Performs string-to-binary conversion, with dict formatted response

        Strings.to_binary("1") => return {'1': '110001'}
