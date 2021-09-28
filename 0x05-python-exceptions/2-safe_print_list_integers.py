#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        for i in range(x):
            if type(my_list[i]) == int:
                counter = counter + 1
                print('{:d}'.format(my_list[i]), end='')
        if counter < x:
            print('')
            return counter
        else:
            print('')
            return x
    except (IndexError):
        return IndexError
