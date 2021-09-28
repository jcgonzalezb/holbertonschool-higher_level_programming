#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0; f = 0
        c = a // b
        f = float(c)
        print('Inside result: {:.1f}'.format(f), end='\n')
    except ZeroDivisionError:
        print('Inside result: None', end='\n')
        return None
    finally:
        if f > 0:
            return f
        else:
            return None