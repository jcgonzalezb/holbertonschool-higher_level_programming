#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    unique_list = []
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        res += x
    return res
