#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print('{:d}'.format(value), end='\n')
    except ValueError:
        pass
    finally:
        return value
