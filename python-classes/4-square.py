#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Instantiation with optional size
    size must be an integer
"""

class Square:
    """Class constructor"""
    def __init__(self, size=0):
           if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """Size getter"""
        @property
    def size(self):
        return self.__size
    """size setter"""
        @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size

