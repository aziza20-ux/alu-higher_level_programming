#!/usr/bin/python3
"""Difine a function to return an object from an json."""
import json


def from_json_string(my_str):
    """Returning an object from json, and no more mudoles."""
    return json.loads(my_str)
