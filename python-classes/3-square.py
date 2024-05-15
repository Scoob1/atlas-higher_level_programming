#!/usr/bin/python3
""" Defining a class square """


class Square:
    """
    Defines a square with size validation
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """
            Returns the area of the square
            """
            return self.__size * self.__size
