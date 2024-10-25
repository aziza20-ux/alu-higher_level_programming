#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == 0:
        return none
    if idx >= leng(my_list):
        return none
    i = 0
    for ele in my_list:
        if i == idx:
            break
        i += 1
    return ele
        
