from functools import lru_cache
from toolz import curry


@lru_cache(maxsize=128)
def cached_adder(a: int, b: int) -> int:
    """
    Adds two numbers. Keeps the last 128 calls in a cache.

    :param a: the first number
    :param b: the second number
    :return: the sum of the two numbers
    """
    return a+b


@curry
def curried_adder(a: int, b: int) -> int:
    """
    Adds two numbers. Has been curried to allow you to call it as curried_adder(1)(2).

    :param a: the first number
    :param b: the second number
    :return: the sum of the two numbers
    """
    return a+b

