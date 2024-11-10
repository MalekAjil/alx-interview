#!/usr/bin/python3
"""NQueens Module"""
import sys


if len(sys.args) != 2 or sys.args[1] is None:
    print("Usage: nqueens N")
    exit(1)
N = sys.args[1]
if type(N) is not int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
