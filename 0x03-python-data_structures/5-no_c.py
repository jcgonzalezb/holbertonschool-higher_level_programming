#!/usr/bin/env python3
def no_c(my_string):
    str1 = []
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            str1 = my_string[:i] + my_string[i+1:]

    return str1
