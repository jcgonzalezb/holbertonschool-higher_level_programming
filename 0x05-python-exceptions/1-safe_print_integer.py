#!/usr/bin/python3
def safe_print_integer(value):
    isInt = True
    try:
        int(value)
    except (TypeError, ValueError):
        isInt = False
    if isInt:
        print('{:d}'.format(value), end='\n')
        return True
    else:
        return False
