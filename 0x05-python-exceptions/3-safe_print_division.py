#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0
        f = 0
        c = a // b
        f = float(c)
    except (ZeroDivisionError, TypeError):
        c = None
    finally:
        if f > 0:
            print('Inside result: {:.1f}'.format(f), end='\n')
            return f
        else:
            print('Inside result: {}'.format(c), end='\n')
            return None
