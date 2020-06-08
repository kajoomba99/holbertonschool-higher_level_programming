#!/usr/bin/python3


"""Modute contain class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Entry point"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_rep = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return dict_rep

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and args != []:
            attr_list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for kw in kwargs:
                setattr(self, kw, kwargs[kw])

    @property
    def size(self):
        """return the size value"""
        return super().width

    @size.setter
    def size(self, size):
        """set new value to size"""
        self.width = size
        self.height = size
