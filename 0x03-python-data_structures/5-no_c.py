#!/usr/bin/env python3
def no_c(my_string):
    return "".join(i for i in my_string if i.lower() not in 'cC')

