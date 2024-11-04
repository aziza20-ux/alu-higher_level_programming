#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Instantiation with optional size
    size must be an integer
"""

class Square:
    """Class constructor"""
    def __init__(self, size=0):
        @property
    def size(self):
        print("{}".format(self.__size))
        @sizesetter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size

