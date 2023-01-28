#!/usr/bin/python3
""" This module deletes keys with a specific value """


def complex_delete(a_dictionary, value):
    """ This function deletes keys with specific values """
    if value in a_dictionary.items():
        del a_dictionary[key]
    else:
        pass
    return a_dictionary
