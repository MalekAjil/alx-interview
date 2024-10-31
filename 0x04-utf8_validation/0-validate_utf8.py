#!/usr/bin/python3
"""validate_utf8 module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    nb = 0
    for x in data:
        byte = x & 0xFF
        if nb == 0:
            if (byte >> 5) == 0b110:
                nb = 1
            elif (byte >> 4) == 0b1110:
                nb = 2
            elif (byte >> 3) == 0b11110:
                nb = 3
            elif (byte >> 7) != 0:
                return False
            else:
                if (byte >> 6) != 0b10:
                    return False
                nb -= 1
    return nb == 0
