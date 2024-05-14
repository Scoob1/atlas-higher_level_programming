#!/usr/bin/python3
"""
Module - 2-square
Defines a class Square with private atribute size
"""


class Square:
    """
    Defines a square
    """


    def __init__(self, size=0):
        """
        Initializes the Square instance
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
