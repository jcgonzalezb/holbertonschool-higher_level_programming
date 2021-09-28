#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0
        f = 0
        c = a / b
        f = float(c)
    except (ZeroDivisionError, TypeError):
        f = None
    finally:
        print('Inside result: {}'.format(f))
        return f
