#!/usr/bin/python3
""" Class Rectangle """


class rectangle():
      """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and heigh
    """
    def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

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

