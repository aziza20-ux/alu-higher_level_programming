#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Method for validating value"""
        if type(value) != int:
            raise TypeError("{} <name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} <name> must be greater than 0".format(name))

                    
