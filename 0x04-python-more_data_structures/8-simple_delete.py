#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key in a_dictionary.keys():
        if key == a_dictionary[key]:
            del a_dictionary[key]
        else:
            return a_dictionary
