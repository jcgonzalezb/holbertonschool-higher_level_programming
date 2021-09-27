#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in my_list:
            counter = counter + 1
        for i in range(0, x):
            print('{:d}'.format(my_list[i]), end='')
    except IndexError:
        pass
    finally:
        if counter < x:
            print('')
            return counter
        else:
            print('')
            return x
