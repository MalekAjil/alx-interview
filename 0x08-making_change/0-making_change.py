#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1"""
    if total <= 0:
        return 0
