#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    for i in reversed(my_list):
        print("{:d}".format(i, end=''))
