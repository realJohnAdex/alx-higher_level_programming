#!/usr/bin/python3

"""
This is "0-add_integer" module

The module supplies add_integers function, that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Default is 98.

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
