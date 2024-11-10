#!/usr/bin/python3
"""NQueens Module"""
import sys


if len(sys.argv) != 2 or sys.argv[1] is None:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
