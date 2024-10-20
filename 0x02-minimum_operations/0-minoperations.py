#!/usr/bin/python3
"""Minoperation"""

def minOperations(n):
    """In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates
    the fewest number of operations needed to result in exactly n H characters
    in the file."""
    if n <= 1:
        return 0

    opt = 0
    f = 2

    while n > 1:
        while n % f == 0:
            opt += f
            n //= f
        f += 1

    return opt
