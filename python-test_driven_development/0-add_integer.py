#!/usr/bin/python3
"""This module defines a function that adds two integers"""


def add_integer(a, b=98):
    """
    This function adds two integers
    
    Args:
    a: the firs num (int or float).
    b: the second num (int or float), default is 98.
    
    Returns:
    The sum of the two num as an integer.
    
    Raises:
    ypeError: If a or b is not an integer or float.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
