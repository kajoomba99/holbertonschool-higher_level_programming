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
            attr_list = list(self.__dict__)
            j = 0
            for i in range(len(args)):
                setattr(self, attr_list[j], args[i])
                if i == 1:
                    setattr(self, attr_list[j + 1], args[i])
                    j += 1
                j += 1
        else:
            for kw in kwargs:
                if kw == "size":
                    setattr(self, "width", kwargs[kw])
                    setattr(self, "height", kwargs[kw])
                if hasattr(self, kw):
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
