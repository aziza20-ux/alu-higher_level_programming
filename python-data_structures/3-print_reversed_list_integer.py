#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(reverse(my_list)), end="")
        i += 1
