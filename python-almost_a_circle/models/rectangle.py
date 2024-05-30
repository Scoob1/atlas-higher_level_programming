#!/usr/bin/python3
"""Module class Rectangle inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints a rectangle in stdout using '#' character"""
        disRectangle = self.y * "\n"

        for i in range(self.height):
            disRectangle += (" " * self.x)
            disRectangle += ("#" * self.width) + "\n"

        print(disRectangle, end='')

    def __str__(self):
        """Override of __str__ builtin"""
        str_Rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_Rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            listAttr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, listAttr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        listAttr = ['id', 'width', 'height', 'x', 'y']
        dictionary = {}

        for key in listAttr:
            dictionary[key] = getattr(self, key)

        return dictionary
