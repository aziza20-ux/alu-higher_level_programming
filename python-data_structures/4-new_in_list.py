#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new.extend(my_list)
    new[idx] = element
    return new
