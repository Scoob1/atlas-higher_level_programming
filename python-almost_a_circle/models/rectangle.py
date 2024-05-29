#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base



class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        @property
        def width(self):
            """Getter for width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """Setter for width with validation"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
            
            @property
            def height(self):
                """Getter for height"""
                return self.__height
            
            @height.setter
            def height(self, value):
                """Setter for height with validation"""
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value <= 0:
                    raise ValueError("height must be > 0")
                self.__height = value
                
                @property
                def x(self):
                    """Getter for x"""
                    return self.__x
                
                @x.setter
                def x(self, value):
                    """Setter for x with validation"""
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                    
                    @property
                    def y(self):
                    """Getter for y"""
                    return self.__y
                
                @y.setter
                def y(self, value):
                    """Setter for y with validation"""
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value
                    
                    def area(self):
                        """Return the area of the rectangle"""
                        return self.width * self.height
                    
                    def display(self):
                        """Print the rectangle with the character #"""
                        print("\n" * self.y, end="")
                        for _ in range(self.height):
                            print(" " * self.x + "#" * self.width)
                            
                            def __str__(self):
                                """
                                Override the __str__ method,
                                return a formatted string
                            """
                            return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
                        
                        def update(self, *args, **kwargs):
                            """Update the rectangle attributes"""
                            if args:
                                attributes = ['id', 'width', 'height', 'x', 'y']
                                for i, value in enumerate(args):
                                    if i < len(attributes):
                                        setattr(self, attributes[i], value)
                                    else:
                                        for key, value in kwargs.items():
                                            if hasattr(self, key):
                                                setattr(self, key, value)
                                                
                                                def to_dictionary(self):
                                                    """
                                                    Return the dictionary representation of a Rectangle
                                                    """
                                                    return {
                                                            'id': self.id,
                                                            'width': self.width
                                                            'height': self.height,
                                                            'x': self.x,
                                                            'y': self.y
                                                            }
