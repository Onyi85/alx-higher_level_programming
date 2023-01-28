#!/usr/bin/python3
""" This module returns all values multiplied by 2 """


def multiply_by_2(a_dictionary):
    """ This function multiplies the values by 2"""
    b_dictionary = dict(list(a_dictionary.items())[:])
    for key, value in b_dictionary.items():
        b_dictionary[key] = value * 2
    return b_dictionary
