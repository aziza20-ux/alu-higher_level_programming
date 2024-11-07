#!/usr/bin/python3
""" inhereting a class"""

class my_list(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

