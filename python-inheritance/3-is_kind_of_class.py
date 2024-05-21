#!/usr/bin/python3
"""
This module defines a function that checks
if a class is inherited from a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if the object is an instance of a class that inherited from,
    the specified class; otherwise false.
    """
    return isinstance(obj, a_class)
