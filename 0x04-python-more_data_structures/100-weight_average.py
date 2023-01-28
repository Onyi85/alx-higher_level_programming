#!/usr/bin/python3
""" This module returns the weighted average of all integers """


def weight_average(my_list=[]):
    """ This function returns a weighted average """
    if my_list:
        sum_of_last_index = 0
        product = 1
        sum_of_product = 0
        for tuple_a in my_list:
            product = tuple_a[0] * tuple_a[1]
            sum_of_product += product
            sum_of_last_index += tuple_a[1]
        return (sum_of_product / sum_of_last_index)
    else:
        return 0
