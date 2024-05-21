#!/usr/bin/python3
"""
Defines a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a Square"""
    def __init__(self, size):
        """Initializes a Square
            Args:
            size (int): the size of the square
            """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
