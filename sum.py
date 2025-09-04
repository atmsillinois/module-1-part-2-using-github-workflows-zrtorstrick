"""Contain functions related to mathematical sums."""


def sum_of_integers(a, b):
    """
    Return the sum of two integers.

    Raise a TypeError if either argument is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError(f'"{a}" is not an integer', a)

    if not isinstance(b, int):
        raise TypeError(f'"{b}" is not an integer', b)

    return a + b
