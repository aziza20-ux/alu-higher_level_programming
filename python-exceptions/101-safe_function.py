#!/usr/bin/python3


def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except exception as e:
        print("Exception:{}".format(e), file=sys.stderror)
        return None
