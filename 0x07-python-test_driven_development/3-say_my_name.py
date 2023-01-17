#!/usr/bin/python3
""" This module prints a full name or first name if it's a
    string else it gives a typeerror
"""


def say_my_name(first_name, last_name=''):
    """ This function prints a name to the stdout,
    whether a first name or full name
    """

    # ------ checking if first name is not a string ----
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # ------checking if last name is not a string -----
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # ------if everything works well print the name to stdout ---
    print("My name is {} {}".format(first_name, last_name))
