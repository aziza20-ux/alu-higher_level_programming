#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    i = 0
    for ele in my_list:
        if i == idx:
            my_list[i] = element
            i += 1
    return my_list
