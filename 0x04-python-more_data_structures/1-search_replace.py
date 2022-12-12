#!/usr/bin/python3
# _ _ _ _ THIS PROGRAM FINDS AND REPLACES AN ITEM IN A LIST _ _ _ _
def search_replace(my_list, search, replace):
    my_own_list = my_list[:]
    for i in range(len(my_own_list)):
        if my_own_list[i] == search:
            my_own_list[i] = replace
    return my_own_list
