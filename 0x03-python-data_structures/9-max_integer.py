#!/usr/bin/python3
def max_integer(my_list=[]):

    lenght = len(my_list)
    if lenght > 0:
        max = 0
        for i in my_list:
            if i > max:
                max = i
        res = max
    else:
        res = None

    return res
