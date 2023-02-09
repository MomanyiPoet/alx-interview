#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    '''
    min operations
    Args:
      n:
    Returns:
      n is impossible to achieve, return 0
    '''
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations
