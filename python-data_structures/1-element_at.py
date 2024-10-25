#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    i = 0
    for ele in my_list:
        if i == idx:
            break
        i += 1
    return ele
        
