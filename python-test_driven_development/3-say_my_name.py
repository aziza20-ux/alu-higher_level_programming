#!/usr/bin/python3
#say my name
"""Thhis module is all about,
printing string names.
"""
def say_my_name(first_name, last_name=""):
    """The say my name functions are about,
    to display strings name.
    """
    if not isinstance(first_name, string):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, string):
        raise TypeError("last_name must be a string")
    print ("My name is"\<{}\>\<{}\>.format(first_name, last_name))
