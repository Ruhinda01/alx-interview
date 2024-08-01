#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins to meet a given amount total
    Params:
    coins (list): list of the values of the coins
    total (int): the value of the total
    Returns:
    int: the fewest number of coins
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1

    if total == 0:
        return count
    return -1
