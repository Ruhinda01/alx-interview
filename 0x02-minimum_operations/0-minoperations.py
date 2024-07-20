#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    chars = 1
    start = 0
    count = 0

    while chars < n:
        remainder = n - chars
        if (remainder % chars == 0):
            start = chars
            chars += start
            count += 2
        else:
            chars += start
            count += 1

    return count
