#!/usr/bin/python3
def max_integer(my_list=[]):
    length == len(my_list)
    if length == 0:
        return None
    large = my_list[0]
    for i in range(length):
        if my_list[i] > large:
            my_list[i] = large
    return large
