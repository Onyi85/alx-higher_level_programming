#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    list_index = length - 1
    if idx < 0:
        return my_list
    elif idx > list_index:
        return my_list
    else:
        my_list[idx] = element
