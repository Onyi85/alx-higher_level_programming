#!/usr/bin/python3
""" This module deletes a key in dicionary """


def simple_delete(a_dictionary, key=""):
    """ This function deletes a key in dictionary """
    if key != "" and key in a_dictionary:
        a_dictionary.pop(key)
    return (dict(list(a_dictionary.items())[:]))
