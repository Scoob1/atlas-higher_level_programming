#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance"""
        super().__init__(size, size, x, y, id)
        
        @property
        def size(self):
            """Getter for size"""
            return self.width
        
        @size.setter
        def size(self, value):
            """Setter for size"""
            self.width = value
            self.height = value
            
            def __str__(self):
                """Override the __str__ method to return a formatted string"""
                return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
            
            def update(self, *args, **kwargs):
                """Update the square attributes"""
                if args:
                    attributes = ['id', 'size', 'x', 'y']
                    for i, value in enumerate(args):
                        if i < len(attributes):
                            setattr(self, attributes[i], value)
                        else:
                            for key, value in kwargs.items():
                                if hasattr(self, key):
                                    setattr(self, key, value)
                                    
                                    def to_dictionary(self):
                                        """Return the dictionary representation of a Square"""
                                        return {
                                                'id': self.id,
                                                'size': self.size,
                                                'x': self.x,
                                                'y': self.y
                                                }
