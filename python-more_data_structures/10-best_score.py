#!/usr/bin/python3
# A Function that returns a key with the biggest integer value.


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key = list(a_dictionary.keys())[0]
    largest = a_dictionary[key]
    for k, v in a_dictionary.items():
        if v > largest:
            largest = v
            key = k
    return(key)
