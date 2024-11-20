#!/usr/bin/python3
"""The error httperror is nit gonna do any good thing to me"""

from urllib import requests
from sys import argv

if __name__ ="__main__":
    r = request.get(argv[1])
    if r.status_code > 400:
        print('error code is:', r.status_code)
    else:
        print(r.text)

