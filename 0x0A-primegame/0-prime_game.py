#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    primeNum = []
    fil = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (fil[prime]):
            primeNum.append(prime)
            for i in range(prime, n + 1, prime):
                fil[i] = False
    return primeNum


def isWinner(x, nums):
    """
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNum = primeNumbers(nums[i])
        if len(primeNum) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
