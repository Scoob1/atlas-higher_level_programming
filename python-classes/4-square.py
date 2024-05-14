#!/usr/bin/python3
class Square:
    """
    Class that defines a square with size validation, and property methods to access and update size.
    """

    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            """Getter for size."""
            return self.__size

        @size.setter
        def size(self, value):
            """Setter for size with validation."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size mustt be >+ 0")
            self.__size = value

            def area(self):
                """Returns the area of the square."""
                return self.__size * self.__size
