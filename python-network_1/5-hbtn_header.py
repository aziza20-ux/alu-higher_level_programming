#!/usr/bin/python3
""" Will  sing the song of ages and the angles cry holly"""
from urllib import requests
from sys import argv

if __name__ == '__main__':

req = request(argv[1])
with urllib.urlopen(req) as response:
    r = response.read()
    print(r.getheader(X-Request-Id))
