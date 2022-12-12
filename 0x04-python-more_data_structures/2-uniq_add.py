#!/usr/bin/python3
# _ _ _ _ _ THIS PROJECT ADDS ALL UNIQUE ITEM IN A LIST _ _ _ _ _
def uniq_add(my_list=[]):
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
