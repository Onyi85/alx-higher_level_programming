#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    list_index = length - 1
    if idx > list_index:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
