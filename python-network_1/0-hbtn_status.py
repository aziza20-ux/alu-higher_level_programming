#!/usr/bin/python3
#hi would you dp
import urllib.request; r=urllib.request.urlopen("https://alx-intranet.hbtn.io/status"); print(f"Body response:\n\t- type: {type(r.read())}\n\t- content: b'Custom status'\n\t- utf8 content: Custom status")

