#!/usr/bin/python3
"""
modiule that contains class Student
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Entry point"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        my_dict = {}
        if attrs is not None:
            for atr in attrs:
                if atr in self.__dict__:
                    my_dict[atr] = self.__dict__[atr]
            return my_dict
        else:
            return self.__dict__
