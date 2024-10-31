#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return ret
    except exception as e:
        print("Exception:{}".format(e),file = sys.stderror)
        return None
