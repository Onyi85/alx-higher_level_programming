#!/usr/bin/python3
""" This module returns the biggest integer value """


def best_score(a_dictionary):
    """ This function returns the biggest integer value """
    best_score = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
        for key, value in a_dictionary.items():
            if a_dictionary[key] == best_score:
                return key
    else:
        return None
