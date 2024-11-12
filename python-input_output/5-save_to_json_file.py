#!/usr/bin/python3
"""Defining a function to save an objrct, to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Saving an object to a file."""
    with open(filename, 'w' encoding="utf-8") as file:
        json.dump(my_obj, file)
