#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    values = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                values.append(True)
            else:
                values.append(False)
        return values
