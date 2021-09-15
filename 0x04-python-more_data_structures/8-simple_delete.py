#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = {}
    key_del = key
    for key, value in a_dictionary.items():
        if key is not key_del:
            new_dict[key] = value
    return new_dict
