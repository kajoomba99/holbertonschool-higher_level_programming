#!/usr/bin/python3

"""
Module that contains the class Base
"""

import json
import os
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Entry point"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        des = -200
        turtle.speed(3)
        for rec in list_rectangles:
            w = rec.to_dictionary()["width"]
            h = rec.to_dictionary()["height"]
            turtle.penup()
            turtle.setpos(des, 0)
            turtle.pendown()
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
            des += w
        des = -200
        turtle.speed(1)
        for squ in list_squares:
            s = squ.to_dictionary()["size"]
            turtle.penup()
            turtle.setpos(des, 0)
            turtle.pendown()
            turtle.forward(s)
            turtle.right(90)
            turtle.forward(s)
            turtle.right(90)
            turtle.forward(s)
            turtle.right(90)
            turtle.forward(s)
            turtle.right(90)
            des += s
        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            to_dict = list(map(lambda x: x.to_dictionary(), list_objs))
            to_json = cls.to_json_string(to_dict)
        else:
            to_json = cls.to_json_string([])
        with open(cls.__name__ + ".json", mode="w") as json_file:
            json_file.write(to_json)

    @staticmethod
    def int_validator(name, value):
        """Validate if value is type int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def under_equal_zero(name, value):
        """Validate if value is less or equal to zero"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_of_class = []
        with open(cls.__name__ + ".json") as a_file:
            file_cont = json.loads(a_file.read())
        for i in file_cont:
            list_of_class.append(cls.create(**i))
        return list_of_class

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV:"""
        list_dict = list(map(lambda x: x.to_dictionary(), list_objs))
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", mode="w") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(fields)
            for line in list_dict:
                csv_writer.writerow(line.values())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV:"""
        dict_temp = {}
        obj_list = []
        with open(cls.__name__ + ".csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                for reg in line:
                    dict_temp[reg] = int(line[reg])
                obj_list.append(cls.create(**dict_temp))
        return obj_list

    @staticmethod
    def under_zero(name, value):
        """validate if value is under zero"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
