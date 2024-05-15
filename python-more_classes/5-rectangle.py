#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    def __inti__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.seer
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >+ 0")
            self.__width = value

            @property
            def height(self):
                return self.__heigh

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

                def area(self):
                    return self.__width * self.__height

                def perimeter(self):
                    if self.__width == 0 or self.__height == 0:
                        return 0
                    return 2 * (self.__width + self.__height)

                def __str__(self):
                    if self.__width == 0 or self.__height == 0:
                        return ""
                    for i in range(self.__height):
                        rect += "#" * self.__widt
                        if i != self.__height - 1:
                            rect += "\n"
                            return rect

                        def __repr__(self):
                            return "Rectangle({}, {})".format(self.__width, self.__height)

                        def __del__(self):
                            print("Bye recangle...")
