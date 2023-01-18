#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    x = 0
    z = 0
    if len(tuple_b) == 0:
        a = 0
        b = 0
    elif len(tuple_a) == 0:
        x = 0
        z = 0
    elif len(tuple_a) == 1:
        x = tuple_a[0]
        z = 0
    elif len(tuple_b) == 1:
        a = tuple_b[0]
        b = 0
    elif len(tuple_a) >= 2:
        x = tuple_a[0]
        z = tuple_a[1]
    elif len(tuple_b) >= 2:
        a = tuple_b[0]
        b = tuple_b[1]
    first_sum = a + x
    second_sum = b + z
    sum = (first_sum, second_sum)
    return sum
