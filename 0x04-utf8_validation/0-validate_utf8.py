#!/usr/bin/python3
"""validate_utf8 module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    for x in data:
        if x < 0 or x > 255:
            return False
    return True
