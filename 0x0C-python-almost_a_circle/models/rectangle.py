#!/usr/bin/python3


"""
Module that contains class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Entry point"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """str method"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_rep = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict_rep

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and args != []:
            v = 0
            lng = len(args)
            for i in self.__dict__:
                if v >= lng:
                    break
                self.__dict__[i] = args[v]
                v += 1
        else:
            for kw in kwargs:
                if hasattr(self, kw):
                    setattr(self, kw, kwargs[kw])

    def display(self):
        """
        print in stdout the Rectangle instance with the character #
        by taking care of x and y
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    @property
    def width(self):
        """return the value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set new value to width"""
        super().int_validator("width", width)
        super().under_zero("width", width)
        self.__width = width

    @property
    def height(self):
        """return the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set new value to width"""
        super().int_validator("height", height)
        super().under_zero("height", height)
        self.__height = height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set new value to x"""
        super().int_validator("x", x)
        super().under_zero("x", x)
        self.__x = x

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set new value to y"""
        super().int_validator("y", y)
        super().under_zero("y", y)
        self.__y = y
