#!/usr/bin/python3
"""
This module defines a function that identifies an object's subclass
"""


def inherits_from(obj, a_class):
    """
    This function indetifies an object's subclass
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
