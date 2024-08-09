#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Returns the winner of the prime game
    Params:
    x (int): number of rounds
    nums (list): list of numbers
    Return:
    The winner of the prime game
    """
    def SieveOfEratosthenes(max_num):
        """
        Returns a list of prime numbers up to max_num
        """
        primes = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if primes[p]:
                for i in range(p * 2, max_num + 1, p):
                    primes[i] = False
            p += 1
        primes[0], primes[1] = False, False
        return [p for p in range(max_num + 1) if primes[p]]

    # edge cases
    if x <= 0 or not nums:
        return None

    # calculate primes up to max
    max_num = max(nums)
    prime = SieveOfEratosthenes(max_num)

    players = {"Maria": 0, "Ben": 0}

    for n in nums:
        current_round_primes = [p for p in prime if p <= n]

        if len(current_round_primes) % 2 == 0:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Ben"] > players["Maria"]:
        return "Ben"
    else:
        return None
