#!/usr/bin/python3
""" reading from a file and create it if it doesn't exist, and count the number of characters."""


def write_file(filename="", text=""):
    """ a function to overwrite, a file if it exists or create it if it doesn't exist."""
    with open(filename, mode='w' encoding="utf-8") as myfile:
        return myfile.write(text)
