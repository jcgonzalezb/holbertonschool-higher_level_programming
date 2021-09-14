#!/usr/bin/python3
def common_elements(set_1, set_2):
    unique_list = []
    for x in set_1:
        for y in set_2:
            if x == y:
                unique_list.append(x)
    return unique_list
