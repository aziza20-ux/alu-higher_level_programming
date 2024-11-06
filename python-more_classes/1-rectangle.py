#!/usr/bin/python3
""" defining a classes with getters and setters"""
class rectangle():
""" defining a class"""
    def __init__(self, width=0, height=0):
    self.__width = width
    self.__height = height

     """ getter for width"""
    @property
    def width(self):
        return self.__width

    """ setter for width"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        """ getter for heigth"""
     @property
    def height(self):
        return self.__height

    """ setter for heigth"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

