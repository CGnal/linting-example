"""
Fibonacci sequence generator
"""

from typing import Iterator


def fib(last_upper_limit: int) -> Iterator[int]:
    """
    Generates a Fibonacci sequence given an upper limit for the last number
    of the sequence

    :param last_upper_limit: upper limit for the last number of the sequence
    :return: an iterator to the Fibonacci sequence
    """
    second_last, last = 0, 1
    while second_last < last_upper_limit:
        yield second_last
        second_last, last = last, second_last + last
