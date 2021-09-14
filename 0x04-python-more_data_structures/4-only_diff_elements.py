#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 or set_2 is not None:
        new_set = []
        set_1 = list(set_1)
        set_2 = list(set_2)      
        new_set1 = list(set(set_1)-set(set_2))
        new_set2 = list(set(set_2)-set(set_1))
        new_set = new_set1+new_set2
        return new_set
