#!/usr/bin/python3
""" reading through, a file and printing it on sysout."""


def read_file(filename=""):
    """ reading from a file and print it on sysout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
