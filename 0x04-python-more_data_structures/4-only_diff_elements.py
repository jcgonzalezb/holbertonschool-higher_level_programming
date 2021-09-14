#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    not_unique_list = []
    final_list = []
    for x in set_1:
        for y in set_2:
            if x == y:
                not_unique_list.append(x)

    set_1 = list(set_1)
    set_2 = list(set_2)
    new_set = set_1+set_2

    for x in new_set:
        for y in not_unique_list:
            if x != y:
                final_list.append(x)

    return final_list
