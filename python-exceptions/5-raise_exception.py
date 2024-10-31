#!/usr/bin/python3
def raise_exception():
    a = 1 / b
    print("{}".format(a))
try:
    raise_exception()
    raise TypeError
except TypeError as e:
    print(e)

