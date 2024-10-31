#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("{}".format(sys.exc_info()[1]), file = sys.strerr)
        return (False)
