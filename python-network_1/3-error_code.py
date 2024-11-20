#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
from urllib import request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ ="__main__":

    url = argv[1]
    req = request(url)
    try:
        with urlopen(req) as response
        r = response.read()
        print(r.decode('utf-8'))
    except HTTPError as e:
        print("code:" e.code)
